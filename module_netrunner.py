from PIL import Image
import tkinter as tk

baseDeck = [ '', '', '', '', '', '', '']

def showCard(cardName):
        with Image.open(f"Netrunning Deck v2 Individual PNGs/{cardName}.png") as img:
            size = (206, 281)
            cardSize = img.resize(size)
            cardSize.show()

def deckList():
      with open('deckList.txt', 'r') as premadeDeck:
        i = 0
        for line in premadeDeck:
              baseDeck[i] = line.strip()
              i = i + 1
      
      print(baseDeck)

loadDeck = tk.Tk() # This object it meant to open a GUI element to input a deck list rather than hard coding it.
loadDeck.title("Please Select Cyberdeck loadout")
loadDeck.geometry("500x600")

deck_var = tk.StringVar()
deck_var2 = tk.StringVar()
deck_var3 = tk.StringVar()
deck_var4 = tk.StringVar()
deck_var5 = tk.StringVar()
deck_var6 = tk.StringVar()
deck_var7 = tk.StringVar()

def submit(): # For placing input into the baseDeck array variable.
        deckInput=deck_var.get()
        baseDeck[0] = deckInput

        deckInput2=deck_var2.get()
        baseDeck[1] = deckInput2

        deckInput3=deck_var3.get()
        baseDeck[2] = deckInput3

        deckInput4=deck_var4.get()
        baseDeck[3] = deckInput4

        deckInput5=deck_var5.get()
        baseDeck[4] = deckInput5

        deckInput6=deck_var6.get()
        baseDeck[5] = deckInput6

        deckInput7=deck_var7.get()
        baseDeck[6] = deckInput7

        print(f'{deckInput}, {deckInput2}, {deckInput3}, {deckInput4}, {deckInput5}, {deckInput6}, {deckInput7}')