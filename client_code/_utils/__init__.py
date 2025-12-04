import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
_id = 0
_prefix = "m3-"


def gen_id():
    global _id, _prefix
    _id += 1
    return f":{_prefix}{_id}:"


def noop(*args, **kws):
    pass
