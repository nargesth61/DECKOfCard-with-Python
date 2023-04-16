
class Card:
    """
    .گاهی اوقات میخواهیم یک صفت بین تمامی آبجکت های یک کلاس مشترک باشد از چنین صفت هایی استفاده میکنیم
    (class attribute)
    .این صفت متعلق به کلاس است و نه به یک آبجکت خاص
    """
    FACES=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    SUITS=['Hearts','Diamonds','Clubs','Spades']

    def __init__(self,face,suit):
        self._face = face
        self._suit = suit
   
    """
     .دکوراتورِی که اجازه می دهد تا یک تابع مانند یک ویژگی قابل دسترسی باشد @property 
     .هستند readonly  هستند یعنی  getter نکته خاصیت های این کلاس به صورت
    """
    @property
    def face(self):
        """  را برمیگرداند self._face  """    
        return self._face
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def image_name(self):
         return str(self).replace(' ', '_') + '.png'
    
    def __repr__(self):
        return f"card(face='{self.face}', suit='{self.suit}')"
    
    def __str__(self):
        return f'{self.face} of {self.suit}'
    
    def __format__(self,format):
        return f'{str(self):{format}}'
