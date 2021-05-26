import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()    

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='ds4h',  
    version='0.1',
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kotzly/DS4H_Course",
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
    include_package_data=True,
    package_data={"": ["*.r", "*.R"]},
 )
