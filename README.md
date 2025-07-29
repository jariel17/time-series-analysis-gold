# 🪙 Análisis del Precio del Oro con Series de Tiempo

---

## 📌 Introducción
Este proyecto fue desarrollado como parte del curso de Modelos Predictivos y tiene como objetivo analizar el comportamiento histórico del precio del oro para construir modelos de predicción basados en técnicas de series de tiempo.  La motivación principal fue explorar el análisis de series de tiempo y probar diferentes modelos como ARIMA, Holt-Winters y Prophet. El precio del diario del oro, aunque en general se considera un activo estable, su precio en ciertos momentos puede 
resultar muy volátil, lo que representa un desafío interesante.

---

## 📂 Descripción de los datos
Los datos provienen de un dataset de Kaggle [Gold Prices Dataset](https://www.kaggle.com/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series)
Los precios del oro están en INR (rupias de la India) por 10 gramos de oro de 24K.
El dataset cubre desde el 01 de enero de 2014 al 6 de enero de 2025.

| Columna  | Descripción |
|----------|-------------|
| **Date** | Fecha del registro en formato `AAAA-MM-DD`. El día en que se registró el precio del oro. |
| **Price** | Precio de cierre del oro para la fecha indicada. Es el valor final del día, utilizado como referencia principal para el análisis. |
| **Open** | Precio de apertura del oro al inicio del día. Indica el primer valor negociado en esa jornada. |
| **High** | Precio más alto alcanzado durante el día. Representa el máximo valor de negociación. |
| **Low**  | Precio más bajo alcanzado durante el día. Representa el mínimo valor de negociación. |
| **Volume** | Volumen de operaciones registrado durante el día.|
| **Chg%** | Cambio porcentual en el precio del oro respecto al día anterior. Un valor positivo indica una subida, y uno negativo una baja. Por ejemplo, `0.95` significa un aumento del 0.95% frente al día previo. |

---

## 🔎 Hallazgos
- El precio del oro muestra una tendencia creciente a largo plazo.
- No parece tener una una estacionalidad clara.
- La serie no es estacionaria, es decir, sus propiedades de estadísticas de media y varianza no son constantes en el tiempo.

---

## 🎯 Conclusiones
- El modelo ARIMA no funciona porque la serie no es estacionaria.
- El modelo Holt-Winters captura la tendencia pero no refleja las variaciones en el precio.
- El modelo Prophet captura la tendencia y algunos cambios en el precio, sin embargo falla en los momentos en que el precio es muy volátil.
- Se recomienda a futuro integrar variables externas que estén relacionadas con el precio del oro.  

---
## ▶️ Instalación
Para correr el proyecto:
- Descarga el repositorio: `git clone https://github.com/jariel17/time-series-analysis-gold.git`
- Crea un ambiente virtual: `python -m venv env`
- Activa el ambiente virtual: `source env/bin/activate`
- Instala las librerías utilizadas: `pip install -r requirements.txt`
- Desde [Kaggle](https://www.kaggle.com/datasets/nisargchodavadiya/daily-gold-price-20152021-time-series) descarga el dataset.
- Muevel el archivo `Gold Price.csv` a la carpeta data.
- Corre el notebook `main_notebook.ipynb`
