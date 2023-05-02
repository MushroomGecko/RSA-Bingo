# RSABingoBoardGenerator.py easily creates an RSA bingo board for your class
# The minimum RSA size allowed for a 1 byte char is 90. Anything lower may produce an error

import rsa
import random
import argparse
import os

if __name__ == "__main__":

    # Required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--board-name", type=str, required=True, help="Name of bingo board")
    parser.add_argument("--rsa-size", type=int, required=True, help="RSA encryption size")
    args = parser.parse_args()

    bingo_range = []
    if args.rsa_size == 0:
        bingo_range = [80, 90, 100, 110, 120]
    else:
        bingo_range = [args.rsa_size]
    bingo_chars = ['B', 'I', 'N', 'G', 'O']
    board_size = 5
    used_nums = [1]
    lower = 1
    upper = 15

    board_path_base = os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Boards" + "\\" + args.board_name
    board_path_ans = os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Answer Keys" + "\\" + args.board_name
    if not os.path.isdir(os.getcwd()+"\\"+ "RSABingoBoards"):
        os.mkdir(os.getcwd()+"\\"+ "RSABingoBoards")
    if not os.path.isdir(os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Boards"):
        os.mkdir(os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Boards")
    if not os.path.isdir(os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Answer Keys"):
        os.mkdir(os.getcwd()+"\\"+ "RSABingoBoards" + "\\" + "Answer Keys")
    if not os.path.isdir(board_path_base):
        os.mkdir(board_path_base)
    if not os.path.isdir(board_path_ans):
        os.mkdir(board_path_ans)


    board = open(board_path_base + "\\"  + args.board_name + ".txt", 'w')
    boardAns = open(board_path_ans + "\\" + args.board_name + "AnswerKey.txt", 'w')

    board.write(args.board_name + " - (RSA Size of " + str(bingo_range[0]) + " to " + str(bingo_range[len(bingo_range)-1]) + ")" + '\n' + '\n')
    boardAns.write(args.board_name + " Answer Key" + " - (RSA Size of " + str(bingo_range[0]) + " to " + str(bingo_range[len(bingo_range)-1]) + ")" + '\n' + '\n')

    for c in bingo_chars:
        spacers = 10
        letter = '#' * spacers + " " + c + " " + '#' * spacers + "\n"
        board.write(letter)
        boardAns.write(letter)

        for n in range(board_size):

            if c == 'N' and n == 2:
                board.write(str("Position On Board: " + c + "," + str(n + 1)) + '\n')
                board.write("FREE SPACE" + '\n')

                boardAns.write(str("Position On Board: " + c + "," + str(n + 1)) + '\n')
                boardAns.write("FREE SPACE" + '\n')

                board.write('\n')
                boardAns.write('\n')

                continue

            rand = random.randint(lower, upper)
            while rand in used_nums:
                rand = random.randint(lower, upper)
            used_nums.append(rand)
            rsa_size = bingo_range[random.randint(0, len(bingo_range) - 1)]
            (pubkey, privkey) = rsa.newkeys(rsa_size)
            crypto = pow(rand, privkey.e, privkey.n)
            board.write("Position On Board: " + c + "," + str(n + 1) + '\n')
            board.write("RSA Size: " + str(rsa_size) + '\n')
            board.write("Encrypted Number: " + str(crypto) + '\n')
            board.write("n: " + str(privkey.n) + '\n')
            board.write("e: " + str(privkey.e) + '\n')

            boardAns.write(str("Position On Board: " + c + "," + str(n + 1)) + '\n')
            boardAns.write("RSA Size: " + str(rsa_size) + '\n')
            boardAns.write("Encrypted Number: " + str(crypto) + '\n')
            boardAns.write("n: " + str(privkey.n) + '\n')
            boardAns.write("e: " + str(privkey.e) + '\n')
            boardAns.write("p: " + str(privkey.p) + '\n')
            boardAns.write("q: " + str(privkey.q) + '\n')
            boardAns.write("d: " + str(privkey.d) + '\n')
            boardAns.write("Decrypted Number: " + str(pow(crypto, privkey.d, privkey.n)) + '\n')

            board.write('\n')
            boardAns.write('\n')
        board.write('\n')
        boardAns.write('\n')

        lower += 15
        upper += 15
        used_nums.clear()

    board.close()
    boardAns.close()
