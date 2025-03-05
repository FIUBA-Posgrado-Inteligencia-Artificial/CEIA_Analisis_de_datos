
![](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos/blob/main/banner.png)


Bienvenidos al repositorio de la materia **Análisis de Datos**! Aquí encontrarán los materiales de clase, notebooks, datasets y recursos adicionales.

## 📂 Estructura del Repositorio

- **`notebooks/`** → Contiene las notebooks con los ejemplos y ejercicios de cada clase.
- **`datasets/`** → Conjunto de datos utilizados en los ejemplos y prácticas.
- **`recursos/`** → Artículos, enlaces y materiales de referencia recomendados.
- **`scripts/`** → Código adicional o funciones auxiliares utilizadas en las notebooks.
- **`imagenes/`** → Gráficos, diagramas y visualizaciones relevantes para el curso.

## 📚 Contenido del Curso

| Clase | Tema | Notebooks |
|--------|-----------------------------|-----------------------------|
| 1️⃣ | Introducción al Análisis de Datos | [notebook_clase_1](notebooks/clase_01_introduccion.ipynb) |
| 2️⃣ | Visualización y exploración de datos | [notebook_clase_2](notebooks/clase_02_preprocesamiento.ipynb) |
| 3️⃣ | Caracterización de variables e imputación de datos faltantes | [notebook_clase_3](notebooks/clase_03_visualizacion.ipynb) |
| 4️⃣ | Outliers, discretización y escalamiento | [notebook_clase_4](notebooks/clase_04_outliers_discretizacion_escalamiento.ipynb)|
| 5️⃣ | Ingeniería de features | [notebook_clase_5](notebooks/clase_05_ingenieria_de_features.ipynb) |
| 6️⃣ | Taller práctico | [notebook_clase_6](notebooks/clase_06_taller.ipynb)|
| 7️⃣ | Presentación de trabajos finales | N/A |
| 8️⃣ | Reducción de dimensionalidad | [notebook_clase_8](notebooks/clase_08_reduccion_dimensionalidad.ipynb) |


## ⚙️ Instalación y Configuración del Entorno

En esta sección se explican los pasos para utilizar este repositorio.

### 🔹 Opción 1: Usar un env de Conda

1. Clonar el repositorio:

```bash
git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos.git
cd CEIA_Analisis_de_datos
```

2. Crear y activar el environment:

```bash
conda env create -f environment.yml
conda activate add-env
```

3. Abrir Jupyter

```bash
jupyter notebook
```

### 🔹 Opción 2: Usar un env de Poetry

Este proyecto también permite usar Poetry para manejo de dependencias. Seguir los pasos detallados a continuación para crear un environment a partir de los archivos `pyproject.toml` y `poetry.lock` proporcionados.

#### Prerrequisitos 
 * Poetry : [Instrucciones de instalación](https://python-poetry.org/docs/#installing-with-the-official-installer)
 * Python 3.11 o 3.12

1. Clonar el repo:

```bash
git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos.git
cd CEIA_Analisis_de_datos
```

2. Crear el environment (ejemplo con Python 3.11, ajustar a 3.12 de ser necesario):

* macOS/Linux

```bash
poetry env use python3.11  
```
* Windows

```bash
poetry env use "py -3.11" 
```

3. Instalar dependencias (Linux/MacOS/Windows)
```bash
poetry install --no-root 
```
Nota: --no-root evita la instalación como package que no es necesaria aquí.

4. Verificar que el environment se instaló correctamente

```bash
poetry env list
```
> Este comando devuelve todos los environments asociados al proyecto (verificar que `ceia-analisis-de-datos-xxxxxxx-py3.11` aparece en la lista)

```bash
poetry env info
```
> Este comando muestra detalles tales como la versión de Python y el path (ej., `/Users/<username>/Library/Caches/pypoetry/virtualenvs/...` en macOS o `C:\Users\<username>\AppData\Local\pypoetry\...` en Windows).


5. Activar el environment

* macOS/Linux (zsh/bash):

```bash
eval "$(poetry env activate)" 
```

* Windows (PowerShell/CMD):

```bash
Invoke-Expression (poetry env activate)
```

> Después de ejecutar el comando, el nombre del environment debería aparecer en el prompt de la terminal entre paréntesis (ej., `ceia-analisis-de-datos-xxxxxxx-py3.11`).

7. Verificar activación

```bash
python --version
```
> Debería mostrar Python 3.11.X o 3.12.X.


```bash
which python  # macOS/Linux
where python  # Windows
```
> Debería apuntar al Pyhton del env. de Poetry (ej., /Users/<username>/.../bin/python o C:\Users\<username>\...\Scripts\python.exe).


6. Abrir Jupyter

```bash
poetry run jupyter notebook
```


### 🔹 Opción 3: Usar Google Colab

Al momento de la actualización de este repositorio (Marzo 2025) Colab utiliza Python 3.11 y no debería haber inconvenientes para ejecutar las notebooks de la materia con esta herramienta. Pasos a seguir:

1. Desde Colab, ir al menú 'File' y hacer click en 'Open Notebook'

2. En la nueva ventana que se abre, ir a la opción 'GitHub' (en el menú de la derecha).

3. En la barra buscadora, copiar el nombre del repo: 

```bash
FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos
```

4. Asegurarse que en 'Repository' aparezca el nombre correcto (FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos) y la branch sea 'main'. Hacer click en la notebook deseada para abrir.



## 📫 Contacto

* [✉️](macroldan@fi.uba.edu.ar) María Carina Roldán 
* [✉️](arigarmendia@gmail.com) Ariadna Garmendia
