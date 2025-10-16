"""
Author: Jaquaz Keech
Student ID: 20699210
Email: jaquazk@umich.edu
Collaborators: None 
"""

import csv

#Function to read the CSV file and return a list of dictionaries
def read_csv(file_name):
    with open(file_name, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# Calclulate total profit by summing up the 'Profit' column
def total_profit(data):
    return sum(float(row['Profit']) for row in data)

# Aggregate total profit by product category and return sored list by profit descending
def profit_by_category(data):
    Profit_sum = {}
    for row in data:
        category = row['Category']
        profit = float(row['Profit'])
        if category in Profit_sum:
            Profit_sum[category] += profit
        else:
            Profit_sum[category] = profit
    # Sort categories by profit in descending order
    sorted_profit = sorted(Profit_sum.items(), key=lambda x: x[1], reverse=True)
    return sorted_profit

# Calculate average profit per product category
def average_profit_per_product(data):
    profit_sum = {}
    count = {}
    for row in data:
        category = row['Category']
        profit = float(row['Profit'])
        profit_sum[category] = profit_sum.get(category, 0) + profit
        count[category] = count.get(category, 0) + 1

    #calculate average profit per category
    avg_profit = {category: profit_sum[category] / count[category] for category in profit_sum}
    return avg_profit

# Main function to execute the analysis
def main():
    #read data from CSV file
    data = read_csv('SampleSuperstore.csv')

    # Calculate and print total profit
    total = total_profit(data)
    print(f"Total Profit: ${total:.2f}")

    # Calculate profit by category and print sorted results
    profit_category = profit_by_category(data)
    print("Profit by Category (most to least):")
    for category, profit in profit_category:
        print(f"  {category}: ${profit:.2f}")

    # Calculate average profit per product category and print results
    avg_profit = average_profit_per_product(data)
    print("Average Profit per Product Category:")
    for category, avg in avg_profit.items():
        print(f"  {category}: ${avg:.2f}")

# run main function if this script is executed
if __name__ == "__main__":
    main()
