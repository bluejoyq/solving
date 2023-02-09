

import random
from time import sleep
from typing import List

import keyboard


class Card:
    def __init__(self,number : int, kind : str):
        self.number :int = number
        self.kind : str = kind
    def __str__(self) -> str:
        return f"{self.kind} - {self.number}"
class Deck:
    def __init__(self, _deck = []) -> None:

        self.deck  : List[Card] = _deck[:]

    def init_deck(self) -> None: # 덱을 만드는 함수임
        deck_info = [(1,5),(2,3),(3,3),(4,2),(5,1)]
        for fruit in ["바나나","사과","포도", "샤인머스켓"]:
            for fruit_num, card_num in deck_info:
                for i in range(card_num):
                    self.deck.append(Card(fruit_num,fruit))
    def suffle_split_deck(self): # 랜덤 덱 생성을 하는
        # 섞어
        # 반으로 나눠
        random.shuffle(self.deck)
        player = self.deck[:28]
        ai = self.deck[28:]
        return Deck(player), Deck(ai)

    def is_not_empty(self) -> bool:
        return self.deck
    def add_card(self, card: Card) -> bool:
        self.deck.append(card)
    def show_last(self):
        if len(self.deck) > 0:
            print(self.deck[-1])
        else:
            print('없음')
    def pop_last(self)->Card:
        return self.deck.pop()
    def __str__(self) -> str:
        result = ''
        for card in self.deck:
            result += card.__str__() + '/'
        return result
    def print(self):
        print(self.deck)
card_list = Deck()
player_open_deck = Deck()
ai_open_deck = Deck()
card_list.init_deck()
player_deck, ai_deck = card_list.suffle_split_deck()
turn = 0

while player_deck.is_not_empty() and ai_deck.is_not_empty():
   
    if turn % 2 == 0 :
        while True:
            if keyboard.is_pressed(' '):
                player_open_deck.add_card(player_deck.pop_last())
                break
    else:
        num = random.random()
        sleep(num)
        ai_open_deck.add_card(ai_deck.pop_last())
    print('=============나===========')
    player_open_deck.show_last()
    print('=============상대===========')
    ai_open_deck.show_last()
    turn += 1
