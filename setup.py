# Copyright (C) 2020  Johannes Kepler University Linz, Institute of Networks and Security
# Copyright (C) 2020  CDL Digidow <https://www.digidow.eu/>
#
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
# the European Commission - subsequent versions of the EUPL (the "Licence").
# You may not use this work except in compliance with the Licence.
# 
# You should have received a copy of the European Union Public License along
# with this program.  If not, you may obtain a copy of the Licence at:
# <https://joinup.ec.europa.eu/software/page/eupl>
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='arcface',
    version='0.0.7',
    author="Philipp Hofer",
    author_email="philipp.hofer@ins.jku.at",
    description="ArcFace face recognition implementation in Tensorflow Lite.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mobilesec/arcface-tensorflowlite",
    packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
    install_requires=[
          "tensorflow>=2.3.0",
          "pyyaml>=5.3",
          "opencv-python>=4.4",
          "numpy",
          "requests>=2.24.0",
          "errno",
      ],
    extras_require = {
          'testing': [
                "pytest-runner",
                "pytest"
             ],
          'default_model': [
              "astropy"
            ]
      },
    license="European Union Public Licence 1.2 (EUPL 1.2)",
    classifiers=[
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    include_package_data=False,
)
