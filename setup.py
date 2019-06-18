import setuptools
import senscritiquescraper

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="senscritiquescraper",
    version=senscritiquescraper.__version__,
    author="dbeley",
    author_email="dbeley@protonmail.com",
    description="Senscritique scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbeley/senscritiquescraper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=["requests", "pandas", "bs4", "lxml"],
)
