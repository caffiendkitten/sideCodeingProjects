import hashlib

def cyclePasswordList(hash, dictionary):
    for word in dictionary:
        word = word.rstrip()
        # print("word: ",type(hash))
        hashed_word = hashlib.sha1(word.encode())
        if hashed_word.hexdigest() == hash:
            return word
    return "PASSWORD NOT IN DATABASE"

def cycleSalts(hash, saltList, dictionary):
    for saltz in saltList:
        saltz = saltz.rstrip()
        # print("salt: ", saltz)
        for word in dictionary:
            word = word.rstrip()
            # print("word: ", word)
            frontSalt = saltz + word
            endSalt = word + saltz

            # print("frontSalt: ", frontSalt)
            # print("endSalt: ", endSalt)
            frontSaltHashedWord = hashlib.sha1(frontSalt.encode())
            endSaltHashedWord = hashlib.sha1(endSalt.encode())
            # print("frontSaltHashedWord: ", frontSaltHashedWord.hexdigest())
            # print("endSaltHashedWord: ", endSaltHashedWord.hexdigest())
            # print(hash)
            # hashed_word2 = str(frontSalt) + str(hashlib.sha1(word.encode()))
            if (frontSaltHashedWord.hexdigest() == hash) or (endSaltHashedWord.hexdigest() == hash):
                return word

    return "PASSWORD NOT IN DATABASE"


def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt") as file_handle:
        dictionary = file_handle.readlines()
    if use_salts == False:
        return cyclePasswordList(hash, dictionary)
    else:
        with open("known-salts.txt") as file_handle:
            saltList = file_handle.readlines()
        return cycleSalts(hash, saltList, dictionary)