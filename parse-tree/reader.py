from tokenizer import Token

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
        x = Token(data[0], data[1])
        print(x.value)
        

if __name__ == "__main__":
    reader()