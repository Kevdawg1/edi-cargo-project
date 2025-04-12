from pydantic import BaseModel
from typing import List, Optional


class CargoItem(BaseModel):
    cargo_type: str
    number_of_packages: int
    container_number: Optional[str] = None
    master_bill_of_lading_number: Optional[str] = None
    house_bill_of_lading_number: Optional[str] = None
    
class EDIRequest(BaseModel):
    cargo_items: List[CargoItem]