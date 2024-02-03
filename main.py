from functions import pdf_to_str_arr, print_fem, print_masc

if __name__ == "__main__":
    resume = pdf_to_str_arr(input("Type in your resume's relative path: "))
    print("Here are the feminine coded words:")
    print_fem(resume)
    print("Here are the masculine coded words:")
    print_masc(resume)
