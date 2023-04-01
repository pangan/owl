from setuptools import setup


setup(
 name = "owl",
 version = "0.0.1",
 entry_points={
     'console_scripts': ['owl = src.main:foo',]
 },
 packages = ['src']
)
