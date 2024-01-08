from setuptools import find_packages, setup

setup(
    name="test_dag_postgres",
    packages=find_packages(exclude=["test_dag_postgres_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
