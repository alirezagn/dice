# Import the needed libraries
import random as rnd
import numpy

# Move dice function
def movedice(direction, current_loc, dice):
    dice_move = ["up", "left"]
    current_face = dice
    dice_val = []
    mv = rnd.choice(dice_move)
    
    while current_loc != direction:
        if mv == "up":
            current_loc[0] = current_loc[0] + 1
            if current_loc[0] <= direction[0]:
                # Move dice to up: top, bot, left, right, front, back ---> back, front, left, right, top, bot
                new_face = [current_face[5], current_face[4], current_face[2], current_face[3], current_face[0], current_face[1]]
                current_face = new_face
                dice_val.append(new_face[0])
                mv = rnd.choice(dice_move)
            else:
                current_loc[0] = direction[0]
                mv = "left"
        if mv == "left":
            current_loc[1] = current_loc[1] + 1
            if current_loc[1] <= direction[1]:
                # Move dice left: top, bot, left, right, front, back ---> right, left, top, bot, front, back
                new_face = [current_face[3], current_face[2], current_face[0], current_face[1], current_face[4], current_face[5]]
                current_face = new_face
                dice_val.append(current_face[0])
                mv = rnd.choice(dice_move)
            else:
                current_loc[1] = direction[1]
                mv = "up"
    return sum(dice_val)

# Main function
if __name__ == '__main__':
    m, n = 5, 5  # Board max m and n
    rolls = 610  # No. of times of rolls
    way_val = []  # The list of sum of the faces in each roll
    
    # Defaults of the dice faces numbers
    init_dice = [1, 6, 3, 4, 2, 5]  # Dice faces: top, bot, left, right, front, back
    
    # Initialize the board
    board = numpy.zeros((m, n)).tolist()
    for i in range(m):
        for j in range(n):
            board[i][j] = [i, j]
    
    # Call the function in n = rolls times.
    for i in range(rolls):
        way_val.append(movedice(board[3][3], [0, 0], init_dice))
    
    # Print the roll results
    print('Times to roll: ', rolls)
    print('Minimum way to target: ', min(way_val))
    print('Times to reach the minimum path: ', way_val.count(min(way_val)))
