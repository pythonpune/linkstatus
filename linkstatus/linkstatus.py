from urllib import request
from urllib.error import URLError
from urllib.error import HTTPError


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
