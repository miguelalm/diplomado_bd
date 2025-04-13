
DROP TABLE IF EXISTS diagnostico_examen, orden_examen, diagnostico, estancia_paciente, paciente, medico, examen, enfermedad, cama, habitacion CASCADE;

CREATE TABLE habitacion (
    id SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL
);

CREATE TABLE cama (
    id SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL,
    habitacion_id INTEGER REFERENCES habitacion(id)
);

CREATE TABLE paciente (
    id SERIAL PRIMARY KEY,
    rut VARCHAR(12) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE medico (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE examen (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE enfermedad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE estancia_paciente (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES paciente(id),
    medico_id INTEGER REFERENCES medico(id),
    cama_id INTEGER REFERENCES cama(id),
    fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_egreso TIMESTAMP
);

CREATE TABLE diagnostico (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES paciente(id) not NULL,
    medico_id INTEGER REFERENCES medico(id) not NULL,
    enfermedad_id INTEGER REFERENCES enfermedad(id) not NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP not NULL,
    PRIMARY KEY (paciente_id, medico_id, enfermedad_id)
);

CREATE TABLE orden_examen (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES paciente(id),
    medico_id INTEGER REFERENCES medico(id),
    examen_id INTEGER REFERENCES examen(id),
    posible_diagnostico TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE diagnostico_examen (
    diagnostico_id INTEGER REFERENCES diagnostico(id),
    examen_id INTEGER REFERENCES examen(id),
    PRIMARY KEY (diagnostico_id, examen_id)
);