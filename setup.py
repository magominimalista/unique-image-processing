from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    page_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name='unique-image-processing',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-image',
        'matplotlib'
    ],
    author='Philipe Cairon',
    author_email='magominimalista@gmail.com',
    description='Um módulo de exemplo para processamento de imagens',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/magominimalista/unique-image-processing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
