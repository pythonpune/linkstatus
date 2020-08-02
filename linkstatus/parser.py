from collections import namedtuple

from urlextract import URLExtract

LINKS = namedtuple("LINKS", ["line", "urls", "skip"])

EXTRACTOR = URLExtract()


def parse_line(line):
    """Parse links from line/string

    Args:
        line: data line
    Returns:
        list of links
    """
    links = EXTRACTOR.find_urls(line)
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
