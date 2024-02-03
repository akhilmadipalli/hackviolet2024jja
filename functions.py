import pdfplumber
import re

from lists import feminine_coded_words, masculine_coded_words


def pdf_to_str_arr(file_path):
    resume = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text1 = page.extract_text(x_tolerance=1, y_tolerance=1)
            resume.extend(text1.lower().split())
    return [clean_string(s) for s in resume]


def word_containing_part(part, words):
    for word in words:
        if part in word:
            return word
    return None


def print_fem(resume):
    fem_list = []
    for bias in feminine_coded_words:
        for word in resume:
            if word.startswith(bias):
                fem_list.append(word)
    fem_list = list(set(fem_list))
    for word in fem_list:
        print(word)


def print_masc(resume):
    masc_list = []
    for bias in masculine_coded_words:
        for word in resume:
            if word.startswith(bias):
                masc_list.append(word)
    masc_list = list(set(masc_list))
    for word in masc_list:
        print(word)


def clean_string(input_string):
    cleaned_string = re.sub(r"[^a-zA-Z\-]", "", input_string)
    return cleaned_string
