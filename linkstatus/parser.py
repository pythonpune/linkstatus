import re
from collections import namedtuple

import markdown


REGULAR_EXP = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

LINKS = namedtuple("LINKS", ["line", "urls", "skip"])


def parse_line(line):
    """Parse links from line/string

    Args:
        string: data string
    Returns:
        list of links
    """
    string = line.strip()
    html_format = markdown.markdown(string, output_format="html")
    links = re.findall(REGULAR_EXP, html_format)

    # TODO: Improve regex to remove this workaround for trailing </p> or </li>
    links = [
        l.replace("</p>", "").replace("</li>", "").replace("</a>", "").replace(")", "")
        for l in links
    ]
    return links


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
                skip = True if "noqa" in line else False
                links.append(LINKS(line=line_number + 1, urls=line_links, skip=skip))
    return links
