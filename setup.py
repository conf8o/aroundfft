from setuptools import setup
from setuptools import find_packages


setup(
    name="aroundfft",
    version="0.1.0",
    license="MIT",
    description="高速フーリエ変換まわりのやつ",
    author="conf8o",
    url="https://github.com/conf8o",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
