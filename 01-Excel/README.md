## 01 - Excel Challenge

### Kickstarter Campaigns
#### Modify and analyze the provided .csv table data (4,000 past Kickstarter projects) to identify market trends.
* Apply conditoional formatting text/background colors to "state" column: Successful (green/pale green), Failed (red/pink), Canceled (black/blue), Currently Live (brown/yellow).
* Add col O ("Percent Funded"); enter formula showing the percentage each campaign has been funded to reach its initial goal. Apply three-color scale conditional formatting to the col, starting at 0% (dark red), transitioning to green at 100%, and blue at 200%.
* Add col P ("Average Donation"); enter formula showing the average $ amount contributed per # of campaign backers.
* Add cols Q ("Category") and R ("Sub-Category"); enter formulas splliting column N ("Category and Sub-Category") into the new cols. 
* Add cols S ("Date_Created_Conversion") and T ("Date_Ended_Conversion"); enter formulas converting the Unix timestamps in cols I ("deadline") and J ("launched"), respectively, to Excel date format in the new cols.

#### Category Stats

Create Pivot Table (PT) on sheet 'Campaigns by Category' to calculate the # of Successsful, Failed, Canceled, or Currently Live compaigns, per "Category". Illustrate the PT as a Stacked Column Pivot Chart, w country filter.

#### Subcategory Stats

Create PT on sheet 'Campaigns by Sub-Cat' to calculate # of Successsful, Failed, Canceled, or Currently Live compaigns, per "Sub-Category"; illustrate PT as a Stacked Column Pivot Chart, w filters by country and parent-category.

#### Outcomes Based on Launch Date

Create PT on sheet 'Campaign Ct Over Time' using "state" "Date_Created_Conversion" as the col and row data, respectively. Use count of "state as table values. Add filter based on "Category." Use PT grouping to view data by month or by year. Illustrate PT as a Line Graph Pivot Chart.

#### Analysis (Answer the following in a separate Word document)

    Given the provided data, what are three conclusions we can draw about Kickstarter campaigns?

    What are some limitations of this dataset?

    What are some other possible tables and/or graphs that we could create?