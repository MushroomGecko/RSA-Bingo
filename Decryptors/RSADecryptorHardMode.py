# RSADecryptorHardMode.py makes you calculate both q and d values used in decryption
# If your instructor gave you this for decryption, thank them for appreciating your RSA cracking knowledge and abilities
# All you have to do is input various values and the encrypted message into the blank variables
# The printed result is the number used on your board

import rsa

if __name__ == "__main__":
    n = None  # Given n value
    e = None  # Given e value
    p = None  # Calculated p value from your Pollard's Rho or Pollard's P-1 implementation
    q = None  # Calculated q value from your Pollard's Rho or Pollard's P-1 implementation
    d = None  # Calculated d value
    message = None  # Given encrypted message

    privkey = rsa.PrivateKey(n, e, d, p, q)
    print("Decrypted Board Number:", ord(rsa.decrypt(message, privkey).decode('utf8')))