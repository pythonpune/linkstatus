from ruamel.yaml import safe_load
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def data():
    with open(os.path.join(BASE_DIR, "data.yaml"), "r") as f:
        data = safe_load(f)
    return data


@pytest.fixture(
    params=["file", "files", "directory", "directories", "file-directory"], scope="module"
)
def sources(request):
    SOURCES_TYPE = {
        "file": [os.path.join(BASE_DIR, "data", "text_file")],
        "files": [
            os.path.join(BASE_DIR, "data", "text_file"),
            os.path.join(BASE_DIR, "data", "recursive", "recursive_text_file.txt")
        ],
        "directory": [os.path.join(BASE_DIR, "data")],
        "directories": [
            os.path.join(BASE_DIR, "data"),
            os.path.join(BASE_DIR, "data", "recursive")
        ],
        "file-directory": [
            os.path.join(BASE_DIR, "data", "text_file"),
            os.path.join(BASE_DIR, "data")
        ]
    }
    return SOURCES_TYPE[request.param]
