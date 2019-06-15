import setuptools
import senscritique_scraper

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="senscritique_scraper",
    version=senscritique_scraper.__version__,
    author="dbeley",
    author_email="dbeley@protonmail.com",
    description="Senscritique scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbeley/senscritique_scraper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "scr_get_top=senscritique_scraper.scr_get_top:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=["requests", "pandas", "bs4", "lxml"],
)
