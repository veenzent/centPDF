import os
from io import BytesIO
import pytest
from fastapi.testclient import TestClient
from typing import List
from . import test_dependencies
from ..pdfapp.routes import pdf


client = TestClient(pdf)

# def test_rotate_pdf_empty_file():
#     """
#     Test the rotate_pdf endpoint with an empty list of files
#     """
#     response = client.post("/rotate")
    # assert response.status_code == 422  # Unprocessed Entity
    # assert b"No files uploaded" in response.content


# - - - - - - - - - - - - - - - - - TEST SINGLE PDF ROTATION - - - - - - - - - - - - - - - - -
@pytest.fixture
def single_pdf_file():
    """
    Creates a single PDF file for testing the rotation functionality.

    This fixture creates a PDF file named "pdf_test_file.pdf" with the content "Testing the rotation of single pdf file\n".
    It then reads the content of the file "tests/2.pdf" and yields it.

    After the test is finished, the temporary file "pdf_test_file.pdf" is removed.

    Returns:
        bytes: The content of the "tests/2.pdf" file.

    """
    pdf_content = "Testing the rotation of single pdf file\n"
    test_dependencies.create_pdf("pdf_test_file.pdf", pdf_content)
    with open("pdf_test_file.pdf", "rb") as f:
        pdf_content = f.read()
        yield pdf_content

    # Remove the temporary file
    os.remove("pdf_test_file.pdf")

# def test_rotate_pdf_single_file(single_pdf_file):
#     """
#     Test the rotate_pdf endpoint with a single valid PDF file
    
#     Args:
#         pdf_file (bytes): The content of a valid PDF file.
#     """
#     # Simulate a file upload
#     file = {"pdf_files": single_pdf_file}

#     response = client.post("/rotate-pdf",files=file)
#     assert response.status_code == 200
#     assert response.headers['Content-Type'] == "application/pdf"
#     assert "attachment; filename=rotated_pdf.pdf" in response.headers["Content-Disposition"]


# - - - - - - - - - - - - - - - - - TEST MULTIPLE PDF ROTATION - - - - - - - - - - - - - - - - -
@pytest.fixture
def multiple_pdf_files():
    """
    Fixture that generates multiple PDF files with the same content and returns a list of bytes representing each file.
    The generated PDF files are named "pdf_test_file{i}.pdf" for i in range(5).
    After the test using this fixture is complete, the temporary files are removed.
    
    Returns:
        List[bytes]: A list of bytes representing each generated PDF file.
    """
    pdf_content = "Testing the rotation of multiple pdf files\n"
    multiple_files = []

    for i in range(5):
        test_dependencies.create_pdf(f"pdf_test_file{i}.pdf", pdf_content)
        with open(f"pdf_test_file{i}.pdf", "rb") as f:
            pdf = f.read()
            multiple_files.append(pdf)

    yield multiple_files

    # Remove the temporary files
    for i in range(5):
        os.remove(f"pdf_test_file{i}.pdf")

def test_rotate_multiple_pdf_files(multiple_pdf_files):
    files = {
        "pdf_files": [
            (f"pdf_file{i}", pdf_file)
            for i, pdf_file in enumerate(multiple_pdf_files)
        ]
    }

    response = client.post("/rotate-pdf",files=files)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/pdf"
    assert "attachment; filename=rotated_pdf.pdf" in response.headers["Content-Disposition"]







# def test_split_pdf():
#     response = client.post("/split-pdf")
