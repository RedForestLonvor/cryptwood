import pickle
import inspect
from cryptwood import AES256cryptor
import os
import configparser

# config = configparser.ConfigParser()
# config.read('config.ini')
# DEFAULT_KEY_PATH = config.get('PathConfig','KEY_PATH')

DEFAULT_KEY_PATH = 'HOMEPATH'

class fileManager():

    @staticmethod
    def getKeyPath(projectPath):
        homePath = os.path.expanduser('~')if DEFAULT_KEY_PATH == "HOMEPATH" else DEFAULT_KEY_PATH

        keyPath = os.path.join(homePath,".cryptUserDataKey",(projectPath.replace(os.sep, '_')).replace(":",''))
        return keyPath

    @staticmethod
    def getCiphertextPath(projectPath):
        projectPath = os.path.join(projectPath,".cryptUserData")
        return projectPath

    @staticmethod
    def addToFile(cryptAns, key, iv, path):
        keyPath = fileManager.getKeyPath(path)
        directory = os.path.dirname(keyPath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(keyPath+"key", 'wb') as file:
            file.write(key)
        with open(keyPath + "iv", 'wb') as file:
            file.write(iv)
        with open(fileManager.getCiphertextPath(path), "wb") as file:
            file.write(cryptAns)

class dataCrypter:

    @staticmethod
    def encrypt(userData):
        key = os.urandom(32)
        projectPath = os.path.dirname(inspect.stack()[1].filename)
        dumpData = pickle.dumps(userData)
        cryptAns, iv = AES256cryptor.aes_cbc_encrypt(key=key, plaintext=dumpData)
        fileManager.addToFile(cryptAns,key, iv ,projectPath)

    @staticmethod
    def decrypt():
        projectPath = os.path.dirname(inspect.stack()[1].filename)
        keyPath = fileManager.getKeyPath(projectPath)
        with open(keyPath + "key", "rb") as file:
            key = file.read()
        with open(keyPath + "iv", "rb") as file:
            iv = file.read()
        with open(fileManager.getCiphertextPath(projectPath), "rb") as file:
            userData = file.read()
        dumpData = AES256cryptor.aes_cbc_decrypt(key=key, iv=iv, ciphertext=userData)
        return pickle.loads(dumpData)