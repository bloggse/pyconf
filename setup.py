from distutils.core import setup

d = {}
exec(compile(open("pyconf.py").read(), "pyconf.py", 'exec'), d, d)
long_desc = d["__doc__"]

setup(name="pyconf", version="0.4.2",
    url="http://blogg.se",
    description="Python-based configuration reader",
    long_description=long_desc,
    author="Blogg Esse AB",
    author_email="info@blogg.se",
    py_modules=["pyconf"])
