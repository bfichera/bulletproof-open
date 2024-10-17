from pathlib import Path
import logging
from uuid import uuid4


logger = logging.getLogger(__file__)


def open(file, *args, **kwargs):
    path = Path(file)
    if path.exists():
        newpath = path.parent / (path.name+uuid4().hex)
        logger.warning(f'Path {path} exists! Creating new filepath {newpath}.')
        return open(newpath, *args, **kwargs)
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        logger.warning(
            f'Directory path {path.parent} does not exist!'
            f' Creating new directory (including parents) {path.parent}.'
        )
    return open(path, *args, **kwargs)
