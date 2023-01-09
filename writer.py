from tkinter import *
from tkinter.ttk import *

# characters are arrays of booleans of length 15
# 32768 different characters

class Phrase():
    def __init__(self, list):
        self.char_list = list
        self.length = len(self.char_list)
        for c in self.char_list:
            if len(c) != 15 or 0:
                raise Exception("Invalid Character Length")

def phrase_append(phrase,character):
    if len(character) != 15 and len(character) != 0:
        raise Exception("Invalid Character Length")
    phrase.append(character)

c1 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
c2 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
c3 = []
p1=[[],[]]
print(p1)
phrase_append(p1,c1)
print(p1)

window = Tk()
window.title("Tunic Writer")
lbl_title = Label(text="dfjkslfjdsfnjdsfjndskfhjdksfhndsfkhdjsdjsk")
lbl_title.pack()
window.mainloop()
