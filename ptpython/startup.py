from glob import glob

try:
    import numpy as np
    from numpy import (
        array,zeros,ones,where,arange,linspace,logspace,
        sqrt, exp, cos, sin, tanh, arctanh, log, log10, median,
        diag
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
