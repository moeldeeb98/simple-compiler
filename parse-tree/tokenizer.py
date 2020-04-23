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
        """ return list of Token objects """
        return TokenRepo.__queue

    def add_token(self, token):
        """ add a token Obj """
        if isinstance(token, Token):
            TokenRepo.__queue.append(token)
        else:
            raise Exception("this method take Token obj")

    def has_next(self):
        pass

    def get_next(self):
        pass

    def consume(self):
        pass

