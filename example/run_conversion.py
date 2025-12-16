from pdf_chunker import convert_pdf

convert_pdf(
    pdf_path="D:\TOPICS\datafoundry\RAG\chunker_package\example\small.pdf",
    output_dir="output",
    hierarchical=True,
    flat=True
)
