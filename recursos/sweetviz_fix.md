### Pasos para arreglar el bug de Sweetviz (Actualizado al 25/04/2025)

Contexto: la biblioteca Sweetviz tiene un bug que afecta la generación de reportes. Esto se debe a dependencias con la biblioteca Numpy, que realizô ciertos cambios a partir de la versión 2. 0.0. En particular, la advertencia `VisibleDeprecationWarning` ha cambiado su forma de importarse y ahora se encuentra dentro del módulo `numpy.exceptions`.
Como resultado, cuando se utiliza la función 'analyze' se produce el error "AttributeError: module 'numpy' has no attribute 'VisibleDeprecationWarning'"



Para solucionar este problema, se recomienda seguir uno de los siguientes pasos:


Localizar el archivo graph_numeric.py (está localizado dentro de la carpeta de instalación de Sweetviz) y realizar los siguientes cambios:

1. Importar la siguiente librería al inicio del archivo:

```python
from numpy.exceptions import VisibleDeprecationWarning
```

2. En las líneas 71 y 74, cambiar 

```python
category = VisibleDeprecationWarning 
```
por:
```python
category=np.exceptions.VisibleDeprecationWarning
```

3. Reiniciar el kernel de Jupyter y ejecutar.

Nota: el archivo graph_numeric.py se encuentra en las siguiente rutas:


1) ...miniconda3/envs/add-env/lib/sweetviz/graph_numeric.py
2) ...pypoetry/virtualenvs/ceia-analisis-de-datos-xxxxxx-<version>/lib/python3.11/site-packages/sweetviz/graph_numeric.py
