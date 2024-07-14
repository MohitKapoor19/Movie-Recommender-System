from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "coding-raja-technologies-internship"
AUTHOR_USER_NAME = "MohitKapoor19"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
    'streamlit',
    'pandas',
    'requests',
    'numpy',
    'scikit-learn'
]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohitKapoor19/coding-raja-technologies-internship",
    author_email="mohit22csu349@ncuindia.edu",
    packages=find_packages(where=SRC_REPO),
    package_dir={"": SRC_REPO},
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
