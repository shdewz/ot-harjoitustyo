# User guide

## Requirements

- Python `>=3.12`

## Configuration

Enter the app directory first:

```bash
cd relic-manager
```

Configure the `.env` file as follows:

```env
DATABASE_FILENAME=database.sqlite
```

The database is saved to the `data` folder by default. Create this folder before first start if it does not exist.

## Starting up

Install all dependencies with

```bash
poetry install
```

After installing dependencies, initialize the project with

```bash
poetry run invoke build
```

After initialization, the program can be started with

```bash
poetry run invoke start
```

Additionally, the database may be pre-populated with some items using

```bash
poetry run python3 src/create_sample_db.py
```

## Usage

The main page shows all added relics in the database. Using the *Add new relic* button a new relic can be added, though currently only with predetermined fixed attributes.
