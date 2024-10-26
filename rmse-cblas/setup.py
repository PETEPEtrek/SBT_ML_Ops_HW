from setuptools import setup, find_packages
from glob import glob

so_files = glob("rmse_cblas/python/linalg_core*.so")

setup(
    name="rmse_cblas",
    version="0.1",
    description="RMSE with Python bindings",
    packages=find_packages(),
    package_data={
        "rmse_cblas": ["python/*.so"],
    },
)
