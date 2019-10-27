import re
from collections import namedtuple

import markdown


REGULAR_EXP = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

LINKS = namedtuple("LINKS", ["line", "urls"])


def parse_line(string):
    """Parse links from line/string

    Args:
        string: data string
    Returns:
        list of links
    """
    # if `noqa` (no quality assurance) marked in line then just skip that string
    if "noqa" not in string:
        html_format = markdown.markdown(string, output_format="html")
        links = re.findall(REGULAR_EXP, html_format)

        # TODO: Improve regex to remove this workaround for trailing </p> or </li>
        links = [l.replace("</p>", "").replace("</li>", "") for l in links]
        return links
    else:
        return []


def parse_file(file_path):
    """Read file and parse links
    Args:
        file_path: path of file
    Return:
        list of LINKS nametuple
    """
    links = []
    with open(file_path) as f:
        for line_number, line in enumerate(f):
            line_links = parse_line(line)
            if line_links:
                links.append(LINKS(line=line_number + 1, urls=line_links))
    return links
