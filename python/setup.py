from setuptools import setup

DESCRIPTION = "Generate JANcode"
NAME = "jancode"
AUTHOR = "kota"
AUTHOR_EMAIL = "52403688+yashikota@users.noreply.github.com"
URL = "https://github.com/yashikota/jancode"
LICENSE = "MIT"
DOWNLOAD_URL = URL
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.6"
PACKAGES = [
    "jancode"
]
KEYWORDS = "jancode"
CLASSIFIERS=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6"
]
with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
)
