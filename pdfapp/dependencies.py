import os
import PyPDF2
# from PyPDF2 import PdfReader, PdfWriter
from . import schemas

# - - - - - - - - - - - - Merge PDF - - - - - - - - - - - -
# cwd = os.getcwd()
# files = os.listdir(cwd)
# pdf_files = [file for file in files if file.endswith('.pdf')]

def merge_files(pdf_files):
    # Create a pdf merger object
    pdf_merger = PyPDF2.PdfMerger()
    for file in pdf_files:
        # Open the pdf file and merge it to the pdf_merger object
        with open(file, 'rb') as f:
            pdf_merger.append(f)

    with open('merged file.pdf', 'wb') as merged_file:
        pdf_merger.write(merged_file)

    print(f"Successfully merged {len(pdf_files)} files;")
    for file in pdf_files:
        print(f"  - {file}")


# - - - - - - - - - - - - Rotate PDF - - - - - - - - - - - -
def rotate_pdf(cwd, pdf_files):
    # Rotate each PDF file -90 degrees
    for file in pdf_files:
        file = os.path.join(cwd, file)
        # Read the PDF file
        with open(file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)

            # Create a PdfFileWriter object for writing the rotated PDF
            writer = PyPDF2.PdfWriter()

            # Iterate over the pages in the PDF file
            for page in reader.pages:
                # Rotate the page 90 degrees counter clockwise
                page.rotate(-90)

                # Add the rotated page to the PdfWriter object
                writer.add_page(page)

            # Write the rotated PDF to a new file
            with open(file, 'wb') as rotated_file:
                writer.write(rotated_file)
        print(f"Rotated {file} 90 degrees counter clockwise")


def split_pdfs(directory, output_folder=None):
  """
  Splits PDF files in a directory with more than one page.

  Args:
      directory: Path to the directory containing the PDF files.
      output_folder: Optional path to the directory where split PDFs will be saved.
                        If not provided, uses the same directory as the input files.
  """
  for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
      input_file = os.path.join(directory, filename)
      
      with open(input_file, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        if num_pages > 1:
          if not output_folder:
            output_folder = directory  # Use the same directory if no output folder provided
          
          for page_num in range(num_pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
            output_filename = f"{filename.split('.')[0]}_page {page_num + 1}.pdf"
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, 'wb') as output_file:
              pdf_writer.write(output_file)
          
          print(f"Split {filename} into {num_pages} separate PDFs.")
        else:
	        shutil.copy(os.path.join(directory, filename), os.path.join(output_folder, filename))
