import re
import math
import string

def decipher():
    alphabet = string.ascii_lowercase
    finalword = ''

    with open('input.txt') as f:
        contents = f.read()

    code_list = re.findall("{{[[]!\d{1,5}![\]]}}", contents)

    for word in code_list:
        code = re.findall('\d{1,5}', word)
        alphabet_index = math.sqrt(int(code[0]))
        if(alphabet_index.is_integer()):
            try:
                finalword += alphabet[int(alphabet_index) - 1]
            except:
                continue
    
    print(finalword)


decipher()