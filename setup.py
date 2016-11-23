import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

__version__ = None
with open('namecheap/version.py') as f:
    exec(f.read())

if sys.argv[-1] == 'publish':
    os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (__version__, __version__))
    print("  git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='python-namecheap',
    version=__version__,
    description="""EasyEngine Python Module""",
    long_description=readme + '\n\n' + history,
    author='Cubo',
    author_email='somos@cubo.pe',
    url='https://github.com/cubope/python-namecheap',
    keywords=['python', 'namecheap', 'management'],
    install_requires=[
        'paramiko>=2.0.2',
    ],
    extras_require={
    },
    packages=find_packages(),
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ],
)
