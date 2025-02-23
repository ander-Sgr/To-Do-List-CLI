# To-Do List CLI

Esta es una aplicación de línea de comandos (CLI) para gestionar una lista de tareas. Permite crear, listar, editar y eliminar tareas de manera sencilla.

## Requisitos

- Python 3.8 o superior

## Instalación

Clona este repositorio e instala los paquetes necesarios:

```sh
$ git clone git@github.com:ander-Sgr/to-do-list.git
```

## Uso

Ejecuta el script principal `main.py` con las siguientes opciones:

### Agregar una nueva tarea

```sh
$ python main.py --create --title "Nueva tarea" --descrip "Descripción de la tarea"
```

### Listar todas las tareas

```sh
$ python main.py --list
```

Ejemplo de salida:

```
┌────────────┬────────────────────┬─────────┬─────────────────────┬──────────────┐
│   Title    │    Description     │  Status │      Created at     │ Completed at │
├────────────┼────────────────────┼─────────┼─────────────────────┼──────────────┤
│ Nuevo item │ realizar un insert │ Pending │ 2025-02-18 00:52:15 │ N/A          │
│ hola       │ descip             │ Pending │ 2025-02-18 00:52:21 │ N/A          │
└────────────┴────────────────────┴─────────┴─────────────────────┴──────────────┘
```

### Editar una tarea

```sh
$ python main.py --edit <ID_TAREA> --newTitle "Nuevo título" --newDescrip "Nueva descripción" --completed Y
```

### Eliminar una tarea

```sh
$ python main.py --delete <ID_TAREA>
```

## Estructura del Proyecto

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
