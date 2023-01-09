# Goals:
# Convert english into phonetic spelling
# Map phonetic spellings to symbols
# Combine vowels and consonants
# Display finished product (Image? Ascii?)
# Maybe:
# GUI output
# GUI input
# Big Maybe:
# Reverse translation

# Planning:
# English phrases will be converted to lists of words
# English words will be strings
# Those words will be converted to lists of phonetic characters
# Converted phrases will be lists of lists of phonetic characters

# List of phonetic spellings and representations
# I might just use the IPA standard though, but I'll have to map multiple IPA characters to the same symbol
# Vowels: ee, a, ih, eh, ah, uu, oo, up, er, ur, ar, or, ow, ay, oh, i, oy, ?
# Consonants: p, b, t, d, k, g, ch, j, f, v, th, Th, s, z, sh, zh, h, m, n, ng, l, r, y, w

import eng_to_ipa as ipa

def separate_words(phrase):
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

print(separate_words("deez nuts fortnite battle pass"))