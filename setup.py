import setuptools

setuptools.setup(
    name="face_detection",
    version="0.2.1",
    author="Originally: Håkon Hukkelås, modifications by: Johannes Kolbe",
    description="A simple and lightweight package for state of the art face detection with GPU support.",
    long_description="".join(open("README.md", "r").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/johko/DSFD-Pytorch-Inference",
    python_requires='>=3.6',
    license="apache-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "torch>=1.6",
        "torchvision>=0.3.0",
    ],
    packages=setuptools.find_packages()
)
