import requests  # Para hacer solicitudes HTTP a la API
import json       # Para manejar datos JSON
import os         # Para leer variables de entorno
from dotenv import load_dotenv 

load_dotenv()

# ============================================================
# ZONA: CONFIGURACIÓN
# ============================================================
BASE_URL = "https://api.balldontlie.io/v1"
API_KEY = os.getenv("BALLDONTLIE_API_KEY", "")  # La key se lee desde variable de entorno


HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

# ============================================================
# ZONA: LLAMADA HTTP — Buscar jugador por nombre
# ============================================================
def buscar_jugador(nombre):
    """Busca un jugador NBA por nombre y retorna su información."""
    print(f"\n🔍 Buscando jugador: {nombre}")

    try:
        # Realizamos la solicitud GET a la API
        respuesta = requests.get(
            f"{BASE_URL}/players",
            headers=HEADERS,
            params={"search": nombre},
            timeout=10  # Timeout de 10 segundos
        )

        # ============================================================
        # ZONA: MANEJO DE ERRORES HTTP
        # ============================================================

        # Error 404 — Recurso no encontrado
        if respuesta.status_code == 404:
            print("❌ Error 404: El recurso solicitado no existe en la API.")
            return None

        # Código inesperado — cualquier otro error HTTP
        if respuesta.status_code != 200:
            print(f"⚠️  Error inesperado: Código HTTP {respuesta.status_code}")
            return None

        # ============================================================
        # ZONA: PARSEO JSON
        # ============================================================
        datos = respuesta.json()
        jugadores = datos.get("data", [])

        if not jugadores:
            print("⚠️  No se encontró ningún jugador con ese nombre.")
            return None

        # Retornamos el primer resultado
        return jugadores[0]

    # Error de conexión — sin internet o servidor caído
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión: No se pudo conectar a la API. Verifica tu internet.")
        return None

    # Error de timeout — la API tardó demasiado en responder
    except requests.exceptions.Timeout:
        print("❌ Error de Timeout: La API tardó demasiado en responder.")
        return None


# ============================================================
# ZONA: LLAMADA HTTP — Obtener estadísticas del jugador
# ============================================================
def obtener_estadisticas(jugador_id, temporada=2024):
    """Obtiene las estadísticas promedio de un jugador en una temporada."""

    try:
        respuesta = requests.get(
            f"{BASE_URL}/season_averages",
            headers=HEADERS,
            params={"player_ids[]": jugador_id, "season": temporada},
            timeout=10
        )

        if respuesta.status_code == 404:
            print("❌ Error 404: No se encontraron estadísticas para este jugador.")
            return None

        if respuesta.status_code != 200:
            print(f"⚠️  Error inesperado: Código HTTP {respuesta.status_code}")
            return None

        # ============================================================
        # ZONA: PARSEO JSON
        # ============================================================
        datos = respuesta.json()
        estadisticas = datos.get("data", [])

        if not estadisticas:
            print(f"⚠️  Sin estadísticas para la temporada {temporada}.")
            return None

        return estadisticas[0]

    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión: No se pudo conectar a la API.")
        return None

    except requests.exceptions.Timeout:
        print("❌ Error de Timeout: La API no respondió a tiempo.")
        return None


# ============================================================
# ZONA: PRESENTACIÓN DE DATOS
# ============================================================
def mostrar_info_jugador(jugador, stats):
    """Muestra la información del jugador de forma clara en consola."""
    print("\n" + "="*50)
    print("🏀  NBA STATS — balldontlie API")
    print("="*50)

    # Campo 1: Nombre completo
    nombre = f"{jugador.get('first_name', 'N/A')} {jugador.get('last_name', 'N/A')}"
    print(f"👤  Jugador     : {nombre}")

    # Campo 2: Equipo
    equipo = jugador.get("team", {})
    print(f"🏟️   Equipo      : {equipo.get('full_name', 'Sin equipo')}")

    # Campo 3: Posición
    print(f"📌  Posición    : {jugador.get('position', 'N/A')}")

    # Campo 4: Altura y peso
    print(f"📏  Altura      : {jugador.get('height', 'N/A')}")
    print(f"⚖️   Peso        : {jugador.get('weight', 'N/A')} lbs")

    if stats:
        print("\n📊  ESTADÍSTICAS TEMPORADA 2024:")
        print(f"    🎯 Puntos por partido   : {stats.get('pts', 'N/A')}")
        print(f"    🔄 Rebotes por partido  : {stats.get('reb', 'N/A')}")
        print(f"    🤝 Asistencias partido  : {stats.get('ast', 'N/A')}")
        print(f"    🔒 Robos por partido    : {stats.get('stl', 'N/A')}")
        print(f"    🚫 Tapones por partido  : {stats.get('blk', 'N/A')}")
        print(f"    🎯 % Tiro de campo      : {stats.get('fg_pct', 'N/A')}")

    print("="*50)


# ============================================================
# ZONA: SOLICITUD — Punto de entrada principal
# ============================================================
if __name__ == "__main__":
    print("🏀 Bienvenido al buscador de estadísticas NBA")
    print("   Powered by balldontlie.io API\n")

    # Pedimos el nombre del jugador al usuario
    nombre_buscado = input("Ingresa el nombre del jugador: ").strip()

    if not nombre_buscado:
        print("⚠️  Debes ingresar un nombre.")
    else:
        # Paso 1: Buscar el jugador
        jugador = buscar_jugador(nombre_buscado)

        if jugador:
            jugador_id = jugador.get("id")

            # Paso 2: Obtener sus estadísticas
            stats = obtener_estadisticas(jugador_id)

            # Paso 3: Mostrar todo
            mostrar_info_jugador(jugador, stats)
