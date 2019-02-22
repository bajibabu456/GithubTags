import os
import codecs

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with codecs.open(os.path.join(here, 'nferx_py', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(name=about['__title__'],
      version=about['__version__'],
      description=about['__description__'],
      author=about['__author__'],
      packages=['GithubTags'],
      install_requires=[
          'requests'
      ],
      include_package_data=True)
