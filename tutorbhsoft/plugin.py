from __future__ import annotations

import functools
import os
import typing as t
# from glob import glob

# import importlib_resources
# from tutor import fmt
from tutor import hooks
from tutor.__about__ import __version_suffix__
# from tutor.hooks import priorities
# from tutor.types import Config, get_typed

from .__about__ import __version__
from tutormfe.hooks import MFE_APPS

# from .hooks import MFE_APPS, MFE_ATTRS_TYPE

# Handle version suffix in nightly mode, just like tutor core
if __version_suffix__:
    __version__ += "-" + __version_suffix__


################# Configuration
config: t.Dict[str, t.Dict[str, t.Any]] = {
    # Add here your new settings
    "defaults": {
        "VERSION": __version__
    },
    "unique": {},
    "overrides": {},
}


@MFE_APPS.add()
def mfe_forks(mfes):
    mfes["home"] = {
        "repository": "https://github.com/BacHaSoftware/frontend-app-home.git",
        "port": 3001,
        "version": "main",
        "name": "home"
    }
    return mfes


hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "mfe-dockerfile-post-npm-install",
            """
    RUN npm install '@edx/frontend-component-footer@git+https://github.com/BacHaSoftware/frontend-component-footer.git#main' --registry=$NPM_REGISTRY
    """
        ),
    ]
)