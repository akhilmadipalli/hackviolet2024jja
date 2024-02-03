from lists import feminine_coded_words, masculine_coded_words
from functions import pdf_to_str_arr


resume = pdf_to_str_arr(input("Type in your resume's relative path: "))
print("Here are the feminine coded words:")
for bias in feminine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
print("Here are the masculine coded words:")

for bias in masculine_coded_words:
    for word in resume:
        if word.startswith(bias):
            print(word)
print(resume)
