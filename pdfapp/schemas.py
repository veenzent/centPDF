from pydantic import BaseModel
from fastapi import File, UploadFile

# upload file
class PDFFile(BaseModel):
    file: list[UploadFile] = File(...)

# merge PDF
class MergePDF(PDFFile):
    pass

# rotate PDF
class RotatePDF(PDFFile):
    pass

# split PDF
class SplitPDF(PDFFile):
    pass
