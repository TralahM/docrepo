
[![Build Status](https://travis-ci.com/TralahM/docrepo.svg?branch=master)](https://travis-ci.com/TralahM/docrepo)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pull/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/TralahM/docrepo/pull/)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/TralahM/docrepo).

# docrepo.
Automate the Boring Stuff of Creating Common Git Repo Files using some universal
templates.
This tool will generate:
- A template README.md that you can customize and edit to suit your needs
- A template CONTRIBUTING guideline
- A PULL_REQUEST_TEMPLATE
- A template CODE_OF_CONDUCT.md
- A bug_report ISSUE_TEMPLATE
- A feature_request ISSUE_TEMPLATE
- A sample gitignore with common entries

This might come in handy to ensure your project meets the common community guidelines and
save you your most valuable resource which is time. And as the adage goes __Time is
Money__ so save some Money. :heavy_dollar_sign:


[![TralahM](https://img.shields.io/badge/Author-TralahM-cyan.svg?style=for-the-badge)](https://github.com/TralahM)

### Installation
This package is available on pypi you can install it using pip
:100:

```Bash
pip install initgitdoc
```
#### Usage
After pip install you can invoke the command line for help
```Bash
mkdir <A-Folder-Name>

cd <A-Folder-Name>

git init .

git remote add origin \
https://github.com/<Your-Github-User-Name>/<Your-Github-Repository-Name>.git

initgitdoc --help

initgitdoc -n <Your-Github-Repository-Name> -a <Your-Github-User-Name>

ls

```
### Development

```Bash
git clone https://github.com/TralahM/docrepo.git
cd docrepo
python setup.py bdist_wheel
python -m pip install dist/initgitdoc-0.1-py3-none-any.whl
```

## Scripts Herein.

* [templates.py](https://github.com/TralahM/docrepo/blob/master/templates.py)

* [docgitinit.py](https://github.com/TralahM/docrepo/blob/master/docgitinit.py)

* [initgitdoc](https://github.com/TralahM/docrepo/blob/master/initgitdoc)

* [LICENSE](https://github.com/TralahM/docrepo/blob/master/LICENSE)

* [__pycache__](https://github.com/TralahM/docrepo/blob/master/__pycache__)

* [CONTRIBUTING.rst](https://github.com/TralahM/docrepo/blob/master/CONTRIBUTING.rst)

* [README.md](https://github.com/TralahM/docrepo/blob/master/README.md)

* [CODE_OF_CONDUCT.md](https://github.com/TralahM/docrepo/blob/master/CODE_OF_CONDUCT.md)

# Contributors.

* [TralahTek](https://github.com/TralahTek)
* [TralahM](https://github.com/TralahM)
