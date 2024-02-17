SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('a', 'i', 'e', 'o', 'u')
      AND RIGHT(CITY, 1) NOT IN ('a', 'i', 'e', 'o', 'u');
