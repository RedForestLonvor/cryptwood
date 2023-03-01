from setuptools import setup, find_packages
# import os
# import configparser
# from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# def getCustomPath():
    # while (True):
    #     customPath = input("custom directory to keep key(none for default:current user root directory):")
    #     if customPath == '':
    #         customPath = 'HOMEPATH'
    #         break
    #     if not os.path.exists(customPath):
    #         if os.path.isabs(customPath):
    #             opt = input("path not exists,creat directory(s)?(y/n)")
    #             if (opt == 'y'):
    #                 if not os.path.exists(customPath):
    #                     os.makedirs(customPath)
    #                     break
    #         else:
    #             print(r"illegal key path!(\ for windows /for linux)")
    #     elif os.path.isfile(customPath):
    #         print(r"expected directory path not file path")
    #     else:
    #         break
    # opt = input("key file will stored in " + customPath + os.sep + ".cryptUserDataKey" + "(y/n):")
    # if opt == 'n':
    #     getCustomPath()
    # return customPath

# class CustomInstallCommand(install):
#     def run(self):
#         install.run(self)
#         customPath = getCustomPath()
#         config_file = os.path.join(self.install_lib, 'cryptwood', 'config.ini')
#         open(config_file, 'a')
#         print(config_file)
#         config = configparser.ConfigParser()
#         config.read(config_file)
#         print(config_file)
#         config.add_section('PathConfig')
#         config.set('PathConfig', 'KEY_PATH', customPath)

setup(
    name='cryptwood',
    version='0.1.4',
    license='GPL-3.0',
    description=r"A tool for encrypting sensitive data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='RedForestLonvor',
    author_email='redforestlonvor@outlook.com',
    url='https://github.com/RedForestLonvor/cryptwood',
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.0'
    ],
    # entry_points={
    #     'console_scripts': [
    #         'cryptree_setup = cryptwood.setup:run_setup'
    #     ]
    # },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    # cmdclass={
    #     'install': CustomInstallCommand,
    # }
)
