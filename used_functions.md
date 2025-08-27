# Used Functions and Modules

## Python Standard Library
- `datetime` – for date and time operations, e.g., calculating session durations

## Pandas (`import pandas as pd`)
- `pd.read_csv(path, parse_dates=[...])` – read CSV files into a DataFrame, optionally parsing columns as dates  
- `df.values.tolist()` – convert DataFrame to list of lists (e.g., for tables in PDF)  
- `df['column'].mean()` – calculate the mean of a column  
- `df['column'].sum()` – calculate the sum of a column  
- `df['column'].nunique()` – count unique values in a column  
- `df.groupby('column')` – group data by a specific column  
- `df.to_csv(path, index=False)` – save DataFrame to CSV  

## Matplotlib (`import matplotlib.pyplot as plt`)
- `plt.figure(figsize=(w, h))` – create a new figure with specified size  
- `df.plot(kind='bar', color='color')` – create a bar chart  
- `plt.title("...")` – set chart title  
- `plt.ylabel("...")` – set y-axis label  
- `plt.tight_layout()` – adjust layout to prevent clipping  
- `plt.savefig(path)` – save the chart as an image file  
- `plt.close()` – close the figure to free memory  

## ReportLab
- `SimpleDocTemplate(output_path, pagesize=A4)` – create a PDF document  
- `Paragraph(text, style)` – add a paragraph of text with a style  
- `Spacer(width, height)` – add vertical space between elements  
- `Table(data, hAlign='LEFT')` – create a table in the PDF  
- `TableStyle([...])` – define table styles (colors, fonts, grid, padding)  
- `getSampleStyleSheet()` – get sample styles for paragraphs  

## Custom Functions
- `generate_pdf_report(kpi_csv_path, output_pdf_path)` – generates a PDF KPI report from CSV data, including title, introduction, KPI table, and conclusion  
- `analyze_sessions(sessions_path, output_dir)` – analyzes session data: calculates session duration, cart abandonment rate, average session duration, and creates bar charts by channel  
- `generate_kpis(customers_path, orders_path, returns_path, sessions_path, support_path, output_path)` – computes key performance indicators (KPIs) from multiple CSV files and saves results as a CSV report  
