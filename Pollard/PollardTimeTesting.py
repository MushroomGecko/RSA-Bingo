import argparse
import gmpy2
from gmpy2 import mpz
import rsa
import time
# to measure factoring time
from timeit import default_timer as timer

########## Pollard Rho Testing ##########
def PollardRhoBase(n, rand):
    start = timer()
    i = 1
    x = gmpy2.mpz_random(gmpy2.random_state(rand), n-1)
    y = x
    k = 2
    while True:
        i += 1
        x = gmpy2.powmod((pow(x, 2)-1), 1, n)
        d = gmpy2.gcd(y-x, n)
        if d != 1 and d != n:
            return timer() - start
        if i == k:
            y = x
            k = k * 2

def PollardRhoMPZ(n, rand):
    start = timer()
    i = mpz(1)
    x = gmpy2.mpz_random(gmpy2.random_state(rand), n-1)
    y = x
    k = mpz(2)
    while True:
        i = gmpy2.add(i, 1)
        x = gmpy2.powmod((pow(x, 2)-1), 1, n)
        d = gmpy2.gcd(gmpy2.sub(y, x), n)
        if d != 1 and d != n:
            return timer() - start
        if i == k:
            y = x
            k = gmpy2.mul(mpz(k), 2)

########## PollardP1 Testing ##########
def PollardP1Base(n):
    start = timer()
    a = 2
    B = 2
    while True:
        a = gmpy2.powmod(a, B, n)
        g = gmpy2.gcd((a-1), n)
        if g != 1 and g != n:
            return timer() - start
        B += 1

def PollardP1MPZ(n):
    start = timer()
    a = mpz(2)
    B = mpz(2)
    while True:
        a = gmpy2.powmod(mpz(a), B, n)
        g = gmpy2.gcd(mpz(a-1), n)
        if g != 1 and g != n:
            return timer() - start
        B = gmpy2.add(B, 1)

########## Multi Threaded Testing ##########
def PollardRhoBaseMulti(num_processes, size):
    time_var = int(time.time())
    processes = num_processes
    t1 = 0
    for i in range(1,processes+1):
        (pubkey, privkey) = rsa.newkeys(size)
        t1 = t1 + PollardRhoBase(privkey.n, time_var)
        time_var = time_var + 10000
    print("Pollard Base Avg:", t1/i)

def PollardRhoMPZMulti(num_processes, size):
    time_var = int(time.time())
    processes = num_processes
    t1 = 0
    for i in range(1,processes+1):
        (pubkey, privkey) = rsa.newkeys(size)
        t1 = t1 + PollardRhoMPZ(privkey.n, time_var)
        time_var = time_var + 10000
    print("Pollard MPZ Avg:", t1/i)

def PollardP1BaseMulti(num_processes, size):
    time_var = int(time.time())
    processes = num_processes
    t1 = 0
    for i in range(1,processes+1):
        (pubkey, privkey) = rsa.newkeys(size)
        t1 = t1 + PollardP1Base(privkey.n)
        time_var = time_var + 10000
    print("P1 Base Avg:", t1/i)

def PollardP1MPZMulti(num_processes, size):
    time_var = int(time.time())
    processes = num_processes
    t1 = 0
    for i in range(1,processes+1):
        (pubkey, privkey) = rsa.newkeys(args.rsa_size)
        t1 = t1 + PollardP1MPZ(privkey.n)
        time_var = time_var + 10000
    print("P1 MPZ Avg:", t1/i)

if __name__ == "__main__":
    # Required command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--rsa-size", type=int, required=True, help="Number to factor")
    parser.add_argument("--processes", type=int, required=False, default=1, help="Number of process to run")
    parser.add_argument("--do-rho", type=int, required=False, default=1, help="Activate Pollard's Rho. 0 to deactivate, 1 to activate (defaulted to 1)")
    parser.add_argument("--do-p1", type=int, required=False, default=1, help="Activate Pollard's P-1. 0 to deactivate, 1 to activate (defaulted to 1)")
    args = parser.parse_args()

    if args.do_rho > 0:
        PollardRhoBaseMulti(args.processes, args.rsa_size)
        PollardRhoMPZMulti(args.processes, args.rsa_size)
    if args.do_p1 > 0:
        PollardP1BaseMulti(args.processes, args.rsa_size)
        PollardP1MPZMulti(args.processes, args.rsa_size)

# Links to sites that inspired my Pollard's P-1
# https://www.geeksforgeeks.org/pollard-p-1-algorithm/
# https://www.cs.purdue.edu/homes/ssw/cs355/2009f.pdf
# https://www.untruth.org/~josh/math/pollard-p-1.pdf
# https://gist.github.com/leogemetric/8e0344df87e5ae880de81a031f26bc62