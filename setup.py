import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='watermoccasin',  
     version='1.01',
     author="Alex Reich",
     author_email="watermoccasin@alexreich.com",
     description="Convert a NPR ONE news feed for offline listening with options for speed up and timed playlist",
     long_description=long_description,
     license='CC BY-SA',
     long_description_content_type="text/markdown",
     url="https://github.com/watermoccasin",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3',
 )