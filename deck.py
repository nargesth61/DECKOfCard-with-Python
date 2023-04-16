from card import Card
import random


class Deckofcard:
    NUMBER_of_card = 52
    
    def __init__(self):
        """
         .صفت اول اندیس ورقی است که در نوبت بعد باید کشیده شود
         .است Card صفت دوم یک لیستی از 52 شی 
        """
        self.current_card = 0
        self._deck = []
        
        """
        .ایجاد میکند و بعد آن را مقدار دهی میکندCard این حلقه در هر تکرار یک شی از 
        .همیشه مقداری بین 0 تا 12 میسازد که به عنوان اندیس استفاده میشود[count % 13] عبارت 
        .همیشه مقداری بین 0 تا 3 میسازد که به عنوان اندیس استفاده میشود[count // 13] عبارت 
        """

        for count in range(Deckofcard.NUMBER_of_card):  
            self._deck.append(Card(Card.FACES[count % 13], 
                Card.SUITS[count // 13]))

    def shuffle(self):
        """
        لیست random را به صفر برمیگرداند و سپس ماژول current_card این متد ابتدا صفت 
        .ترتیب ورق های آن را بهم میریزد _deck را روی 
        """
        self.current_card = 0
        random.shuffle(self._deck)    
    
    def deal_card(self):
        """
        .بیرون میکشد _deck  یک ورق را از لیست 
        """
        try:
            card = self._deck[self.current_card]
            self.current_card += 1
            return card
        except:
            return None  

        
    def __str__(self):

        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self.deal_card():<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        
        return s        

