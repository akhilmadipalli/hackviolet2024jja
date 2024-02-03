import pdfplumber


def pdf_to_str_arr(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text1 = page.extract_text()
        resume = text1.lower().split()
    return resume


def word_containing_part(part, words):
    for word in words:
        if part in word:
            return word
    return None
