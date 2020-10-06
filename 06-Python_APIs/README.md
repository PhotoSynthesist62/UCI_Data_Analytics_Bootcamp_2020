## 06 - Python APIs

### WeatherPy (Part 1)

Python script (within a Jupyter Notebook) visualizing weather characteristics of 500+ cities across the world, of varying distance from the equater. Unique cities are selected at random using CityPy library. Weather characteristics are identified using *OpenWeatherMap API* [https://openweathermap.org/api] to create representative model of global weather patterns. 

1. Randomly select 500 sets of coordinates to populate a list 'lats_lngs.' Identify nearest city nearest each coordinate set and populate to a list called 'cities.'

2. Perform API call to OpenWeatherMap to obtain the following characteristics for each city: City Name, Coordinates, Max Temperature, Humidity, Cloudiness, Wind Speed, Country and API Call Date. Process 50 cities at a time, identified in a print log. Where city not found, print "City not found. Skipping." Print "Complete" when show call is finished.

3. Convert results to a Data Frame, review and eliminate results where Humidity is > 100%. Export results to a .csv file.

4. Create Scatter Plots to illustrate the following:
    * Temperature (F) vs. Latitude
    * Humidity (%) vs. Latitude
    * Cloudiness (%) vs. Latitude
    * Wind Speed (mph) vs. Latitude

5. Split Data Frame by Northern and Southern Hemisphere. Calculuate Linear Regression and illustrate with a series of Scatter Plots for the same features listed in #4.

### VacationPy (Part 2)

1. Import .csv results from Part 1 to a Data Frame.
2. Using GMaps, create a Heat Map to display the humidity for each city in the Data Frame.
3. Using Google Places API to find the first hotel for each city located within 5000 meters of your coordinates. 
4. Plot the hotels as pins over the Heat Map, with each pin identifying the Hotel Name, City, and Country.