try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

opts = dict(name='MyScripts',
            maintainer='Kerstin Wagner',
            maintainer_email='kwagnerbln@gmail.com',
            description='Simple example of a Travis setup',
            long_description='Simple example of a Travis setup',
            url='https://github.com/kwbln/AdvSE',
            download_url='https://github.com/kwbln/AdvSE',
            packages=find_packages())

if __name__ == '__main__':
    setup(**opts)
