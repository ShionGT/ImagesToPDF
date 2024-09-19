from fpdf import FPDF
import fileinput

def convert(pdf, file_location, destination):
    # image list is the list with all image filenames
    for line in fileinput.input(file_location):
        pdf.add_page()
        print(line)
        pdf.image(line)

    pdf.output("merged.pdf", destination)


def main():
    convert(FPDF("P", "mm", "Letter"),
            "/Users/shion/Downloads/Elf-Kyoi-Iku/[Ikutontomato] Kairaku Jigoku - LEVEL 1 (One Piece)",
            "Samsung USB")

if __name__ == "__main__":
    main()