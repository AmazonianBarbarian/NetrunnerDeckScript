# Uses the PNG files from the digital version of the Netrunner Deck for Cyberpunk RED.
# [ https://www.drivethrurpg.com/en/product/372730/netrunning-deck ] You can by the files here.
# Output opens the Cards using the default image viewer.

from PIL import Image # For pulling images and formating them.
import tkinter as tk # For adding GUI elements to a python script.

#using a with statement so I don't have to close the file manually.
#Needs to show in a specific size so it doesn't fill the screen.
def showCard(cardName):
        with Image.open(f"Netrunning Deck v2 Individual PNGs/{cardName}.png") as img:
            size = (206, 281)
            cardSize = img.resize(size)
            cardSize.show()



baseDeck = [ "See Ya", 'Worm', 'Vrizzbolt', 'Armor', 'Sword', 'Deckkrash', 'Shield']

# GUI code
#---------------------------------------------------------------------------------------------------------------------------------
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

def deckList(): # pulls list Cyberdeck loadout from a text file called deckList.txt and places it within the baseDeck Array
      premadeDeck = open('deckList.txt', 'r')
      i = 0
      for line in premadeDeck:
            baseDeck[i] = line.strip()
            i = i + 1
      
      premadeDeck.close()
      print(baseDeck)
            
     

deckEntry = tk.Entry(loadDeck, textvariable=deck_var)
deckEntry.pack(pady=20) # "pady={someNumber}" places the text field lower vertically in the window.

deckEntry2 = tk.Entry(loadDeck, textvariable=deck_var2)
deckEntry2.pack(pady=20)

deckEntry3 = tk.Entry(loadDeck, textvariable=deck_var3)
deckEntry3.pack(pady=20)

deckEntry4 = tk.Entry(loadDeck, textvariable=deck_var4)
deckEntry4.pack(pady=20)

deckEntry5 = tk.Entry(loadDeck, textvariable=deck_var5)
deckEntry5.pack(pady=20)

deckEntry6 = tk.Entry(loadDeck, textvariable=deck_var6)
deckEntry6.pack(pady=20)

deckEntry7 = tk.Entry(loadDeck, textvariable=deck_var7)
deckEntry7.pack(pady=20)

submit_button = tk.Button(loadDeck, # Meant to submit the info entered into the fields above.
                        text="Submit", 
                        font=('Arial', 18), 
                        command = submit)
submit_button.pack()

close_button = tk.Button(loadDeck, # Meant to submit the info entered into the fields above.
                        text="Close", 
                        font=('Arial', 18), 
                        command = loadDeck.destroy)
close_button.pack()

prebuit_button = tk.Button(loadDeck, # Meant to submit the info entered into the fields above.
                        text="From Decklist", 
                        font=('Arial', 18), 
                        command = deckList)
prebuit_button.pack()

loadDeck.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------
# GUI code
print(baseDeck)
for x in range(len(baseDeck)):
    try:
        showCard(baseDeck[x])
    except:
         continue #If the Card is not found then it will just continue so the next one.
