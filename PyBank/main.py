import os
import csv

# This is the path of the CSV file relative to this file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Opening CSV file to read
with open(budget_csv) as csvfile:

    #Reading in the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    #Saving the header row in case for later and to skip the header row for analysis
    csv_header = next(csvreader)

    # Initializing a bunch of variables to use in the for loop
    # This will be used to find the overall profit
    total_profit = 0
    # This will be used to calculate the number of months
    count_of_months = 0
    # This will be used to store the months starting at the second row as it'll be the difference in profit
    month = []
    # This will store the difference of profit
    profit_difference = []
    
    # All interation over the csv.reader file needs to be done in the same for loop as it can only be iterated over once.
    for row in csvreader:
        total_profit += int(row[1])
        count_of_months += 1
        # This is used to calculate the profit_start and the profit of the first month
        if row[0] == "Jan-10":
            profit_start = int(row[1])
            last_month = profit_start
        # This is used to calculate the profit_end, as well as add the current month, and calculate and append the difference in profit between the last 2 months
        elif row[0] == "Feb-17":
            month.append(row[0])
            profit_end = int(row[1])
            new_month = int(row[1]) - last_month
            profit_difference.append(new_month)
            last_month = int(row[1])
        # This is used to add the current month (starting at month 2), and calculate and append the difference in profit between the current and previous months
        else:
            month.append(row[0])
            new_month = int(row[1]) - last_month
            profit_difference.append(new_month)
            last_month = int(row[1])
        
    # Now that we have the list of all months (except the first), we can find the months that have the max and min profit difference
    max_month = month[profit_difference.index(max(profit_difference))]
    min_month = month[profit_difference.index(min(profit_difference))]
    
    # This is a list I created to be able to print to the terminal and the file at the same time
    # The first 2 items in the list are the header text and separator in the text file. The next two items are the total number of
    # months and total profit. The third item calculates the average profit by taking the difference between profit_end profit_start, 
    # then dividing by the count of months in the months list which is 1 month less than the total number of months.
    # The last two items are the greatest increase and decrease in profits, and getting the months that have the max and min profit_difference, and print that difference.
    output_file = ["Financial Analysis", "----------------------------", \
        f'Total Months: {count_of_months}', f'Total: ${total_profit}', \
        f'Average Change: ${round((profit_end - profit_start)/(len(month)), 2)}', \
        f'Greatest Increase in Profits: {max_month} (${max(profit_difference)})', \
        f'Greatest Decrease in Profits: {min_month} (${min(profit_difference)})']

    # This defines the output path for the file to write to. It's being written in the Analysis folder that we were told to create.
    output_path = os.path.join("Analysis", "pybank.txt")

    # This is the code that writes both to the terminal and the output file, and I used a for loop to do both at the same time.
    with open(output_path, "w") as pybank:
        for string in output_file:
            print(string)
            pybank.write(string)
            pybank.write('\n')