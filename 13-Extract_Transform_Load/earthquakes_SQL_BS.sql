drop table earthquakes;
create table earthquakes (
	Date varchar(30) not null,
	Latitude varchar(30) not null,
	Longitude varchar(30) not null,
	Depth float,
	Magnitude float
);
select * from earthquakes;

select * from earthquakes
where ("Magnitude" > 8);