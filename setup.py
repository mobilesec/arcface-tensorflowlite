# Licensed under the EUPL.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='arcface',
    version='0.0.2',
    author="Philipp Hofer",
    author_email="philipp.hofer@ins.jku.at",
    description="ArcFace face recognition implementation in Tensorflow Light.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mobilesec/arcface-tensorflowlight",
    packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
    install_requires=[
          "tensorflow>=2.0.0",
          "pyyaml>=5.3",
          "opencv-python>=4.4",
          "numpy<1.19.0",
          "requests>=2.24.0"
      ],
    tests_require=['pytest'],  
    license="European Union Public Licence 1.2 (EUPL 1.2)",
    classifiers=[
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    include_package_data=False,
)
