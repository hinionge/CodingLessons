# 30.7.2023
# CTCI Chapter 1 Q1.4

####### QUESTION: Given a string, write a function to check if it is a permutation of a palindrome.

                            # To be a permutation of a palindrome, all characters must:
                            # -- (for a palindrome of even length) occur an even number of times
                            # -- (for a palindrome of odd length) the same is true, plus one character which
                            #     must occur exactly once (the "middle" or "pivot" of the palindrome)

def PalindromePermutationCheck(stringX):
                            # Question says ignore non-letter characters; this is a placeholder e.g. to delete spaces
                            # but I haven't stripped the non-letters (or included a "same case" method)
    stringX = stringX.replace(" ","")
    tally = TallyChars(stringX)

                            # Why not set it to True and switch it off when it encounters a counterexample
    PalinPermutation = True

                            # Ok, so if the input string is of even length....
    if len(stringX) % 2 == 0:
                            # Check that all characters appear an even number of times
        AllEven = True

        for char in tally:
            if char % 2 != 0:
                AllEven = False
                            # Convert that result to the final result
        PalinPermutation = AllEven
                            # Or, if it's of odd length...
    else:
                            # There should be exactly 1 character which occurs exactly once. If that isn't true, we stop
        if tally.count(1) != 1:
            PalinPermutation = False

    return PalinPermutation



                            # Method re-used from Q1.2
def TallyChars(stringX):
    tally = [0] * 256

    for char in stringX:
        tally[ord(char)] += 1

    return tally


if __name__ == "__main__":
    stringA = "able was i ere i saw elba"

    print(PalindromePermutationCheck(stringA))