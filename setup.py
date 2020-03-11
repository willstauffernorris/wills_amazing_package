# setup.py
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="wills_amazing_package",
    version="1.1",
    author="Will SN",
    author_email="willsn@gmail.com",
    description="Testing packages",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/willstauffernorris/wills_amazing_package",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)