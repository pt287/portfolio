from PyPDF2 import PdfReader
import sys

pdf_path = r"c:\Users\AN515-45\Downloads\pt287.github.io-main\pt287.github.io-main\pt287.pdf"
out_path = r"c:\Users\AN515-45\Downloads\pt287.github.io-main\pt287.github.io-main\pt287.txt"

try:
    reader = PdfReader(pdf_path)
    texts = []
    for p in reader.pages:
        t = p.extract_text()
        if t:
            texts.append(t)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(texts))
    print("EXTRACTION_DONE")
except Exception as e:
    print("ERROR", e)
    sys.exit(1)
