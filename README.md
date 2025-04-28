# 🧩 Práctica UNIR - Pokémon App

Este repositorio fue creado como parte de una actividad práctica para profundizar en el uso de **Forks** y **Pull Requests** en GitHub.

---

## 🎯 Objetivo

El objetivo principal de este proyecto es practicar el flujo de trabajo colaborativo en GitHub, simulando un entorno real de desarrollo de software.  
Cada participante debe:

- Realizar un Fork del repositorio.
- Crear una nueva rama para su funcionalidad.
- Implementar cambios o mejoras en la aplicación.
- Crear un Pull Request para fusionar sus cambios al repositorio principal.

---

## 🕹️ Aplicación Pokémon

La aplicación incluida (`pokemon_app.py`) permite:

- Listar los Pokémon disponibles.
- Atrapar un Pokémon aleatorio.

### Catch Random Pokémon 🎲

La función `catch_random_pokemon()` simula la captura de un Pokémon de forma aleatoria.

- Hay un **75% de probabilidad** de atrapar exitosamente un Pokémon.
- Hay un **25% de probabilidad** de que el Pokémon se escape y no pueda ser atrapado.

La función elige un Pokémon aleatorio de la lista disponible (`POKEMONS`) y, dependiendo de la suerte, muestra un mensaje de éxito o de consolación.


---

## 🛠️ Cómo ejecutar la aplicación

### Opción 1: Ejecutar directamente con Python

```bash
python3 pokemon_app.py

### Opción 2: usar Make file

Asegúrate de tener instalado make en tu entorno.

En Linux y MacOS viene preinstalado.

En Windows puede ser necesario instalarlo usando Chocolatey o agregando make.exe a Git Bash.

Dentro de la carpeta raíz del proyecto, ejecuta:

bash
Copiar
Editar
make run
Esto ejecutará internamente:

bash
Copiar
Editar
python3 pokemon_app.py

✅ Esta opción es útil para simplificar la ejecución durante el desarrollo colaborativo.