select COUNT(*) as COUNT from ECOLI_DATA 
where (GENOTYPE & b'1' or GENOTYPE & b'100') and not GENOTYPE & b'10';