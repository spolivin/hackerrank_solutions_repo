SELECT SUM(CITY.Population)
FROM CITY
LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE Continent = 'Asia';
