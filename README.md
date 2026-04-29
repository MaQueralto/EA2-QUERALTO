# 🏀 NBA Stats CLI

Proyecto desarrollado para la **Evaluación 2 — DRY7122** (DuocUC).

Programa en Python que se conecta a la API pública de [balldontlie.io](https://www.balldontlie.io/) para consultar estadísticas de jugadores NBA, empaquetado con Docker y desplegado automáticamente con Jenkins.

---

## 📌 ¿Qué hace el programa?

- Busca un jugador NBA por nombre usando la API REST de balldontlie
- Extrae y muestra: nombre, equipo, posición, altura, peso, puntos, rebotes y asistencias
- Maneja 4 tipos de errores: `404`, `ConnectionError`, `Timeout` y código HTTP inesperado

---

## 🛠️ Tecnologías usadas

| Herramienta | Uso |
|---|---|
| Python 3.11 | Lenguaje principal |
| requests | Llamadas HTTP a la API |
| Docker | Empaquetado del programa |
| Jenkins | Despliegue automático |
| GitHub | Control de versiones |

---

## ▶️ Cómo ejecutar el programa

### Opción 1 — Con Python directo

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar
python main.py
```

### Opción 2 — Con Docker (recomendado)

```bash
# 1. Construir la imagen
docker build -t nba-stats .

# 2. Correr el contenedor (modo interactivo para ingresar nombre)
docker run -it nba-stats
```

---

## 🔑 API Key

Esta API requiere una key gratuita de [balldontlie.io](https://www.balldontlie.io/).

Para usarla de forma segura, crea un archivo `.env` (ya está en `.gitignore`) o pásala como variable de entorno:

```bash
export BALLDONTLIE_API_KEY="tu_key_aqui"
```

---

## 📁 Estructura del proyecto

```
EA2-Queralto/
├── main.py           # Script principal
├── Dockerfile        # Configuración Docker
├── requirements.txt  # Dependencias Python
├── .gitignore        # Archivos ignorados por git
└── README.md         # Este archivo
```

---

## 👨‍💻 Autor

Desarrollado por [Matias Queralto] — DuocUC.
