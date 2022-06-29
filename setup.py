from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tiejan/__init__.py
from tiejan import __version__ as version

setup(
	name="tiejan",
	version=version,
	description="Tiejan Customizations",
	author="Neeraj VK",
	author_email="neerajvkn@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
