## Setting up the environment

### With Rye

We use [Rye](https://rye.astral.sh/) to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Or [install Rye manually](https://rye.astral.sh/guide/installation/) and run:

```sh
$ rye sync --all-features
```

You can then run scripts using `rye run python script.py` or by activating the virtual environment:

```sh
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `rye run` prefix
$ python script.py
```

### Without Rye

Alternatively if you don't want to install `Rye`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -r requirements-dev.lock
```

## Modifying/Adding code

> [!WARNING]
> Most of this SDK is generated from the OpenAPI specification using [Stainless](https://www.stainless.com/).
> **Manual edits to generated files are discouraged**, as they may conflict with or be overwritten during future SDK generations.

If you encounter a bug or missing feature in the generated API client, types, or endpoints, please [open an issue](https://github.com/OneBusAway/python-sdk/issues) so maintainers can address it in the OpenAPI specification or generator configuration rather than patching generated files directly.

### Where contributions are encouraged

The Stainless generator ignores custom directories and preserves hand-maintained areas. Contributions are welcome in:

- `src/onebusaway/lib/` — Custom modules and helpers that extend the SDK (ignored by Stainless; see `src/onebusaway/lib/.keep`).
- `examples/` — Example scripts, `examples/README.md`, and helper utilities under `examples/helpers/` (ignored by Stainless; see `examples/.keep`).
- Documentation — Hand-maintained guides such as `CONTRIBUTING.md` and `examples/README.md`.
- `tests/` — Custom test files for code added in `src/onebusaway/lib/`.

### Generated files (avoid editing manually)

Avoid direct edits to files generated or managed by Stainless, including:

- `src/onebusaway/_client.py`, `src/onebusaway/resources/`, `src/onebusaway/types/`, and core client/runtime modules in `src/onebusaway/` (such as `src/onebusaway/_base_client.py`).
- `tests/api_resources/` and `tests/test_client.py` (generated API resource and client tests).
- `api.md` (generated API reference documentation).

## Adding and running examples

All files in the `examples/` directory are not modified by the generator and can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S rye run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/OneBusAway/python-sdk.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ rye build
# or
$ python -m build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

Most tests require you to [set up a mock server](https://github.com/dgellow/steady) against the OpenAPI spec to run the tests.

```sh
$ ./scripts/mock
```

```sh
$ ./scripts/test
```

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) and
[black](https://github.com/psf/black) to format the code in the repository.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Changes made to this repository via the automated release PR pipeline should publish to PyPI automatically. If
the changes aren't made through the automated pipeline, you may want to make releases manually.

### Publish with a GitHub workflow

You can release to package managers by using [the `Publish PyPI` GitHub action](https://www.github.com/OneBusAway/python-sdk/actions/workflows/publish-pypi.yml). This requires a setup organization or repository secret to be set up.

### Publish manually

If you need to manually release a package, you can run the `bin/publish-pypi` script with a `PYPI_TOKEN` set on
the environment.
