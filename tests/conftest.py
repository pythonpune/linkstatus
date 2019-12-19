import os
from collections import namedtuple

import pytest
from ruamel.yaml import safe_load

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def data():
    with open(os.path.join(BASE_DIR, "data.yaml"), "r") as f:
        data = safe_load(f)
    return data


SOURCES_TYPE = {
    "file": [os.path.join(BASE_DIR, "data", "markdown_file.md")],
    "files": [
        os.path.join(BASE_DIR, "data", "text_file"),
        os.path.join(BASE_DIR, "data", "recursive", "recursive_text_file.txt"),
    ],
    "directory": [os.path.join(BASE_DIR, "data")],
    "directories": [os.path.join(BASE_DIR, "data"), os.path.join(BASE_DIR, "data", "recursive")],
    "file-directory": [os.path.join(BASE_DIR, "data", "text_file"), os.path.join(BASE_DIR, "data")],
}


@pytest.fixture(
    params=["file", "files", "directory", "directories", "file-directory"], scope="module"
)
def sources(request):
    return SOURCES_TYPE[request.param]


@pytest.fixture(scope="module")
def files(data):
    File = namedtuple("File", ["name", "abs_path", "link_data"])
    _files = []

    for d, f in data.items():
        dir = os.path.join(f["parent"], d) if f["parent"] else d

        for f, link_data in data[d]["files"].items():
            _files.append(File(f, os.path.join(BASE_DIR, dir, f), link_data))
    return _files
