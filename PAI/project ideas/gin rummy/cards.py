import random
class Cards:
    def __init__(self, chrtype:str):
        self.__cards = []
        self.__type = chrtype
        if chrtype.lower() == "diamond":
            self.sort("D")
        if chrtype.lower() == "club":
            self.sort("C")
        if chrtype.lower() == "heart":
            self.sort("H")
        if chrtype.lower() == "spades":
            self.sort("S")
    def sort(self,t:str):
        for i in range(1,14):
            self.__cards.append(t + str(i))

    def showvalue(self,index:int):
        return self.__cards[index]
class Deck:
    def __init__(self):
        self.__diamonds = Cards("Diamond")
        self.__clubs = Cards("Club")
        self.__hearts = Cards("Heart")
        self.__spades = Cards("Spades")
        self.__deck = []
        for i in range (0 ,52):
            if(i >=0 and i <= 12):
                self.__deck.append(self.__diamonds.showvalue(i))
            if(i >=13 and i <= 25):
                self.__deck.append(self.__clubs.showvalue(i-13))
            if(i >=26 and i <= 38):
                self.__deck.append(self.__hearts.showvalue(i-26))
            if(i >=39 and i <= 51):
                self.__deck.append(self.__spades.showvalue(i-39))
    def shuffle(self):
        random.shuffle(self.__deck)
    def draw_card(self):
        return self.__deck.pop()
    def restock_deck(self,cards):
        self.__diamonds = Cards("Diamond")
        self.__clubs = Cards("Club")
        self.__hearts = Cards("Heart")
        self.__spades = Cards("Spades")
        self.__deck = []
        for i in range(0, 52):
            if (i >= 0 and i <= 12):
                self.__deck.append(self.__diamonds.showvalue(i))
            if (i >= 13 and i <= 25):
                self.__deck.append(self.__clubs.showvalue(i - 13))
            if (i >= 26 and i <= 38):
                self.__deck.append(self.__hearts.showvalue(i - 26))
            if (i >= 39 and i <= 51):
                self.__deck.append(self.__spades.showvalue(i - 39))
        temp = [card for card in self.__deck if card not in cards]
        self.__deck = temp




