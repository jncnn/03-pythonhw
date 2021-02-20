import os
import csv

csvfile=os.path.join("budget_data.csv")
profit=[]
monthly_changes=[]
date=[]

#initialize the variable
count =0
total_profit=0
initial_profit=0
monthly_change=0
total_monthly_change=0
greatest_increase=0
greatest_decrease=0

with open (csvfile) as budgetdata:
    csvreader=csv.reader(budgetdata)
    header=next(csvreader)
    
    for row in csvreader:

        total_profit=total_profit+int(row[1])
        count=count+1
        if count==1:
             last_month_profit=int(row[1])
        else:
            monthly_change=int(row[1])-last_month_profit
            total_monthly_change=total_monthly_change + monthly_change
            last_month_profit=int(row[1])

            if greatest_increase<monthly_change:
                greatest_increase=monthly_change
            if greatest_decrease>monthly_change:
                greatest_decrease=monthly_change

average_monthly_change=total_monthly_change/(count-1)
# print(f"average monthly change: {average_monthly_change}")
# print(f"greatest monthly decrease: {greatest_decrease}")
# print(greatest_increase)

# print(total_profit)
# print(count)


print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_monthly_change)))
print("Greatest Increase in Profits: " + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + " ($" + str(greatest_decrease)+ ")")
print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_monthly_change)) + "\n")
    text.write("    Greatest Increase in Profits: "  + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: "  + " ($" + str(greatest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")


#solution 
#   #Financial Analysis
#   #----------------------------
#   #Total Months: 86
#   #Total: $38382578
#   #Average  Change: $-2315.12
#   #Greatest Increase in Profits: Feb-2012 ($1926159)
#   #Greatest Decrease in Profits: Sep-2013 ($-2196167)

            













