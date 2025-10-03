from importlib.metadata import version, PackageNotFoundError

# Expose Dagster Definitions object at the package root so that commands like
# `dagster dev -m workbench` or auto-discovery mechanisms that import the
# top-level `workbench` module can locate the object without needing to know
# its nested path.

from .defs.definitions import defs  # noqa: F401  (re-export for Dagster discovery)

# Optional: expose package version if installed via pip/poetry
try:
    __version__: str = version("workbench")
except PackageNotFoundError:  # package likely in editable mode
    __version__ = "0.0.0"

__all__ = [
    "defs",
    "__version__",
]
