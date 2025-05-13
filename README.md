# desarrollo_web_nahuel_sanhueza
Tareas Desarrollo Web

## Estructura de archivos

La estructura que segui para ordenar los archivos tiene relacion respecto a la logica de representacion a traves de modelos:

```txt
desarrollo_web_nahuel_sanhueza
│   README.md 
│
└───app
│   │   run.py // punto principal de ejecucion de la app
│   │   db.py // inicializacion y manejo de uso de la db
│   │   requirements.txt
│   │
│   └───models // Representacions de las entidades de la BD, enums y clases de datos
│       │   ...
│   
└───routes // Definicion de rutas por medio de blueprints de flask
│       │   ...
└───static // Archivos estaticos
│       │   ...
└───templates // Templates de paginas
│       │   ...
└───utilities // Archivos de utilidades principalmente para parsing de datos
```

## Comentarios

- Existen varios metodos y funciones que no poseen documentacion dado que el mismo nombre de este es descriptivo respecto a lo que realiza, un ejemplo es el metodo `get_entitie_by_id` que existe en `base.py`, como dice su nombre este metodo obtiene una entidad por su id.

- Al comienzo utilizaba una estructura de datos especifica para enviar los datos hacia el front-end, sin embargo despues conoci `joinedload` para cargar los datos de las entidades relacionadas a una entidad para asi solo enviar la entidad especificaba utilizada en la pagina deseada.
