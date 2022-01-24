import click

from dao.list_dao import remove_all_values


@click.command()
def clear_all():
    """Remove value from clipboard"""
    remove_all_values()


if __name__ == '__main__':
    clear_all()
