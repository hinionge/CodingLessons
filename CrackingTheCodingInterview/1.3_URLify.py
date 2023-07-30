# 30.7.2023
# CTCI Chapter 1 Q1.3

####### QUESTION: Write a method to replace all spaces in a string with '%20'

                            # There is a simple library function in Python to do this: $string.replace(" ","%20")
                            # Commented out working method using it, here:
# def URLify(stringX):
#     stringX = stringX.replace(" ","%20")
#     return stringX

                            # Here is another way:

def URLify(stringX):
                            # create empty string
    newstring = ""
                            # just go through the string character by character
    for char in stringX:
                            # if a sppace is found, add the escape code
        if char == " ":
            newstring += "%20"
                            # otherwise just copy exactly
        else:
            newstring += char

    return newstring

if __name__ == "__main__":
    X = "THIS IS THE NEWS"

    print(URLify(X))