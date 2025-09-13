[![Documentation Status](https://readthedocs.org/projects/kinovea/badge/?version=latest)](https://kinovea.readthedocs.io/en/latest/?badge=latest)

# kinovea-docs

This is Kinovea's user-documentation project.

Introduction
------------
Kinovea is an open source video player and camera capture software with features tailored to sports applications such as comparison, annotation and measurement. It is a relatively mature project, it has been in development since 2004, has been downloaded more than a million times and is cited in many scientific papers in the field of sports science. 

**Main website**: https://www.kinovea.org/

Links
---------
The current live documentation can be found here: https://www.kinovea.org/help/index.htm

The manual in this repository is automatically rebuilt at readthedocs here: https://kinovea.readthedocs.io/en/latest/


History of release posts
-------

List of successive release posts since version 0.8.15, containing descriptions of new features (some of the features have seen multiple updates over the course of these versions):

|    Link   | Release date |
|:----------:|:----------------:|
| [2024.1](https://www.kinovea.org/en/forum/viewtopic.php?id=1959) | 2024-08 |
| [2023.1](https://www.kinovea.org/en/forum/viewtopic.php?id=1589) | 2023-08 |
| [0.9.5](https://www.kinovea.org/en/forum/viewtopic.php?id=1030) | 2021-10 |
| [0.9.4](https://www.kinovea.org/en/forum/viewtopic.php?id=1011) | 2021-04 |
| [0.9.2 / 0.9.3](https://www.kinovea.org/en/forum/viewtopic.php?id=953) | 2020-07 |
| [0.9.1](https://www.kinovea.org/en/forum/viewtopic.php?id=928) | 2019-12 |
| [0.8.27](https://www.kinovea.org/en/forum/viewtopic.php?id=886) | 2018-10 |
| [0.8.26](https://www.kinovea.org/en/forum/viewtopic.php?id=854) | 2017-11 |
| [0.8.25](https://www.kinovea.org/en/forum/viewtopic.php?id=816) | 2016-08 |
| [0.8.24](https://www.kinovea.org/en/forum/viewtopic.php?id=771) | 2015-03 |
| [0.8.23](https://www.kinovea.org/en/forum/viewtopic.php?id=745) | 2014-10 |
| [0.8.22](https://www.kinovea.org/en/forum/viewtopic.php?id=732) | 2014-06 |
| [0.8.21](https://www.kinovea.org/en/forum/viewtopic.php?id=700) | 2013-10 |
| [0.8.20](https://www.kinovea.org/en/forum/viewtopic.php?id=664) | 2013-01 |
| [0.8.19](https://www.kinovea.org/en/forum/viewtopic.php?id=638) | 2012-09 |
| [0.8.18](https://www.kinovea.org/en/forum/viewtopic.php?id=628) | 2012-08 |
| [0.8.17](https://www.kinovea.org/en/forum/viewtopic.php?id=598) | 2012-03 |
| [0.8.16](https://www.kinovea.org/en/forum/viewtopic.php?id=483) | 2011-08 |
| [0.8.15](https://www.kinovea.org/en/forum/viewtopic.php?id=409) | 2011-05 |

Compiling the documentation
---------------------------

The documentation uses Sphinx. Sphinx is essentially a static website generator that takes a collection of reStructuredText text files and compiles them into static HTML pages. This website is then manually copied to the server under https://www.kinovea.org/help/en/

Installation

- Create a python venv on python 3.11
- `> pip install -U sphinx`
- `> pip install sphinx-rtd-theme`

Build
- from kinovea-docs root:
- `> sphinx-build -M html source output`
- site is built in output.

Live testing (auto-build on changes)
- `> pip install sphinx-autobuild`
- `> sphinx-autobuild -M html source output`
- http://127.0.0.1:8000/



