"""Automatically call nest-asyncio."""

import nest_asyncio
nest_asyncio.apply()

from importlib import reload
import stan

# force reload
stan = reload(stan)
del stan
del reload
del nest_asyncio

from stan import *
