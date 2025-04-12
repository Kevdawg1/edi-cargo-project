from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import re
import uvicorn
import jsonify
from src.logging.logger import logging
from src.config.cargo_item import CargoItem, EDIRequest
from src.config.edi_request import EDIParseRequest
from src.utils.utils import generate_edi_segment, parse_edi_segment
from src.testing.unit_test import TestGenerateEdiSegment
import unittest

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper functions



@app.post('/generate-edi')
async def generate_edi(request: EDIRequest):
    """
    Endpoint to generate an EDI message from a list of cargo items.

    Args:
        request (EDIRequest): The request object containing a list of cargo items.

    Returns:
        dict: A dictionary containing the generated EDI message under the key 'edi_message'.

    Raises:
        HTTPException: If any error occurs during EDI generation, a 400 error is raised with the error message.
    """

    logging.info(f"Received cargo items: {request.cargo_items}")
    if not request.cargo_items:
        raise HTTPException(status_code=400, detail="cargo_items are required")
    try:
        edi_segments = []
        for index, item in enumerate(request.cargo_items, start=1):
            segments = [
                f"LIN+{index}+I'",
                f"PAC+++{item.cargo_type}:67:95'",
                f"PAC+{item.number_of_packages}+1'",
                "PCI+1'"
            ]
            
            if item.container_number:
                segments += [
                    f"RFF+AAQ:{item.container_number}'",
                    "PCI+1'"
                ]
            
            if item.master_bill_of_lading_number:
                segments += [
                    f"RFF+MB:{item.master_bill_of_lading_number}'",
                    "PCI+1'"
                ]
            
            if item.house_bill_of_lading_number:
                segments.append(f"RFF+BH:{item.house_bill_of_lading_number}'")
            
            edi_segments.append('\n'.join(segments))
        logging.info(f"Generated EDI segments: {edi_segments}")
        return {"edi_message": '\n'.join(edi_segments)}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/parse-edi")
async def parse_edi(request: EDIParseRequest):
    """
    Parse the given EDI content into a list of cargo items.

    Args:
        request: A request body containing the EDI content to parse.

    Returns:
        A response containing a list of cargo items.

    Raises:
        HTTPException: If the given EDI content is invalid, a 400 error is raised with the error message.
    """
    logging.info(f"Received EDI content: {request.edi_content}")
    if not request.edi_content:
        raise HTTPException(status_code=400, detail="edi_content is required")
    try:
        # Split the EDI into segments for each cargo item
        segments = re.split(r'(?=LIN\+\d+\+I\')', request.edi_content.strip())
        segments = [s.strip() for s in segments if s.strip()]
        
        cargo_items = []
        for segment in segments:
            cargo_items.append(parse_edi_segment(segment))
        logging.info(f"Parsed cargo items: {cargo_items}")
        return {"cargo_items": cargo_items}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid EDI format: {str(e)}")

if __name__ == "__main__":
    test = TestGenerateEdiSegment(unittest.TestCase)
    unittest.main()
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)