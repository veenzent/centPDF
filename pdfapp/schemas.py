from pydantic import BaseModel


# merge PDF
class File(BaseModel):
    path_to_file: str
