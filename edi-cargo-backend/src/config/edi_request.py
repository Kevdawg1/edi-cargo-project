from pydantic import BaseModel

class EDIParseRequest(BaseModel):
    edi_content: str