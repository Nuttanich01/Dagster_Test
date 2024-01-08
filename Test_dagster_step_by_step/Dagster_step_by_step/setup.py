from setuptools import find_packages, setup

setup(
    name="Dagster_step_by_step",
    packages=find_packages(exclude=["Dagster_step_by_step_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
