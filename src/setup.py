import setuptools

with open('./requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='ds4h',  
    version='1.0',
    author="",
    author_email="",
    description="",
    url="https://github.com/Kotzly/DS4H_Course",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=required,
    include_package_data=True,
    package_data={"": ["*.r", "*.R"]},
 )
