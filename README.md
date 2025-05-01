
![](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos/blob/main/banner.png)


Bienvenidos al repositorio de la materia **Análisis de Datos**! Aquí encontrarán los materiales de clase, notebooks, datasets y recursos adicionales.

## 📂 Estructura del Repositorio

- **`notebooks/`** → Contiene las notebooks con los ejemplos y ejercicios de cada clase.
- **`datasets/`** → Conjunto de datos utilizados en los ejemplos y prácticas.
- **`recursos/`** → Ejericios, reportes y otros materiales útiles.
- **`scripts/`** → Código adicional o funciones auxiliares utilizadas en las notebooks.
 <!---
- **`imagenes/`** → Gráficos, diagramas y visualizaciones relevantes para el curso.
--->

### 🎓 ¿Sos alumno de una cohorte anterior? Encontrá [aquí](recursos/guia-coh-anterior.md) las instrucciones para descargar los contenidos correspondientes a tu curso y bimestre.

## 📚 Contenido del Curso 

<table>
    <tr>
        <td>Clase</td>
        <td>Tema</td>
        <td>Notebooks</td>
    </tr>
    <tr>
        <td>1️⃣</td>
        <td>Introducción al Análisis de Datos</td>
        <td><a href=notebooks/clase_01_introduccion.ipynb>notebook_clase_1</a></td>
    </tr>
    <tr>
        <td>2️⃣</td>
        <td>Análisis exploratorio de datos (EDA)</td>
        <!---
        <td><a href=notebooks/clase_02_visualizacion.ipynb>notebook_clase_2</a></td>
        --->
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>2️⃣</td>
        <td>Análisis exploratorio de datos (EDA)</td>
    <!---
        <td rowspan="5">3️⃣</td>
        <td rowspan="5">EDA (cont.) y preprocesamiento</td> 
        <td><a href=notebooks/clase_03_1_outliers.ipynb>notebook_clase_3_outliers</a></td>
    </tr>
    <tr>
        <td><a href=notebooks/clase_03_2_codificacion.ipynb>notebook_clase_3_codificación</a></td>
    </tr>
    <tr>
        <td><a href=notebooks/clase_03_3_discretizacion.ipynb>notebook_clase_3_discretización</a></td>
    </tr>
    <tr>
        <td><a href=notebooks/clase_03_4_desbalance.ipynb>notebook_clase_3_desbalance</a></td>
    </tr>
    <tr>
        <td><a href=notebooks/clase_03_5_normalizacion_estandarizacion.ipynb>notebook_clase_3_desbalance</a></td>
    --->
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>4️⃣</td>
        <td>Preprocesamiento (cont.) y Feature Engineering</td>
         <!---
        <td><a href=notebooks/clase_04_outliers_discretizacion_escalamiento.ipynb>notebook_clase_4</a></td>
         --->
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>5️⃣</td>
        <td>Taller práctico - parte 1</td>
        <!---
        <td><a href=notebooks/clase_05_reduccion_de_dimensionalidad.ipynb>notebook_clase_5</a></td>
         --->
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>6️⃣</td>
        <td>Pruebas estadísticas y reducción de la dimensionalidad</td>
        <!---
        <td><a href=notebooks/clase_06_taller.ipynb>notebook_clase_6</a></td>
         --->
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>7️⃣</td>
        <td>Taller práctico - parte 2</td>
        <td>A ser agregada</td>
    </tr>
    <tr>
        <td>8️⃣</td>
        <td>Automatización del análisis de datos</td>
        <!---
        <td><a href=notebooks/clase_08_reduccion_dimensionalidad.ipynb>notebook_clase_8</a></td>
        --->
        <td>A ser agregada</td>
    </tr>
</table>


## 📅 Fechas importantes

<!---
* Entrega del trabajo práctico final: **Martes 15 de abril de 2025 (hasta las 23:59 hora de Argentina)**.

* Presentación del trabajo práctico final: **Jueves 17 de abril de 2025**.

--->
* Entrega del TP parte 1: **Lunes 2 de junio de 2025 (hasta las 23:59 hora de Argentina)**.

* Entrega del TP parte 2: **Lunes 16 de junio de 2025 (hasta las 23:59 hora de Argentina)**.

* Última clase: **Jueves 19 de junio de 2025**.



## ⚙️ Instalación y Configuración del Entorno

En esta sección se explican los pasos para utilizar este repositorio.

### **🔹 Opción 1: Usar un env de Conda**

#### Prerrequisitos 
* Anaconda o miniconda
* Git

#### 1. Clonar el repositorio:

```bash
git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos.git
cd CEIA_Analisis_de_datos
```

#### 2. Crear y activar el environment:

```bash
conda env create -f environment.yml
conda activate add-env
```

#### 3. Abrir Jupyter:

```bash
jupyter notebook
```

### **🔹 Opción 2: Usar un env de Poetry**

Este proyecto también permite usar Poetry para manejo de dependencias. Seguir los pasos detallados a continuación para crear un environment a partir de los archivos `pyproject.toml` y `poetry.lock` proporcionados.

#### Prerrequisitos 
 * Poetry : [Instrucciones de instalación](https://python-poetry.org/docs/#installing-with-the-official-installer)
 * Python 3.11 o 3.12
 * Git

#### 1. Clonar el repo:

```bash
git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos.git
cd CEIA_Analisis_de_datos
```

#### 2. Crear el environment (ejemplo con Python 3.11, ajustar a 3.12 de ser necesario):

* macOS/Linux

```bash
poetry env use python3.11  
```
* Windows

```bash
poetry env use "py -3.11" 
```

#### 3. Instalar dependencias (Linux/MacOS/Windows):
```bash
poetry install --no-root 
```
Nota: --no-root evita la instalación como package que no es necesaria aquí.

#### 4. Verificar que el environment se instaló correctamente:

```bash
poetry env list
```
> Este comando devuelve todos los environments asociados al proyecto (verificar que `ceia-analisis-de-datos-xxxxxxx-py3.11` aparece en la lista)

```bash
poetry env info
```
> Este comando muestra detalles tales como la versión de Python y el path (ej., `/Users/<username>/Library/Caches/pypoetry/virtualenvs/...` en macOS o `C:\Users\<username>\AppData\Local\pypoetry\...` en Windows).


#### 5. Activar el environment:

* macOS/Linux (zsh/bash):

```bash
eval "$(poetry env activate)" 
```

* Windows (PowerShell/CMD):

```bash
Invoke-Expression (poetry env activate)
```

> Después de ejecutar el comando, el nombre del environment debería aparecer en el prompt de la terminal entre paréntesis (ej., `ceia-analisis-de-datos-py3.11`).

#### 6. Verificar activación:

```bash
python --version
```
> Debería mostrar Python 3.11.X o 3.12.X.


```bash
which python  # macOS/Linux
where python  # Windows
```
> Debería apuntar al Pyhton del env. de Poetry (ej., /Users/<username>/.../bin/python o C:\Users\<username>\...\Scripts\python.exe).


#### 7. Registrar el environment en Jupyter:

```bash
poetry run python -m ipykernel install --user --name=ceia-analisis-de-datos --display-name "Python (CEIA)"
```


#### 8. Abrir Jupyter y seleccionar el kernel correcto:

```bash
jupyter notebook
```
Una vez abierto Jupyter, ir a **Kernel** → **Change Kernel** y seleccionar **"Python (CEIA)"**.




### **🔹 Opción 3: Usar Google Colab**

Al momento de la actualización de este repositorio (Marzo 2025) Colab utiliza Python 3.11 y no debería haber inconvenientes para ejecutar las notebooks de la materia con esta herramienta. Pasos a seguir:

1. Desde Colab, ir al menú **File** y hacer click en **Open** **Notebook**.

2. En la nueva ventana que se abre, ir a la opción **GitHub** (en el menú de la derecha).

3. En la barra buscadora, copiar el nombre del repo: 

```bash
FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos
```

4. Asegurarse que en **Repository** aparezca el nombre correcto (`FIUBA-Posgrado-Inteligencia-Artificial/CEIA_Analisis_de_datos`) y la branch sea **main**. Hacer click en la notebook deseada para abrir.



## 📫 Contacto

* [✉️](macroldan@fi.uba.edu.ar) María Carina Roldán 
* [✉️](arigarmendia@gmail.com) Ariadna Garmendia
