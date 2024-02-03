from lists import feminine_coded_words, masculine_coded_words
from functions import pdf_to_str_arr

# pdfs
akhil = "akhil.pdf"
john = "john.pdf"
jin = "jin.pdf"

file_path = input("Type your resume's relative path: ")
resume = pdf_to_str_arr(file_path)
for bias in feminine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
for bias in masculine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
