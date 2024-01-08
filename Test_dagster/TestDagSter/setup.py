from setuptools import find_packages, setup

setup(
    name="TestDagSter",
    packages=find_packages(exclude=["TestDagSter_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
