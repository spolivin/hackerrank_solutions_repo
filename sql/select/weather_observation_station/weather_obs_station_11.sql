SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('a', 'i', 'e', 'o', 'u')
      OR RIGHT(CITY, 1) NOT IN ('a', 'i', 'e', 'o', 'u');
