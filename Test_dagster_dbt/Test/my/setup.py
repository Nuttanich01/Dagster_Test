from setuptools import find_packages, setup

setup(
    name="my",
    packages=find_packages(exclude=["my_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
