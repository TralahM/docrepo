#!python
from datetime import datetime
contributing_template = """
=======================
Contributing Guidelines
=======================

Thanks for your interest in contributing to this project!  Contributions are
welcome and very much appreciated.  If this is your first time contributing to a
Free and Open Source Software project, consider reading `How to Contribute to
Open Source`_ in the Open Source Guides.  Additionally, to maximize the chance
that your contribution will be accepted and minimize wasted effort, consider the
following guidelines:


Tests Must Pass
===============

In order for a pull request to be accepted, it must build and test successfully
on the continuous integration systems.  GitHub displays a build status
indicator on the pull request.  If the build is broken, please fix it (or add a
comment if you think the pull request is not the cause of the breakage).

The CI build runs several linters and tests.  These can be run locally by
invoking ``tox``.  Disabling linter rules using inline configuration is
acceptable, where justified.  Disable specific rules where possible (i.e.
``# noqa: F401`` rather than just ``# noqa``).


Add Tests Where Reasonable
==========================

If the pull request fixes a bug or adds a feature, consider adding a test to
ensure the bug does not reoccur and the feature works as expected.  If testing
is not straightforward, feel free to submit the pull request without tests.
How to test and whether testing is required can be discussed during the review
process.


Consider Discussing Big Changes First
=====================================

If the desired change is large, complex, backwards-incompatible, can have
significantly differing implementations, or may not be in scope for this
project, opening an issue to discuss the change before writing the code can
avoid frustration and save a lot of time and effort.

This is not a hard requirement.  If you'd rather start discussing a big change
with a proposed implementation, feel free.  Be aware that the code may be
rejected outright, or require many changes before it is acceptable.

.. _How to Contribute to Open Source: https://opensource.guide/how-to-contribute/
"""
issue_template = """
Please remove all of this template but the relevant section below, and fill in
each item in that section.

## Feature Request

### Feature Description

Describe in detail the feature you would like to see implemented, especially
how it would work from a user perspective and what benefits it adds. Your description
should be detailed enough to be used to determine if code written for the feature
adequately solves the problem.

### Use Cases

Describe one or more use cases for why this feature will be useful.

### Testing Assistance

Indicate whether or not you will be able to assist in testing pre-release
code for the feature.

## Bug Report

When reporting a bug, please provide all of the following information,
as well as any additional details that may be useful in reproducing or fixing
the issue:

### Version

{0} version, as reported by ``{0} --version``

### Installation Method

How was {0} installed (provide as much detail as possible, ideally
the exact command used and whether it was installed in a virtualenv or not).

### Supporting Software Versions

The output of ``python --version`` and ``virtualenv --version`` in the environment
that {0} is running in, as well as your operating system type and version.

### Actual Output

```
Paste here the output of {0} (including the command used to run it),
run with the -vv (debug-level output) flag, that shows the issue.
```

### Expected Output

Describe the output that you expected (what's wrong). If possible, after your description,
copy the actual output above and modify it to what was expected.

### Testing Assistance

Indicate whether or not you will be able to assist in testing pre-release
code for the feature.
"""
pr_template = """
__IMPORTANT:__ Please take note of the below checklist, especially the first two items.

# Pull Request Checklist

- [ ] All pull requests must include the Contributor License Agreement (see below).

- [ ] Code should conform to the following:

    - [ ] pep8 compliant with some exceptions (see pytest.ini)

    - [ ] 100% test coverage with pytest (with valid tests). If you have difficulty
      writing tests for the code, feel free to ask for help or submit the PR without tests.

    - [ ] Complete, correctly-formatted documentation for all classes, functions and methods.

    - [ ] documentation has been rebuilt with ``tox -e docs``

    - [ ] All modules should have (and use) module-level loggers.

    - [ ] **Commit messages** should be meaningful, and reference the Issue number
      if you're working on a GitHub issue (i.e. "issue #x - <message>"). Please
      refrain from using the "fixes #x" notation unless you are *sure* that the
      the issue is fixed in that commit.

    - [ ] Git history is fully intact; please do not squash or rewrite history.

## Contributor License Agreement

By submitting this work for inclusion in python-package-skeleton, I agree to the following terms:

* The contribution included in this request (and any subsequent revisions or versions of it)
  is being made under the same license as the python-package-skeleton project (the Affero GPL v3,
  or any subsequent version of that license if adopted by python-package-skeleton).
* My contribution may perpetually be included in and distributed with python-package-skeleton; submitting
  this pull request grants a perpetual, global, unlimited license for it to be used and distributed
  under the terms of python-package-skeleton's license.
* I have the legal power and rights to agree to these terms.
"""
readme_template = """
[![Build Status](https://travis-ci.com/{1}/{0}.svg?branch=master)](https://travis-ci.com/{1}/{0})
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![HitCount](http://hits.dwyl.io/{1}/{0}.svg)](http://dwyl.io/{1}/{0})
[![Inline Docs](http://inch-ci.org/github/{1}/{0}.svg?branch=master)](http://inch-ci.org/github/{1}/{0})
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/{1}/pull/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/{1}/{0}/pull/)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/{1}/{0}).

# {0}.

# Description

[![{1}](https://img.shields.io/badge/Engineer-{1}-blue.svg?style=for-the-badge)](https://github.com/{1})
[![{1}](https://img.shields.io/badge/Maintainer-{1}-green.svg?style=for-the-badge)](https://github.com/{1})

# Documentation

[Read the Docs](https://{0}.readthedocs.io)
# Dependencies

# How to Install


## Building from Source for Developers

```Bash
git clone https://github.com/{1}/{0}.git
cd {0}
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Acknowledgements


"""
mit_license = f"""
MIT License

Copyright (c) {datetime.now().date().year} Tralah Brian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
code_of_conduct = """
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at musyoki.tralah@students.jkuat.ac.ke. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
"""
gitignore = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
nohup.out
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule*

# SageMath parsed files
*.sage.py

# dotenv
.env

# virtualenv
.venv
venv/
ENV/
env/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# PyCharm
.idea/

.*~
"""
feature_request = """
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
"""
bug_report = """
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. iOS]
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]

**Smartphone (please complete the following information):**
 - Device: [e.g. iPhone6]
 - OS: [e.g. iOS8.1]
 - Browser [e.g. stock browser, safari]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.
"""
funding_template = """
github: {0}
patreon: {0}
# Custom: [{0}.github.io,TralahTek.github.io,]
"""
pypi_workflow = """
# This workflows will upload a Python Package using Twine when a release is created
# For more information see: https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions#publishing-to-package-registries

name: Upload Python Package

on:
  release:
    types: [created]

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v1
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine
    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python setup.py sdist bdist_wheel
        twine upload dist/*
"""
if __name__ == '__main__':
    print("Run initgitdoc instead!")
