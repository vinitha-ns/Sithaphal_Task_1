# Sithaphal_Task_1

# PDF Data Extractor

This project provides a tool to extract and process data from PDF files. Users can extract text, tables, and images from specific pages of a PDF by entering queries that specify the desired pages. The extracted data is saved locally, providing an efficient solution for parsing complex PDF documents.

---

## Key Features

- **Text Extraction**: Extracts all textual content from specified pages of a PDF.
- **Table Parsing**: Identifies and parses tabular data from PDF pages.
- **Image Extraction**: Extracts and saves images from specific pages.
- **Interactive Query Handling**: Allows users to input queries specifying pages to extract data from.
- **Error Handling**: Includes comprehensive error handling for invalid input and processing issues.

---

## Technology Stack

- **Python**: The primary programming language used for the project.
- **PyMuPDF (fitz)**: Library for handling PDF files and extracting images.
- **pdfplumber**: Library for parsing textual and tabular data from PDFs.
- **colorama**: Library for adding colored output to the console.

---

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/PDFDataExtractor.git
   ```

2. **Install dependencies**:

   ```bash
   pip install pymupdf pdfplumber colorama
   ```

3. **Run the application**:

   Simply run the Python script to start extracting data from a PDF:

   ```bash
   python pdf_data_extractor.py
   ```

4. **Input**:

   After running the script, you will be prompted to enter the file path of the PDF and a query specifying the pages to extract data from.

---

## How to Use

1. Clone the repository and install the dependencies as mentioned above.
2. Run the script by executing `python pdf_data_extractor.py`.
3. When prompted, provide the path to the PDF file you want to process.
4. Enter a query specifying the pages you wish to extract data from (e.g., "Extract data from page 1 and page 3").
5. The program will process the PDF and display the extracted data in the console while saving images to a designated folder.

---

## Example Usage

```bash
Enter the path to the PDF file: sample.pdf
Enter your query: Extract data from page 1 and page 2
```

The program will extract text, tables, and images from pages 1 and 2 of `sample.pdf`. Images will be saved to a local directory, and the extracted text and tables will be displayed in the console.

---

## Licensing

This project is distributed under the MIT License. Refer to the [LICENSE](LICENSE) file for more information.

---

## Acknowledgments

- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) for handling PDF processing and image extraction.
- [pdfplumber](https://github.com/jsvine/pdfplumber) for parsing textual and tabular data.
- [colorama](https://pypi.org/project/colorama/) for enhancing terminal output.
- [Python](https://www.python.org/) for its robust and versatile programming environment.

---

Feel free to customize the repository URL and other details as per your project specifics. Let me know if additional adjustments are needed!

