from flask.cli import FlaskGroup

from src import create_app, db
from src.api.foos.models import Foo


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(Foo(column_one='foo1', column_two="doo1"))
    db.session.add(Foo(column_one='foo2', column_two="doo2"))
    db.session.commit()


if __name__ == '__main__':
    cli()
