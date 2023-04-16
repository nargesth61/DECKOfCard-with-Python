from card import Card
from deck import Deckofcard
import random
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"""
بارگذاری card_images برای نمایش هر تصویر ابتدا باید آن را از پوشه ی 
.کنیم برای این کار برای این کار به مسیر کامل فایل نیزا داریم 
"""
"""
.میتوانیم همزمان چندین تصویر را بارگذاری کنیم subplots با کمک 
"""
deck_of_cards  = Deckofcard()


path = Path('.').joinpath('card_images')
figure, axes_list = plt.subplots(nrows=4, ncols=13)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
    
figure.tight_layout()
deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

plt.show()
