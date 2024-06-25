from pydantic import BaseModel
from fastapi import File, UploadFile
from typing import Annotated, List


# upload file
class PDFFile(BaseModel):
    pass

# merge PDF
class MergePDF(BaseModel):
    pass

# rotate PDF
class RotatePDF(PDFFile):
    pass

# split PDF
class SplitPDF(PDFFile):
    pass
