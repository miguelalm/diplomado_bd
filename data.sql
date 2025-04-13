-- Habitaciones
INSERT INTO habitacion (numero) VALUES ('101'), ('102'), ('103'), ('104'), ('105'), ('106'), ('107'), ('108'), ('109'), ('110');

-- Camas
INSERT INTO cama (numero, habitacion_id) VALUES
('1', 1), ('2', 1), ('1', 2), ('2', 2), ('1', 3), 
('2', 3), ('1', 4), ('2', 4), ('1', 5), ('2', 5);

-- Médicos
INSERT INTO medico (nombre) VALUES
('Dr. House'), ('Dra. Grey'), ('Dr. Strange'), ('Dr. Who'), ('Dr. Wily'),
('Dr. Light'), ('Dra. Quinn'), ('Dr. Octopus'), ('Dr. Watson'), ('Dr. Richards');

-- Pacientes
INSERT INTO paciente (rut, nombre) VALUES
('12345678-9', 'Juan Pérez'), ('98765432-1', 'María Gómez'), ('11111111-1', 'Luis Torres'),
('22222222-2', 'Ana Díaz'), ('33333333-3', 'Carlos Rojas'), ('44444444-4', 'Sofía Herrera'),
('55555555-5', 'Martín Pino'), ('66666666-6', 'Laura Vega'), ('77777777-7', 'Pedro Castillo'),
('88888888-8', 'Daniela Silva');

-- EstanciaPaciente
INSERT INTO estancia_paciente (paciente_id, medico_id, cama_id, fecha_ingreso, fecha_egreso) VALUES
(1, 1, 1, '2024-04-01', NULL), (2, 2, 2, '2024-04-02', NULL), (3, 3, 3, '2024-04-03', NULL),
(4, 4, 4, '2024-04-04', NULL), (5, 5, 5, '2024-04-05', NULL), (6, 6, 6, '2024-04-06', NULL),
(7, 7, 7, '2024-04-07', NULL), (8, 8, 8, '2024-04-08', NULL), (9, 9, 9, '2024-04-09', NULL),
(10, 10, 10, '2024-04-10', NULL);

-- Exámenes
INSERT INTO examen (nombre) VALUES
('Hemograma'), ('Orina completa'), ('Radiografía'), ('Tomografía'), ('PCR'),
('Colesterol'), ('Triglicéridos'), ('Glucosa'), ('Creatinina'), ('Examen de sangre');

-- Enfermedades
INSERT INTO enfermedad (nombre) VALUES
('Gripe'), ('COVID-19'), ('Diabetes'), ('Hipertensión'), ('Anemia'),
('Cáncer de pulmón'), ('Insuficiencia renal'), ('Colesterol alto'), ('Hepatitis'), ('Tuberculosis');

-- OrdenExamen
INSERT INTO orden_examen (paciente_id, medico_id, examen_id, fecha, posible_diagnostico) VALUES
(1,1,1,'2024-04-01','Anemia'), (2,2,2,'2024-04-02','Infección urinaria'),
(3,3,3,'2024-04-03','Fractura costal'), (4,4,4,'2024-04-04','Tumor cerebral'),
(5,5,5,'2024-04-05','COVID-19'), (6,6,6,'2024-04-06','Dislipidemia'),
(7,7,7,'2024-04-07','Hiperglicemia'), (8,8,8,'2024-04-08','Insuficiencia renal'),
(9,9,9,'2024-04-09','Colesterol alto'), (10,10,10,'2024-04-10','Infección viral');

-- Diagnóstico
INSERT INTO diagnostico (paciente_id, medico_id, enfermedad_id, fecha) VALUES
(1,1,5,'2024-04-01'), (2,2,10,'2024-04-02'), (3,3,4,'2024-04-03'),
(4,4,6,'2024-04-04'), (5,5,2,'2024-04-05'), (6,6,8,'2024-04-06'),
(7,7,3,'2024-04-07'), (8,8,7,'2024-04-08'), (9,9,9,'2024-04-09'), (10,10,1,'2024-04-10');

-- Diagnóstico_Examen
INSERT INTO diagnostico_examen (diagnostico_id, examen_id) VALUES
(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10);

