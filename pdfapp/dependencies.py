from io import BytesIO
import PyPDF2
from PyPDF2 import PageObject
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse
from typing import List
from multiprocessing import Pool


# - - - - - - - - - - - - Rotate PDF - - - - - - - - - - - -
def rotate_page(page: PageObject):
    """
    Rotates a page by 90 degrees clockwise.

    Args:
        page (PyPDF2.pdf.PageObject): The page object to rotate.

    Returns:
        PyPDF2.pdf.PageObject: The rotated page object.
    """
    page.rotate(90)
    return page

async def rotate_pdf(files: List[UploadFile] = File(description="Upload pdf files to rotate", media_type="application/pdf")):
    """
    Asynchronously rotates PDF files uploaded as `UploadFile` objects and returns a `StreamingResponse` object
    containing the rotated PDF.

    Args:
        files (List[UploadFile], optional): A list of `UploadFile` objects representing the PDF files to rotate.
            Defaults to `File(description="Upload pdf files to rotate", media_type="application/pdf")`.

    Returns:
        StreamingResponse: A `StreamingResponse` object containing the rotated PDF. The response headers include
        a `Content-Disposition` header with a filename of `rotated_pdf.pdf`.

    Raises:
        None.

    """
    buffer = BytesIO()

    with Pool() as pool:
        for file in files:
            pdf = PyPDF2.PdfReader(file.file)
            writer = PyPDF2.PdfWriter()

            pages = pool.map(rotate_page, pdf.pages)

            for page in pages:
                writer.add_page(page)

            writer.write(buffer)

    buffer.seek(0)

    return StreamingResponse(buffer, media_type='application/pdf', headers={"Content-Disposition": "attachment; filename=rotated_pdf.pdf"})


# - - - - - - - - - - - - Merge PDF - - - - - - - - - - - -
def merge_pdf_files(pdf_files: List[UploadFile]) -> BytesIO:
    merger = PyPDF2.PdfMerger()

    for file in pdf_files:
        merger.append(file.file)

    merge_pdf = BytesIO()
    merger.write(merge_pdf)
    merger.close()

    merge_pdf.seek(0)
    print(f"Successfully merged {len(pdf_files)} files;")
    return merge_pdf



def split_pdf(file: list[str], output_folder=None):
    """
    Splits PDF files in a directory with more than one page.

    Args:
        directory: Path to the directory containing the PDF files.
        output_folder: Optional path to the directory where split PDFs will be saved.
                            If not provided, uses the same directory as the input files.
    """
    pass
#   for filename in file:
#     with open(filename, 'rb') as pdf_file:
#       pdf_reader = PyPDF2.PdfReader(pdf_file)
#       num_pages = len(pdf_reader.pages)

#       if num_pages > 1:
#         if not output_folder:
#           output_folder = file  # Use the same directory if no output folder provided

#         for page_num in range(num_pages):
#           pdf_writer = PyPDF2.PdfWriter()
#           pdf_writer.add_page(pdf_reader.pages[page_num])

#           output_filename = f"{filename.split('.')[0]}_page {page_num + 1}.pdf"
#           # TODO: zip all files
#           output_path = os.path.join(output_folder, output_filename)
#           with open(output_path, 'wb') as output_file:
#             pdf_writer.write(output_file)

#         print(f"Split {filename} into {num_pages} separate PDFs.")
#       else:
#         # TODO: add to zipped files
#         shutil.copy(os.path.join(file, filename), os.path.join(output_folder, filename))
