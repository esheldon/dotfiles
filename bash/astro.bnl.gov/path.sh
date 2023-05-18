append_path PATH /sbin
append_path PATH /usr/sbin

prepend_path PATH /opt/astro/SL64/texlive/2013/bin/x86_64-linux/
prepend_path PATH $HOME/wq.dist/

ANACONDA_DIR=/gpfs02/astro/desdata/esheldon/mambaforge
if [[ -e $ANACONDA_DIR ]]; then
    export ANACONDA_DIR
    prepend_path PATH ${ANACONDA_DIR}/bin
fi
