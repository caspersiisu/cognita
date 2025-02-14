from setuptools import setup, find_packages

setup(
    name="cognita",
    version="0.0.1",
    description="Cognita SDK: An AI-driven research workflow for automated knowledge discovery.",
    author="Caspersiisu",
    url="https://github.com/caspersiisu/cognita",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
