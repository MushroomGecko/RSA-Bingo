import argparse
import gmpy2
from gmpy2 import mpz
import multiprocessing
import time
# to measure factoring time
from timeit import default_timer as timer


# Created from pseudocode in Professor Marron's notes
# takes in an n value and a seed and finds powmods and gcds of y-x and n until variable d is no longer 1 or n
def PollardRho(num, n, rand):
    start = timer()
    i = 1
    x = gmpy2.mpz_random(gmpy2.random_state(rand), n - 1)
    y = x
    k = 2
    while True:
        i = i + 1
        x = gmpy2.powmod((pow(x, 2) - 1), 1, n)
        d = gmpy2.gcd(y - x, n)
        if d != 1 and d != n:
            print("Rho Thread:", num, d)
            print("Rho Time (s):", timer() - start)
            return 1
        if i == k:
            y = x
            k = k * 2

def PollardRho2(num, n, rand):
    start = timer()
    i = 1
    x = gmpy2.mpz_random(gmpy2.random_state(rand), n - 1)
    y = x
    k = 2
    while True:
        i = i + 1
        x = (pow(x, 2) - 1) % n
        d = gmpy2.gcd(y - x, n)
        if d != 1 and d != n:
            print("Rho 2 Thread:", num, d)
            print("Rho 2 Time (s):", timer() - start)
            return 1
        if i == k:
            y = x
            k = k * 2

def g(i, n):
    return (pow(i+1, 2, n))

def PollardRhoRJ(num, n):
    start = timer()
    x = 2
    y = 2
    p = 1
    while p == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        p = gmpy2.gcd(abs(x - y), n)
    if p == n:
        return -1
    else:
        print("Rho RJ Thread:", num, p)
        print("Rho RJ Time (s):", timer() - start)

# Inspired from Geeks For Geeks, Purdue, untruth.org, and a github project (Links to all below)
# Takes in a thread number and an n value. a starts as 2 and B starts as 2. a is the powmod of itself to the B power mod n. g then uses a to fnd the gcd of a-1 and n to see if a factored occurred.
def PollardP1(num, n):
    start = timer()
    a = 2
    B = 2
    while True:
        a = gmpy2.powmod(a, B, n)
        g = gmpy2.gcd((a - 1), n)
        if g != 1 and g != n:
            print("P-1 Thread:", num, g)
            print("P-1 Time (s):", timer() - start)
            return 1
        B = B + 1

# Meant to invoke multiprocessing for Pollard Rho
def PollardRhoMulti(num_processes, num):
    time_var = int(time.time())
    processes = num_processes
    for i in range(1, processes + 1):
        t1 = multiprocessing.Process(target=PollardRho, args=(i, num, time_var,))
        t1.start()
        time_var = time_var + 10000

# Meant to invoke multiprocessing for Pollard Rho
def PollardRho2Multi(num_processes, num):
    time_var = int(time.time())
    processes = num_processes
    for i in range(1, processes + 1):
        t1 = multiprocessing.Process(target=PollardRho2, args=(i, num, time_var,))
        t1.start()
        time_var = time_var + 10000

def PollardRhoRJMulti(num_processes, num):
    # time_var = int(time.time())
    processes = num_processes
    for i in range(1, processes + 1):
        t1 = multiprocessing.Process(target=PollardRhoRJ, args=(i, num))
        t1.start()
        # time_var = time_var + 10000


# Meant to invoke multiprocessing for Pollard P-1 (inspired sources version)
def PollardP1Multi(num_processes, num):
    processes = num_processes
    for i in range(1, processes + 1):
        t1 = multiprocessing.Process(target=PollardP1, args=(i, num,))
        t1.start()


if __name__ == "__main__":
    # Required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True, help="RSA number n to factor")
    parser.add_argument("--threads", type=int, required=False, default=1, help="Number of threads to run")
    parser.add_argument("--do-rho", type=int, required=False, default=1, help="Activate Pollard's Rho. 0 to deactivate, 1 to activate (defaulted to 1)")
    parser.add_argument("--do-p1", type=int, required=False, default=1, help="Activate Pollard's P-1. 0 to deactivate, 1 to activate (defaulted to 1)")
    parser.add_argument("--do-rj", type=int, required=False, default=1, help="Activate Pollard's P-1. 0 to deactivate, 1 to activate (defaulted to 1)")
    parser.add_argument("--do-rho2", type=int, required=False, default=1, help="Activate Pollard's P-1. 0 to deactivate, 1 to activate (defaulted to 1)")
    args = parser.parse_args()

    factor = mpz(args.n)

    if args.do_rho2 > 0:
        PollardRho2Multi(args.threads, factor)
    if args.do_rho > 0:
        PollardRhoMulti(args.threads, factor)
    if args.do_p1 > 0:
        PollardP1Multi(args.threads, factor)
    if args.do_rj > 0:
        PollardRhoRJMulti(args.threads, factor)

# Links to sites that inspired my Pollard's P-1
# https://www.geeksforgeeks.org/pollard-p-1-algorithm/
# https://www.cs.purdue.edu/homes/ssw/cs355/2009f.pdf
# https://www.untruth.org/~josh/math/pollard-p-1.pdf
# https://gist.github.com/leogemetric/8e0344df87e5ae880de81a031f26bc62
