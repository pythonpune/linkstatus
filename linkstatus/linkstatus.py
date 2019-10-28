import glob
import os

import click
import requests

from linkstatus.parser import parse_file


def link_status(link, timeout):
    """Check link status

    Args:
        link: link to check status

    Returns:
        tuple of status (bool) and status code
    """

    try:
        status_code = requests.get(link, timeout=timeout).status_code
    except requests.exceptions.SSLError:
        status_code = requests.get(link, verify=False, timeout=timeout).status_code
    except Exception:  # noqa
        # TODO: include exception in logging
        status_code = None
        pass

    return status_code == 200, status_code


def all_files(source, recursive=False):
    files = []
    for src in source:
        if os.path.isdir(src):
            files.extend(
                [f for f in glob.glob(src + "**/**", recursive=recursive) if os.path.isfile(f)]
            )
        elif os.path.isfile(src):
            files.append(src)
        else:
            click.echo("'{}' not valid source".format(src))
    return files


@click.command(help="Check Link Status")
@click.argument("source", nargs=-1, type=click.Path())
@click.option(
    "-r", "--recursive", is_flag=True, help="Include all files from directories recursively"
)
@click.option("-t", "--timeout", default=5, help="Request timeout (default 4 second)")
@click.option("-rt", "--retry", default=2, help="Retry link status (default 2 time)")
def main(source, recursive, timeout, retry):
    exit_code = 0
    files = all_files(source, recursive=recursive)

    for f in files:
        links = parse_file(f)

        if links:
            click.echo(click.style("File: {}".format(f), bg="blue", fg="white"))

            for link in links:
                for url in link.urls:
                    # try two time at least
                    for _ in range(int(retry)):
                        status, code = link_status(url, int(timeout))
                        if status is True:
                            break

                    if status:
                        fg = "green"
                        icon = "✓"
                    else:
                        fg = "red"
                        icon = "✗"
                        exit_code = 1

                    click.echo(
                        "{icon} L{ln} : {url}".format(
                            icon=click.style(icon, fg=fg, bold=True),
                            ln=link.line,
                            url=click.style(url, fg=fg),
                        )
                    )

    exit(exit_code)
