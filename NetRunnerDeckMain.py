# Uses the PNG files from the digital version of the Netrunner Deck for Cyberpunk RED.
# [ https://www.drivethrurpg.com/en/product/372730/netrunning-deck ] You can by the files here.
# Output opens the Cards using the default image viewer.

from PIL import Image

#using a with statement so I don't have to close the file manually.
#Needs to show in a specific size so it doesn't fill the screen.
def showCard(cardName):
        with Image.open(f"Netrunning Deck v2 Individual PNGs/{cardName}.png") as img:
            size = (206, 281)
            cardSize = img.resize(size)
            cardSize.show()


baseDeck = ['See Ya', 'Worm', 'Vrizzbolt', 'Armor', 'Sword', 'Deckkrash']
print(baseDeck)
for x in range(len(baseDeck)):
    try:
        showCard(baseDeck[x])
    except:
         continue #If the Card is not found then it will just continue so the next one.
