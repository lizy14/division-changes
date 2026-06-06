from glob import glob

from setuptools import find_packages, setup

setup(
    name="division-changes",
    version="0.1.0",
    description="中华人民共和国行政区划代码历史沿革数据库",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    data_files=[
        ("tables", glob("tables/*.csv")),
        ("rules-handwritten", glob("rules-handwritten/*.csv")),
        ("rules-generated", glob("rules-generated/*.csv")),
    ],
    entry_points={
        "console_scripts": ["division-changes=division_changes.translate:main"],
    },
)
