#https://www.w3schools.com/sql/sql_unique.asp

CREATE DATABASE TEST;
USE TEST;
#DROP DATABASE TEST;

#DATA TYPES:
#-----------
#1)NUMERIC,INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT,DECIMAL,FLOAT, DOUBLE
#2)CHAR, VARCHAR,TEXT
#3)DATE,TIME,DATETIME, or TIMESTAMP,

CREATE TABLE table1(id int primary key,
name varchar(30),
dod datetime,
email varchar(40)
);

SHOW TABLES;

DESC table1;#to check table are present or not (desc = describe)

# creat sub table or  add col in existing table or 
CREATE TABLE table2 AS
SELECT id ,name
FROM table1;

DESC table2;

#---------------
#insert data into tables

INSERT INTO table1(id,name,dod,email)
VALUES (1992,'gopi','1992-11-27 10:55:50','gopi@gmail.com');
# or
SELECT * FROM table1;# it selects all col data like desc

INSERT INTO table1
VALUES (2002,'ADBD','2000-02-12 23:44:44','dsd@gmail.com'),
(2037,'ADBD','2000-02-12 23:44:44','dsd@gmail.com'),
(203,'ADBD','2000-02-12 23:44:44','dsd@gmail.com');

#insert data in one tables to other table
#INSERT INTO first_table_name[col1,col2,col3,..]SELECT col1,col2,col3 ....FROM second_table_name[where condition];

CREATE TABLE table3(id int primary key,name varchar(30),dod datetime,email varchar(40));
INSERT INTO table3(id,name,dod,email)
SELECT id,name,dod,email FROM table1;
#select q
SELECT * FROM table1;
SELECT name,email FROM table1;

# operators:ATH:- + - * / %; COMP:-NOTEQUAL TO <> ,<,>,>=,<=,
#LOG :- ALL ,AND, IN ,BETWEEN , LIKE, OR, IS NULL
SELECT 5+ 10;
SELECT 5 % 2;
#COMP
SELECT * FROM table1 WHERE id >1990;
#LOG
SELECT * FROM table1 WHERE id =1992 OR name = 'gopi';
SELECT * FROM table1 WHERE name like 'g%';
SELECT * FROM table1 WHERE email like '%gmail%';
SELECT * FROM table1 WHERE id like '199_';
SELECT * FROM table1 WHERE name like '_o%';
SELECT * FROM table1 WHERE id IN (1992,2002);
SELECT * FROM table1 WHERE id BETWEEN 1992 AND 2002;
SELECT * FROM table1 WHERE id < ALL (SELECT id  FROM table1 WHERE name = 'gopi');
#-----------------------------
# UPDATE AND DELETE
UPDATE  table1  SET id = 2003 WHERE id= 2001;
SELECT * FROM table1;

DELETE FROM table1 WHERE id=2033;
#--------------------
#SELECT TOP id FROM table1  2;#[WHERE]
SELECT * FROM table1 LIMIT 2;
#SHORTING 
#SELECT Cols FROM table1 [WHERE][ORDER BY Cols NAMES][ASC/DESC];
SELECT id,name FROM table1 ORDER BY name ;#[ASE/DESC]
#GROUP BY
#SELECT Cols FROM tablename WHERE[GROUP BBY Cols][ORDER BY Cols NAMES]
SELECT * FROM table3 ;
SELECT email ,COUNT(*) FROM table3 GROUP BY email;
SELECT email ,SUM(id) FROM table3 GROUP BY email;
SELECT DISTINCT email FROM table1 ORDER BY email ;
SELECT id AS ids,name AS 'names' FROM table1;
#--------------
#JOIN
SELECT * FROM table1 ;
CREATE TABLE table4(id int primary key,cell_no int );
INSERT INTO table4 VALUES (203,9840850),(1992,53480),(2001,45375),(2055,305807);
SELECT * FROM table4;
SELECT t1.id,t1.name,t1.email,t4.cell_no FROM table1 AS t1 
JOIN table4 AS t4 ON t1.id = t4.id;
#--0R --
SELECT t1.id,t1.name,t1.email,t4.cell_no FROM table1 AS t1, 
table4 AS t4 WHERE t1.id = t4.id;
#LEFT AND RIGHT JOIN
SELECT t1.id,t1.name,t1.email,t4.cell_no FROM table1 AS t1 
LEFT JOIN table4 AS t4 ON t1.id = t4.id;
SELECT t1.id,t1.name,t1.email,t4.cell_no FROM table1 AS t1 
RIGHT JOIN table4 AS t4 ON t1.id = t4.id GROUP BY t1.email;
#---------------
SELECT t1.email,ROUND(AVG(t4.cell_no))FROM table1 AS t1 JOIN table4 AS t4 ON t1.id = t4.id
 GROUP BY t1.email;
#Numeric Functions
SELECT 5 DIV 2;#%==/
SELECT 5 MOD 2;# ==%
SELECT ABS(-15);
SELECT ROUND(54.45) AS 'ROUND_NUMBER';
SELECT ROUND(54.45,2) AS 'ROUND_NUMBER';
SELECT CEIL(35.33);
SELECT FLOOR(35.33);
SELECT EXP(5);
SELECT LOG(2);
SELECT LOG10(2);
SELECT POW(2,7);
SELECT GREATEST(5,6,7,8,9,0,2,3,4);
SELECT LEAST(5,6,7,8,9,0,2,3,4);
SELECT RADIANS(180);
SELECT SQRT(2);
SELECT TRUNCATE(225.66494,2);#(NUM,.NO.OF DIG REQUIRED)
SELECT RAND();
#STRING FUNCTIONS
SELECT CONCAT('GOPI','KAKARAPALLI');
SELECT UPPER('gopi');
SELECT LOWER('gopi');
SELECT TRIM('             gopi           ');
SELECT SUBSTR('gopi KAKARAPALLI',6,11);#(STRING,START CHAR , REQUIED CHAR)
SELECT RIGHT('gopi KAKARAPALLI',11);#(STRING,START CHAR )
SELECT LEFT('gopi KAKARAPALLI',6);#(STRING,START CHAR)
SELECT LENGTH('gopi KAKARAPALLI');
SELECT CHAR_LENGTH('gopi KAKARAPALLI');
SELECT INSERT('gopi K',6,1,'KAKARAPALLI');#insert STRING

SELECT REPEAT('gopi KAKARAPALLI',10);#LIKE FOR LOOP
SELECT REPLACE('gopi K','K','KAKARAPALLI');
SELECT REVERSE('gopi KAKARAPALLI');
SELECT STRCMP('GOPI','GOPI');#0=,-1:LESS,1=MORE
#Date & Time Functions
SELECT ADDDATE('1989-11-20',INTERVAL 25 DAY);#  +
SELECT ADDDATE('1989-11-20',INTERVAL 12 MONTH );
SELECT ADDDATE('1989-11-20',INTERVAL 25 YEAR);
SELECT SUBDATE('1989-11-20',INTERVAL 25 DAY);# -
SELECT CURDATE();
SELECT CURTIME();
SELECT current_timestamp();
SELECT UNIX_TIMESTAMP();#IN SEC
SELECT NOW();
SELECT DAYNAME('1989-11-20');
SELECT DAYNAME(dod) FROM table1;
SELECT MAKEDATE(2003,365);
SELECT MONTHNAME('2017-03-04');

SELECT TIMEDIFF('1989-11-20 17:50;59','1989-11-20 18:50:59');
SELECT TIME_TO_SEC('18:50:59');
SELECT UNIX_TIMESTAMP();
#EREATE VIEW table viewS 
CREATE VIEW table1_view AS SELECT id,name,email FROM table1 WHERE name IS NOT NULL;
SELECT * FROM table1_view;

INSERT INTO table1_view VALUES (2396,'FSSGDG','SFSKFN2jdan@gmail.com');

INSERT INTO table1_view VALUES (2302,NULL,'SFSKFN2jdan@gmail.com');
SELECT * FROM table1_view;
CREATE VIEW table1_view1 AS SELECT id,name,email FROM table1 WHERE name IS NOT NULL WITH CHECK OPTION;
INSERT INTO table1_view VALUES (2372,NULL,'SFSKFN2jdan@gmail.com');
#also work delete, update drop
DROP VIEW table1_view;

# Aggregate Functions

SELECT COUNT(*) FROM table1;
SELECT MAX(id) FROM table1;
SELECT MIN(id) FROM table1;
SELECT sum(id) FROM table1;
SELECT avg(id) FROM table1;
TRUNCATE TABLE table2;# COMPLATE DELETE

#SUBQUERIES 
SELECT id,name FROM table1 WHERE id=(SELECT MAX(id) FROM table1);
# to add new col
ALTER TABLE table1 ADD city CHAR(20);
select * from table1;
ALTER TABLE table1 DROP city;
select * from table1;
DESC table3;
ALTER TABLE table3 MODIFY name CHAR(30) NOT NULL;
DESC table3;

GRANT FILE ON *.* TO 'gopi'@'localhost';#You have to make sure that the image file is readable by MySQL, and that the MySQL user has the FILE privilege. To grant the FILE privilege, log-in as root and execute
drop table pix;
# insert images
CREATE TABLE pix(image_id int(10) NOT NULL AUTO_INCREMENT primary key , image LONGBLOB NOT NULL);
INSERT INTO pix(image_id,image)VALUES(1,load_file('E:\\img1.jpg'));
select * from pictures;

CREATE TABLE pictures ( image_id int(10) NOT NULL auto_increment,image blob,PRIMARY KEY (image_id) 
);
INSERT INTO pictures VALUES(2, LOAD_FILE('C:\\img2.jpg'));

