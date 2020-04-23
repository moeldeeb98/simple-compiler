class Token():

    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value

class TokenRepo():

    __instance = None
    __queue = []

    @staticmethod
    def get_instance():
        """ static access method """
        if TokenRepo.__instance == None:
            TokenRepo()
        return TokenRepo.__instance

    def __init__(self):
        """ virtually private constructor  """
        super().__init__()
        if TokenRepo.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TokenRepo.__instance = self
    def get_queue(self):
        return TokenRepo.__queue

    def add_token(self, token):
        TokenRepo.__queue.append(token)

    def has_next(self):
        pass

    def get_next(self):
        pass

    def consume(self):
        pass

t2 = TokenRepo.get_instance()
print(t2.get_queue())
t2.add_token(5)

t4 = TokenRepo.get_instance()
print(t4.get_queue())
t4.add_token(7)
t3 = TokenRepo.get_instance()
print(t3.get_queue())