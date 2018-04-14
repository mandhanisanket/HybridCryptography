import os
import sys
import zipfile
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# File name to decrypt
f_name = ""

# Private key password: (Given keys have no password)
priPass = ""


def usage():
    print "python decipher.py <file_name>"
    sys.exit(-1)


def sigVerification(pubKey_fname, f_name):
    # Generating decrypted file's SHA-256

    h = SHA256.new()
    h.update(open(f_name, "r").read())

    # Reading public key to check signature with

    keyPair = RSA.importKey(open(pubKey_fname, "r").read())
    keyVerifier = PKCS1_v1_5.new(keyPair.publickey())

    # If signature is right, prints SHA-256. Otherwise states that the file is not authentic

    if keyVerifier.verify(h, open(f_name + ".sig", "r").read()):
        print "The signature is authentic."
        print "SHA-256 -> %s" % h.hexdigest()
    else:
        print "The signature is not authentic."


def keyReader(privKey_fname, f_name, priPass):
    # Reading private key to decipher symmetric key used

    keyPair = RSA.importKey(open(privKey_fname, "r").read(), passphrase=priPass)
    keyDecipher = PKCS1_OAEP.new(keyPair)

    # Reading iv and symmetric key used during encryption

    f = open(f_name + ".key", "r")
    iv = f.read(16)
    k = keyDecipher.decrypt(f.read())

    return k, iv


def decipher(keyA_fname, keyB_fname, f_name, priPass):
    # Getting symmetric key used and iv value generated at encryption process

    k, iv = keyReader(keyB_fname, f_name, priPass)

    # Deciphering the initial information and saving it to file with no extension

    keyDecipher = AES.new(k, AES.MODE_CFB, iv)
    bin = open(f_name + ".bin", "rb").read()
    f = open(f_name.split('.')[0], "wb")
    f.write(keyDecipher.decrypt(bin))
    f.close()

    # Running a Signature verification

    sigVerification(keyA_fname, f_name)


def auxFilesUnzip(all):
    # Opening the input file

    f = zipfile.ZipFile(all + ".all", "r")

    # Extracting all of its files

    f.extractall()


def cleanUp(sig, key, bin):
    # Removing all of the files created, except for the final deciphered file

    os.remove(sig)
    os.remove(key)
    os.remove(bin)


def checkFiles(f_name, pubKey, priKey, first_run):
    # Checking for decrypting file's existence and access, keys, aux and output files

    if first_run:
        # Checking for decrypting file's existence and access

        if not os.path.isfile(f_name + ".all") or not os.access(f_name + ".all", os.R_OK):
            print "Invalid file to decrypt. Aborting..."
            sys.exit(1)

        # Checking for public key's existence and access

        if not os.path.isfile(pubKey) or not os.access(pubKey, os.R_OK):
            print "Invalid public key file. Aborting..."
            sys.exit(6)

        # Checking for private key's existence and access

        if not os.path.isfile(priKey) or not os.access(priKey, os.R_OK):
            print "Invalid private key file. Aborting..."
            sys.exit(7)

    elif not first_run:
        # Checking if all of the necessary files exist and are accessible

        if not os.path.isfile(f_name + ".sig") or not os.access(f_name + ".sig", os.R_OK):
            print "Invalid *.sig file. Aborting..."
            sys.exit(2)
        if not os.path.isfile(f_name + ".key") or not os.access(f_name + ".key", os.R_OK):
            print "Invalid *.key file. Aborting..."
            sys.exit(3)
        if not os.path.isfile(f_name + ".bin") or not os.access(f_name + ".bin", os.R_OK):
            print "Invalid *.bin file. Aborting..."
            sys.exit(4)

        # Checking if in case of output file's existence, it is writable

        if os.path.isfile(f_name) and not os.access(f_name, os.W_OK):
            print "Can't create output file. Aborting..."
            sys.exit(5)
