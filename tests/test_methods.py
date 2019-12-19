import os

import pytest

from linkstatus.linkstatus import all_files
from linkstatus.linkstatus import link_status
from linkstatus.parser import parse_file


@pytest.mark.parametrize("recursive", [True, False], ids=["recursive", "non-recursive"])
def test_all_files(sources, recursive):
    """Test file collection with all_files method"""

    collected_files = all_files(sources, recursive=recursive)
    expected_files = []

    for source_entity in sources:
        if os.path.isfile(source_entity):
            expected_files.append(source_entity)
        else:
            inside_entities = [os.path.join(source_entity, e) for e in os.listdir(source_entity)]
            inside_files = [f for f in inside_entities if os.path.isfile(f)]

            if recursive:
                for d in [d for d in inside_entities if os.path.isdir(d) and "__" not in d]:
                    files = [
                        os.path.join(d, f)
                        for f in os.listdir(d)
                        if os.path.isfile(os.path.join(d, f))
                    ]
                    inside_files.extend(files)
            expected_files.extend(inside_files)

    assert set(collected_files) == set(expected_files)


def test_parse_file(files):
    """test parse_file l.e. links and line number"""

    for file in files:
        parse_data = parse_file(file.abs_path)
        assert len(file.link_data) == len(
            parse_data
        ), f"File {file.abs_path} link count not matched with expected"

        for links in parse_data:
            for link in links.urls:
                assert file.link_data.get(link), f"link {link} not found in file {file.abs_path}"
                assert (
                    str(links.line) in file.link_data.get(link)["line"]
                ), f"Line number not matched"


def test_link_status(files):
    """test status of link"""

    for file in files:
        for link, data in file.link_data.items():
            status, code = link_status(link)
            assert status == data["status"], f"{link}: status is {status} expected {data['status']}"
