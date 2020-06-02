# Dependencies
import os
import csv

#Set lists to hold values
months = []
revenue = []
monthly_change = []

# Set path for file
bank_csv_path = os.path.join("budget_data.csv")
analysis_file = os.path.join("analysis_file.csv")

# Open and read file
with open(bank_csv_path, newline="",) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    # read thru each row after the header and list months
    for row in csv_reader:
        months.append(row[0])
        revenue.append(row[1])

    #Loop through profits to get changes
    for i in range(len(revenue)-1):
        monthly_change.append(int(revenue[i+1])- int(revenue[i]))

    #Min and max revenue
    max_increase_value = max(monthly_change)
    max_decrease_value = min(monthly_change)     

    max_increase_month = monthly_change.index(max(monthly_change)) + 1
    max_decrease_month = monthly_change.index(min(monthly_change)) + 1 

    #Print data
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months)}")
    print("Total" + "$" + str(revenue))
    print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")

# Write methods to print to Financial_Analysis_Summary 
with open("analysis_file", "w") as text:
    table_holder.write("Financial Analysis")
    table_holder.write("\n")
    table_holder.write("----------------------------")
    table_holder.write("\n")
    table_holder.write(f"Total Months: {len(months)}")
    table_holder.write("\n")
    table_holder.write(("Total" + "$" + str(revenue))
    table_holder.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    table_holder.write("\n")
    table_holder.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    table_holder.write("\n")
    table_holder.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")