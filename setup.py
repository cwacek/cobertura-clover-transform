from setuptools import setup, find_packages

setup(
    name="cobertura-clover-transform",
    version='1.1.4',
    packages=find_packages(),
    include_package_data=True,
    description="Tools for transforming Cobertura test "
                "coverage XML into Clover-style XML",
    install_requires=['lxml'],
    author='Chris Wacek',
    author_email='cwacek@gmail.com',
    url='http://github.com/cwacek/cobertura-clover-transform',
    license='MIT',
    keywords='cobertura coverage test clover xml',
    entry_points = {
        'console_scripts': [
            'cobertura-clover-transform=cobertura_clover_transform.converter:main'
        ]
    }
)
