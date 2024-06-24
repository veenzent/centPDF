from pydantic import BaseModel
from fastapi import File, UploadFile
from typing import Annotated, List


# upload file
class PDFFile(BaseModel):
    file: List[UploadFile] = File(...)

# merge PDF
class MergePDF(BaseModel):
    file: List[UploadFile] = File(description="Upload files to merge", media_type="application/pdf")

# rotate PDF
class RotatePDF(PDFFile):
    pass

# split PDF
class SplitPDF(PDFFile):
    pass
