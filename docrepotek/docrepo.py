#!python
"""
TralahTek LLC Git Repository Code Documentation ToolKit
Making Code Documentation Less of a Pain in the Ass.
"""
import glob
import os
from argparse import ArgumentParser
from random import choice
from docrepotek import templates


def resolve_key(lang: str) -> str:
    if lang in templates.LanguageColorMap.keys():
        return lang
    elif (
         lang not in templates.LanguageColorMap.keys()
         and len([x for x in templates.LanguageColorMap.keys() if lang in x]) > 0
    ):
        return choice([x for x in templates.LanguageColorMap.keys() if lang in x])
    else:
        if lang == "cpp":
            return "c++"
        else:
            return "shell"


def resolve_color(language: str) -> str:
    lookup = language.lower()
    key = resolve_key(lookup)
    return templates.LanguageColorMap.get(key, "1110101")


class GitRepo:
    def link_scripts():
        "generate links to files in the github project."
        base_url = "https://github.com/{1}/{0}/blob/master/"
        return "\n\n".join(
            ["* [%s](%s)" % (r, base_url + r) for r in glob.glob("*", recursive=True)]
        )

    def gen_RMe(rp_name, rp_author, subdir=False, lang="Python"):
        # scripts = GitRepo.link_scripts().format(rp_name, rp_author)
        color = resolve_color(lang)
        content = templates.readme_template.format(rp_name, rp_author, lang, color)
        with open("README.md", "w") as f:
            f.write(content)
        print("Initialized ReadMe.md")

    def gen_Funding(rp_author):
        if not os.path.exists(".github"):
            os.mkdir(".github")
        with open(".github/FUNDING.yml", "w") as f:
            f.write(templates.funding_template.format(rp_author))
        print("Initialized  .github/FUNDING.yml")

    def gen_License():
        content = templates.mit_license
        with open("LICENSE", "w") as f:
            f.write(content)
        print("Initialized LICENSE")

    def gen_Contrib():
        content = templates.contributing_template
        with open("CONTRIBUTING.rst", "w") as f:
            f.write(content)
        print("Initialized CONTRIBUTING.rst")

    def gen_Conduct():
        with open("CODE_OF_CONDUCT.md", "w") as f:
            f.write(templates.code_of_conduct)
        print("Initialized CODE_OF_CONDUCT.md")

    def gen_Issues_PR():
        if not os.path.exists(".github"):
            os.mkdir(".github")
        if not os.path.exists(".github/ISSUE_TEMPLATE"):
            os.mkdir(".github/ISSUE_TEMPLATE")
        with open(".github/ISSUE_TEMPLATE/bug_report.md", "w") as f:
            f.write(templates.bug_report)
        print("Initialized .github/ISSUE_TEMPLATE/bug_report.md")
        with open(".github/ISSUE_TEMPLATE/feature_request.md", "w") as f:
            f.write(templates.feature_request)
        print("Initialized .github/ISSUE_TEMPLATE/feature_request.md")
        with open("PULL_REQUEST_TEMPLATE.md", "w") as f:
            f.write(templates.pr_template)
        print("Initialized PULL_REQUEST_TEMPLATE.md")

    def gen_Gitignore():
        with open(".gitignore", "w") as f:
            f.write(templates.gitignore)
        print("Initialized .gitignore")

    def gen_Gitattributes():
        with open(".gitattributes", "w") as f:
            f.write(templates.gitattributes)
        print("Initialized .gitattributes")

    def gen_pypi_workflow():
        if not os.path.exists(".github"):
            os.mkdir(".github")
        if not os.path.exists(".github/workflows"):
            os.mkdir(".github/workflows")
        with open(".github/workflows/pythonpublish.yml", "w") as f:
            f.write(templates.pypi_workflow)
        print("Initialized .github/workflows/pythonpublish.yml")
        pass


def main():
    epilog = "Author: TralahM\n Email: <briantralah@gmail.com>. Copyright:2019 (All Rights Reserved). "
    ps = ArgumentParser(
        description="Generate Common Documentation files for any git repository.\n",
        epilog=epilog,
    )
    ps.add_argument(
        "-n",
        "--name-repo",
        action="store",
        dest="name",
        help="The name of your github repository. Default is the name of the current directory",
        default=os.path.abspath(".").split("/")[-1],
    )
    ps.add_argument(
        "-a",
        "--author",
        action="store",
        dest="author",
        help="Your github username, default is TralahM",
        default="TralahM",
    )
    ps.add_argument(
        "-l",
        "--language",
        action="store",
        dest="lang",
        help="Main Language of the Repository",
        default="Python",
    )
    ps.add_argument(
        "-s",
        "--sub-directory",
        action="store_true",
        dest="sub",
        default=False,
        help="Is folder already inside a repo, is it a subdirectory ? default=False",
    )
    ps.add_argument(
        "-nr",
        "-no-readme",
        action="store_true",
        dest="noreadme",
        default=False,
        help="Dont generate a ReadMe default=False",
    )
    ps.add_argument(
        "-pw",
        "-pypi-workflow",
        action="store_true",
        dest="pypi_workflow",
        default=False,
        help="Generate a Pypi Workflow default=False",
    )
    psd = ps.parse_args()
    name, author, sub, lang = psd.name, psd.author, psd.sub, psd.lang
    if sub:
        cd = os.environ["PWD"]
        nname = cd.split(name)[-1]
        name = name + nname
    if not psd.noreadme:
        GitRepo.gen_RMe(name, author, sub, lang=lang)
    if not sub:
        GitRepo.gen_Contrib()
        GitRepo.gen_Conduct()
        GitRepo.gen_License()
        GitRepo.gen_Issues_PR()
        GitRepo.gen_Gitignore()
        GitRepo.gen_Funding(author)
        GitRepo.gen_Gitattributes()
    if psd.pypi_workflow:
        GitRepo.gen_pypi_workflow()

if __name__ == '__main__':
    main()
