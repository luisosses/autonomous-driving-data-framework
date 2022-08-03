import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    version="0.1.0",
    description="A Airflow Dag for extracting rosbag topics and labelling images with ML Models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="kevinsoucy",
    install_requires=[
        "aws-cdk-lib==2.20.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Apache License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Typing :: Typed",
    ],
)
