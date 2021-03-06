import os

import click
from flask_migrate import upgrade

from app import app, db, tasks
from app import models
from app.auth.routes import reverify


def get_all_in_all(module):
    return {
        model_name: getattr(module, model_name, None) for model_name in module.__all__
    }


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "tasks": tasks, **get_all_in_all(models)}


@app.cli.group()
def auth():
    """User  and authentication commands."""


@auth.command(with_appcontext=True)
@click.option(
    "--display_name",
    prompt=True,
    default=lambda: os.environ.get("ADMIN_DISPLAY_NAME", ""),
)
@click.option(
    "--email",
    prompt=True,
    default=lambda: os.environ.get("ADMIN_EMAIL", "test@example.com"),
)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    default=lambda: "*" * len(os.environ.get("ADMIN_PASSWORD", "")),
)
def createsuperuser(display_name, email, password):
    """Create a superuser"""
    u = models.User(display_name=display_name, email=email, is_admin=True)
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    with app.test_request_context("/"):
        reverify()


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    upgrade()


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
