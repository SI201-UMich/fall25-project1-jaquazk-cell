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
