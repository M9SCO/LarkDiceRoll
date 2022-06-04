from io import open

from setuptools import setup, find_packages

"""
:authors: M_9SCO
:license: MIT license, see LICENSE file
"""

version = "1.0.0"

setup(
    name='dice_roller',
    version=version,
    author="M_9SCO",
    description=u"Python module for rolling dices  with standard text notation",
    license="MIT license",
    url="https://github.com/M9SCO/dicerollhttps://github.com/M9SCO/diceroll",
    download_url="https://github.com/M9SCO/dicerollhttps://github.com/M9SCO/diceroll/arhive/v{}.zip".format(version),
    install_requires=["lark"],
    packages=find_packages(),
    classifiers = [
                  "Programming Language :: Python :: 3.7",
                  "License :: MIT license",
              ],
)
