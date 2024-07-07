from fastapi.testclient import TestClient
from ..pdfapp.routes import pdf


client = TestClient(pdf)

def test_rotate_pdf():
    response = client.post("/rotate-pdf")
    pass

def test_merge_pdf():
    response = client.post("/merge-pdf")

def test_split_pdf():
    response = client.post("/split-pdf")
