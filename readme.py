#!/data/data/com.termux/files/usr/bin/env python
'''TralahTek LLC Code Documentation ToolKit
Making Code Documentation Less of a Pain in the Ass.'''
import glob
import os
from argparse import ArgumentParser
class GitRepoReadMe:
    version='0.1'
    "A Github Repository ReadMe Generator. "
    _header="""[![Build Status](https://travis-ci.com/{1}/{0}.svg?branch=master)](https://travis-ci.com/{1}/{0})
    [![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
    [![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
    [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
    [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
    [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/{1}/pull/)
    [![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/{1}/{0}/pull/)
    [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/{1}/{0}).

# {0}.
    """
    _author="[![{1}](https://img.shields.io/badge/Author-{1}-cyan.svg?style=for-the-badge)](https://github.com/{1})"

    _cloning="""
### Setup and Usage

```Bash
    git clone https://github.com/{1}/{0}.git
    cd {0}
```
    """

    _scripts="\n".join(glob.glob("*",recursive=True))

    def add_contribs():
        'Add contributors from a list of github usernames'
        contribs=['CentLuc','Chiziroba','TralahTek','{1}']
        h="\n\n# Contributors. \n\n"
        return h+ "\n".join(["* [%s](%s)"%(r,"https://github.com/"+r) for r in contribs])

    def link_scripts():
        'generate links to files in the github project.'
        base_url="https://github.com/{1}/{0}/blob/master/"
        return "\n\n".join(["* [%s](%s)"%(r,base_url+r) for r in glob.glob("*",recursive=True)])
    _scripts=link_scripts()

    def gen_RMe(rp_name,rp_author,subdir=False):
        'generate markdown text with the defined templates and repo_name and author_username. '
        if not subdir:
            content=GitRepoReadMe._header+"\n\n"+GitRepoReadMe._author+"\n"+GitRepoReadMe._cloning
            content+="\n## Project Structure.\n"+GitRepoReadMe._scripts+"\n"+GitRepoReadMe.add_contribs()
        else:
            content="\n\n"+GitRepoReadMe._author+"\n"+"## {0} \n"+GitRepoReadMe._scripts
        content=content.format(rp_name,rp_author)
        with open("README.md",'w') as f:
            f.write(content)
        print("Initialized ReadMe.md")
        print(content)
if __name__=='__main__':
    ps=ArgumentParser(description="Generate a README.md file in markdown for any github repository.")
    ps.add_argument('-n','--name',action='store',dest='name',help="The name of your github repository.",default=os.path.abspath('.').split('/')[-1])
    ps.add_argument('-a','--author',action='store',dest='author',help="Your github username",default="TralahM")
    ps.add_argument('-s',action='store_true',dest='sub',default=False,help='Is folder already inside a repo')
    psd=ps.parse_args()
    name,author,sub=psd.name,psd.author,psd.sub
    if sub:
        cd=os.environ['PWD']
        nname=cd.split(name)[-1]
        name=name+nname
    GitRepoReadMe.gen_RMe(name,author,sub)
