import click

from dao.list_dao import get_value


@click.command()
@click.argument('key')
def get(key):
    """Get value from clipboard"""
    value = get_value(key)
    if value:
        print(value)


if __name__ == '__main__':
    get()
