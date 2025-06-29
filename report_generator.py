from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
import pandas as pd

def generate_pdf_report(kpi_csv_path, output_pdf_path):
    # Wczytaj KPI
    df = pd.read_csv(kpi_csv_path)

    # Utwórz dokument PDF
    doc = SimpleDocTemplate(output_pdf_path, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Nagłówek
    elements.append(Paragraph("📦 E-commerce KPI Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Wprowadzenie
    intro = """
    This report summarizes key performance indicators (KPIs) for an e-commerce platform, 
    based on customer behavior, orders, returns, and support activity. 
    The analysis helps identify business trends, operational bottlenecks, 
    and areas for optimization.
    """
    elements.append(Paragraph(intro, styles["BodyText"]))
    elements.append(Spacer(1, 24))

    # Tabela z KPI
    data = [['Metric', 'Value']] + df.values.tolist()
    table = Table(data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ]))
    elements.append(table)

    # Zakończenie
    elements.append(Spacer(1, 24))
    outro = """
    This automated report was generated as part of a full-stack data pipeline simulation.
    Insights derived from this report can inform product decisions, support staffing,
    and UX improvements.
    """
    elements.append(Paragraph(outro, styles["BodyText"]))

    # Zapisz PDF
    doc.build(elements)
    print(f"PDF report saved to {output_pdf_path}")

if __name__ == "__main__":
    generate_pdf_report("outputs/kpis.csv", "outputs/summary_report.pdf")
