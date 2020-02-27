import glob
import os
from shutil import get_terminal_size

import click
import requests

from linkstatus.parser import link_validator
from linkstatus.parser import parse_file

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def link_status(link, timeout=5):
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
    """Collect all provide file paths
    Args:
        source: file or directory name
        recursive: search recursively directories

    Returns:
        list of files path
    """
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


@click.command(help="Check Link Status", context_settings=CONTEXT_SETTINGS)
@click.argument("source", nargs=-1, type=click.Path())
@click.option(
    "-r", "--recursive", is_flag=True, help="Include all files from directories recursively"
)
@click.option("-t", "--timeout", default=5, help="Request timeout (default 4 second)")
@click.option("-rt", "--retry", default=2, help="Retry link status (default 2 time)")
def main(source, recursive, timeout, retry):
    exit_code = 0
    up_count = 0
    down_count = 0
    skip_count = 0

    if source:
        files = all_files(source, recursive=recursive)
    else:
        click.echo("Source Not Found")
        click.echo("Run 'linkstatus --help' for more information.")
        exit(1)

    for f in files:
        links = parse_file(f)
        links = link_validator(links)
        if links:
            click.echo(click.style("Links in File: '{}'".format(f), bg="blue", fg="white"))

            for link in links:
                for url in link.urls:
                    if link.skip:
                        skip_count += 1
                        click.echo(
                            "{icon} L{ln} : {url} (skip)".format(
                                icon=click.style("…", fg="blue", bold=True),
                                ln=link.line,
                                url=click.style(url, fg="blue"),
                            )
                        )
                    else:
                        # retry to take status default 2 time
                        for _ in range(int(retry)):
                            status, code = link_status(url, int(timeout))
                            if status is True:
                                break

                        if status:
                            fg = "green"
                            icon = "✓"
                            up_count += 1
                        else:
                            fg = "red"
                            icon = "✗"
                            exit_code = 1
                            down_count += 1

                        click.echo(
                            "{icon} L{ln} : {url} {code}".format(
                                icon=click.style(icon, fg=fg, bold=True),
                                ln=link.line,
                                url=click.style(url, fg=fg),
                                code="" if code == 200 else "({})".format(code),
                            )
                        )

    # Print summary
    total_links = up_count + skip_count + down_count

    if total_links:
        columns = get_terminal_size().columns
        click.echo("=" * columns)
        click.echo(click.style("Links Status Summary".center(columns), bold=True))
        click.echo(click.style("Links UP: {}".format(up_count).center(columns), fg="green"))
        click.echo(click.style("Links SKIP: {}".format(skip_count).center(columns), fg="blue"))
        click.echo(click.style("Links DOWN: {}".format(down_count).center(columns), fg="red"))

        if exit_code == 1:
            click.echo(
                "Warning: Use `noqa` inline comment to skip link check. "
                "like, response code 403 due to header restrictions etc..."
            )
        click.echo("=" * columns)
    else:
        click.echo("No link found")
    exit(exit_code)
