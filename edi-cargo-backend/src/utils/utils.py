from src.config.cargo_item import CargoItem, EDIRequest
from src.logging.logger import logging
import re

def generate_edi_segment(cargo_item: CargoItem, index: int) -> str:
    """
    Helper function to generate an EDI segment string for the given cargo item.

    Args:
        cargo_item: The cargo item to generate an EDI segment for.
        index: The index of the cargo item in the list of cargo items.

    Returns:
        The generated EDI segment as a string.
    """
    segments = [
        f"LIN+{index}+I'",
        f"PAC+++{cargo_item.cargo_type}:67:95'",
        f"PAC+{cargo_item.number_of_packages}+1'",
        "PCI+1'"
    ]
    
    if cargo_item.container_number:
        segments.append(f"RFF+AAQ:{cargo_item.container_number}'")
        segments.append("PCI+1'")
    
    if cargo_item.master_bill_of_lading_number:
        segments.append(f"RFF+MB:{cargo_item.master_bill_of_lading_number}'")
        segments.append("PCI+1'")
    
    if cargo_item.house_bill_of_lading_number:
        segments.append(f"RFF+BH:{cargo_item.house_bill_of_lading_number}'")
    
    return '\n'.join(segments)

def parse_edi_segment(segment: str) -> dict:
    """
    Helper function to parse a single EDI segment string into a dictionary of cargo item properties.

    The dictionary will contain the following keys:
        - cargo_type: The type of cargo
        - number_of_packages: The number of packages
        - container_number: The container number (optional)
        - master_bill_of_lading_number: The master bill of lading number (optional)
        - house_bill_of_lading_number: The house bill of lading number (optional)

    Args:
        segment: The EDI segment string to parse

    Returns:
        A dictionary of cargo item properties
    """
    cargo_item = {
        "cargo_type": "",
        "number_of_packages": 0,
        "container_number": None,
        "master_bill_of_lading_number": None,
        "house_bill_of_lading_number": None
    }
    lines = segment.split('\n')
    logging.info(f"Parsing EDI segment: {lines}")
    
    for line in lines:
        logging.info(f"Processing line: {line}")
        if line.startswith("PAC+++"):
            match = re.search(r'PAC\+\+\+([^:]+):', line)
            if match:
                cargo_item["cargo_type"] = match.group(1)
                logging.info(f"Found cargo type: {cargo_item['cargo_type']}")
        elif line.startswith("PAC+") and not line.startswith("PAC+++"):
            match = re.search(r'PAC\+(\d+)', line)
            if match:
                cargo_item["number_of_packages"] = int(match.group(1))
        elif line.startswith("RFF+AAQ:"):
            cargo_item["container_number"] = line.split("RFF+AAQ:")[1].rstrip("'")
        elif line.startswith("RFF+MB:"):
            cargo_item["master_bill_of_lading_number"] = line.split("RFF+MB:")[1].rstrip("'")
        elif line.startswith("RFF+BH:"):
            cargo_item["house_bill_of_lading_number"] = line.split("RFF+BH:")[1].rstrip("'")
    
    return cargo_item