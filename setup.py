from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    # Basic info
    name="MOvie Recommender System",      
    version="0.1.0",                      
    author="Krishna, Shreya, Jhanvi",                  
    author_email="krishnaarnuri6@gmailcom, shreyamarathe03@gmail.com, jhanvigurjar91@gmail.com",
    description="Content-based Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KRISHNA03007", 

    # Packages
    packages=find_packages(),  
    install_requires=[line.strip() for line in (this_directory / "requirements.txt").read_text().splitlines()],
    python_requires='>=3.8',   # Minimum Python version

    # Additional info
    license="MIT",        
    zip_safe=False,            
)