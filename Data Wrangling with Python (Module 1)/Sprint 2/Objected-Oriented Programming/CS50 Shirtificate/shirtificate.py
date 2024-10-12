from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 24)
        self.cell(0, 30, 'CS50 Shirtificate', align='C')


def main():
    name = input("Please enter your name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.image("shirtificate.png", x=0, y=60, w=210)

    pdf.set_font('helvetica', 'B', 24)
    pdf.set_text_color(255, 255, 255)  # White color

    text_y = 140

    pdf.set_y(text_y)
    pdf.cell(0, 10, f"{name} took CS50", align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
