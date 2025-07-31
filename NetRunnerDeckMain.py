# Uses the PNG files from the digital version of the Netrunner Deck for Cyberpunk RED.
# [ https://www.drivethrurpg.com/en/product/372730/netrunning-deck ] You can by the files here.
# Output opens the Cards using the default image viewer.

import tkinter as tk # For adding GUI elements to a python script.
import module_netrunner as mod

#using a with statement so I don't have to close the file manually.
#Needs to show in a specific size so it doesn't fill the screen.


# GUI layout code
#---------------------------------------------------------------------------------------------------------------------------------

deckEntry = tk.Entry(mod.loadDeck, textvariable=mod.deck_var)
deckEntry.pack(pady=10) # "pady={someNumber}" places the text field lower vertically in the window.

deckEntry2 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var2)
deckEntry2.pack(pady=10)

deckEntry3 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var3)
deckEntry3.pack(pady=10)

deckEntry4 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var4)
deckEntry4.pack(pady=10)

deckEntry5 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var5)
deckEntry5.pack(pady=10)

deckEntry6 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var6)
deckEntry6.pack(pady=10)

deckEntry7 = tk.Entry(mod.loadDeck, textvariable=mod.deck_var7)
deckEntry7.pack(pady=10)

deckListEntry = tk.Entry(mod.loadDeck, textvariable=mod.deckSubmit_var)

submit_button = tk.Button(mod.loadDeck, # Meant to submit the info entered into the fields above.
                        text="Enter and Load from Fields", 
                        font=('Arial', 18), 
                        command = mod.submit)
submit_button.pack()

deckListEntry.pack(pady=10) #Field for entering the deck list text file.

prebuit_button = tk.Button(mod.loadDeck, # Meant to add to the array from a deck list.
                        text="Enter and Load from Decklist", 
                        font=('Arial', 18), 
                        command = mod.deckList)
prebuit_button.pack()


close_button = tk.Button(mod.loadDeck, # Meant to close the GUI after Submitting.
                        text="Close after loading Deck", 
                        font=('Arial', 18), 
                        command = mod.loadDeck.destroy)
close_button.pack(pady=10)

mod.loadDeck.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------
# GUI layout code

for x in range(len(mod.baseDeck)):
    try:
        mod.showCard(mod.baseDeck[x])
    except:
         print(f"Potential Error: Card {mod.baseDeck[x]}.png at postition {x + 1} not found or left empty! Did you type it in correctly?")
         # Position is based on the Card number, ex: 5th ot 6th card, not the position in the Array.
         continue #If the Card is not found then it will just continue so the next one.
