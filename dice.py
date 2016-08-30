#
# Q(3)
# import the needed libraries
import random as rnd
import numpy

# move dice function:
# direction is the list, with m x n
# current_location is the pointer to the dice current cell in the board. for the
# first time it is [0][0]
# dice is the initial or
def movedice(direction,current_loc,dice):
    dice_move = ["up", "left"]
    current_face = dice
    dice_val = []
    n = 0
    mv = rnd.choice(dice_move)
    while cmp(current_loc,direction) == -1:
        if mv == "up":
            current_loc[0] = current_loc[0] + 1
            if current_loc[0] <= direction[0]:
                # move dice to up : top , bot,  left, right, front, back ---> back, front, left, right, top, bot
                new_face = [current_face[5], current_face[4], current_face[2], current_face[3], current_face[0],current_face[1]]
                current_face = new_face
                dice_val.append(new_face[0])
                n = n + 1
                mv = rnd.choice(dice_move)
            else:
                current_loc[0] = direction[0]
                mv = "left"
        if mv == "left":
            current_loc[1] = current_loc[1] + 1
            if current_loc[1] <= direction[1]:
                # move diec left: top, bot, left, right, front, back ---> right, left, top, bot, front, back
                new_face = [current_face[3], current_face[2], current_face[0], current_face[1], current_face[4],current_face[5]]
                current_face = new_face
                dice_val.append(current_face[0])
                n = n + 1
                mv = rnd.choice(dice_move)
            else:
                current_loc[1] = direction[1]
                mv = "up"
    else:
        return sum(dice_val)
#
# function main initialize the program and call the function.
if __name__ == '__main__':
    m, n = 5,5      # board max m, and n
    rolls = 610      # No. of the times of rolls.
    way_val = []    # the list of sum of the faces in each roll
    # defaults of the dice faces numbers
    # dice faces for start is suppose to be: top, bot, left, right, front, back
    init_dice = [1, 6, 3, 4, 2, 5]
    # initialize the board
    board = numpy.zeros((m,n)).tolist()
    for i in range(m):
        for j in range(n):
            board[i][j] = [i,j]
    # call the function in n = rolls times.
    for i in range(rolls):
        way_val.append( movedice(board[3][3],[0,0],init_dice))
    # print the roll results in n = 'rolls' times:
    print 'Times to roll: ', rolls #,' Results: ',way_val
    print 'Minimum way to target: ', min(way_val)
    print 'Times to reach the minimum path: ', way_val.count(min(way_val))
