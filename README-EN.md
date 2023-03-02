[![English badge](https://img.shields.io/badge/%E8%8B%B1%E6%96%87-English-blue)[![English badge](https://img.shields.io/badge/%E8%8B%B1%E6%96%87-English-blue)](https://github.com/RedForestLonvor/cryptwood/blob/main/README-EN.md)
[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Simplified%20Chinese-blue)](https://github.com/RedForestLonvor/cryptwood/blob/main/README.md)

# [cryptwood](https://pypi.org/project/cryptwood/)

Encryption tools for protecting private data


# install

install through pip：

```bash
python3 -m pip install cryptwood
```


# overview

Through this tool, a python object can be quickly serialized and encrypted, and then stored in
with the code directory in the project. At this point, objects that exist in the code can be deleted. In wishing to use this object
When you only need to decrypt and deserialize.  

In this way, sensitive information (or any information that you don't want others to see) can be avoided from appearing directly in the
In the code, there is no need to appear in the project file in plain text.

Objects to be serialized and encrypted can be of any type, including custom classes. If using an object of a custom class,
It is necessary to ensure that the class exists when decrypting.  

This tool uses the AES256 algorithm to encrypt data symmetrically.
During the encryption process, the secret key and initial vector are randomly generated. These files will be stored in`~/.cryptUserDataKey`.


# scenes

&emsp;Use this tool to encrypt your information when you need to present projects or hand in assignments to classmates, teachers, etc. (or just for security).
Like encrypting your database`username`,`passwd`,`host`。

&emsp;Use this tool to encrypt a key object when you need to show a project to a client,
Make this project only run on your computer, or only after you authorize it.

# function

+ `cryptwood.dataCrypter.decrypt(object)`:  
  Encrypt the object object and generate an encrypted serialized file in the code directory`.cryptUserData`, no return.  
  Generated`key`and`iv`files are stored in`~/.cryptUserData`folder. The folder name is the code that calls this function
   's parent directory location + "key" or "iv".
+ `cryptwood.dataCrypter.decrypt()`:  
  Decrypts `.cryptUserData` and deserializes, returning an object.


# TODO

+ Provide a method to save `key` and `iv` in remote server using `ssh` for higher security, and the author
  Provide users with real-time code authorization to protect author rights.
+ Provides a method to encrypt multiple classes at the same time
+ Provides a method to store `key` and `iv` in the database for greater security, and the author
  Provide users with real-time code authorization to protect author rights.