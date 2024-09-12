from setuptools import setup, find_packages

setup(
    name="gif_downloader",
    version="0.1",
    packages=find_packages(),
    description="Lib que faz download de gifs",
    long_description=open("README.md").read(),
    long_description_content_type="Lib que faz download de gifs",
    author="Gabriel Mora",
    author_email="seu_email@example.com",
    url="https://github.com/go4Mor4/gif_downloader",
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
