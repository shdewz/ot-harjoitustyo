# User guide

## Configuration

1. Navigate to the app directory and create the data folder

```bash
cd relic-manager
mkdir data
```

2. Configure the `.env` file as follows:

```env
DATABASE_FILENAME=database.sqlite
```

3. Install the dependencies

```bash
poetry install
```

4. Initialize the database

```bash
poetry run invoke build
```

## Starting up

After setup, the program can be started with

```bash
poetry run invoke start
```

## Usage

The main page shows all added relics in the database. Using the *Add new relic* button a new relic can be added and its stats chosen. Relics can be removed by double-clicking the *x* buttons.
