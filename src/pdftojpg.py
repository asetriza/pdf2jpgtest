from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import os


def main():
    images_from_path = convert_from_path(
        "100403pdf.pdf", output_folder=os.getcwd(), fmt="jpg"
    )


if __name__ == "__main__":
    main()
