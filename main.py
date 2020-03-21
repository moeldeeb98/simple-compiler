import re

tokens = {
    'STRING_LITERAL': r'^"[^"]*$"',#done
    'AUTO': r'\bauto\b', #done
    'NEW': r'\bnew\b', #done
    'EOF': r'\b0\b', #done
    'TRUE': r'\btrue\b', #done
    'FALSE': r'\bfalse\b', #done
    'BREAK': r'\bbreak\b', #done
    'BOOL': r'\bbool\b', #done
    'CASE': r'\bcase\b', #done
    'CHAR' : r'\bchar\b', #done
    'CONST': r'\bconst\b',#done
    'CONTINUE': r'\bcontinue\b',#done
    'DEFAULT': r'\bdefault\b',#done
    'DO': r'\bdo\b',#done
    'DOUBLE': r'\bdouble\b',#done
    'ELSE': r'\belse\b',#done
    'ENUM': r'\benum\b',#done
    'EXTERN': r'\bextern\b',#done
    'FLOAT': r'\bfloat\b',#done
    'FOR': r'\bfor\b', #done
    'GOTO': r'\bgoto\b', #done
    'IF': r'\bif\b', #done
    'INT': r'\bint\b', #done
    'LONG': r'\blong\b', #done
    'REGISTER': r'\bregister\b', #done
    'RETURN': r'\breturn\b', #done
    'SHORT': r'\bshort\b', #done
    'SIGNED': r'\bsigned\b', #done
    'SIZEOF': r'\bsizeof\b', #done
    'STATIC': r'\bstatic\b', #done
    'STRUCT': r'\bstruct\b', #done
    'SWITCH': r'\bswitch\b', #done
    'TYPEDEF': r'\btypedef\b', #done
    'UNION': r'\bunion\b', #done
    'UNSIGNED': r'\bunsigned\b', #done
    'VOID': r'\bvoid\b', #done
    'VOLATILE': r'\bvolatile\b', #done
    'WHILE': r'\bwhile\b', #done
    'ID': r'\b[A-Za-z_]\w*\b', #done
    'INTEGRAL_LITERAL': r'^[1-9][0-9]*$',
    'FLOAT_LITERAL': r'\b([0-9]+([.][0-9]*)?|[.][0-9]+)\b', #done
    'CHAR_LITERAL': r"^'[^']'$", #done
    'LEFT_CURLY_B': r'}', #done
    'RIGHT_CURLY_B': r'{', #done
    'LEFT_SQUARE_B': r']', #done
    'RIGHT_SQUARE_B': r'\[', #done
    'LEFT_ROUND_B' : r'\)', #done
    'RIGHT_ROUND_B': r'\(', #done
    'COMMA': r',', #done
    'SEMICOLON': r';', #done
    'DOT': r'\.', #done
    'NOT': r'!', #done
    'ASSIGN_OPERATOR': r'=', #done
    'PREPROCESSOR': r'#', #done
#     'BACKWARD_SLASH': r'\\', #done
    'MINUS': r'-', #done
    'PLUS': r'\+', #done
    'ASTERICK': r'\*', #done
    'DIVIDE': r'/', #done
    'MOD': r'%', #done
    'LESSTHAN': r'>', #done
    'GREATERTHAN': '<',
    'LESS_EQ': '=>',
    'EQUAL': '==',
    'NOT_EQUAL': '!=',
    'AND': '&&',
    'OR': '||',
    'BITWISE_AND': '&',
    'BITWISE_OR': '|',
    'BITWISE_XOR': '^'

}




def splitwithQuotes(string):
    words = []
    word = ""
    opend = False
    for char in string:
        if opend and char != '"':
            word += char
        elif opend and char == '"':
            word += '"'
            opend = False
            words.append(word)
            word = ""
        elif not opend  and char == '"':
            opend = True
            if not (len(word) == 0 or word.isspace()):
                words += splitOnSymboles(word.strip())
            word = '"'
            
        elif  char.isspace():
            if not (len(word) == 0 or word.isspace()):
                words += splitOnSymboles(word.strip())
            word = ""
        else:
            word += char
    if(len(word) > 0):
        words += splitOnSymboles(word.strip())
    return words
            

def splitOnSymboles(string):
    words = []
    symboles = ['(', ')', '{', '}', '+', '-', '=', '/', '*', '<', '>', '[', ']', ',', ';', '&', '|', '^', '!']
    word = ""
    skipOne = False
    for idx, char in enumerate(string) :
        if skipOne:
            skipOne = False
            continue
        if char in symboles:
            if string[idx+1] in ['&', '|', '<', '>', '='] and char == string[idx+1]:
                words.append(char + string[idx+1])
                word = ""
                continue
            if char == '=' and string[idx+1] in ['<', '>']:
                words.append(char + string[idx+1])
                word = ""
                continue
            if char == '!' and string[idx+1] == '=':
                words.append(char + string[idx+1])
                word = ""
                continue
            if not (len(word) == 0 or word.isspace()):
                words.append(word.strip())
            words.append(char)
            word = ""
        elif char == '.' and( (len(word.strip()) > 0 and (not word.isnumeric())) or ((idx < len(string)-1) and (not string[idx+1].isnumeric()))):
            """
            if ( pervious is not numeric or nextChar is not numeric) 
            split
            """
            if(len(word.strip()) > 0):
                words.append(word.strip())
            
            words.append('.')
            word = ""
            
        else: # if number is float will pass
            word += char
    if(len(word) > 0):
        words.append(word.strip())
    return words



def tokenize(word):
    
    for token in tokens:
#         print('regex ' , tokens[token])
        regex_pattern = tokens[token]
#         print(regex_pattern)
        match = re.match(regex_pattern, word)
        if match:
            return token
    return None
#     return tokenizer


# import re

# match = re.findall(Regex_Pattern, data)

# print("Number of matches :", len(match))

file  = open('/home/mohamed/Documents/fci-cu/compilers/data.txt', 'r')
code = file.read()
file.close()

outFile = open('/home/mohamed/Documents/fci-cu/compilers/out.txt','w') 
  
# file.write(“This is our new text file”) 
# file.write(“and this is another line.”) 
# file.write(“Why? Because we can.”) 
 




words = splitwithQuotes(code)

for word in words:
    token = tokenize(word)
    if(token != None):
        outFile.write('(' + token  + ' ==> '+ word + ')\n')
    else:
        outFile.write('(' + "syntax error with word ==> " + word + ')\n')
        
outFile.close()    
print('Done')
