import setuptools
from pathlib import Path

__version__ = '0.0.2'
here = Path(__file__).resolve().parent

def load_requirements():
    requirements_path = here / 'requirements.txt'
    if not requirements_path.exists():
        return []

    lines = requirements_path.read_text().splitlines()
    requirements = []
    for line in lines:
        stripped = line.split('#', 1)[0].strip()
        if stripped:
            requirements.append(stripped)
    return requirements

reqs = load_requirements()
reqs.append('sentence-transformers')

setuptools.setup(
    name="WordTransformer-LanguageChange",
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
