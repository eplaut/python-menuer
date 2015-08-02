from setuptools import setup, find_packages
import functools
import os

_in_same_dir = functools.partial(os.path.join, os.path.dirname(__file__))

with open(_in_same_dir("menuer", "__version__.py")) as version_file:
    exec(version_file.read())  # pylint: disable=W0122


setup(name="menuer",
      classifiers=[
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
      ],
      description="Simple Menu Creator",
      license="BSD",
      author="Eli Plaut",
      author_email="eplaut@gmail.com",
      url="http://eplaut.github.io/menuer",
      version=__version__,
      packages=['menuer'],
      )
