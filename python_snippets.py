#!/usr/bin/env python3
"""
Pandas Week 1 Challenge: Advanced DataFrame Operations

This script contains challenging pandas exercises that go beyond basic operations.
Complete each TODO section to test your understanding of pandas fundamentals.

Instructions:
1. Fork this repository and clone it to your local machine
2. Complete each challenge by replacing TODO comments with working code
3. Test your solutions by running: python pandas_week1_challenge.py
4. Commit and push your solutions back to your fork
5. Create a pull request to submit your work

Author: [Your Name Here]
Date: [Today's Date]
"""

import pandas as pd
import numpy as np

def challenge_1_dataframe_creation():
    """
    Challenge 1: Create and Explore DataFrame
    
    Create a DataFrame with student information and perform advanced queries.
    """
    print("=" * 50)
    print("Challenge 1: DataFrame Creation and Exploration")
    print("=" * 50)
    
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [24, 27, 22, 25, 26],
        "Score": [85, 90, 88, 92, 87],
        "City": ["New York", "London", "Paris", "Tokyo", "Sydney"]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    print()
    
    # TODO: Display first 3 rows
    print("First 3 rows:")
    # Your code here
    
    # TODO: Find the student with the highest score and display their full information
    print("\nStudent with highest score:")
    # Your code here
    
    # TODO: Display basic statistics for the 'Age' and 'Score' columns
    print("\nBasic statistics:")
    # Your code here
    
    return df

def challenge_2_advanced_filtering():
    """
    Challenge 2: Complex Filtering Operations
    
    Apply multiple conditions and advanced filtering techniques.
    """
    print("\n" + "=" * 50)
    print("Challenge 2: Advanced Filtering")
    print("=" * 50)
    
    data = {
        "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Tablet"],
        "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Electronics"],
        "Price": [1200, 25, 80, 300, 150, 500],
        "Stock": [15, 50, 30, 8, 25, 12],
        "Rating": [4.5, 4.2, 4.0, 4.8, 4.3, 4.1]
    }
    df = pd.DataFrame(data)
    
    print("Product DataFrame:")
    print(df)
    print()
    
    # TODO: Filter products where Price > 100 AND Rating >= 4.3
    print("High-value, well-rated products:")
    # Your code here
    
    # TODO: Filter products that are either Electronics OR have Stock < 20
    print("\nElectronics or low-stock items:")
    # Your code here
    
    # TODO: Find the cheapest product in each category
    print("\nCheapest product per category:")
    # Your code here
    
    return df

def challenge_3_data_transformation():
    """
    Challenge 3: Data Transformation and New Columns
    
    Create new columns based on complex conditions and calculations.
    """
    print("\n" + "=" * 50)
    print("Challenge 3: Data Transformation")
    print("=" * 50)
    
    data = {
        "Employee": ["John", "Sarah", "Mike", "Lisa", "Tom", "Anna"],
        "Department": ["Sales", "Engineering", "Sales", "Engineering", "HR", "HR"],
        "Salary": [45000, 75000, 50000, 80000, 55000, 60000],
        "Years_Experience": [2, 5, 3, 7, 4, 6],
        "Performance_Score": [3.2, 4.5, 3.8, 4.2, 3.5, 4.0]
    }
    df = pd.DataFrame(data)
    
    print("Employee DataFrame:")
    print(df)
    print()
    
    # TODO: Create a 'Salary_Grade' column:
    # 'High' if Salary >= 70000, 'Medium' if 50000 <= Salary < 70000, 'Low' otherwise
    print("Adding Salary Grade:")
    # Your code here
    
    # TODO: Create a 'Bonus_Eligible' column:
    # True if Performance_Score >= 4.0 AND Years_Experience >= 5, False otherwise
    print("\nAdding Bonus Eligibility:")
    # Your code here
    
    # TODO: Calculate each employee's 'Salary_Per_Experience_Year'
    print("\nAdding Salary per Experience Year:")
    # Your code here
    
    print("\nTransformed DataFrame:")
    # Your code here (display the updated dataframe)
    
    return df

def challenge_4_groupby_aggregation():
    """
    Challenge 4: Advanced Grouping and Aggregation
    
    Perform complex groupby operations with multiple aggregation functions.
    """
    print("\n" + "=" * 50)
    print("Challenge 4: Grouping and Aggregation")
    print("=" * 50)
    
    data = {
        "Region": ["North", "South", "North", "East", "West", "South", "East", "West"],
        "Product": ["A", "A", "B", "A", "B", "B", "A", "B"],
        "Sales": [1000, 1500, 1200, 900, 1800, 1300, 1100, 1600],
        "Units_Sold": [20, 30, 24, 18, 36, 26, 22, 32],
        "Quarter": ["Q1", "Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q2"]
    }
    df = pd.DataFrame(data)
    
    print("Sales DataFrame:")
    print(df)
    print()
    
    # TODO: Calculate total sales and average units sold by Region
    print("Sales summary by Region:")
    # Your code here
    
    # TODO: Find the best performing Product in each Region (highest total sales)
    print("\nBest product by Region:")
    # Your code here
    
    # TODO: Calculate quarter-over-quarter growth by Region
    # Hint: Use pivot_table or groupby with unstack
    print("\nQuarterly sales by Region:")
    # Your code here
    
    return df

def challenge_5_missing_data_advanced():
    """
    Challenge 5: Advanced Missing Data Handling
    
    Deal with missing data using sophisticated techniques.
    """
    print("\n" + "=" * 50)
    print("Challenge 5: Missing Data Handling")
    print("=" * 50)
    
    # Create data with strategic missing values
    data = {
        "Name": ["Alex", "Betty", "Carlos", "Diana", "Ethan", "Fiona"],
        "Age": [28, np.nan, 35, 29, np.nan, 31],
        "Department": ["IT", "HR", np.nan, "Finance", "IT", np.nan],
        "Salary": [70000, 55000, np.nan, 62000, 75000, np.nan],
        "Years_Experience": [5, 8, 12, 6, np.nan, 9]
    }
    df = pd.DataFrame(data)
    
    print("DataFrame with missing values:")
    print(df)
    print()
    
    # TODO: Display missing value summary (count and percentage)
    print("Missing value analysis:")
    # Your code here
    
    # TODO: Fill missing Ages with the median age of the same Department
    # If Department is also missing, use overall median
    print("\nAfter filling missing Ages:")
    # Your code here
    
    # TODO: Fill missing Departments with the most common department
    print("\nAfter filling missing Departments:")
    # Your code here
    
    # TODO: Fill missing Salaries based on average salary of same Department
    print("\nAfter filling missing Salaries:")
    # Your code here
    
    return df

def challenge_6_comprehensive_analysis():
    """
    Challenge 6: Comprehensive Data Analysis
    
    Combine multiple pandas operations for a complete analysis.
    """
    print("\n" + "=" * 50)
    print("Challenge 6: Comprehensive Analysis")
    print("=" * 50)
    
    # Student grades dataset
    data = {
        "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"],
        "Math": [88, 92, 78, 95, 83, 90, 87, 91],
        "Science": [91, 85, 88, 92, 89, 87, 94, 86],
        "English": [79, 88, 92, 87, 94, 85, 90, 89],
        "History": [85, 90, 85, 91, 88, 92, 86, 93],
        "Grade_Level": [10, 11, 10, 12, 11, 12, 10, 11]
    }
    df = pd.DataFrame(data)
    
    print("Student Grades DataFrame:")
    print(df)
    print()
    
    # TODO: Add a column for each student's overall average
    print("Adding overall averages:")
    # Your code here
    
    # TODO: Add a column for letter grade based on average:
    # A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
    print("\nAdding letter grades:")
    # Your code here
    
    # TODO: Find the top 3 students overall
    print("\nTop 3 students:")
    # Your code here
    
    # TODO: Calculate subject averages by grade level
    print("\nSubject averages by grade level:")
    # Your code here
    
    # TODO: Find which subject has the highest average score
    print("\nBest performing subject:")
    # Your code here
    
    # TODO: Identify students who are above average in all subjects
    print("\nAll-around excellent students:")
    # Your code here
    
    return df

def main():
    """
    Main function to run all challenges.
    
    Uncomment each challenge as you complete it.
    """
    print("PANDAS WEEK 1 CHALLENGE")
    print("Complete each function by replacing TODO comments with working code.")
    print("Test your solutions and commit your changes to GitHub!")
    print()
    
    # Uncomment challenges as you complete them:
    challenge_1_dataframe_creation()
    # challenge_2_advanced_filtering()
    # challenge_3_data_transformation()
    # challenge_4_groupby_aggregation()
    # challenge_5_missing_data_advanced()
    # challenge_6_comprehensive_analysis()
    
    print("\n" + "=" * 50)
    print("🎉 Congratulations! You've completed the Pandas Challenge!")
    print("Don't forget to commit and push your solutions to GitHub!")
    print("=" * 50)

if __name__ == "__main__":
    main()