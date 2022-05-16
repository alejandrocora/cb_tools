import sys
from setuptools import setup, find_packages

requires = [
    'selenium',
    'argparse',
    'telegram-send'
]

setup(
    name='cb_tools',
    description=("Tool set for CoinBase data management"),
    version='0.1.1',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['nawa=cb_tools.nawa:main'],
    },
    long_description=open('README.md').read(),
    keywords=['coinbase', 'cb', 'tools', 'cb_tools', 'assets', 'scraping', 'scraper', 'telegram']
)
