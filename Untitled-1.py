"""
Author: Jaquaz Keech
Student ID: 20699210
Email: jaquazk@umich.edu
Collaborators: None 
"""

import csv

def read_csv_to_dicts(file_name):
    """
    Reads the CSV file and returns a list of dictionaries,
    where each dictionary represents a row with column headers as keys.
    """
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def calculate_total_profit(data):
    """
    Calculates total profit from the dataset.
    """
    total_profit = 0
    for row in data:
        profit = float(row['Profit'])
        total_profit += profit
    return total_profit

def revenue_per_category(data):
    """
    Calculates total revenue (Sales) for each product Category.
    Returns a dictionary with categories as keys and total sales as values.
    """
    revenue_dict = {}
    for row in data:
        category = row['Category']
        sales = float(row['Sales'])
        revenue_dict[category] = revenue_dict.get(category, 0) + sales
    return revenue_dict

def calculate_profitability_per_category(data):
    """
    Calculates profitability by category as total profit divided by total sales.
    Returns a dictionary with categories as keys and profitability ratio as values.
    """
    profit_dict = {}
    sales_dict = {}
    for row in data:
        category = row['Category']
        profit = float(row['Profit'])
        sales = float(row['Sales'])
        profit_dict[category] = profit_dict.get(category, 0) + profit
        sales_dict[category] = sales_dict.get(category, 0) + sales

    profitability = {}
    for category in profit_dict:
        if sales_dict[category] != 0:
            profitability[category] = profit_dict[category] / sales_dict[category]
        else:
            profitability[category] = 0
    return profitability

