from setuptools import setup, find_packages

setup(
    name="cobertura-clover-transform",
    version='1.1.4.post1',
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    entry_points = {
        'console_scripts': [
            'cobertura-clover-transform=cobertura_clover_transform.converter:main'
        ]
    }
)
