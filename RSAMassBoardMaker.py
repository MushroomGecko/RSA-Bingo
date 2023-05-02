import os

board_name = "Board2"
num_boards = 5
rsa_size = 0
for i in range(num_boards):
    os.system("python RSABingoBoardGenerator.py --board-name " + board_name + str(i+1) + " --rsa-size " + str(rsa_size))