# IMPORT MODULES
import os
import csv
from statistics import mean

# SET PATH
csvpath = os.path.join("Resources", "budget_data.csv")

# INITIALIZE VARIABLES
months = 0
pnl_box = []
sum_pnl = 0
delta = 0
prior_month = 0
delta_box = []
sum_delta = 0

greatest_incr = 0
greatest_dcr = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # COUNTER
        months += 1

        pnl_running = int(row[1])

        pnl_box.append("pnl_running")

        # Sum all PnL
        sum_pnl = sum_pnl + pnl_running

        # Count Months
        if months > 1:
            delta = pnl_running - prior_month
            delta_box.append(delta)
            sum_delta = sum_delta + delta

        # Sort for Greatest Increase
        if (months > 0) and (delta > greatest_incr):
            greatest_incr = delta
            greatest_incr_date = row[0]

        # Sort for Greatest Decrease
        if (months > 0) and (delta < greatest_dcr):
            greatest_dcr = delta
            greatest_dcr_date = row[0]

        prior_month = pnl_running

## Average Change Over the Period (using Stats module per GeeksForGeeks & Stephen's recommendation)
def Average(box):
    return mean(box)


box = delta_box
average = Average(box)

# FORMATTING TO PRINT
pnl_sum = "${:,.0f}".format(sum_pnl)
ave_change = "${:,.0f}".format(average)
increase = "${:,.0f}".format(greatest_incr)
decrease = "${:,.0f}".format(greatest_dcr)

## PRINT RESULTS
# The total number of months included in the dataset
print("The total number of months for the period is " + str(months))
# o	The net total amount of "Profit/Losses" over the entire period
print("The net total amount of Profit & Loss is " + str(pnl_sum))
# The average of the changes in "Profit/Losses" over the entire period
print("The average change of the PnL over the period is $" + str(ave_change))
# The greatest increase in profits (date and amount) over the entire period
print(
    "The Greatest Increase during the period was "
    + str(increase)
    + " on "
    + str(greatest_incr_date)
)
# The greatest decrease in profits (date and amount) over the entire period
print(
    "The Greatest Decrease during the period was "
    + str(decrease)
    + " on "
    + str(greatest_dcr_date)
)
