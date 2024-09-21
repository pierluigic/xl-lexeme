import setuptools
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements
from os import path

__version__ = '0.0.1'
here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
# parse_requirements() returns generator of pip._internal.req.req_file.ParsedRequirement objects
session = PipSession()
install_reqs = parse_requirements('requirements.txt', session=session)

# reqs is a list of requirement
try:
    reqs = [str(ir.req) for ir in install_reqs]
except:
    reqs = [str(ir.requirement) for ir in install_reqs]

reqs.append('sentence-transformers')

setuptools.setup(
    name="WordTransformer",
    version=__version__,
    author="Pierluigi Cassotti",
    description="WiC Pretrained Model for Cross-Lingual LEXical sEMantic changE",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/pierluigic/xl-lexeme",
    packages=setuptools.find_packages(),
    platforms=['all'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=reqs
)
