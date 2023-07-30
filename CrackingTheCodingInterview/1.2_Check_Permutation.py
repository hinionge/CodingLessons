# 30.7.2023
# CTCI Chapter 1 Q1.2

####### QUESTION: Given two strings, write a method to determine if one is a permutation of the other.

def CheckPermutation(stringA,stringB):

    Permutation = True

                            # Array will contain two elements, each being a list
    compare = []

                            # Create both lists
                            # Each list is a simple tally of all characters from ASCII 0-255
    compare.append(TallyChars(stringA))
    compare.append(TallyChars(stringB))

                            # If those tallies do not match exactly, then it cannot be a permutation
    if compare[0] != compare[1]:
        Permutation = False

    return Permutation


def TallyChars(stringX):
    tally = [0] * 256

    for char in stringX:
        tally[ord(char)] += 1

    return tally



if __name__ == "__main__":
    A = "carthorse"
    B = "orchestra"

    print(CheckPermutation(A,B))