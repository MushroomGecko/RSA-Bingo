# RSABingoBoardGenerator.py easily creates an RSA bingo board for your class
# The minimum RSA size allowed for a 1 byte char is 90. Anything lower may produce an error

import rsa
import random
import argparse

if __name__ == "__main__":

    # Required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--board-name", type=str, required=True, help="Name of bingo board")
    parser.add_argument("--rsa-size", type=int, required=True, help="RSA encryption size")
    args = parser.parse_args()

    bingo_chars = ['B', 'I', 'N', 'G', 'O']
    board_size = 5
    used_nums = []
    lower = 1
    upper = 15

    board = open(args.board_name + ".txt", 'w')
    boardAns = open(args.board_name + "AnswerKey.txt", 'w')

    board.write(args.board_name + '\n' + '\n')
    boardAns.write(args.board_name + " Answer Key" + '\n' + '\n')

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
            (pubkey, privkey) = rsa.newkeys(args.rsa_size)
            crypto = rsa.encrypt(chr(rand).encode('utf8'), pubkey)
            board.write("Position On Board: " + c + "," + str(n + 1) + '\n')
            board.write("Encrypted Number: " + str(crypto) + '\n')
            board.write("n: " + str(privkey.n) + '\n')
            board.write("e: " + str(privkey.e) + '\n')

            boardAns.write(str("Position On Board: " + c + "," + str(n + 1)) + '\n')
            boardAns.write("Encrypted Number: " + str(crypto) + '\n')
            boardAns.write("n: " + str(privkey.n) + '\n')
            boardAns.write("e: " + str(privkey.e) + '\n')
            boardAns.write("p: " + str(privkey.p) + '\n')
            boardAns.write("q: " + str(privkey.q) + '\n')
            boardAns.write("d: " + str(privkey.d) + '\n')
            boardAns.write("Decrypted Number: " + str(ord(rsa.decrypt(crypto, privkey).decode('utf8'))) + '\n')

            board.write('\n')
            boardAns.write('\n')
        board.write('\n')
        boardAns.write('\n')

        lower += 15
        upper += 15
        used_nums.clear()

    board.close()
    boardAns.close()
