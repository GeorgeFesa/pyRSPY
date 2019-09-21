from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='LAT',
    version='1.0',
    packages=[
        'LAT', 'LAT.Commands',
        'LAT.Optional'
    ],
    install_requires=[
        'mss', 'pynput',
        'scipy', 'sounddevice'
    ],
    url='https://github.com/GeorgeFesa/pyRSPY',
    download_url='https://github.com/GeorgeFesa/pyRSPY',
    license='MIT',
    author='GeorgeFesa',
    author_email='',
    description='A penetration testing command line tool written in python',
    long_description=long_description
)
