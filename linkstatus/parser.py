import re
from collections import namedtuple

import markdown

REGULAR_EXP = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

LINKS = namedtuple("LINKS", ["line", "urls", "skip", "valid"])


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
                links.append(LINKS(line=line_number + 1, urls=line_links, skip=skip, valid=False))
    return links


def link_validator(links_list):
    """Validate link
    Args:
        links_list: List of links.

    Return:
        Named tuple of the valid and invalid links.
    """
    validated_list = []

    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        # for domain
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    for link in links_list:
        urls = []
        for i in link.urls:
            if re.match(regex, i):
                urls.append(i)
            else:
                validated_list.append(LINKS(line=link.line, urls=[i], valid=False, skip=True))
        validated_list.append(LINKS(line=link.line, urls=urls, skip=False, valid=True))
    return validated_list
