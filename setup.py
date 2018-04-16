from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='aws-linter',
      version='0.0.1',
      description=u"AWS Linter",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Frank van Boven",
      author_email='frank@cenotaph.nl',
      url='https://github.com/fatbasstard/aws-linter',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      awslinter=awslinter.scripts.cli:cli
      """
      )
