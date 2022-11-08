from setuptools import find_packages, setup
import os
import io
import re


def parse_requirements_file(filename):
    with open(filename, encoding="utf-8") as fid:
        requires = [line.strip() for line in fid.readlines() if line]
    return requires


# Optional Packages
EXTRAS = {
    "dev": parse_requirements_file("environments/requirements-dev.txt"),
    "tests": parse_requirements_file("environments/requirements-test.txt"),
}


# Get version number (function from GPyTorch)
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = find_version("alti_tools", "__init__.py")
readme = open("README.md").read()


setup(
    name="alti_tools",
    version=version,
    # author="M2Lines",
    author_email="",
    packages=find_packages(".", exclude=["tests"]),
    license="LICENSE",
    description="Lightweight ML Template",
    long_description=readme,
    long_description_content_type="text/markdown",
    # project_urls={
    #     "Documentation": "https://jaxsw.readthedocs.io/en/latest/",
    #     "Source": "https://github.com/jejjohnson/jaxsw",
    # },
    setup_requires=["setuptools-yaml"],
    metadata_yaml="environments/environment.yaml",
    install_requires=parse_requirements_file("environments/requirements.txt"),
    extras_require=EXTRAS,
    keywords=["ml template wandb"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
