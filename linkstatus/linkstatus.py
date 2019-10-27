import os
import glob

import requests
import click

from linkstatus.parser import parse_file

EXIT_STATUS = 0


def link_status(link):
    """Check link status

    Args:
        link: link to check status

    Returns:
        tuple of status (bool) and status code
    """

    try:
        status_code = requests.get(link, timeout=5).status_code
    except requests.exceptions.SSLError:
        status_code = requests.get(link, verify=False, timeout=5).status_code
    except Exception:  # noqa
        # TODO: include exception in logging
        status_code = None
        pass

    return status_code == 200, status_code


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
            click.echo(click.style("File: {}".format(f), bg="blue", fg="white"))

            for link in links:
                for url in link.urls:
                    # try two time at least
                    for _ in range(2):
                        status, code = link_status(url)
                        if status:
                            break

                    if status:
                        fg = "green"
                        icon = "✓"
                    else:
                        fg = "red"
                        icon = "✗"
                        EXIT_STATUS = 1

                    click.echo(
                        "{icon} L{ln} : {l}".format(
                            icon=click.style(icon, fg=fg, bold=True),
                            ln=link.line,
                            l=click.style(url, fg=fg),
                        )
                    )

    exit(EXIT_STATUS)
