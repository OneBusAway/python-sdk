# Examples README

## Setting up the environment

### With Rye

We use [Rye](https://rye.astral.sh/) to manage dependencies so we highly recommend [installing it](https://rye.astral.sh/guide/installation/) as it will automatically provision a Python environment with the expected Python version.

After installing Rye, you'll just have to run this command:

```sh
$ rye sync --all-features
```

You can then run scripts using `rye run python script.py` or by activating the virtual environment:

```sh
$ rye shell
# or manually activate - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `rye run` prefix
$ python script.py
```

### Without Rye

Alternatively if you don't want to install `Rye`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -r requirements-dev.lock
```

## Run the examples

```bash
python EXAMPLE_NAME.py
```

## `.env` file: API keys and server URLs

Copy the file `.env.example` to `.env` and edit it with your preferred API key and server URL.
