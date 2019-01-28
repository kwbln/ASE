from distutils.core import setup


def readme():
    with open('README.md') as f:
        return f.read()


files = ['things/*']

setup(name='petproject',
      version='0.9',
      description='Example project with advanced software engineering',
      author='Kerstin Wagner',
      author_email='kwagnerbln@gmail.com',
      url='https://github.com/kwbln/AdvSE',
      packages=['petproject'],
      package_data={'petproject': files},
      # 'runner' is in the root.
      scripts=['runner'],
      long_description=readme()
      )
