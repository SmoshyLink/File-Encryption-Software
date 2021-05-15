#take message string
#encrypt and print
#decrypt and print

import random

#HELPER FUNCTION: check if numbers are coprime
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

#HELPER FUNCTION: check if integers are primes
def isPrime(numb):
    if numb == 2:
        return True
    if numb < 2 or numb % 2 == 0:
        return False
    for n in range(3, int(numb**0.5)+2, 2):
        if numb % n == 0:
            return False
    return True

#list of prime numbers global variable
primes = [i for i in range(0,100) if isPrime(i)]

#HELPER FUNCTION: finding d
def mod_inverse(a,b):
    x1=0
    x2=1
    y1=1
    y2=0
    a_unchanged=a
    b_unchanged=b

    while b !=0:
        q=a//b
        r=a-(q*b)
        x=x2-(q*x1)
        y=y2-(q*y1)
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    if x2<0:
        x2+=b_unchanged
    if y2<0:
        y2+=a_unchanged
    return x2



#Generate a pair of public and private keys
def create_keys():
    p = random.choice(primes)
    q = random.choice(primes)
    while p==q:
        q=random.choice(primes)
    #find n
    n = p*q

    phi=(p-1)*(q-1)

    #find e such that e and phi are coprime
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #find d
    d = mod_inverse(e, phi)

    #return public and private key tuples
    return ((e,n),(d,n))

#Function to encrypt plaintext
def encrypt(publikKey, plainText):
    
    e, n = publikKey
    cipherText = [(ord(char) ** e) % n for char in plainText]
    return cipherText

#function to decrypt ciphertext
def decrypt(privateKey, cipherText):
    
    d, n = privateKey
    plainText = [chr((char ** d) % n) for char in cipherText]
    return ''.join(plainText)


#### RUN PROGRAM ####------------------------
print("You have chosen RSA encryption\nGenerating keys......")
publicKey, privateKey = create_keys()
print("Public key: ",publicKey, "\nPrivate key: ", privateKey)
plainText=input("Type a message to encrypt: ")
cipherText=encrypt(publicKey, plainText)
print("This is your cipher text: ", ''.join(map(str, cipherText)))
print("Now decrypting......")
print("This is your decrypted text: ", decrypt(privateKey, cipherText))