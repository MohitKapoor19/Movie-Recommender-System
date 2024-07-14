from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "coding-raja-technologies-internship"
AUTHOR_USER_NAME = "MohitKapoor19"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/MohitKapoor19/take_two",
    author_email="mohit22csu349@ncuindia.edu",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
