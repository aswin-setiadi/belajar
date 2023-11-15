SELECT c.FirstName , c.LastName 
FROM Customer c 
WHERE 
ORDER BY c.FirstName DESC , c.LastName DESC ; -- default is ASC so if 2 col, for desc must declare for both
--comment
/*comments*/

SELECT i.CustomerId , COUNT(i.InvoiceId) FROM Invoice i GROUP BY i.CustomerId ;

SELECT DISTINCT i.CustomerId FROM Invoice i ;

SELECT COUNT( DISTINCT i.CustomerId) total_customer FROM Invoice i ;

--https://www.instagram.com/p/CzpWjsCBpnQ
--find total profit
SELECT SUM(Profit) as total_profit FROM Transaksi;
--find total profit for each year-month
SELECT STRFTIME('%Y-%m',i.InvoiceDate) as tahun_bulan, SUM(i.Total)  FROM Invoice i GROUP BY tahun_bulan ORDER BY tahun_bulan; 
--find top 3 customers based on profit sum
SELECT i.CustomerId, SUM(i.Total) profit FROM Invoice i GROUP BY i.CustomerId ORDER BY profit DESC LIMIT 3;

------------------------------------------
SELECT DISTINCT il.Quantity FROM InvoiceLine il ;


--https://www.instagram.com/p/CzaBrJRvRPf
SELECT COUNT(t.TrackId) total_track  from Track t;

-- find tracks that no one purchase
SELECT t.TrackId , il.InvoiceId  FROM Track t  left join InvoiceLine il on il.TrackId = t.TrackId WHERE il.InvoiceId is NULL ORDER BY t.TrackId ;

-------------------------------------------

--https://www.instagram.com/p/Cy5tFRWv-T9
--find al transaction for customerId 2
SELECT i.InvoiceDate , i.CustomerId cid FROM Invoice i WHERE cid = 2;
--find rows where year 2007 and customerId 2
SELECT STRFTIME('%Y',i.InvoiceDate) iYear , i.CustomerId FROM Invoice i WHERE iYear = '2007' AND i.CustomerId =2;
--find rows where year is 2007 group by customerId
SELECT i.CustomerId , COUNT(i.InvoiceId) FROM Invoice i WHERE STRFTIME('%Y',i.InvoiceDate) = '2007' GROUP BY i.CustomerId; 

-------------------------------------------
--https://www.sqlitetutorial.net/sqlite-full-outer-join/
--sqlite no full outer join and right outer join, so emulate
-- create and insert data into the dogs table
CREATE TABLE dogs (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    type       TEXT,
    color TEXT
);

INSERT INTO dogs(type, color) 
VALUES('Hunting','Black'), ('Guard','Brown');

-- create and insert data into the cats table
CREATE TABLE cats (
    type       TEXT,
    color TEXT
);

INSERT INTO cats(type,color) 
VALUES('Indoor','White'), 
      ('Outdoor','Black');
      
-- to emulate full outer join, use UNION ALL and remove the duplicate with WHERE
-- right join, just left join but reverse the table order
SELECT d."Type" ,d.Color ,c."Type" ,c.Color  
FROM Dogs d 
LEFT JOIN Cats c USING(color) --column name seemed to be capital agnostic
UNION ALL 
SELECT d2."Type" ,d2.Color ,c2."Type" ,c2.Color 
FROM Cats c2 
LEFT JOIN Dogs d2 USING(Color) 
WHERE d2.Color IS NULL ;
--------------------------------------------