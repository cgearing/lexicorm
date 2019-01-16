import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lexicorm',
    version='0.0.4',
    author='Chris Gearing',
    author_email="chrisagearing@outlook.com",
    description="An ORM helper package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cgearing/lexicorm',
    packages=setuptools.find_packages(exclude=['test', 'test.*']),
    python_requires=">=3.6",
    install_requires=[
        'sqlalchemy>=1.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
