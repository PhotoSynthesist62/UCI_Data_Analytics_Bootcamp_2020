# ETL-Project
#### Brandon Su and Andrea Rosenberger

##### Sources of Data 
1.	Kaggle: Significant Earthquake data [NEIC]. https://www.kaggle.com/usgs/earthquake-database/data
2.	National Geophysical Data Center / World Data Service (NGDC/WDS): Significant Earthquake Database. National Geophysical Data Center, NOAA. 	
	https://www.ngdc.noaa.gov/nndc/struts/form?t=101650&s=1&d=1

##### Purpose
We chose these datasets because of a general interest in the trends and frequency of significant earthquakes. We both live in Southern California and are interested in the decades-long threat from seismologists that “The Big One” is coming.  By using data sets from unique sources, we can compare and contrast the accuracy and consistent of collected seismological data.

##### Extract & Transform
The Kaggle dataset was downloaded from the site as a .CSV.  The NGDC data set was downloaded from that site as a tab-delimited text file and converted to a .CSV in Excel.

The Kaggle dataset did not need much transformation aside from cleaning. There were extra columns dedicated to depth error, magnitude types and stations that were not needed for what we wanted to see, which was a basic measure of the earthquake, location, and time. 

The NGDC data set was larger and more sophisticated with additional incremental chronology data (columns split by Year, Month, Day, Hour and Second), tsunami status, residential damages, and loss of life related to each event.  The incremental chronology data, for example, was merged in a simple date column, to correspond with the Kaggle data set. The ultimate goal was to have multiple columns that were parallel with Kaggle data set for joining.

##### Loading Data into PgAdmin4 Database
We chose PGAdmin4 due to general preference and usability of the tool. Much of the transformation revolved around creating parallel column headers so the larger data set could be joined with the smaller one in different increments, as needed.  The visual interface of PGAdmin4 makes it easier to work with and to visualize the data we imported into the database.




		

		
