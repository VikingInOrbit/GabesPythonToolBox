import os

__path__.insert(
    0,
    os.path.normpath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "Tests")
    ),
)
