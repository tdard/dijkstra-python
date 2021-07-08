from setuptools import setup, find_packages

setup(
    name="dijkstra",
    version="0.1",
    description="Utilitaries for building graph and computing shortest path using Dijkstra algorithm",
    author="Tristan Dardoize",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
