import pytest
import os

from linkstatus.linkstatus import all_files


@pytest.mark.parametrize("recursive", [True, False], ids=["recursive", "non-recursive"])
def test_all_files(sources, recursive):
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
                    files = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(
                        os.path.join(d, f))]
                    inside_files.extend(files)
            expected_files.extend(inside_files)

    assert set(collected_files) == set(expected_files)
