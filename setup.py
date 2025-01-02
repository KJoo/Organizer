from setuptools import setup, find_packages

setup(
    name="organizer",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tqdm",
        "py7zr",
        "schedule",
        "rarfile",
        "termcolor",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "organize=organizer.core:main",
        ],
    },
    description="A flexible file organization tool with scheduling and configuration support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="KJoo",
    author_email="kjoo@example.com",
    url="https://github.com/KJoo/organizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
