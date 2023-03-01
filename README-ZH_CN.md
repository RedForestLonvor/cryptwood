[![English badge](https://img.shields.io/badge/%E8%8B%B1%E6%96%87-English-blue)](./README.md)
[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-Simplified%20Chinese-blue)](https://github.com/RedForestLonvor/cryptwood/blob/main/README-ZH_CN.md)

# [cryptwood](https://pypi.org/project/cryptwood/)

用于保护隐私数据的加密工具


# 安装

可以使用pip安装：

```bash
python3 -m pip install cryptwood
```


# 概述

通过这个工具，可以快速的序列化一个python对象并对其进行加密，然后存储在
与项目中的代码目录下。这时，就可以将存在于代码中的对象删除。在希望使用这个对象
的时候只需要解密并反序列化即可。  

通过这样的方式，可以避免敏感信息（或者是一切不希望别人看到的信息）不用直接出现在
代码中，也不用明文出现在项目文件中。

被序列化并加密的对象可以是任何类型，包括自定义的类。如果使用自定义类的对象，
在解密时需要保证类存在。  

这个这个工具使用了AES256算法对数据进行对称加密。
加密过程中随机产生秘钥和初始向量。 这些文件将被存储在`~/.cryptUserDataKey`中。


# 使用场景

&emsp;当你需要向同学，老师等人展示项目或交作业时（或者仅仅为了安全），使用此工具加密你的信息。
比如加密你的数据库`username`,`passwd`,`host`等信息。

&emsp;当你需要向客户展示项目时，使用此工具加密一个关键的对象，
使这个项目只能在你的电脑，或者只有你进行授权以后才能运行。


# 函数

+ `cryptwood.dataCrypter.decrypt(object)`:  
  加密object对象并在代码目录下生成加密过的序列化文件`.cryptUserData`，没有返回值。  
  生成的`key`和`iv`文件存储在`~/.cryptUserData`文件夹下。文件名为调用此工具的代码
  所在位置的上级目录+"key"或"iv"。
+ `cryptwood.dataCrypter.decrypt()`:
  解密`.cryptUserData`并反序列化，返回一个对象。


# TODO

+ 提供使用`ssh`将`key`和`iv`保存在远程服务器的方法，以便于更高的安全性，以及作者
  向用户提供实时的代码授权以保护作者权益。
+ 提供同时间加密多个类的方法
+ 提供将`key`和`iv`存储在数据库中的方法以便于更高的安全性，以及作者
  向用户提供实时的代码授权以保护作者权益。