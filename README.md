# Ohjelmistotekniikka, harjoitustyö

This program will be a **relic manager** for the gacha game *Honkai: Star Rail*, letting users manage and automatically score the value of their in-game items.

## Documentation

- [User guide](relic-manager/docs/user-guide.md)
- [Requirements specification](relic-manager/docs/requirements-specification.md)
- [Architecture](relic-manager/docs/architecture.md)
- [Working hours](relic-manager/docs/working-hours.md)
- [Changelog](relic-manager/docs/changelog.md)

## Setup

1. Navigate to the app directory

```bash
cd relic-manager
```

2.  Install the dependencies

```bash
poetry install
```

3. Initialize the database

```bash
poetry run invoke build
```

4. Start the app

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
