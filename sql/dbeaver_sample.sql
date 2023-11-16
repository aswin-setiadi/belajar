SELECT c.FirstName , c.LastName 
FROM Customer c 
WHERE 
ORDER BY c.FirstName DESC , c.LastName DESC ; -- default is ASC so if 2 col, for desc must declare for both
--comment
/*comments*/

SELECT i.CustomerId , COUNT(i.InvoiceId) FROM Invoice i GROUP BY i.CustomerId ;

SELECT DISTINCT i.CustomerId FROM Invoice i ;

SELECT COUNT( DISTINCT i.CustomerId) total_customer FROM Invoice i ;
SELECT COUNT(i.CustomerId) total_customer FROM Invoice i ;

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

SELECT STRFTIME('%Y', i.InvoiceDate) as y, i.CustomerId , COUNT(i.CustomerId) from Invoice i GROUP BY y, i.CustomerId ; 
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

-- data lemur https://datalemur.com/questions/matching-skills easy
--Aswin
SELECT candidate_id 
FROM candidates
WHERE skill IN ('Python','Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(candidate_id) >2;
--lazy_leopard
SELECT candidate_id FROM candidates WHERE skill= 'Python'
INTERSECT 
SELECT candidate_id FROM candidates WHERE skill= 'Tableau'
INTERSECT 
SELECT candidate_id FROM candidates WHERE skill= 'PostgreSQL'
ORDER BY 1;
--john britto
SELECT candidate_id
FROM candidates
GROUP BY candidate_id
HAVING COUNT(CASE WHEN skill in ('Python', 'Tableau','PostgreSQL') THEN 1 ELSE NULL END)=3
ORDER BY candidate_id

--temidayo joshua omotinugbon, improve use in instead of multiple when
with c1 as (
select candidate_id, sum(case when skill in ('Python', 'Tableau','PostgreSQL') then 1 else 0 end) as skill_count
from candidaters
group by candidate_id
)
select candidate_id
from c1 where skill_count = 3
order by candidate_id;

SELECT t.TrackId , t.Name FROM Track t WHERE t.AlbumId = 4;
--find all album that has 8 tracks
SELECT a2.Name  , a.Title  
FROM Track t 
LEFT JOIN Album a 
ON t.AlbumId = a.AlbumId 
LEFT JOIN Artist a2 
ON a.ArtistId = a2.ArtistId
GROUP BY a2.Name ,a.Title 
HAVING COUNT(a.Title)=8;

--find all invoices that has total < average
select i.InvoiceId , i.Total 
from Invoice i
where i.Total < (select AVG(i2.Total) from Invoice i2)
order by i.InvoiceId ;

--find all customers with purchase less than avg invoice total
select c.FirstName , c.LastName 
from Customer c
where EXISTS (select i.InvoiceId from Invoice i where i.CustomerId=c.CustomerId AND i.Total< (SELECT AVG(i2.Total) from Invoice i2))

--find top 20 invoice value
select i3.total from Invoice i3 order by i3.total desc limit 20;

--find 2nd largest value
select max(i2.Total) from Invoice i2 where i2.Total != (select max(i.Total) from Invoice i ); --can use not in other than !=
--use distinct in case of employees salary cause can have same salary between multiple employee
select i.Total from Invoice i where 2= (SELECT count(DISTINCT i2.Total) from Invoice i2 where i.Total<=i2.Total);

SELECT i2.Total from (select i.Total from Invoice i order by i.Total desc LIMIT 2) i2 order by i2.Total asc;
--limit can have offset-> 2,1 means get 1 row after 2 row i.e. 3rd highest
select salary from employeeInfo order by salary desc limit 2,1; 
select salary from employeeInfo order by salary desc limit 1 offset 2; 
--leetcode https://leetcode.com/problems/game-play-analysis-iv/
--find fraction of players that logged in again on the day after first day login, round to 2 decimal
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN
(SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id)

SELECT DATE('now');

--find all artist that starts with A, then artist that has /
SELECT a.Name from Artist a WHERE a.Name LIKE 'A%';
SELECT a.Name from Artist a WHERE a.Name LIKE '%/%';
-- get substring that start at 2 ends at 5 (index start from 1)
SELECT SUBSTRING(a.Name,2,5) from Artist a; 

--find invoice that is billed at least twice to a customer (duplicate rows)
select i.CustomerId  , COUNT(i.CustomerId) from Invoice i group by i.CustomerId  HAVING COUNT(i.CustomerId)>1;
--find customer with invoice count less than invoice count average
select i.CustomerId  , COUNT(i.CustomerId) from Invoice i group by i.CustomerId
HAVING COUNT(i.CustomerId)<(SELECT AVG(i3.c) from (select i2.CustomerId , COUNT(*) c from Invoice i2 group by i2.CustomerId) i3 group by i3.CustomerId);

--find album with the most tracks
select a.Title , COUNT(*) track_count from Album a left join Track t ON a.AlbumId = t.AlbumId group by a.Title ORDER BY track_count DESC limit 5; 
--find customer with even id
SELECT c.CustomerId , c.FirstName , c.LastName from Customer c WHERE c.CustomerId%2 =0; 

-- get first and last customer id
SELECT c.CustomerId from Customer c WHERE c.CustomerId = (select min(c2.customerid) from Customer c2) union
SELECT c3.CustomerId from Customer c3 WHERE c3.CustomerId = (select max(c4.customerid) from Customer c4); 

-- copy dogs to dogs2
CREATE table Dogs2 as select * FROM Dogs d ;
-- use IN 'otherdb.md' after Dogs3 to migrate to other db
SELECT * INTO Dogs3 from Dogs;

-- copy schema of table
create table Dogs4 as select * from Dogs where 3=4;

-- find all customer in same city
select DISTINCT i.CustomerId ,i2.CustomerId ,i.BillingCity 
from Invoice i , Invoice i2 
WHERE i.BillingCity  = i2.BillingCity AND i.CustomerId  != i2.CustomerId  ;

SELECT c.CustID, c.CustName, C.CustMobile, c.CustEmail, a.AcctID, a.AcctStatus, m.Program, m.Start, m.End
from Customer as c 
left join Account as a ON c.CustID = a.CustID 
left join Membership as m on c.CustID = m.CustID 
order by c.CustName;

SELECT c.CustID, c.CustName, C.CustMobile, c.CustEmail, a.AcctID, a.AcctStatus, m.Program, m.Start, m.End
from Customer as c 
left join Account as a ON c.CustID = a.CustID 
left join Membership as m on c.CustID = m.CustID
where a.AcctStatus = 'Active' 
order by c.CustName;

select a.AcctID, STRFTIME('%Y', SA.TransDate) as tYear, 'ShopA' as Shop, sum(SA.Total) 
from Account as a
left join ShopATrans as SA ON a.AcctID = SA.AcctID
GROUP BY tYear
UNION ALL 
select a.AcctID, STRFTIME('%Y', SB.TransDate) as tYear, 'ShopB' as Shop, sum(SA.Total) 
from Account as a
left join ShopBTrans as SB ON a.AcctID = SB.AcctID
GROUP BY tYear

-- fill column with fixed value
select c.FirstName , "last name" LastName FROM Customer c; 