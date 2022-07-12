from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Curl_Req low level requests library'
LONG_DESCRIPTION = 'Python Wrapper for high performance requests for large systems'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="curl_req", 
        version=VERSION,
        author="David Marko",
        author_email="info@davidmarko.me",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests', 'pycurl'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'curl_req', 'requests', 'pycurl'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)