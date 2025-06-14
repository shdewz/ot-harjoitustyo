# Ohjelmistotekniikka, harjoitustyö

This program will be a **relic manager** for the gacha game *Honkai: Star Rail*, letting users manage and automatically score the value of their in-game items.

## Releases

- [Week 7](https://github.com/shdewz/ot-harjoitustyo/releases/tag/viikko7)
- [Week 6](https://github.com/shdewz/ot-harjoitustyo/releases/tag/viikko6)
- [Week 5](https://github.com/shdewz/ot-harjoitustyo/releases/tag/viikko5)

## Documentation

- [User guide](relic-manager/docs/user-guide.md)
- [Requirements specification](relic-manager/docs/requirements-specification.md)
- [Architecture](relic-manager/docs/architecture.md)
- [Working hours](relic-manager/docs/working-hours.md)
- [Changelog](relic-manager/docs/changelog.md)

## Setup

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

5. (Optional) Populate the database with sample data

```bash
poetry run invoke populate
```

6. Start the app

```bash
poetry run invoke start
```

## Other command line functions

### Testing

Tests can be run with the following command:

```bash
poetry run invoke test
```

### Test coverage

A test coverage report can be created with the following command:

```bash
poetry run invoke coverage-report
```

### Pylint

The code can be checked through pylint with the following command:

```bash
poetry run invoke lint
```
