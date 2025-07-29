from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", size=50)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", align="C")
        self.ln(50)


name = input("Name: ").title()
pdf = PDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Courier", "B", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 170, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
