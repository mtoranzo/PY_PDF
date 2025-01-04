FROM python:3.9-slim
RUN pip install PyPDF2 PyMuPDF
COPY . /app
WORKDIR /app
CMD ["python", "process_pdf.py"]