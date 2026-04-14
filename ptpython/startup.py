from glob import glob

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

    src = inspect.getsource(obj)
    hsrc = _maybe_highlight(src)
    fname = inspect.getfile(obj)
    hsrc = hsrc + f'\nFile: {fname}'
    pydoc.pager(hsrc)


def doc(obj):
    import inspect
    import pydoc

    d = inspect.getdoc(obj)
    fname = inspect.getfile(obj)
    d = d + f'\nFile: {fname}'
    pydoc.pager(d)

