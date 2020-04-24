from tokenizer import Token, TokenRepo

def filter(str):
    new_str = str.replace('<', '')
    new_str = new_str.replace('>', '')
    new_str = new_str.replace(' ', '')
    new_str = new_str.replace('\n', '')
    return new_str

def spliter(str):
    str = filter(str)
    colon_split = str.split(":")
    return colon_split

def reader():
    file = open("TestCase1.txt", "r")
    for line in file:
        data = spliter(line)
        T = TokenRepo.get_instance()
        token = Token(data[0], data[1])
        T.add_token(token)
        

if __name__ == "__main__":
    reader()