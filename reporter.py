# reporter.py

from fpdf import FPDF
from summarizer import summarize_text

def export_to_pdf(relevant_data, filename="report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for item in relevant_data:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"URL: {item['url']}", ln=True)
        pdf.set_font("Arial", size=12)
        summary = summarize_text(item['text'])
        pdf.multi_cell(0, 10, f"Summary:\n{summary}\n")
        pdf.cell(0, 10, "="*50, ln=True)

    pdf.output(filename)
    print(f"PDF saved as '{filename}'")
