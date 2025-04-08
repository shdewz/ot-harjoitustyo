from invoke import task
import sys
pty_enable = False if sys.platform=="win32" else True


@task
def start(ctx):
    ctx.run("python src/index.py", pty=pty_enable)

@task
def build(ctx):
    ctx.run("python src/build.py", pty=pty_enable)

@task
def test(ctx):
    ctx.run("pytest src", pty=pty_enable)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=pty_enable)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty_enable)

@task
def lint(ctx):
    ctx.run("pylint src", pty=pty_enable)
