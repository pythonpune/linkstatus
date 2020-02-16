import nox


@nox.session
def run_tests(session):
    session.install("-r", "dev-requirements.txt")
    session.install("-e", ".")
    session.run("pytest", "tests")
