#input user for camelcase
camel_case = input("camelCase: ")

#convert camel case into pythoncase
def convert(t):
    t2 = ""
    for letter in t:
        if letter.islower():
            t2 += letter

        elif letter.isupper():
            t2 += "_"
            t2 += letter.lower()      
    t = t2
    return t  


#print python case
python_case = convert(camel_case)
print(f"snake_case: {python_case}")