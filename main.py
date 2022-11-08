
def is_it_palind(word):
# Assume it's a palindrome: switch this to false as soon as a pair doesn't match
    palind = True
# Variable for length of string
    c = len(word)
# Variable for the character toward the end of the string
    e = c
# Loop using variable for character toward the start of the string
    for s in range (c):
# Subtract the count from the length; deal with the zero indexing with a -1
        e = c-s-1
#        print (word[s],word[e])
# Do the check!
        if word[s] != word[e]:
            palind = False

    return palind



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    word = input("Word to check:")

# Option to discount spaces
#    word = word.replace(" ", "")

    print (is_it_palind(word))