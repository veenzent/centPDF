import os
from io import BytesIO
import PyPDF2
import pytest
from fastapi.testclient import TestClient
from ..pdfapp.routes import pdf


client = TestClient(pdf)

# def test_rotate_pdf_empty_file():
#     """
#     Test the rotate_pdf endpoint with an empty list of files
#     """
#     response = client.post("/rotate")
    # assert response.status_code == 422  # Unprocessed Entity
    # assert b"No files uploaded" in response.content

def test_rotate_pdf_single_file(single_pdf_file):
    """
    Test the rotate_pdf endpoint with a single valid PDF file
    
    Args:
        pdf_file (bytes): The content of a valid PDF file.
    """

    # Simulate a file upload
    file = {"pdf_files": single_pdf_file}

    response = client.post("/rotate-pdf",files=file)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/pdf"
    assert "attachment; filename=rotated_pdf.pdf" in response.headers["Content-Disposition"]

@pytest.fixture
def single_pdf_file():
    """
    Fixture to provide a valid PDF file.

    Returns:
        bytes: The content of a valid PDF file.
    """
    with open("tests/2.pdf", "rb") as f:
        return f.read()

# @pytest.fixture
# def single_pdf_file():
#     """
#     Fixture to provide a valid PDF file.

#     This fixture creates a temporary PDF file with the content "Testing the rotation of single pdf file"
#     and yields its content.
#     After the test using this fixture is done, the temporary file is removed.

#     Returns:
#         bytes: The content of the temporary PDF file.
#     """

#     # Create a temporary file
#     with open("temp_pdf_test_file.pdf", "wb") as f:
#         f.write(b"Testing the rotation of single pdf file\n")

#     with open("temp_pdf_test_file.pdf", "rb") as f:
#         pdf_content = f.read()
#         yield pdf_content

#     # Remove the temporary file
#     os.remove("temp_pdf_test_file.pdf")



# def test_merge_pdf():
#     response = client.post("/merge-pdf")

# def test_split_pdf():
#     response = client.post("/split-pdf")
