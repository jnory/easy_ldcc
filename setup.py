from setuptools import setup

setup(
    name='easy_ldcc',
    version='0.0.1',
    packages=['easy_ldcc'],
    url='https://github.com/jnory/easy_lddc',
    license='MIT',
    author='Jun-ya NORIMATSU',
    author_email='',
    description='',
    install_requires=[
        "mecab-python3==0.996.3",
        "python-dateutil",
        "requests",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Japanese",
        "Programming Language :: Python :: 3 :: Only",
    ]
)
