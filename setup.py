import os
from distutils.core import setup, Command

long_desc = """Loads a file into a Python module object but does not place it in the module cache or otherwise bind it. Useful for loading Python-based config files."""

class RunDocTests(Command):
    description = "run doctests"
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        import doctest
        import pyconf
        failures, tests = doctest.testmod(m=pyconf)
        if failures == 0:
            print("Ran %s tests with 0 failures" % (tests,));

setup(name="pyconf", version="0.5",
      url="http://blogg.se",
      description="Python-based configuration reader",
      long_description=long_desc,
      author="Blogg Esse AB",
      author_email="teknik@blogg.se",
      py_modules=["pyconf"],
      cmdclass={"test": RunDocTests}
      )

