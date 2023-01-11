# RSADecryptorEasyMode.py calculates the private values d and q used in the private key for you
# If your instructor gave you this for decryption, thank them for not giving you extra work
# All you have to do is input various values and the encrypted message into the blank variables
# The printed result is the number used on your board

import rsa

if __name__ == "__main__":
    n = None  # Given n value
    e = None  # Given e value
    p = None  # Calculated p value from your Pollard's Rho or Pollard's P-1 implementation
    message = None  # Given encrypted message
    q = n // p
    d = pow(e, -1, ((p - 1) * (q - 1)))


    privkey = rsa.PrivateKey(n, e, d, p, q)
    print("Decrypted Board Number:", ord(rsa.decrypt(message, privkey).decode('utf8')))
