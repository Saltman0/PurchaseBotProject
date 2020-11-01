from Card import Card

class User:

    def __init__(self, email: str, password: str, card: Card.Card):
        self.email = email
        self.password = password
        self.card = card


    def setEmail(self, email: str):
        self.email = email

    def setPassword(self, password: str):
        self.password = password