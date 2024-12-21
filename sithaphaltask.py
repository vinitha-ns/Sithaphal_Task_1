# -*- coding: utf-8 -*-
"""SithaphalTask.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/102muMQsKtCMRJLkEnJtJE9e0nYNHECIE
"""

!pip install fitz
!pip install PyMuPDF
!pip install pdfplumber
!pip install colorama

import os
import fitz  # PyMuPDF
import pdfplumber
from colorama import Fore, Style

def fetch_text_and_tables(pdf_file, page_index):
    """
    Extracts text and tables from the specified page of the PDF.

    Args:
        pdf_file (str): Path to the PDF file.
        page_index (int): Page index (0-based).

    Returns:
        tuple: Extracted text (str) and tables (list of lists).
    """
    try:
        with pdfplumber.open(pdf_file) as pdf:
            if not (0 <= page_index < len(pdf.pages)):
                return None, None
            page = pdf.pages[page_index]
            text = page.extract_text()
            tables = page.extract_tables()
            return text, tables
    except Exception as e:
        print(Fore.RED + f"Error extracting text and tables: {e}" + Style.RESET_ALL)
        return None, None

def save_images_from_page(pdf_file, page_index, output_dir):
    """
    Saves images from the specified page of the PDF to a directory.

    Args:
        pdf_file (str): Path to the PDF file.
        page_index (int): Page index (0-based).
        output_dir (str): Directory to save extracted images.

    Returns:
        list: Paths to the saved images.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        image_paths = []
        with fitz.open(pdf_file) as pdf:
            if not (0 <= page_index < len(pdf)):
                return []
            page = pdf[page_index]
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = pdf.extract_image(xref)
                image_bytes = base_image["image"]
                img_path = os.path.join(output_dir, f"page_{page_index + 1}_img{img_index + 1}.png")
                with open(img_path, "wb") as img_file:
                    img_file.write(image_bytes)
                image_paths.append(img_path)
        return image_paths
    except Exception as e:
        print(Fore.RED + f"Error extracting images: {e}" + Style.RESET_ALL)
        return []

def parse_query_for_pages(query):
    """
    Parses a user query to extract requested page numbers.

    Args:
        query (str): User query string (e.g., "Extract page 1 and page 3").

    Returns:
        list: List of page indices (0-based).
    """
    try:
        return [int(word) - 1 for word in query.split() if word.isdigit()]
    except ValueError:
        raise ValueError("Invalid query format. Ensure page numbers are specified correctly.")

def process_page(pdf_file, page_index, image_dir):
    """
    Extracts and processes data from a single PDF page.

    Args:
        pdf_file (str): Path to the PDF file.
        page_index (int): Page index (0-based).
        image_dir (str): Directory to save extracted images.

    Returns:
        str: Processed results including text, tables, and image paths.
    """
    result = f"\n{Fore.YELLOW}--- Page {page_index + 1} Data ---{Style.RESET_ALL}\n"

    text, tables = fetch_text_and_tables(pdf_file, page_index)
    if text:
        result += f"\n{Fore.GREEN}Text Content:\n{text}{Style.RESET_ALL}\n"
    else:
        result += f"\n{Fore.RED}No text found on this page.{Style.RESET_ALL}\n"

    if tables:
        result += f"\n{Fore.CYAN}Tables:\n{Style.RESET_ALL}"
        for table in tables:
            for row in table:
                result += " | ".join(str(cell) for cell in row) + "\n"
    else:
        result += f"\n{Fore.RED}No tables found.{Style.RESET_ALL}\n"

    images = save_images_from_page(pdf_file, page_index, image_dir)
    if images:
        result += f"\n{Fore.BLUE}Images saved:\n{Style.RESET_ALL}"
        result += "\n".join(images) + "\n"
    else:
        result += f"\n{Fore.RED}No images found on this page.{Style.RESET_ALL}\n"

    return result

def process_query(pdf_file, query, image_dir):
    """
    Processes a user query to extract data from specified PDF pages.

    Args:
        pdf_file (str): Path to the PDF file.
        query (str): User query specifying pages.
        image_dir (str): Directory to save extracted images.

    Returns:
        str: Consolidated extraction results.
    """
    try:
        page_indices = parse_query_for_pages(query)
        if not page_indices:
            return f"{Fore.RED}No valid pages specified.{Style.RESET_ALL}"

        results = ""
        for page_index in page_indices:
            results += process_page(pdf_file, page_index, image_dir)
        return results
    except ValueError as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"

def main():
    pdf_path = "/content/NLP.pdf"
    img_dir = "extracted_images"

    print(Fore.BLUE + "Welcome to the Enhanced PDF Extractor!" + Style.RESET_ALL)
    print("Extract text, tables, and images from specific pages.")

    user_query = input(Fore.YELLOW + "Enter your query: " + Style.RESET_ALL)
    extraction_results = process_query(pdf_path, user_query, img_dir)

    print(Fore.GREEN + "\n--- Extraction Results ---\n" + Style.RESET_ALL)
    print(extraction_results)


if __name__ == "__main__":
    main()