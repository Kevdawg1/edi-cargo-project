import unittest
from src.config.cargo_item import CargoItem
from src.utils.utils import generate_edi_segment
from src.logging.logger import logging

class TestGenerateEdiSegment(unittest.TestCase):

    def test_all_optional_fields(self):
        cargo_item = CargoItem(
            cargo_type="FCL",
            number_of_packages=10,
            container_number="123456",
            master_bill_of_lading_number="ABC123",
            house_bill_of_lading_number="DEF456"
        )
        index = 1
        expected_edi_segment = (
            "LIN+1+I'\n"
            "PAC+++FCL:67:95'\n"
            "PAC+10+1'\n"
            "PCI+1'\n"
            "RFF+AAQ:123456'\n"
            "PCI+1'\n"
            "RFF+MB:ABC123'\n"
            "PCI+1'\n"
            "RFF+BH:DEF456'"
        )
        self.assertEqual(generate_edi_segment(cargo_item, index), expected_edi_segment)
        logging.info("All optional fields test passed.")

    def test_no_optional_fields(self):
        cargo_item = CargoItem(
            cargo_type="FCL",
            number_of_packages=10
        )
        index = 1
        expected_edi_segment = (
            "LIN+1+I'\n"
            "PAC+++FCL:67:95'\n"
            "PAC+10+1'\n"
            "PCI+1'"
        )
        self.assertEqual(generate_edi_segment(cargo_item, index), expected_edi_segment)
        logging.info("No optional fields test passed.")
        
    def test_only_container_number(self):
        cargo_item = CargoItem(
            cargo_type="FCL",
            number_of_packages=10,
            container_number="123456"
        )
        index = 1
        expected_edi_segment = (
            "LIN+1+I'\n"
            "PAC+++FCL:67:95'\n"
            "PAC+10+1'\n"
            "PCI+1'\n"
            "RFF+AAQ:123456'\n"
            "PCI+1'"
        )
        self.assertEqual(generate_edi_segment(cargo_item, index), expected_edi_segment)
        logging.info("Only container number test passed.")

    def test_only_master_bill_of_lading_number(self):
        cargo_item = CargoItem(
            cargo_type="FCL",
            number_of_packages=10,
            master_bill_of_lading_number="ABC123"
        )
        index = 1
        expected_edi_segment = (
            "LIN+1+I'\n"
            "PAC+++FCL:67:95'\n"
            "PAC+10+1'\n"
            "PCI+1'\n"
            "RFF+MB:ABC123'\n"
            "PCI+1'"
        )
        self.assertEqual(generate_edi_segment(cargo_item, index), expected_edi_segment)
        logging.info("Only master bill of lading number test passed.")

    def test_only_house_bill_of_lading_number(self):
        cargo_item = CargoItem(
            cargo_type="FCL",
            number_of_packages=10,
            house_bill_of_lading_number="DEF456"
        )
        index = 1
        expected_edi_segment = (
            "LIN+1+I'\n"
            "PAC+++FCL:67:95'\n"
            "PAC+10+1'\n"
            "PCI+1'\n"
            "RFF+BH:DEF456'"
        )
        self.assertEqual(generate_edi_segment(cargo_item, index), expected_edi_segment)
        logging.info("Only house bill of lading number test passed.")


    def test_invalid_cargo_item(self):
        cargo_item = CargoItem(
            number_of_packages=10
        )
        index = 1
        with self.assertRaises(AttributeError):
            generate_edi_segment(cargo_item, index)
            
        logging.info("Invalid cargo item test passed.")

if __name__ == "__main__":
    unittest.main()