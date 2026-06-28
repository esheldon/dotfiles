from glob import glob
import re

try:
    import numpy as np
    from numpy import (
        array,
        zeros,
        ones,
        where,
        arange,
        linspace,
        logspace,
        sqrt,
        exp,
        cos,
        sin,
        tanh,
        arctanh,
        log,
        log10,
        median,
        diag,
    )
except ModuleNotFoundError:
    print('could not import numpy')

try:
    import ngmix
except ModuleNotFoundError:
    print('could not import ngmix')

try:
    import esutil as eu
    from esutil.numpy_util import ahelp, aprint, where1, between
    from esutil.misc import colprint, ptime
    from esutil.stat import get_stats, print_stats
except ModuleNotFoundError:
    print('could not import esutil')

try:
    import espy.plotting
    from espy.plotting import plot
    from espy.plotting import plot_hist
except ModuleNotFoundError:
    print('could not import espy')

try:
    import fitsio
except ModuleNotFoundError:
    print('could not import fitsio')

try:
    import matplotlib
    import matplotlib.pyplot as mplt
except ModuleNotFoundError:
    print('could not import matplotlib')


def _maybe_highlight(src):
    try:
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import Terminal256Formatter

        formatter = Terminal256Formatter(
            bg='dark',
            style='coffee',
        )
        highlighted_source = highlight(
            src,
            PythonLexer(),
            formatter,
        )
        return highlighted_source
    except ModuleNotFoundError:
        return src


def src(obj):
    import inspect
    import pydoc

    try:
        src = inspect.getsource(obj)
        hsrc = _maybe_highlight(src)
        fname = inspect.getfile(obj)
        hsrc = hsrc + f'\nFile: {fname}'
        pydoc.pager(hsrc)
    except TypeError as err:
        print(err)


def docold(obj):
    import inspect
    import pydoc

    try:
        d = inspect.getdoc(obj)
        fname = inspect.getfile(obj)
        d = f'File: {fname}\n\n{d}'
        pydoc.pager(d)
    except TypeError:
        help(obj)


ANSI = {
    'reset':  '\033[0m',
    'bold':   '\033[1m',
    'dim':    '\033[2m',
    'cyan':   '\033[36m',
    'yellow': '\033[33m',
    'green':  '\033[32m',
}

ROLE_RE   = re.compile(r':(\w+):`~?([^`]+)`')
CODE_RE   = re.compile(r'``([^`]+)``')
EMPH_RE   = re.compile(r'(?<!\*)\*([^*\n]+)\*(?!\*)')
STRONG_RE = re.compile(r'\*\*([^*\n]+)\*\*')


def _render_rst(doc):
    """
    Simple renderer for rich text in doc strings

    if you start expanding the renderer:

        the order of those regexes matters.

        STRONG_RE has to run before EMPH_RE (otherwise **bold** gets eaten as
        two *emph* matches with an empty middle)

        CODE_RE for double-backticks has to run before any single-backtick
        handling you might add later.
    """

    def role_sub(m):
        target = m.group(2).rsplit('.', 1)[-1]      # drop dotted prefix
        return f"{ANSI['cyan']}{target}{ANSI['reset']}"

    doc = ROLE_RE.sub(role_sub, doc)
    doc = CODE_RE.sub(lambda m: f"{ANSI['green']}{m.group(1)}{ANSI['reset']}", doc)
    doc = STRONG_RE.sub(lambda m: f"{ANSI['bold']}{m.group(1)}{ANSI['reset']}", doc)
    doc = EMPH_RE.sub(lambda m: f"{ANSI['dim']}{m.group(1)}{ANSI['reset']}", doc)
    return doc


def doc(obj):
    import pydoc

    try:
        pydoc.pager(_render_rst(obj.__doc__ or ''))
    except TypeError:
        help(obj)
