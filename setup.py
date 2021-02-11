import setuptools

requirements = ["apache-airflow", "requests"]

setuptools.setup(
    name="airflow_trifacta",
    version="0.1.0",
    description="Hooks, sensors and operators for the Trifacta API",
    author="Glenn Russell",
    author_email="glennadjrussell@gmail.com",
    install_requires=requirements,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/glennadjrussell/airflow_trifacta",
    license="MIT license",
)

