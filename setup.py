from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="testfooproject",
    version="release/0.0.0rc0",
    description="TEST",
    long_description=long_description,
    long_description_content_type="text/markdown",
        
    author="aletgn",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT license",
        "Operating System :: OS Independent",
    ],
    
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    
    extras_require={"test" : ["notebook"],
                    "dev" : ["pytest", "twine", "setuptools", "build"]}
)
