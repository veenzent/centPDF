from io import BytesIO
from . import dependencies
import PyPDF2
from fastapi import APIRouter, UploadFile, File
from typing import List
from fastapi.responses import StreamingResponse


pdf = APIRouter()


@pdf.post("/rotate-pdf")
async def rotate_pdf(pdf_files: List[UploadFile] = \
        File(description="Upload files to rotate", media_type="application/pdf")
    ):

    return await dependencies.rotate_pdf(pdf_files)


@pdf.post("/merge-pdf")
async def merge_pdf(pdf_files: List[UploadFile] = File(description="Upload files to merge", media_type="application/pdf")):
    merge_pdf = await dependencies.merge_pdf_files(pdf_files)

    return StreamingResponse(merge_pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=merged.pdf"})
