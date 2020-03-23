import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='initgitdoc',
    version='0.3.2',
    scripts=['initgitdoc'],
    author="Tralah M Brian",
    author_email="musyoki.brian@tralahtek.com",
    description="A utility to generate common git repository files, Readmes,Licenses,..etc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/TralahM/docrepo",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
