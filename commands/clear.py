import click

from dao.list_dao import remove_value


@click.command()
@click.argument('key')
def clear(key):
    """Remove value from clipboard"""
    remove_value(key)


if __name__ == '__main__':
    clear()
