import fileinput,string,math,random

## gibify
##    Arguments
##        word: a string of characters to be turned into gibberish keeping the
##         first and last characters in place and ignoring non-letters Assumes
##         input is one word, without any spaces (it will work ine if spaces
##         exist but it will only ignore the first and last letters it sees in
##         the string so to qualify as "Gibberish" this would have to be true)
##    Return
##        a string that has been turned into gibberish
##    Method
##        loops through characters of the word, appends the indices of the
##         letters to an array.  Removes first and last indices and performs the
##         swap.
##        swap: new_indices is a jumbled version of swappable_char_indices where each
##        index in new_indices is the future index of the corresponding index in
##        swappable_char_indices. For example if swappable_char_indices =
##        [1,2,3] and new_indices = [3,2,1] for the word "brave", we place
##        chars[1] in its new home, chars[3] such that the word reads "brare"
##        and we continue until our word reads "bvare"

def gibify(word):
    
##    swappable_char_indices: an array of indices into word
    swappable_char_indices=[] 
    for i,char in enumerate(word):
        if char in string.ascii_letters: # Only appends letters
            swappable_char_indices.append(i)
            
##    check if word actually needs to be jumbled, if not then return
    if len(swappable_char_indices)>3 and not word.isupper():
        swappable_char_indices.pop(0) # remove first char
        swappable_char_indices.pop()  # remove last char

        chars = list(word)
        new_indices = swappable_char_indices[:]
        
##        keep a copy of the chars array so we can swap in place without
##        loosing our data
        chars_copy = chars[:]
        random.shuffle(new_indices)
        for original_i,new_i in zip(swappable_char_indices,new_indices):
            chars[new_i]=chars_copy[original_i]
        return "".join(chars)
    else:
        return word

for line in fileinput.input():
    output=""
    tokens = line.split(" ")
    for token in tokens:
        output+=gibify(token)+" "
    print output[:-1] #trims the last space that we added
