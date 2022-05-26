# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='thousandeyessdk',
    version='0.0.6a7',
    description='Python SDK for ThousandEyes API Monitoring Service',
    long_description="Python SDK for ThousandEyes API Monitoring Service",
    long_description_content_type='text/markdown',
    url='https://github.com/CiscoAandI/ThousandEyesSDK',
    author='Ava Thorn',
    author_email='avthorn@cisco.com',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='thousandeyes, api, rest, sdk, cisco',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['requests==2.25.1', 'werkzeug==2.0.1'],
    extras_require={
        'dev': ['wheel'],
        'test': ['pytest==6.2.4', 'pytest-blockage==0.2.2', 'pytest-cov==2.12.0'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/CiscoAandI/ThousandEyesSDK/issues',
        'Source': 'https://github.com/CiscoAandI/ThousandEyesSDK/',
    },
)
