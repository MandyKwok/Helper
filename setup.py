from setuptools import setup, find_packages

setup(
    name = 'lazyhelpers',
    version = "0.0.7",
    author = "lazy",
    author_email = "lg2691@nyu.edu",
    license = 'MIT',
    description = "Cheatsheet for handy functions",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"" : "src"},
    packages = find_packages(where = "src"),
    python_requires = ">=3.6",
    url = 'https://github.com/MandyKwok/Helper',
#     py_modules = ['visualization']
)
