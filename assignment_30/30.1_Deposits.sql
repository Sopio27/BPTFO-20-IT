--1,2

CREATE SCHEMA IF NOT EXISTS deposit
    AUTHORIZATION postgres;
	
CREATE TABLE IF NOT EXISTS deposits."Deposits"
(
    "DepositId" integer NOT NULL DEFAULT nextval('"Deposits_DepositId_seq"'::regclass),
    "DepositOwnerName" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "DateOfBirth" date NOT NULL,
    "City" character varying(28) COLLATE pg_catalog."default" NOT NULL,
    "StreetName" character varying(46) COLLATE pg_catalog."default" NOT NULL,
    "DepositAmount" money NOT NULL,
    "InterestAmount" money NOT NULL,
    "ComissionAmount" money NOT NULL,
    "TotalAmount" money NOT NULL,
    CONSTRAINT "UniqueDepositId" PRIMARY KEY ("DepositId")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS deposits."Deposits"
    OWNER to postgres;
	
	
--3,4

INSERT INTO deposit."Deposits"(
	"DepositOwnerName", 
	"DateOfBirth",
	"City", 
	"StreetName", 
	"DepositAmount", 
	"InterestAmount", 
	"ComissionAmount", 
	"TotalAmount")
	VALUES
	('Mari', '11-01-2000', 'Tbilisi', 'Pekini Str.', 2000, 10, 0, 2010),
	( 'Gio', '10-10-2000', 'Batumi', 'Gorgasali Str.', 10000, 30, 10, 10040),
	( 'Dato', '03-28-1989', 'Tbilisi', 'Aleksidze Str.', 250000, 40, 100, 250140),
	( 'Dea', '12-10-2009', 'Tbilisi', 'Rustaveli Str.', 345, 1, 0,  346),			
	( 'Lika', '10-03-2005', 'Batumi', 'Tsereteli Str.', 25, 0.02, 0, 25.02)		

--5

select * from deposit."Deposits";

--6

select * from deposit."Deposits"
where "DepositAmount" > '1500';

--7

select * from deposit."Deposits"
where upper("City") like N'%TBILISI%'AND  upper("StreetName") like N'%RUSTAVELI%';

--8
select * from deposit."Deposits"
where 
upper("City") like N'%BATUMI%'
AND upper("StreetName") like N'%GORGASALI%'
AND "DepositAmount" > '1000' AND "DepositAmount" < '2000';

--9
select * from deposit."Deposits"
where 
upper("DepositOwnerName") like N'D%';

--10
DELETE FROM deposit."Deposits"

--11
drop table deposit."Deposits"
