from distutils.core import setup

long_desc = """Loads a file into a Python module object but does not place it in the module cache or otherwise bind it. Useful for loading Python-based config files."""

setup(name="pyconf", version="0.5",
    url="http://blogg.se",
    description="Python-based configuration reader",
    long_description=long_desc,
    author="Blogg Esse AB",
    author_email="teknik@blogg.se",
    py_modules=["pyconf"])
