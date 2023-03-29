from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cryptwood',
    version='0.1.6',
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
