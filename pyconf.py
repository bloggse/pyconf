"""Python-based configuration reader

Simply enough, loads a file into a Python module object but does not place it
in the module cache or otherwise bind it.

>>> import posixpath
>>> conf = load(posixpath.__file__)
>>> conf  # doctest: +ELLIPSIS
<module '<config>' from '...'>
>>> conf.pathsep
':'

And so on. You could also use `load_dict` to get a dict instead:

>>> type(load_dict(posixpath.__file__))
<type 'dict'>

Though, if you try to load files that aren't recognized or loadable, you get
an error:

>>> load("lala.ini")
Traceback (most recent call last):
  ...
ConfigurationError: no suitable loader for config module 'lala.ini'
"""

import os
import imp

default_conf_dir = os.environ.get("PYCONF_DIR", "/etc/pyconf")

class ConfigurationError(Exception):
    pass

def load(filename=None, pkgname=None, conf_dir=None):
    """Load module at *filename* with the proper module loader.

    The module loader is chosen based on *filename*'s extension.

    If *pkgname* is given, sets the default for *filename* based on the
    constant global `pyconf.default_conf_dir`:

        filename = default_conf_dir '/' pkgname '.conf.py'
    """
    if filename is None and pkgname is not None:
        env_var = pkgname.replace("-", "_").upper() + "_CONF"
        if env_var in os.environ:
            filename = os.environ[env_var]
        else:
            conf_dir = conf_dir or default_conf_dir
            filename = os.path.join(conf_dir, pkgname + ".conf.py")
    for (suffix, mode, type_) in imp.get_suffixes():
        if filename.endswith(suffix):
            fp = file(filename, mode)
            desc = (suffix, mode, type_)
            try:
                mod = imp.load_module("<config>", fp, filename, desc)
                return mod
            finally:
                fp.close()
    else:
        raise ConfigurationError("no suitable loader for config module %r" %
            (filename,))

def load_dict(filename):
    """Like `load`, but return a dict with the module's contents."""
    d = vars(load(filename))
    d.pop("__builtins__", None)
    return d

if __name__ == "__main__":
    import sys
    import doctest
    num_fail, num_run = doctest.testmod()
    sys.exit(int(num_fail > 0))
