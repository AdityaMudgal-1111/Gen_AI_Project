from setuptools import findpackages, setup


setup (

    name= 'My_MCQ_Generator',
    version = '0.1',
    author = 'Adi',
    author_email = 'adii.mudgal@gmail.com',
    install_requires = ["langchain", "openai", "pandas", "streamlit", "python-dotenv", "PyPDF2"]
    packages= findpackages()
    
)