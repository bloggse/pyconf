from distutils.core import setup

d = {}
execfile("pyconf.py", d, d)
long_desc = d["__doc__"]

setup(name="pyconf", version="0.3",
    url="http://blogg.se",
    description="Python-based configuration reader",
    long_description=long_desc,
    author="Blogg Esse AB",
    author_email="software@blogg.se",
    py_modules=["pyconf"])
