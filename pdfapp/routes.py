from io import BytesIO
import PyPDF2
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from . import schemas



pdf = APIRouter()


@pdf.post("/merge-pdf")
async def merge_pdf(files: schemas.MergePDF):
    merger = PyPDF2.PdfMerger()

    for pdf_file in files:
        pdf_bytes = await pdf_file.read()
        pdf_stream = BytesIO(pdf_bytes)
        merger.append(pdf_file.file)

    merge_pdf = BytesIO()
    merger.write(merge_pdf)
    merger.close()

    merge_pdf.seek(0)

    return StreamingResponse(merge_pdf, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=merged.pdf"})


@pdf.post("/rotate-pdf")
async def rotate_pdf(file: schemas.RotatePDF):
    if len(file) == 1:
        pdf_bytes = await file[0].read()
        reader = PyPDF2.PdfFileReader(BytesIO(pdf_bytes))
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            page.rotateClockwise(90)
            writer.addPage(page)

        rotated_pdf = BytesIO()
        writer.write(rotated_pdf)
