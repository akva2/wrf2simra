from wrf2simra import WRFConverter

import click
import sys


@click.command()
@click.argument('infile', type=click.Path(exists=True))
@click.argument('inmesh', type=click.Path(exists=True))
@click.argument('outfile', type=click.Path())
def main(infile, inmesh, outfile):
    try:
        conv = WRFConverter(infile, inmesh, outfile)
        conv.doConvert()
    except AssertionError as e:
        print('Error:', str(e), file=sys.stderr)
        sys.exit(1)
