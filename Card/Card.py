class Card:

    def __init__(self, cardNumber: str, cardName: str, cardExpireDate: str, cardCryptogram: str):
        self.cardNumber = cardNumber
        self.cardName = cardName
        self.cardExpireDate = cardExpireDate
        self.cardCryptogram = cardCryptogram

    def setCardNumber(self, cardNumber: str):
        self.cardNumber = cardNumber

    def setCardName(self, cardName: str):
        self.cardName = cardName

    def setCardExpireDate(self, cardExpireDate: str):
        self.cardExpireDate = cardExpireDate

    def setCardCryptogram(self, cardCryptogram: str):
        self.cardCryptogram = cardCryptogram