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
    try:
        contents = await file.read()
        # Do something with the file contents
        return {"filename": file.filename, "contents": contents}
    except Exception as e:
        return {"error": str(e)}
