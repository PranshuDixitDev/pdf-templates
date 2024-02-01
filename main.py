from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("pdf_topics.csv")

for index, row in df.iterrows():
	pdf.add_page()

	pdf.set_font(family="Times", style="B", size=12)
	pdf.set_text_color(100, 100, 100)
	pdf.cell(w=35, h=12, txt=row["Topic"], align="L", ln=1)
	pdf.line(10, 25, 200, 25)
# pdf.set_font(family="Times", size=14)
# pdf.cell(w=30, h=12, txt="Write your thoughts!", align="L", ln=1)

	for i in range(row["Pages"] - 1):
		pdf.add_page()

pdf.output("output.pdf")
