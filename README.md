## wrf2simra

This repository contains the `wrf2simra` program: a script that reads WRF result files and
produces a SIMRA cont.res file for further manipulation.

### Installation

This program requires Python 3 and the `click` package. Recommended installation is with `pip` to
the user home directory, i.e.

    pip install --user .

If `pip` points to Python 2 (which is the case on some systems), you may need to use `pip3` instead.

    pip3 install --user .

To use `wrf2simra`, the directory `$HOME/.local/bin` must be added to your path, e.g. in `.bashrc`:

    export PATH=$PATH:$HOME/.local/bin

### Usage

For usage run

    wrf2simra --help
