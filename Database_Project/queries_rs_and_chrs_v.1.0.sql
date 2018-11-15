-----------------------------------------------------------------------------------------------------------

-- Nombre: queries_rs_and_chrs_v.1.0.sql
-- Autora: Diana Salazar
-- Version 1.0
-- Creado: 13/11/10
-- Descripción: Código que permite hacer las consultas a la base de datos solicitadas por  
--    la cliente. Regresa las búsquedas de RS (tres opciones) y búsquedas por cromosoma 
--    a pantalla (1 opción).
-- Lenguaje: MySQL

------------------------------------------- Búsquedas para RS ---------------------------------------------

-- Opción 1:
-- Mostrar el rs, cromosoma posición de inicio y fin, cadena, alelo de referencia, 
-- alelo alternativo, tipo de variación, fuente de la que proviene y su link a NCBI

SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position, rs.strand, 
rs.reference_allele, alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI 
FROM RS rs LEFT JOIN ALTERNATIVE_ALLELE alt 
ON (rs.rs_id = alt.rs_id)
WHERE rs.rs_id LIKE 'rs%'; -- valor ejemplo

-- Opción 2:
-- Las frecuencias relacionadas a un RS

SELECT rs.rs_id, rs.reference_allele, alt.alternative_allele, 
f.AFR, f.AMR, f.EAS, f.EUR, f.SAS, f.GLOBALFREQS, rs.link_NCBI
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f) 
ON (rs.rs_id = alt.rs_id AND alt.id_alternative_allele = f.id_alternative_allele)
where rs.rs_id like 'rs%'; -- valor ejemplo

-- Opción 3:
-- Unión de las dos anteriores

SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position, 
rs.strand, rs.reference_allele,  alt.alternative_allele, rs.variation, 
rs.source, rs.link_NCBI, f.AFR, f.AMR, f.EAS, f.EUR, f.SAS, f.GLOBALFREQS
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f)
ON (rs.rs_id = alt.rs_id 
AND alt.id_alternative_allele = f.id_alternative_allele)
where rs.rs_id like 'rs%'; -- valor ejemplo

--------------------------------------- Búsquedas para cromosomas -----------------------------------------
-- Opción 1:
-- Lista de rs's en un intervalo de posiciones definido

SELECT rs.rs_id, rs.link_NCBI
FROM RS rs, ALTERNATIVE_ALLELE alt
WHERE rs.chromosome like 'chr1%' -- valor ejemplo
AND rs.rs_id = alt.rs_id
AND rs.start_position BETWEEN 10 and 100 -- valores ejemplo
AND alt.end_position BETWEEN 10 and 100; -- valores ejemplo

