import subprocess
import sys

from setuptools import find_packages, setup

__version__ = "0.2.0"


if sys.argv[-1] == "publish":
    subprocess.run("python setup.py sdist bdist_wheel".split())
    subprocess.run("twine upload dist/*".split())
    subprocess.run(
        ["git", "tag", "-a", f"v{__version__}", "-m", f"'Version {__version__}'"]
    )
    subprocess.run(["git", "push", "origin", "--tags"])
    sys.exit()


setup(
    name="mkdocs-ivory",
    version=__version__,
    description="Ivory theme for MkDocs",
    url="https://github.com/daizutabi/mkdocs-ivory",
    author="daizutabi",
    author_email="daizutabi@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"mkdocs.themes": ["ivory = mkdocs_ivory"]},
)
