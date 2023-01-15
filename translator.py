import eng_to_ipa as ipa
from PIL import Image
import tkinter as tk

vowels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ʊ", "u", "ɪ", "ə", "i", "e", "ɔ", "æ"]
consonants = ["b", "ʧ", "d", "f", "g", "h", "ʤ", "k", "l", "m", "n", "ŋ", "p", "r", "s", "ʃ", "t", "θ", "ð", "v", "w", "y", "z", "ʒ"]

def separate_words(phrase: str) -> list:
    result = []
    word = ""
    for letter in phrase:
        if letter == ' ':
            if word != "":
                result.append(word)
                word = ""
        else:
             word += letter
    if word != "":
        result.append(word)
    return result

# Key for Multi Letter Vowels
# ɑr = 1
# eɪ = 2
# ɪr = 3
# ɛr = 4
# aɪ = 5
# ər = 6
# oʊ = 7
# ɔɪ = 8
# aʊ = 9
# ʊr = 0

def convert_to_ipa(phrase: list) -> list:
    result = []
    for word in phrase:
        new_word = None
        if word[0] == "*":
            new_word = word
        else:
            new_word = ipa.convert(word)
        new_word = new_word.replace("ˈ", "")
        new_word = new_word.replace("ˌ", "")
        new_word = new_word.replace(",", "")
        new_word = new_word.replace(".", "")
        new_word = new_word.replace("*", "")
        new_word = new_word.replace("ɑr", "1")
        new_word = new_word.replace("eɪ", "2")
        new_word = new_word.replace("ɪr", "3")
        new_word = new_word.replace("ɛr", "4")
        new_word = new_word.replace("aɪ", "5")
        new_word = new_word.replace("ər", "6")
        new_word = new_word.replace("oʊ", "7")
        new_word = new_word.replace("ɔɪ", "8")
        new_word = new_word.replace("aʊ", "9")
        new_word = new_word.replace("ʊr", "0")
        new_word = new_word.replace("ɛ", "e")
        new_word = new_word.replace("ɑ", "ɔ")
        print(new_word)
        result.append(new_word)
    return result

def separate_pairs(word: str) -> list:
    result = []
    i = 0
    while(i < len(word)):
        char = word[i]
        if i == len(word)-1:
            result.append(char)
            i+=1
        elif consonants.count(char) != 0:
            next = word[i+1]
            if vowels.count(next) != 0:
                result.append(char + next)
                i+=2
            else:
                result.append(char)
                i+=1
        elif vowels.count(char) != 0:
            next = word[i+1]
            if consonants.count(next) != 0:
                result.append(char + next)
                i+=2
            else:
                result.append(char)
                i+=1
        else:
            i+=1
    return result

def pair_to_image(pair: str):
    result = Image.open(r"Letters/empty.png")
    if len(pair) == 1:
        img1 = Image.open(r"Letters/"+ pair +".png")
        result.paste(img1, (0,0), mask = img1)
    else:
        img1 = Image.open(r"Letters/"+ pair[0] +".png")
        img2 = Image.open(r"Letters/"+ pair[1] +".png")
        result.paste(img1, (0,0), mask = img1)
        result.paste(img2, (0,0), mask = img2)
        if vowels.count(pair[0]) != 0:
            dot = Image.open(r"Letters/dot.png")
            result.paste(dot, (0,0), mask = dot)
    return result

def append_image(img1, img2):
    w1 = img1.size[0]-15
    width = w1+img2.size[0]
    height = img1.size[1]
    result = Image.new("RGBA", (width,height), (0,0,0,0))
    result.paste(img1, (0,0), mask = img1)
    result.paste(img2, (w1,0), mask = img2)
    return result

def combine_words(img1, img2):
    w1 = img1.size[0]+100
    width = w1+img2.size[0]
    height = img1.size[1]
    result = Image.new("RGBA", (width,height), (0,0,0,0))
    result.paste(img1, (0,0), mask = img1)
    result.paste(img2, (w1,0), mask = img2)
    return result

def add_bg(img):
    result = Image.new("RGBA", img.size, (255,255,255,255))
    result.paste(img, (0,0), mask = img)
    return result

def translate(phrase: str):
    word_list = separate_words(phrase)
    ipa_list = convert_to_ipa(word_list)
    print(ipa_list)
    split_list = []
    for word in ipa_list:
        split_word = separate_pairs(word)
        print(split_word)
        split_list.append(split_word)
    result = None
    print(split_list)
    for word in split_list:
        word_result = None
        for pair in word:
            pimg = pair_to_image(pair)
            if word_result == None:
                word_result = pimg
            else:
                word_result = append_image(word_result,pimg)

        if result == None:
            result = word_result
        else:
            result = combine_words(result, word_result)
    result = add_bg(result)
    return result

def translate_input():
    translation = translate(entry.get())
    translation.show()
    
window = tk.Tk()
text = tk.Label(text="Enter text to be translated. Use * to denote a word already in IPA.")
text.pack()
entry = tk.Entry(width=50)
entry.pack()
button = tk.Button(window, text="Translate", command= translate_input)
button.pack()
window.mainloop()