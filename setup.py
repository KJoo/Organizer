from setuptools import setup, find_packages

setup(
    name="organizer",
    version="1.0.0",
    packages=find_packages(),  # Automatically finds 'organizer' package
    entry_points={
        "console_scripts": [
            "organize=organizer.core:main",  # Maps the `organize` command to `main` in `core.py`
        ],
    },
    include_package_data=True,
    data_files=[
        ("config", ["config.yaml"]),  # Ensures `config.yaml` is included
    ],
    install_requires=[
        "setuptools>=40.0.0",  # Ensure setuptools is installed
        "tqdm",
        "py7zr",
        "schedule",
        "rarfile",
        "termcolor",
        "PyYAML",
    ],
    description="A flexible file organization tool with scheduling and configuration support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/username/organizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

