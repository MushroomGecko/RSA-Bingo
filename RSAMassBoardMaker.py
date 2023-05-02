import os

board_name = "Board"
num_boards = 100
rsa_size = 100
for i in range(num_boards):
    os.system("python RSABingoBoardGenerator.py --board-name " + board_name + str(i+1) + " --rsa-size " + str(rsa_size))