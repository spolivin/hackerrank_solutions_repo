SELECT CITY.Name
FROM CITY
LEFT JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE Continent = 'Africa';
