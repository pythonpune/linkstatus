import os
import glob
from urllib import request
from urllib.error import URLError
from urllib.error import HTTPError

import click

from src.parser import parse_file


def link_status(link):
    """Check link status

    Args:
        link: link to check status

    Returns:
        tuple of status (bool) and status code/ reason
    """
    try:
        connection = request.urlopen(link)
        return True, connection.code
    except HTTPError as e:
        return False, e.code
    except URLError as e:
        return False, e.reason


def all_files(source):
    files = []
    for src in source:
        if os.path.isdir(src):
            files.extend([f for f in glob.glob(src + "**/**", recursive=True) if os.path.isfile(f)])
        elif os.path.isfile(src):
            files.append(src)
        else:
            click.echo("'{}' not valid source".format(src))
    return files


@click.command(help="Check Link Status")
@click.argument("source", nargs=-1, type=click.Path())
def main(source):
    files = all_files(source)

    for f in files:
        links = parse_file(f)

        if links:
            click.echo(click.style("File: {}".format(f), bg='blue', fg='white'))

            for link in links:
                for url in link.urls:
                    status, code = link_status(url)

                    fg = "green" if status else "red"
                    _status = "UP" if status else "DOWN"

                    click.echo(
                        "L{}: {} ==> {}".format(link.line, url, click.style(_status, fg=fg))
                    )
