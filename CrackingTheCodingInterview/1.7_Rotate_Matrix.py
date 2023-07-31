# 31.7.2023
# CTCI Chapter 1 Q1.7

####### QUESTION: (part 1) Given an image of N x N, where each pixel is an integer, rotate the image 90 degrees.

                            # Method to display the image visually (just easier for me to check it's working)
def DisplayGrid(Image):
    Output = ""
    for y in range(len(Image)):
        for x in range(len(Image)):
            Output += str(Image[y][x])
        Output += "\n"

    print(Output)

                            # Very simple method reads columns upwards from the corner, writes them as rows
def RotateGrid(Image):
    Rotated = []
    for y in range(len(Image)):
        temp = []
        for x in range(len(Image)):
            temp.append(Image[len(Image)-x-1][y])
        Rotated.append(temp)

    return Rotated



####### QUESTION: (part 2) Can you do this in place?









if __name__ == "__main__":
                            # Example 'image'' to work with
    Image = [[1,2,3],[4,5,6],[7,8,9]]

    DisplayGrid(Image)

    Image = RotateGrid(Image)

    DisplayGrid(Image)