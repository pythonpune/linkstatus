import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_linkstatus_command():
    result = subprocess.run("linkstatus", stdout=subprocess.PIPE)
    assert result.returncode == 1
    assert "Source Not Found" in result.stdout.decode()
    assert "Run 'linkstatus --help' for more information." in result.stdout.decode()


def test_linkstatus_command_with_source():
    src = os.path.join(BASE_DIR, "conftest.py")
    result = subprocess.run(["linkstatus", src], stdout=subprocess.PIPE)
    assert result.returncode == 0
    assert result.stdout.decode().strip() == "No link found"
