def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if (len(root_word) < len(i) and root_word.lower() in i.lower()) or (len(root_word) > len(i) and i.lower() in root_word.lower()):
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)