# Tunic Translator
# Goals:
Convert english into phonetic spelling
Map phonetic spellings to symbols
Combine vowels and consonants
Display finished product
Maybe:
GUI output
GUI input
Big Maybe:
Reverse translation

# Planning:
English phrases will be converted to lists of words
English words will be strings
Those words will be converted to strings of phonetic characters
Vowels and consonants will be paired together to create a list of strings, each string corresponding to one Tunic rune

# List of phonetic spellings and representations
I might just use the IPA standard though, but I'll have to map multiple IPA characters to the same symbol

# Possible Improvements
I could break each symbol down line by line and reconstruct them as I needed them.
This would save on storage space for the images, but I would have to assign a ~7 boolean list to each sound in order to show which lines were needed.
It would also probably take longer to run since it requires a lot more paste operations, but that time might be negligible.
Considering a long passage takes a decent amount of time to translate, I don't think that time is negligable, and this would probably be really slow.