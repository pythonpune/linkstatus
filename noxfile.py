import nox


@nox.session
def pre_commit(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")


@nox.session(python=["3.6", "3.7"])
def tests(session):
    session.install("pytest", "ruamel.yaml", ".")
    session.run("pytest", "-sqvv", "tests")
