from cards import *
import random
class Sorter:
    def find_runs(self, cards):
        runs = {}
        for card in cards:
            number = int(card[1:])
            if number not in runs:
                runs[number] = []
            runs[number].append(card)
        valid_runs   = {}
        invalid_runs = {}
        for number, group in runs.items():
            if len(group) >= 3:
                valid_runs[number] = group
            else:
                invalid_runs[number] = group
        return valid_runs, invalid_runs
    def find_suits(self, cards):
        suit_groups = {}
        for card in cards:
            suit = card[0]
            if suit not in suit_groups:
                suit_groups[suit] = []
            suit_groups[suit].append(int(card[1:]))
        valid_suits   = {}
        invalid_suits = {}
        for suit, numbers in suit_groups.items():
            numbers.sort()
            group = [numbers[0]]
            best  = []
            worst = []
            for i in range(1, len(numbers)):
                if numbers[i] == numbers[i-1] + 1:
                    group.append(numbers[i])
                else:
                    if len(group) >= 3:
                        best.extend(group)
                    else:
                        worst.extend(group)
                    group = [numbers[i]]
            if len(group) >= 3:
                best.extend(group)
            else:
                worst.extend(group)
            if best:
                valid_suits[suit]   = [suit + str(n) for n in best]
            if worst:
                invalid_suits[suit] = [suit + str(n) for n in worst]
        return valid_suits, invalid_suits
class Hands:
    def __init__(self):
        self.__cards = []
        self.__won = False
        self.__sorter = Sorter()
    def put_in_hand(self,cards:str):
        self.__cards.append(cards)
    def sort_cards(self):
        valid, invalid = self.__sorter.find_runs(self.__cards)
        all_invalid = [card for group in invalid.values() for card in group]
        valid_suits, invalid_suits = self.__sorter.find_suits(all_invalid)
        all_invalid = [card for group in invalid_suits.values() for card in group]
        value =0
        for card in all_invalid:
            value += int(card[1:])
        temp = [card for group in valid.values()   for card in group]
        temp +=[card for group in valid_suits.values() for card in group]
        temp +=[card for group in invalid_suits.values() for card in group ]
        self.__cards = temp
        return value
    def discard_cards(self,card:str):
        while card not in self.__cards:
            self.show()
            card  = input("which card do you want to discard\n")
        self.__cards.remove(card)
        return card
    def show(self):
        print(self.__cards)
    def get_won(self):
        return self.__won
    def get_cards(self):
        return self.__cards
    def win(self):
        self.__won = True
class DiscardPile:
    def __init__(self):
        self.__cards = []
    def put_in_hand(self,cards:str):
        self.__cards.append(cards)
    def show(self):
        print(self.__cards[-1])
    def take_a_card(self):
        return self.__cards.pop()
    def get_top_card(self):
        temp = self.__cards[-1]
        return temp
class Cardmanuplation:
    def __init__(self,hand1:Hands,hand2:Hands,deck:Deck,discard_pile:DiscardPile):
        self.__hand1 = hand1
        self.__hand2 = hand2
        self.__deck = deck
        self.__discard_pile = discard_pile
    def knock(self):
        if self.__hand1.sort_cards() > self.__hand2.sort_cards():
            self.__hand2.win()
            print("opponent won!")
        elif self.__hand1.sort_cards() < self.__hand2.sort_cards():
            self.__hand1.win()
            print("you won!")
        elif self.__hand1.sort_cards() == self.__hand2.sort_cards():
            self.__hand2.win()
            print("draw")
    def check_for_knock_hand1(self):
        if self.__hand1.sort_cards() <= 10:
            if self.__hand1.sort_cards() == 0:
                print("you won !")
                self.__hand1.win()
                return
            choice = input("do you want to knock\n")
            if choice.lower() == "yes":
                self.knock()
    def check_for_knock_hand2(self):
        if self.__hand2.sort_cards() <= 10:
            if self.__hand2.sort_cards() == 0:
                print("opponent won !")
                self.__hand2.win()
                return
            self.knock()
    def handle_discard(self,card):
        self.__hand1.put_in_hand(card)
        self.__hand1.sort_cards()
        self.__hand1.show()
        card = input("which card do you want to discard\n")
        card = self.__hand1.discard_cards(card)
        self.__discard_pile.put_in_hand(card)
        self.__hand1.sort_cards()
    def draw(self):
        card = self.__deck.draw_card()
        self.handle_discard(card)
        self.check_for_knock_hand1()
    def take_from_discard(self):
        card = self.__discard_pile.take_a_card()
        self.handle_discard(card)
        self.check_for_knock_hand1()
class Play:
    def __init__(self):
        self.__deck = Deck()
        self.__hand1 = Hands()
        self.__hand2 = Hands()
        self.__discard_pile = DiscardPile()
        self.__deck.shuffle()
        for i in range(0,7):
            self.__hand1.put_in_hand(self.__deck.draw_card())
        self.__hand1.sort_cards()
        for i in range(0,7):
            self.__hand2.put_in_hand(self.__deck.draw_card())
        self.__hand2.sort_cards()
        self.__discard_pile.put_in_hand(self.__deck.draw_card())
        self.__card_manuplator = Cardmanuplation(self.__hand1,self.__hand2,self.__deck,self.__discard_pile)
    def first_play(self):
        a=random.randint(1,2)
        if a ==1:
            self.__hand1.show()
            self.__discard_pile.show()
            choice = input("DO you want this card\n")
            while choice.lower() !="yes" and choice.lower() !="no":
                choice = input("try again yes or no\n")
            if choice.lower() == "yes":
                self.__card_manuplator.handle_discard(self.__discard_pile.take_a_card())
                return 1
            if choice.lower() == "no":
                b = random.randint(1,2)
                if b ==1 :
                    self.__hand2.put_in_hand(self.__discard_pile.take_a_card())
                    self.__discard_pile.put_in_hand(self.__hand2.discard_cards(random.choice(self.__hand2.get_cards())))
                    self.__hand2.sort_cards()
                    return 1
                if b ==2 :
                    return 1
        if a ==2:
            b = random.randint(1, 2)
            if b == 1:
                self.__hand2.put_in_hand(self.__discard_pile.take_a_card())
                self.__discard_pile.put_in_hand(self.__hand2.discard_cards(random.choice(self.__hand2.get_cards())))
                self.__hand2.sort_cards()
                return 2
            if b == 2:
                self.__hand1.show()
                self.__discard_pile.show()
                choice = input("DO you want this card\n")
                while choice.lower() != "yes" or choice.lower() != "no":
                    choice = input("try again yes or no\n")
                if choice.lower() == "yes":
                    self.__card_manuplator.handle_discard(self.__discard_pile.take_a_card())
                    return 2
                if choice.lower() == "no":
                    return 2
    def hand1_play(self):
        self.__hand1.show()
        self.__discard_pile.show()
        if self.__hand1.sort_cards() <= 10:
            if self.__hand1.sort_cards() == 0:
                self.__hand1.win()
                print("You won!")
            else:
                choice= input("You can do the following :\n 1)Knock \n 2)draw from deck \n 3)take from discard pile\n")
                if choice == "1":
                    self.__card_manuplator.knock()
                elif choice == "2":
                    self.__card_manuplator.draw()
                elif choice == "3":
                    self.__card_manuplator.take_from_discard()
        else:
            choice = input("You can do the following :\n 1)draw from deck \n 2)take from discard pile\n")
            if choice == "1":
                self.__card_manuplator.draw()
            elif choice == "2":
                self.__card_manuplator.take_from_discard()
    def hand2_play(self):
        if self.__hand2.sort_cards() <= 10:
            self.__card_manuplator.check_for_knock_hand2()
        else:
            a = random.randint(1,2)
            if a ==1:
                self.__hand2.put_in_hand(self.__deck.draw_card())
                self.__discard_pile.put_in_hand(self.__hand2.discard_cards(random.choice(self.__hand2.get_cards())))
                self.__card_manuplator.check_for_knock_hand2()
            elif a == 2:
                self.__hand2.put_in_hand(self.__discard_pile.take_a_card())
                self.__discard_pile.put_in_hand(self.__hand2.discard_cards(random.choice(self.__hand2.get_cards())))
                self.__card_manuplator.check_for_knock_hand2()
    def play(self):
        a =  self.first_play()
        while not self.__hand1.get_won() and not self.__hand2.get_won():
            if a == 1:
                self.hand1_play()
                self.hand2_play()
            if a == 2:
                self.hand2_play()
                self.hand1_play()
            temp = self.__hand1.get_cards() +self.__hand2.get_cards() +list( self.__discard_pile.get_top_card())
            self.__deck.restock_deck(temp)
            self.__deck.shuffle()




