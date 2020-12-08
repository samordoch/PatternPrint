# this func will print a diamond depending on given number of rows with default of 5
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
def printDiamond(rows=5):
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

    k = rows - 2

    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")


# this func will print a word like in the nachman stickers
# n
# na
# nac
# nach
# nachm
# nachma
# nachman
def printNachmanStylePyramid(word="nachman moman"):
    x = ""
    for i in word:
        x += i
        print(x)


# this func will print a half pyramid that counts up to the given parm defualt is 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
def printCountingHalfPyramid(rows=5):
    for row in range(1, rows + 1):
        for column in range(1, row + 1):
            print(column, end=' ')
        print("")


# this func will print a downward pyramid with the given parm as height defualt is 5
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
def printDownwardPyramid(rows=5):
    k = 2 * rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")
