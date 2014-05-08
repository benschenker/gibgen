import fileinput, string,math,random

def gibify(word):
    swappable_char_indices=[]
    for i,char in enumerate(word):
        if i!=0 and char in string.ascii_letters:
            swappable_char_indices.append(i)
    
    if len(swappable_char_indices)>2 and not word.isupper():
        swappable_char_indices.pop()
        return swap(word,swappable_char_indices)
    else:
        return word

def swap(word,indices):
    chars = list(word)
    new_indices = indices[:]
    random.shuffle(new_indices)
    chars_copy = chars[:]
    for i,j in zip(indices,new_indices):
        chars[j]=chars_copy[i]
    return "".join(chars)

for line in fileinput.input():
    output=""
    tokens = line.split(" ")
    for token in tokens:
        output+=gibify(token)+" "
    print output[:-1]
