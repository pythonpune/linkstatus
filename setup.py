from setuptools import find_packages
from setuptools import setup


with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = ["markdown"]

setup_requirements = ["setuptools_scm"]

setup(
    author="Nikhil Dhandre",
    author_email="nik.digitronik@live.com",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.5",
    description="Simple text/ markdown links status checker",
    entry_points={"console_scripts": ["linkstatus=linkstatus:main"]},
    install_requires=install_requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    setup_requires=setup_requirements,
    use_scm_version=True,
    keywords="linkstatus, linkchecker, link-checker, markdown, text, linklint",
    name="linkstatus",
    packages=find_packages(include=["linkstatus"]),
    url="https://github.com/digitronik/linkstatus",
    license="GPLv3",
    zip_safe=False,
)
