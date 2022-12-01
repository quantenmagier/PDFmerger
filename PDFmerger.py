"""
author: Niels Joseph

Before use install the package PyPDF2 with either pip install PyPDF2 or conda install PyPDF2 in the terminal.
Just ignore the error warnings concerning superfluos whitespace it seems to work nonetheless.
"""
import os
from PyPDF2 import PdfFileMerger

# Set the directory in which the PDFs should be merged
directory = r"set your own directory"


def merge_pdfs(directory: str) -> None:
    """
    Merges all the pdfs in a given directory into a new file called mergedPDF that is saved within the same directory.
    They are merged in alphanumeric order. So numbering them 01, 02, 03... can produce the desired ordering.
    The script cannot merge encrypted PDFs.
    :param directory: The directory of the PDFs that are to be merged.
    :return:
    """
    # Call the constructor for the file merger
    merger = PdfFileMerger()

    # Merge the files in the directory
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            merger.append(os.path.join(directory, file))

    # Save the merged files
    with open(directory + r"\\mergedPDF.pdf", "wb") as f:
        merger.write(f)


# proceed only when called as main
if __name__ == "__main__":
    merge_pdfs(directory=directory)
