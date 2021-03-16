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

if [[ -d ${HOME}/scripts ]]; then
    prepend_path PATH $HOME/scripts
fi

ANACONDA_DIR=$HOME/miniconda3
if [[ -e $ANACONDA_DIR ]]; then
    export ANACONDA_DIR
    prepend_path PATH ${ANACONDA_DIR}/bin
fi
