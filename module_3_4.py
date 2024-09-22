def single_root_words (root_word, *other_word):
    root_word_lower = root_word.lower()
    same_words = []
    for word in other_word:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
