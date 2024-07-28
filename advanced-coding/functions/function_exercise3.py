# txt = "Hello World"[::-1]
# print(txt)

# attempt 1
# def master_yoda(sentence):
#    return sentence[::-1]

# my_text = master_yoda("Fear is the path to the dark side.")
# print(my_text)

def master_yoda(sentence):
    # creating list of words
    words = []
    for word in sentence.split(' '):
        words.append(word)

    terminator = ""
    # If the sentence ends with a dot(.) we need to extract that
    if words[-1].endswith('.') or words[-1].endswith('?'):
        terminator = words[-1][-1]
        words[-1] = words[-1][:-1]

    # reversing the words
    words.reverse()

    # recreating the sentence with reversed words
    new_sentence = " ".join(words)
    new_sentence = new_sentence + terminator
    return new_sentence


print(master_yoda("I am learning Python."))
print(master_yoda("Hello World"))