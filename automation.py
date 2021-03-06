import nox  # type: ignore


python = ["3.6"]


@nox.session(python=["3.6", "3.7"])
def develop(session):
    session.install(".[dev]", ".[docs]")
    session.install("-e", ".")


@nox.session(python=python)
def build(session):
    session.install("setuptools")
    session.install("wheel")
    session.install("twine")
    session.run("rm", "-rf", "dist", external=True)
    session.run("python", "setup.py", "--quiet", "sdist", "bdist_wheel")


@nox.session(python=python)
def publish(session):
    build(session)
    print("REMINDER: Has the changelog been updated?")
    session.run("python", "-m", "twine", "upload", "dist/*")


@nox.session(python=python)
def watch_docs(session):
    session.install(".[docs]")
    session.run("mkdocs", "serve")


@nox.session(python=python)
def publish_docs(session):
    session.install(".[docs]")
    session.run("python", "generate_docs.py")
    session.run("mkdocs", "gh-deploy")
