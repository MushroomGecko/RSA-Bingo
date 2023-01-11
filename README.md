# RSA-Bingo
A form of bingo where students must crack RSA public key value n to find p and/or q to decrypt numbers on their bingo board. The intent of this project is to get students familiar with the Pollard's Rho and/or Pollard's P-1 RSA cracking algorithms as well as getting them familiar with RSA in general.

## Generating an RSA Bingo Board
This is intended for instructor use so the instructor can give each student participating in this activity an RSA bingo board. Creating an RSA Bingo Board is as simple as running the RSABingoBoardGenerator.py file. There are only two arguments which you need to worry about. --board-name which is the name of the board you wish to generate, and --rsa-size which is the RSA size of each square of the board. Running this outputs a playing board and an answer key board.

## Using an RSA Bingo Board
Students will be given a play board and the intructor will have an answer key board for every play board. Play boards have an n value, e value, an encrypted bingo board number that must be decrypted, and a board position telling the student what spot of the bingo board the decrypted number corresponds to. Once the student has decrypted every given number, they should have a completely filled out, normal looking bingo board. Answer key boards are used to confirm decrypted student boards and/or to help students if they are stuck.

## Decryptors
Instructors may choose to give out one of two decryptors to their students so they may decrypt a square of their board with the p and/or q values they have found. This directory contains two types of decryptors. The easy mode decryptor calculates q given a found p value, and also calculates private value d. The hard mode decryptor has the students manually calculate/find both q and d. There are no command line arguments for these files, so students must edit the given decryptor file manually to see their unencrypted board number.

## Pollard
This directory contains two files; PollardSolution.py and PollardTimeTest.py. The intent of this exercice is for students to create their on Pollard algorithms to crack the n value of an RSA key, but PollardSolution.py can be given to students who are having a particularly difficult time creating a Pollard algorithm of their own. There are four command line arguments for this file. --n takes in the RSA n value that is trying to be factored, --threads takes in the number of threads one wishes to run this program with (this is optional and defaults to 1 thread), and --do-rho and --do-p1 take in either 1 or 0 to activate or deactivate a specific Pollard algorithm (both default to 1). PollardTimeTest.py can be ignored as it is mainly meant for testing out optimizations for PollardSolution.py.
