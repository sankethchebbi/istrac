from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="justruss",
    version="0.0.1",
    description="Truss construction and analysis",
    long_description=readme,
    license=license,
    author="Sanketh Chebbi",
    author_email="sanketh@duck.com",
    url="https://github.com/sankethchebbi/istrac",
    install_requires=["numpy", "pandas", "tabulate", "matplotlib", "scipy"],
    packages=find_packages(exclude="tests"),
)
