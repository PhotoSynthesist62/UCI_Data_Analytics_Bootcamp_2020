DROP TABLE quake_table;

CREATE TABLE quake_table (
	"Date" VARCHAR(30) NOT NULL,
	"Tsunami" VARCHAR,
	"Depth" float,
	"Magnitude" float,
	"Country" VARCHAR,
	"State" VARCHAR,
	"Location" VARCHAR,
	"Latitude" VARCHAR(30) NOT NULL,
	"Longitude" VARCHAR(30) NOT NULL,
	"Deaths" float,
	"Injuries" float,
	"Damages_Millions" float,
	"Houses_Destroyed" float,
	"Houses_Damaged" float,
	"Total_Deaths" float,
	"Total_Injuries" float,
	"Total_Damages_Millions" float,
	"Tot_Houses_Destroyed" float,
	"Tot_Houses_Damaged" float
);

SELECT * FROM quake_table;
