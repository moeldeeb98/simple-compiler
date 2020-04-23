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
        """ return flase if the queue is empty otherwise return true """
        if len(TokenRepo.__queue) > 0:
            return True
        else:
            return False

    def get_next(self):
        """ return the first Token Obj in the Queue """
        if self.has_next():
            return TokenRepo.__queue[0]
        else:
            raise Exception("The Queue is Empty")

    def consume(self):
        """ return the first Token Obj in the Queue and delete it """
        if self.has_next():
            token = TokenRepo.__queue.pop(0)
            return token
        else:
            raise Exception("The Queue is Empty")

