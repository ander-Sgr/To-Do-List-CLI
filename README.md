# To-Do List CLI

This is an application on CLI for manage a a to-do list. Allows to create, modify, list and delete tasks in a easy way

## Requirements

- Python 3.8 o higher

## Installation

Clone this repo.

```sh
$ git clone git@github.com:ander-Sgr/to-do-list.git
```

## Use

Runs the main script `main.py` with follow options.

### Add a new task

```sh
$ python main.py --create --title "New task" --descrip "Description's task"
```

### List all task

```sh
$ python main.py --list
```

Output example:

```
┌────────────┬────────────────────┬─────────┬─────────────────────┬──────────────┐
│   Title    │    Description     │  Status │      Created at     │ Completed at │
├────────────┼────────────────────┼─────────┼─────────────────────┼──────────────┤
│ Nuevo item │ insert insert      │ Pending │ 2025-02-18 00:52:15 │ N/A          │
│ hola       │ descip             │ Pending │ 2025-02-18 00:52:21 │ N/A          │
└────────────┴────────────────────┴─────────┴─────────────────────┴──────────────┘
```

### Edit a task

```sh
$ python main.py --edit <ID_TAREA> --newTitle "New title" --newDescrip "New description" --completed Y
```

### Delete a task

```sh
$ python main.py --delete <ID_TASK>
```

## Project structure

```
.
├── data
│   └── tasks.json
├── main.py
├── README.md
├── tasks
│   ├── __init__.py
│   ├── manager.py
│   ├── models.py
│   └── storage.py
└── utils
    ├── display.py
    ├── __init__.py
```
