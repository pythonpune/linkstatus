import nox

nox.options.sessions = ["pre_commit", "tests"]


@nox.session
def pre_commit(session):
    """pre-commit checks"""
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")


@nox.session(python=["pypy3", "3.6", "3.7", "3.8"])
def tests(session):
    """Run unit test over different python env with code coverage"""
    session.install("pytest", "pytest-cov", "ruamel.yaml", "-e", ".")
    session.run(
        "py.test",
        "--cov=linkstatus",
        "--cov-report",
        "term-missing",
        "--cov-branch",
        "--color=yes",
        "-s",
        "-v",
    )


@nox.session()
def ci_tests(session):
    """This is only to run test on ci"""
    session.install("pytest", "pytest-cov", "coverage", "ruamel.yaml", "-e", ".")
    session.run(
        "py.test",
        "--cov=linkstatus",
        "--cov-report=xml",
        "--cov-branch",
        "--color=yes",
        "-s",
        "-v",
    )
    session.run("coverage", "report")


@nox.session()
def package(session):
    """Build and verify package"""
    session.install("twine", "setuptools", "wheel")
    session.run("python", "setup.py", "sdist", "bdist_wheel")
    session.run("ls", "-l", "dist")
    session.run("python", "-m", "twine", "check", "dist/*")


@nox.session()
def dev_setup(session):
    """Ensure development environment works everywhere. mainly with ci on different platform"""
    session.run("python", "-m", "pip", "install", "-e", ".[dev]")
    session.run("python", "-c", "import linkstatus; print(linkstatus.__spec__)")
    session.install("pytest", "ruamel.yaml")
    session.run("py.test", "-v", "tests/test_linkstatus.py")
