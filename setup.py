import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="ploo",
  version="0.0.1",
  author="Tripboi",
  author_email="tripboi817@gmail.com",
  description="Make random loop for tripbois",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)