from . import schemas
from io import BytesIO
import PyPDF2
from fastapi import UploadFile
from typing import List



# - - - - - - - - - - - - Rotate PDF - - - - - - - - - - - -
def rotate_pdf(direction: str, pdf_files: list[UploadFile]):
    # Rotate each PDF file -90 degrees
    for file in pdf_files:
        # Read the PDF file
        with open(file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)

            # Create a PdfFileWriter object for writing the rotated PDF
            writer = PyPDF2.PdfWriter()

            # Iterate over the pages in the PDF file
            for page in reader.pages:
                # Rotate the page with the given direction
                # clockwise (right) = 90
                # counter_clockwise (left) = -90
                page.rotate(direction)

                # Add the rotated page to the PdfWriter object
                writer.add_page(page)

            # Write the rotated PDF to a new file
            with open(file, 'wb') as rotated_file:
                writer.write(rotated_file)
        print(f"Rotated {file} 90 degrees counter clockwise")


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



# def split_pdfs(file: list[str], output_folder=None):
#   """
#   Splits PDF files in a directory with more than one page.

#   Args:
#       directory: Path to the directory containing the PDF files.
#       output_folder: Optional path to the directory where split PDFs will be saved.
#                         If not provided, uses the same directory as the input files.
#   """
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
