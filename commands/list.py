import click

from dao.list_dao import list_values


@click.command()
def list():
    """Get all values from clipboard"""
    values = list_values()
    for key, value in values.items():
        print(key + " -> " + value)


if __name__ == '__main__':
    list()
