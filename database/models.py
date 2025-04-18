
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="dell040502",
        host="localhost",
        port="15432",
        options="-c search_path=dbo,diplomado"
    )

def traer_pacientes():
    query = """
    SELECT 
        p.rut, p.nombre, en.nombre AS enfermedad, m.nombre AS medico, h.numero AS habitacion, c.numero as cama
    FROM paciente p
    JOIN estancia_paciente ep ON p.id = ep.paciente_id
    JOIN medico m ON ep.medico_id = m.id
    JOIN cama c ON ep.cama_id = c.id
    JOIN habitacion h ON c.habitacion_id = h.id
    LEFT JOIN diagnostico d ON p.id = d.paciente_id
    LEFT JOIN enfermedad en ON d.enfermedad_id = en.id
    WHERE ep.fecha_egreso IS NULL;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

def traer_detalle_paciente_por_rut(rut):
    query = """
    SELECT 
        p.rut, p.nombre,
        en.nombre AS diagnostico,
        m.nombre AS medico,
        e.nombre AS ultimo_examen,
        h.numero AS habitacion,
        c.numero AS cama
    FROM paciente p
    LEFT JOIN estancia_paciente ep ON p.id = ep.paciente_id
    LEFT JOIN medico m ON ep.medico_id = m.id
    LEFT JOIN cama c ON ep.cama_id = c.id
    LEFT JOIN habitacion h ON c.habitacion_id = h.id
    LEFT JOIN diagnostico d ON d.paciente_id = p.id
    LEFT JOIN enfermedad en ON d.enfermedad_id = en.id
    LEFT JOIN orden_examen oe ON oe.paciente_id = p.id
    LEFT JOIN examen e ON oe.examen_id = e.id
    WHERE p.rut = %s
    ORDER BY oe.fecha DESC
    LIMIT 1;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (rut,))
            return cur.fetchone()

def cambiar_cama_paciente(rut, nueva_cama_id):
    query = """
    UPDATE estancia_paciente
    SET cama_id = %s
    WHERE paciente_id = (SELECT id FROM paciente WHERE rut = %s)
    AND fecha_egreso IS NULL;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (nueva_cama_id, rut))
            conn.commit()

def cambiar_medico_paciente(rut, nuevo_medico_id):
    query = """
    UPDATE estancia_paciente
    SET medico_id = %s
    WHERE paciente_id = (SELECT id FROM paciente WHERE rut = %s)
    AND fecha_egreso IS NULL;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (nuevo_medico_id, rut))
            conn.commit()

def crear_habitacion(numero):
    query = "INSERT INTO habitacion (numero) VALUES (%s);"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (numero,))
            conn.commit()

def crear_cama(numero, habitacion_id):
    query = "INSERT INTO cama (numero, habitacion_id) VALUES (%s, %s);"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (numero, habitacion_id))
            conn.commit()

def obtener_numero_camas(habitacion_id):
    query = "SELECT max(numero) FROM cama WHERE habitacion_id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (habitacion_id, ))
            return cur.fetchone()[0]