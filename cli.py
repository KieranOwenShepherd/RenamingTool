""" A command line interface for renaming file sequentially

    TODO - This could be modified reasonably quickly to be able to rename 
    multiple folder depths, or specific files within a folder, searching with glob patterns

dependencies - click, renaming
"""

import click
import renaming

@click.command()
@click.argument('path')
@click.option('-s', '--start', default=1, help="new file numbers will start at this")
@click.option('-p', '--pad', default=None, type=int, help="zeros will be padded to numbers to fit this field size")
def cli(path, start, pad):
    """Renames all files in the folder to a sequential list.
    The expected file format is <name>.<number>.<extension> 
    eg.
    prodeng.27.jpg

    The <number> will be renamed sequentially with buffered zeros
    eg.
    prodeng.27.jpg prodeng.32.jpg
    becomes
    prodeng.01.jpg prodeng.02.jpg

    Unless pad is specified, zeros will be padded automatically to fit the largest number (min 2).
    If 0 is given, no padding will be assigned.

    Args:
        PATH (str): path to the directory with the files
    """

    changes = renaming.sequential_rename(path, start, pad)

    if changes:
        click.echo("Changed")
        click.echo('\n'.join("{} -> {}".format(old,new) for old, new in changes))
    else:
        click.echo("No files were changed")


if __name__ == '__main__':
    cli(obj={})
