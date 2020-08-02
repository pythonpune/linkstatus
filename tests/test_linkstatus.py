import os
import subprocess
from pathlib import Path

import pytest

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


def test_linkstatus_command():
    result = subprocess.run("linkstatus", stdout=subprocess.PIPE)
    assert result.returncode == 1
    assert "Source Not Found" in result.stdout.decode()
    assert "Run 'linkstatus --help' for more information." in result.stdout.decode()


@pytest.mark.parametrize(
    "file",
    [BASE_DIR / "conftest.py", BASE_DIR / "data" / "text_file"],
    ids=["no-link", "with-link"],
)
def test_linkstatus_command_with_source(file):
    result = subprocess.run(["linkstatus", file], stdout=subprocess.PIPE)
    data = result.stdout.decode().strip()

    if file.name == "text_file":
        assert result.returncode == 1
        assert all([check in data for check in ["Links SKIP: 0", "Links DOWN: 1", "Links UP: 3"]])
    else:
        assert result.returncode == 0
        assert data == "No link found"
