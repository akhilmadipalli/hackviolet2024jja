from lists import feminine_coded_words, masculine_coded_words
from functions import pdf_to_str_arr


resume = pdf_to_str_arr(input("Type in your resume's relative path: "))
for bias in feminine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
for bias in masculine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
