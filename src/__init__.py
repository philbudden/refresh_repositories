import logging
import os
logging.basicConfig(
    level=int(os.getenv('LOGLEVEL', '20')),
    format='(%(levelname)s) %(message)s'
)

from ._version import __version__
