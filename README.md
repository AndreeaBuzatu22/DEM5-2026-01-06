# Library Data Automation Project

## 1. Project Introduction

### Background
The library currently performs data quality checks and reporting manually. This process is time-consuming, prone to human error, and difficult to scale as data volumes increase. There is also limited automation, which prevents stakeholders, librarians, and users from accessing up-to-date information.

### Project Aim
The aim of this project is to design and implement an **automated data processing pipeline** using Python, GitHub, and Azure DevOps. The solution will clean, validate, and transform library data, producing a presentation-ready dataset for reporting in Power BI.

### Objectives
- Reduce manual effort through automation  
- Improve data quality, consistency, and reliability  
- Enable repeatable and auditable data transformations  
- Provide timely insights for operational and strategic decision-making  

---

## 2. Project Timeline & Phases

| Phase | Description | Duration |
|-----|------------|----------|
| Planning & Exploration | Requirements gathering, data exploration, architecture design | 10 days |
| Data Storage & Cleaning | Data quality checks, table definition, validation, reporting | 10 days |
| Test & Development | Python development and unit testing | 5 days |
| Deployment | CI/CD pipeline setup | 3 days |
| Automation | Automated pipeline execution | 3 days |
| Reporting & Visualisation | Power BI dashboards and insights | 7 days |
| Technical Documentation | Final documentation and handover | 2 days |

---

## 3. Architecture Overview

<img width="741" height="137" alt="image" src="https://github.com/user-attachments/assets/8758a4cc-80ba-40eb-a6de-77f8397015ce" />

## 4. Data Processing Script Overview

### Purpose of the Python Script
The core of this project is a Python data cleaning and transformation script. Its purpose is to automate tasks that were previously performed manually, ensuring that library data is processed in a consistent, reliable, and repeatable way.
The script takes raw library data as input and produces a cleaned, validated dataset that is ready for reporting and visualisation in Power BI.

### What the Script Does
At a high level, the script performs the following steps:

- Loads the raw library dataset from a CSV file  
- Removes empty and duplicate records  
- Standardises column names and data formats  
- Cleans and standardises book titles for consistent presentation  
- Converts identifiers (IDs) to text to avoid reporting issues  
- Parses checkout and return dates into proper date formats  
- Calculates the number of days a book was borrowed  
- Removes invalid records where borrowed time is negative  
- Outputs a clean CSV file for downstream use  


---

## 5. Data Quality Rules and Validation

To ensure the data is reliable for decision-making, several data quality rules are applied within the script:

- **Empty rows** are removed  
- **Duplicate records** are dropped  
- **Invalid dates** are set to null  
- **Negative borrow durations** (return date before checkout date) are removed  
- **Book titles** are standardised so they are consistently formatted
- **Borrowed time** columns is added 

---


## 6. Testing 

### Unit Testing Approach
Unit tests are implemented using Python’s built-in `unittest` framework. Individual functions are tested in isolation to confirm they return the correct results under different scenarios.

The tests focus on:
- Correct calculation of borrowed time  
- Handling of missing or invalid dates  


### Benefits 
- Increased confidence in the accuracy of reports  
- Reduced risk of faulty data reaching Power BI dashboards  


---

## 7. Output and Reporting Readiness

The final output of the script is a cleaned CSV file that is consistent in structure, free from obvious data quality issues and ready to be consumed by Power BI  

## 8. Arhitecture Design for Login Platform
<img width="1043" height="198" alt="image" src="https://github.com/user-attachments/assets/a11636a1-3221-4905-a7f5-fa45241dd240" />

---







