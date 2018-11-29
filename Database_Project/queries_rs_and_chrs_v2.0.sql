-------------------------------------------------------------------v2------------------------------------------------------------------
----- Version 1.5 - No funcionales

----- Opción 1: rs
SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position,  rs.strand,
rs.reference_allele,  alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI,
coalesce(f.AFR, 'NA'), coalesce(f.AMR, 'NA'), coalesce(f.EAS, 'NA'), coalesce(f.EUR, 'NA'), coalesce(f.SAS, 'NA'), coalesce(f.GLOBALFREQS, 'NA') 
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f)
ON (rs.rs_id = alt.rs_id 
AND alt.id_alternative_allele = f.id_alternative_allele)
where rs.rs_id like '{}%';

----- Opción 2: Cromosomas
SELECT DISTINCT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position,  rs.strand,
rs.reference_allele,  alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI,
coalesce(f.AFR, 'NA'), coalesce(f.AMR, 'NA'), coalesce(f.EAS, 'NA'), coalesce(f.EUR, 'NA'), coalesce(f.SAS, 'NA'), coalesce(f.GLOBALFREQS, 'NA') 
FROM RS rs LEFT JOIN (ALTERNATIVE_ALLELE alt, FREQUENCY_RS_CONTINENT f)
ON (rs.rs_id = alt.rs_id
AND rs.start_position BETWEEN '{}' and '{}'
AND alt.end_position BETWEEN '{}' and '{}')
WHERE rs.chromosome like '{}%';

-----------------------------------------------------Pruebas de este pedo-------------------------------------------
----- Version 2.0

----- Opción 1: rs con sus alternativos
SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position,  rs.strand,
rs.reference_allele,  alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI,
coalesce(f.AFR, 'NA'), coalesce(f.AMR, 'NA'), coalesce(f.EAS, 'NA'), coalesce(f.EUR, 'NA'), coalesce(f.SAS, 'NA'), coalesce(f.GLOBAL, 'NA') 
FROM RS rs LEFT JOIN ALTERNATIVE_ALLELE alt on rs.rs_id = alt.rs_id
LEFT JOIN FREQUENCY_RS_CONTINENT f on alt.id_alternative_allele = f.id_alternative_allele
WHERE rs.rs_id like '{}%'; 

----- Opción 2: cromosomas y rangos cromosomicos
SELECT rs.rs_id, rs.chromosome, rs.start_position, alt.end_position,  rs.strand,
rs.reference_allele,  alt.alternative_allele, rs.variation, rs.source, rs.link_NCBI,
coalesce(f.AFR, 'NA'), coalesce(f.AMR, 'NA'), coalesce(f.EAS, 'NA'), coalesce(f.EUR, 'NA'), coalesce(f.SAS, 'NA'), coalesce(f.GLOBAL, 'NA') 
FROM RS rs LEFT JOIN ALTERNATIVE_ALLELE alt on rs.rs_id = alt.rs_id
LEFT JOIN FREQUENCY_RS_CONTINENT f on alt.id_alternative_allele = f.id_alternative_allele
WHERE rs.chromosome like '{}%'
AND rs.start_position BETWEEN '{}' and '{}'
AND alt.end_position BETWEEN '{}' and '{}';
