# 29.7.2023
# CTCI Chapter 1 Q1.1

####### QUESTION: (part 1) Implement an algorithm to determine if a string has all unique characters

def AllCharsUnique(StringToCheck):
                            # Set a boolean to be flipped if a repeated character occurs
    AllUnique = True
                            # Create an array of size 256, each element set to zero
                            # (I'm not convinced that array multiplication is good coding behaviour, but it works)
    AllChars = [0] * 256
                            # When the string is checked, character by character, the element in this array
                            # whose index is the ASCII code for the character will increment by one
                            # Therefore, if ever one of those numbers becomes two, the string does not
                            # contain all unique characters

                            # Incremental counter to move through the string
    CharToCheck = 0

                            # Done as a while loop to enable a shortcut out if a match is found
    while CharToCheck < len(StringToCheck):
                            # Read a character and stores its ASCII code as a variable
        CharCode = ord(StringToCheck[CharToCheck])
                            # Add one to the relevant index in the character-count array
        AllChars[CharCode] += 1
                            # Increment to next character to check
        CharToCheck +=1
                            # This checks that no character has yet repeated: if it finds a repeat,
                            # sets the boolean to False, and then exits the while loop by meeting its condition
                            # (after one single match there is no need to check any more characters)
        if AllChars.count(2) > 0:
            AllUnique = False
            CharToCheck = len(StringToCheck)
                            # Return the boolean
    return AllUnique



# ###### QUESTION (part 2) What if you cannot use additional data structures?

def AllCharsUnique_InPlace(StringToCheck):
    AllUnique = True

                            # I feel like this method is somehow cheating, given it uses a built-in Python thing?
                            # Literally just goes through character by character and then checks to see if that
                            # character only occurs once.
    for char in StringToCheck:
        if StringToCheck.count(char) > 1:
            AllUnique = False

    return AllUnique



if __name__ == "__main__":
    UserChoice = input("String to check: ")
    print(AllCharsUnique(UserChoice))
    print(AllCharsUnique_InPlace(UserChoice))