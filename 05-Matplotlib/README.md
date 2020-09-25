## 05 - Matplotlib Challenge

### Pymaceuticals
A Jupyter Notebook using Matplotlib to visualize science study data. 249 mice identified with SCC tumor growth were treated through a variety of drug regimens. Tumor development was observed and measured at intervals over 45 days. The study's objective was to compare  Pymaceuticals' drug of interest, Capomulin against other comparable regimens. The visualizations, including a top-level summary of the study results, are intended for use in a technical report to be presented to an executive team.

**Objectives**
1. Data Cleanup. Review data for duplicate mice and associated data.

2. Summary Statistics Table consisting of the mean, median, variance, standard deviation, and SEM of the tumor volume for each drug regimen.

3. Bar Plot using both Pandas's DataFrame.plot() and Matplotlib's pyplot showing the number of mice per time point for each treatment regimen throughout the course of the study. [These plots are identical, serving only to illustrate the two methods]

4. Pie Plot using both Pandas's DataFrame.plot() and Matplotlib's pyplot showing the distribution of female or male mice in the study. [These plots are identical, serving only to illustrate the two methods]

5. Final tumor volume calculation of each mouse across four of the most promising treatment regimens. Calculate the Quartiles and Interquartile Range (IQR) and quantitatively determine if there are any potential outliers across all four treatment regimens.

6. Box and Whisker Plot of the final tumor volume for all four treatment regimens, highlighting any potential outliers in the plot by changing their color and style.

7. Line Plot of time point versus tumor volume for a single mouse treated with Capomulin.

8. Scatter Plot of mouse weight versus average tumor volume for the Capomulin treatment regimen.

9. Correlation Coefficient and Linear Regression Model between mouse weight and average tumor volume for the Capomulin treatment. Plot the Linear Regression Model on top of the previous scatter plot.