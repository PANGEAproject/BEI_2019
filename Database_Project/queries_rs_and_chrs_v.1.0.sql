--------------- Para RS

---- Opción 1: mostrar el rs, el cromosoma, la posición de inicio y fin, la cadena a la que pertenece,
---- alelo de referencia, variación, fuente de la que proviene y su link a NCBI

SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position, rs.strand, 
rs.reference_allele, alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI 
FROM RS rs LEFT JOIN ALTERNATIVE_ALLELE alt 
ON (rs.rs_id = alt.rs_id)
WHERE rs.rs_id LIKE 'rs%';

---- Opción 2: Las frecuencias relacionadas a un RS

SELECT rs.rs_id, rs.reference_allele, alt.alternative_allele, 
f.AFR, f.AMR, f.EAS, f.EUR, f.SAS, f.GLOBALFREQS, rs.link_NCBI
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f) 
ON (rs.rs_id = alt.rs_id 
AND alt.id_alternative_allele = f.id_alternative_allele)
where rs.rs_id like 'rs%';

-- Opción 3: Unión de las dos anteriores

SELECT rs.rs_id 'RS', rs.chromosome 'CHR', rs.start_position 'INI', alt.end_position 'FIN', 
rs.strand '+/-', rs.reference_allele 'REF',  alt.alternative_allele 'ALT', rs.variation 'VAR', 
rs.source 'FUENTE', rs.link_NCBI 'LINK', f.AFR, f.AMR, f.EAS, f.EUR, f.SAS, f.GLOBALFREQS 'ALL' 
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f)
ON (rs.rs_id = alt.rs_id 
AND alt.id_alternative_allele = f.id_alternative_allele)
where rs.rs_id like 'rs%';


--------------- Para cromosomas
-- Opción 1:Lista de rs en esa posición o posiciones

SELECT rs.rs_id, rs.link_NCBI
FROM RS rs, ALTERNATIVE_ALLELE alt
WHERE rs.chromosome like 'chr1%'
AND rs.rs_id = alt.rs_id
AND rs.start_position BETWEEN 10 and 100
AND alt.end_position BETWEEN 10 and 100;

