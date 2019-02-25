USE etlproject;


CREATE TABLE unemployment2
    SELECT 
        e.state, e.rate, s.abbreviation 
    FROM
        unemployment e
            JOIN
        states s ON e.state = s.state
	ORDER BY s.state;
    
    
    
CREATE TABLE population2
    SELECT 
        p.population, p.state, s.abbreviation 
    FROM
        population p
            JOIN
        states s ON p.state = s.state
	ORDER BY p.state;
    
    

CREATE TABLE jobcount SELECT COUNT(j.job_title) AS job_count, j.state FROM
    jobs j
GROUP BY j.state;


#Create final table with aggregated values
CREATE TABLE final
SELECT 
     j.state, p.population, j.job_count, u.rate AS unemp_rate
FROM
    jobcount j
        INNER JOIN
    population2 p ON p.abbreviation = j.state
        INNER JOIN
    unemployment2 u ON u.abbreviation = j.state;
    
Select * from final;






		
		
    


    