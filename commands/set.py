import click

from dao.list_dao import save_value


@click.command()
@click.argument('key', required=True)
@click.argument('value', required=True)
def set(key, value):
    """Save value to clipboard"""
    save_value(key, value)


if __name__ == '__main__':
    set()
