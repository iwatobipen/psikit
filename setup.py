from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup
from setuptools import find_packages
import os

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

here = os.path.dirname(os.path.abspath(__file__))
version = next(line.split('=')[1].split().replace("'", '') for line in open(os.path.join(here, 'psikit','__init__.py')) if line.startwith('__version__ = '), '0.0.dev0')

setup(
        name='psikit',
        version=version,
        description='RDKit extension for quantom chemistry',
        url='https://github.com/Mishima-syk/psikit',
        author='Takayuki Serizawa',
        author_email='seitaka@gmail.com',
        description='RDKit extension for quantom chemistry',
        long_description=readme,
        packages=find_packages(),
        intall_requires=_requires_from_file('requirements.txt'),
        license='MIT',  #check license
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approaved :: MIT License',
            ]
        entry_points="""
        -*- Entry points: -*-
        [console_scripts]
        pkgdep = pypipkg.scripts.command:main
        """,
        )
