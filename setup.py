from setuptools import setup, find_packages

setup(
    name="cobertura-clover-transform",
    version='1.1.1',
    packages=find_packages(),
    include_package_data=True,
    description="Tools for transforming Cobertura test "
                "coverage XML into Clover-style XML",
    author='Chris Wacek',
    author_email='cwacek@gmail.com',
    url='http://github.com/cwacek/cobertura-clover-transform',
    license='MIT',
    keywords='cobertura coverage test clover xml'
)
