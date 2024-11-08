localdir=$HOME/local

if [[ -d $localdir/bin ]]; then
    prepend_path PATH ${localdir}/bin
fi

if [[ -d $localdir/lib ]]; then
    prepend_path LD_LIBRARY_PATH ${localdir}/lib
    prepend_path LIBRARY_PATH    ${localdir}/lib
fi

if [[ -d $localdir/include ]]; then
    prepend_path C_INCLUDE_PATH  ${localdir}/include
    prepend_path CPATH           ${localdir}/include
fi

alt_localdir=$HOME/.local
if [[ -d $alt_localdir/bin ]]; then
    prepend_path PATH ${alt_localdir}/bin
fi

ANACONDA_DIR=$HOME/miniconda3
if [[ -e $ANACONDA_DIR ]]; then
    export ANACONDA_DIR
    prepend_path PATH ${ANACONDA_DIR}/bin
else
    ANACONDA_DIR=$HOME/miniforge3
    if [[ -e $ANACONDA_DIR ]]; then
        export ANACONDA_DIR
        prepend_path PATH ${ANACONDA_DIR}/bin
    else
        ANACONDA_DIR=$HOME/mambaforge
        if [[ -e $ANACONDA_DIR ]]; then
            export ANACONDA_DIR
            prepend_path PATH ${ANACONDA_DIR}/bin
        fi
    fi
fi
