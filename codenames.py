from nltk.tokenize import word_tokenize
import nltk
import re
import tkinter as tk
import random

## passage --------------------------------------------------------------
with open("passage.txt", encoding='utf8') as file:
    passage = file.read().replace("\n","")

##print(passage)

## word filter ----------------------------------------------------------
sentences = re.split(r'[.“:?;]',passage)

words = []
count = 0

for sentence in sentences:
    if len(sentence) < 2:
        continue
    while not sentence[0].isalpha():
        sentence = sentence[1:]
    while not sentence[-1].isalpha():
        sentence = sentence[:-1]    
    sentence += ". "
    
    lot = nltk.pos_tag(word_tokenize(sentence))
    for pair in lot:
        word, word_type = pair[0].upper(), pair[1]
        if len(word) < 4:
            continue
        elif (word_type in ('NN','VB','NNP','JJ') and (word not in words)):
            words.append(word)
            
## color chart --------------------------------------------------------

colors = []
for i in range(7): #neutral
   colors.append('#ebe6df')
for i in range(9): #red team
   colors.append('#edb9af')
for i in range(8): #blue team
   colors.append('#b6c2f0')
for i in range(1): #black
   colors.append('#a4a1a6')


#tkinter ------------------------------------------------------------
root = tk.Tk()

mainframe = tk.Frame(root, height=810, width=690, bg='white')
mainframe.pack(fill=tk.BOTH, expand=True)

def refresh(event=None):
    random.shuffle(words)
    random.shuffle(colors)
   
    values = []
    num = 0 
    for i in range(5):
        for j in range(5):
            values.append((words[num],
                        i * 130 + 30,
                        j * 70 + 20,
                        colors[num]))
            values.append((words[num],
                        i * 130 + 30,
                        j * 70 + 450,
                        '#ebe6df'))
            num += 1

    for value in values: 
        tk.Label(mainframe, text = value[0],
                width = 15, height = 3,
                bg = value[3]).place(x = value[1], y = value[2]) #individual words
    return 

generate_button = tk.Button(mainframe, text = "Generate",
         width = 15, height = 3,
         command = refresh).place(x = 290, y = 370) #refresh button
root.bind('g',refresh)
root.mainloop()
