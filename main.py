import re

tokens = {
    'STRING_LITERAL': r'^"[^"]*$"',#done
    'AUTO': r'^auto$', #done
    'NEW': r'^new$', #done
    'EOF': r'^0$', #done
    'TRUE': r'^true$', #done
    'FALSE': r'^false$', #done
    'BREAK': r'^break$', #done
    'BOOL': r'^bool$', #done
    'CASE': r'^case$', #done
    'CHAR' : r'^char$', #done
    'CONST': r'^const$',#done
    'CONTINUE': r'^continue$',#done
    'DEFAULT': r'^default$',#done
    'DO': r'^do$',#done
    'DOUBLE': r'^double$',#done
    'ELSE': r'^else$',#done
    'ENUM': r'^enum$',#done
    'EXTERN': r'^extern$',#done
    'FLOAT': r'^float$',#done
    'FOR': r'^for$', #done
    'GOTO': r'^goto$', #done
    'IF': r'^if$', #done
    'INT': r'^int$', #done
    'LONG': r'^long$', #done
    'REGISTER': r'^register$', #done
    'RETURN': r'^return$', #done
    'SHORT': r'^short$', #done
    'SIGNED': r'^signed$', #done
    'SIZEOF': r'^sizeof$', #done
    'STATIC': r'^static$', #done
    'STRUCT': r'^struct$', #done
    'SWITCH': r'^switch$', #done
    'TYPEDEF': r'^typedef$', #done
    'UNION': r'^union$', #done
    'UNSIGNED': r'^unsigned$', #done
    'VOID': r'^void$', #done
    'VOLATILE': r'^volatile$', #done
    'WHILE': r'^while$', #done
    'ID': r'^[A-Za-z_]\w*$', #done
    'INTEGRAL_LITERAL': r'^[1-9][0-9]*$',
    'FLOAT_LITERAL': r'^([0-9]+([.][0-9]*)?|[.][0-9]+)$', #done
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
    'ASSIGN_OPERATOR': r'^=$', #done
    'PREPROCESSOR': r'#', #done
#     'BACKWARD_SLASH': r'\\', #done
    'MINUS': r'-', #done
    'PLUS': r'\+', #done
    'ASTERICK': r'\*', #done
    'DIVIDE': r'/', #done
    'MOD': r'%', #done
    'LESSTHAN': r'>', #done
    'GREATERTHAN': r'<',
    'LESS_EQ': r'=>',
    'EQUAL': r'==',
    'NOT_EQUAL': r'!=',
    'AND': r'&&',
    'OR': r'||',
    'BITWISE_AND': r'&',
    'BITWISE_OR': r'|',
    'BITWISE_XOR': r'^',
    'LEFT_SHIFT': r'>>',
    'RIGHT_SHIFT': r'<<',
    'BITWISE_NOT': r'~',
    'SINGLE_COMMENT': r'//[^\r\n]*',
    'MULTI_COMMENT': r'/\(.)\*/'

}




def splitwithQuotes(string):
    words = []
    word = ""
    opend = False
    commentOpened = False
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
            if idx+1 < len(string) and string[idx+1] in ['&', '|', '<', '>', '='] and char == string[idx+1]:
                skipOne = True
                words.append(char + string[idx+1])
                word = ""
                continue
            if  idx+1 < len(string) and char == '=' and string[idx+1] in ['<', '>']:
                skipOne = True
                words.append(char + string[idx+1])
                word = ""
                continue
            if  idx+1 < len(string) and char == '!' and string[idx+1] == '=':
                skipOne = True
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

file  = open('data.txt', 'r')
code = file.read()
file.close()

outFile = open('out.txt','w') 
  
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
