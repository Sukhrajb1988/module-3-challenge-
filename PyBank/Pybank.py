import csv
import os

#read csv
bank = r"C:\Users\sukhr\Desktop\module-3-challenge-\PyBank\Resources\budget_data.csv"
with open(bank, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)

#set variable sup
    count = 0 
    total = 0
    prev_revenue = 0 
    revenue_change_list = []
    month_of_change = []
    total_change = 0 
    
    #run loop to read through data set
    for row in reader:
        count = count + 1
        current_revenue = int(row[1])
        total = total + current_revenue
        
        #set up condition to autopopulate revenue change
        if prev_revenue != 0 :
            revenue_change = current_revenue - prev_revenue
            revenue_change_list.append(revenue_change)
            month_of_change.append(row[0])
            total_change = total_change + revenue_change
            
        prev_revenue = current_revenue
    
    avg_change = total_change / (count - 1)

    
    print(f'Total number of months: {count}')
    print(f'Total profit/loss: ${total}')
    print(f'Total change: {total_change}')
    print(f'Average change: ${avg_change:.2f}')
    
    max_increase = max(revenue_change_list)
    max_increase_month = month_of_change[revenue_change_list.index(max_increase)]
  
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
  
    max_decrease = min(revenue_change_list)
    max_decrease_month = month_of_change[revenue_change_list.index(max_decrease)]

    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})") 

output = (
    
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

print(output)

output_file = r"C:\Users\sukhr\Desktop\module-3-challenge-\PyBank\Analysis/result.txt"
with open(output_file, "w") as f:
    f.write(output)


      
      

