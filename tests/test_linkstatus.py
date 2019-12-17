import os


def test_linkstatus_command():
    return_code = os.system("linkstatus")
    assert return_code == 0
