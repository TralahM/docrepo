#!python
'''TralahTek LLC Git Repository Code Documentation ToolKit
Making Code Documentation Less of a Pain in the Ass.'''
import glob
import os
from argparse import ArgumentParser
import templates


class GitRepo:
    def link_scripts():
        'generate links to files in the github project.'
        base_url = "https://github.com/{1}/{0}/blob/master/"
        return "\n\n".join(["* [%s](%s)" % (r, base_url+r) for r in glob.glob("*", recursive=True)])

    def gen_RMe(rp_name, rp_author, subdir=False):
        scripts = GitRepo.link_scripts().format(rp_name, rp_author)
        content = templates.readme_template.format(rp_name, rp_author, scripts)
        with open("README.md", 'w') as f:
            f.write(content)
        print("Initialized ReadMe.md")

    def gen_License():
        content = templates.mit_license
        with open("LICENSE", 'w') as f:
            f.write(content)
        print("Initialized LICENSE")

    def gen_Contrib():
        content = templates.contributing_template
        with open("CONTRIBUTING.rst", "w") as f:
            f.write(content)
        print("Initialized CONTRIBUTING.rst")

    def gen_Conduct():
        with open("CODE_OF_CONDUCT.md", 'w') as f:
            f.write(templates.code_of_conduct)
        print("Initialized CODE_OF_CONDUCT.md")

    def gen_Issues_PR(rp_name):
        if not os.path.exists('.github'):
            os.mkdir('.github')
        with open(".github/ISSUE_TEMPLATE.md", 'w') as f:
            f.write(templates.issue_template.format(rp_name))
        print("Initialized .github/ISSUE_TEMPLATE.md")
        with open(".github/PULL_REQUEST_TEMPLATE.md", 'w') as f:
            f.write(templates.pr_template)
        print("Initialized .github/PULL_REQUEST_TEMPLATE.md")

    def gen_Gitignore():
        with open(".gitignore", 'w') as f:
            f.write(templates.gitignore)
        print("Initialized .gitignore")


if __name__ == '__main__':
    docs = '\n'.join(['README.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.rst',
                      '.github/PULL_REQUEST_TEMPLATE.md', '.github/ISSUE_TEMPLATE.md', 'LICENSE', '.gitignore'])
    epilog = "Author: TralahM\n Email: <briantralah@gmail.com>. Copyright:2019 (All Rights Reserved). "
    ps = ArgumentParser(
        description="Generate Common Documentation files for any git repository.\n"+docs, epilog=epilog)
    ps.add_argument('-n', '--name-repo', action='store', dest='name',
                    help="The name of your github repository. Default is the name of the current directory", default=os.path.abspath('.').split('/')[-1])
    ps.add_argument('-a', '--author', action='store', dest='author',
                    help="Your github username, default is TralahM", default="TralahM")
    ps.add_argument('-s', '--sub-directory', action='store_true', dest='sub',
                    default=False, help='Is folder already inside a repo, is it a subdirectory ? default=False')
    psd = ps.parse_args()
    name, author, sub = psd.name, psd.author, psd.sub
    if sub:
        cd = os.environ['PWD']
        nname = cd.split(name)[-1]
        name = name+nname
    GitRepo.gen_RMe(name, author, sub)
    if not sub:
        GitRepo.gen_Contrib()
        GitRepo.gen_Conduct()
        GitRepo.gen_License()
        GitRepo.gen_Issues_PR(name)
        GitRepo.gen_Gitignore()
