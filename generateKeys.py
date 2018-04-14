from Crypto.PublicKey import RSA

def genkey():
    keyPair = RSA.generate(1024)

    # For PrivateKey Generation

    f = open("priKey.pem", "w")
    f.write(keyPair.exportKey("PEM", "abc"))
    f.close()
    # For PublicKey Generation

    f = open("pubKey.pem", "w")
    f.write(str(keyPair.publickey().exportKey()))
    f.close()
