# Architecture

## Structure

The application structure follows the same three layer architecture as the reference app:

```
 ui

 |
 v

services  -----> entities

  |                ^
  v                |
                   |
repositories  -----|
```

where `ui` handles the interface, `services` the application logic, and `repositories` the data storage side. `entities` contains the data structures used by the application.
