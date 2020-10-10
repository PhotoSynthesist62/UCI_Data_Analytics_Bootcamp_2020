## 11 - HTML / CSS Challenge

### Web Visualization Dashboard (Latitude Analysis)

A HTML dashboard of visualizations previously created for WeatherPy (09-Python APIs). 

The website consists of 7 pages:

* #index: Summary explanation of the project and links to each visualization page.
* #visualizations (pages 1-4): Each of these incldude a descriptive title, heading tag, the visualization (plotted data) for the selected comparison, and a summary explanation.
* #comparisons: All visualizations on one page, for ease of comparison, presented in a responsive Bootstrap grid.
* ##data:  A responsive table of the visualizations' source data - `cities.csv` - converted to HTML. (see Notebook under /Resources).

Navigation through the site is conducted through a responsive navbar (uses media queries) at the top of each page, with the following features:
* "Latitude Analysis Dashboard" link returning the user to #index. 
* "Plots" linking to a drop-down menu. The user may navigate to any of the 4 #visualization pages.
* "Comparisons" linking to the #comparisons page.
* "Data" linking to #data page.