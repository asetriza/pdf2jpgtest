from pdf2image import convert_from_path, convert_from_bytes
import tempfile


def main():
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path("100403pdf.pdf", output_folder=path)


if __name__ == "__main__":
    main()
