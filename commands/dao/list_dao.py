import io
import json
import os
from typing import Optional

store_file_path = os.path.expanduser('~') + '/.custom_clipboard_store'


def check_store():
    """Check if key value store is created. If not, create it"""
    if not os.path.isfile(store_file_path):
        open(store_file_path, 'a').close()


def run_before(function):
    """Call functions in parameter and after that execute original function"""

    def wrapper(f):
        def wrapped(*args, **kwargs):
            function()
            ret = f(*args, **kwargs)
            return ret

        return wrapped

    return wrapper


@run_before(check_store)
def list_values() -> {}:
    """List all values from database"""
    with open(store_file_path, 'r') as database:
        try:
            return json.load(database)
        except (io.UnsupportedOperation, json.decoder.JSONDecodeError):
            return {}


@run_before(check_store)
def get_value(key: str) -> Optional[str]:
    """Load stored data with specified key"""
    values = list_values()
    if key in values:
        return values[key]
    else:
        return None


@run_before(check_store)
def save_value(key: str, value: str):
    """Store new key value pair to json database"""
    values = list_values()
    values[key] = value

    with open(store_file_path, 'w') as database:
        json.dump(values, database)


@run_before(check_store)
def remove_value(key):
    """Remove key value pair to json database"""
    values = list_values()
    if key in values:
        values.pop(key)
        with open(store_file_path, 'w') as database:
            json.dump(values, database)


@run_before(check_store)
def remove_all_values():
    """Remove all from database"""
    with open(store_file_path, 'w') as database:
        json.dump({}, database)
