#import
import os
import csv
 
#save file path
budget_data = os.path.join('..','Python_Challenge','Resources', 'budget_data.csv')
 
# Reading the CSV file
with open(budget_data) as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')
 
    print(csvreader)

    header = next(csvreader)
    first_row = next(csvreader)
    
    #define variables
    total_month = 1
    total_net = 1088983

    #define empty lists
    previous = first_row[1]
    changes_list = []

    #create a list to fine total month and store changes
    for row in csvreader:
        total_month += 1
        total_net += int(row[1])
        changes = int(row[1])-int(previous)
        changes_list.append(changes)
        previous = row[1]

    #find average change
    def average_change(changes_list):
        length = len(changes_list)
        total = 0
        for change in changes_list:
            total += change
        return total/length

#Check 
    print("Financial Analysis")
    print(f"Total Months: {total_month}")
    print(f"Total:{total_net}")
    print(f"Average Change: {average_change(changes_list):.1f}") 
    print(f"Greatest Increase in Profits: {max(changes_list)}")
    print(f"Greatest Decrease in Profits: {min(changes_list)}")

#export to txt file
save_file = os.path.join("..",'Python_Challenge', 'PyBank','PyBank.txt')
with open(save_file, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------------------------------\n")
    txt_file.write(f"Total Months: {total_month}\n")
    txt_file.write(f"Total: {total_net}\n")
    txt_file.write(f"Average Change: {average_change(changes_list)}\n")
    txt_file.write(f"Greatest Increase in Profits: {max(changes_list)}\n")
    txt_file.write(f"Greatest Decrease in Profits: {min(changes_list)}\n")
    txt_file.close()