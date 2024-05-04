from pydantic import BaseModel


# upload file
class File(BaseModel):
    upload_file: str

# merge PDF
class MergePDF(File):
    pass

# rotate PDF
class RotatePDF(File):
    pass

# split PDF
class SplitPDF(File):
    pass
