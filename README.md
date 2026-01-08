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

## 7. Output and Automation

### Containerisation with Docker
The data cleaning script has been containerised using Docker to improve portability, reliability, and automation readiness.

### Benefits of Docker
- Ensures consistent execution across different environments  
- Eliminates local dependency and configuration issues  
- Simplifies execution for developers and reviewers  
- Provides a foundation for CI/CD integration  
- Supports scalable and repeatable data processing  

### Execution Model
The Docker container runs as a batch job:
1. Reads raw input data from a mounted directory  
2. Executes the data cleaning and validation logic  
3. Writes the cleaned dataset back to the host system  

This design allows cleaned data to persist outside the container and be easily consumed by downstream processes.

--- 

## 8. Arhitecture Design for Login Platform
<img width="1043" height="198" alt="image" src="https://github.com/user-attachments/assets/a11636a1-3221-4905-a7f5-fa45241dd240" />

---







