import pandas as pd
from datetime import datetime

def load_and_clean_data(file):

    # Load the CSV file
    df = pd.read_csv(file)
    import pandas as pd
from datetime import datetime


def load_and_clean_data(file):
    """
    Loads the raw library CSV file and performs initial cleaning steps:
    - Removes empty rows
    - Renames columns for consistency
    - Removes duplicates
    - Cleans and parses date fields
    - Converts identifier columns to strings
    """

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # Remove rows where all values are missing
    df = df.dropna(how="all")

    # Rename columns to consistent, Python-friendly names
    df.rename(
        columns={
            "Id": "id",
            "Books": "book_title",
            "Book checkout": "checkout_date",
            "Book Returned": "return_date",
            "Days allowed to borrow": "time_allowed_to_barrow",
            "Customer ID": "customer_id",
        },
        inplace=True,
    )

    # Remove duplicate rows and reset the index
    df = df.drop_duplicates().reset_index(drop=True)

    # Clean date columns by removing quotes and extra whitespace
    # This ensures dates can be parsed correctly
    for col in ["checkout_date", "return_date"]:
        df[col] = (
            df[col]
            .astype("string")
            .str.replace('"', "", regex=False)
            .str.strip()
        )

    # Convert identifier and text columns to string type
    # IDs are stored as strings to avoid numeric interpretation issues
    df["id"] = df["id"].astype(str)
    df["book_title"] = df["book_title"].astype(str)
    df["customer_id"] = df["customer_id"].astype(str)

    # Convert date columns to datetime format (UK date format)
    df["checkout_date"] = pd.to_datetime(
        df["checkout_date"], errors="coerce", dayfirst=True
    )
    df["return_date"] = pd.to_datetime(
        df["return_date"], errors="coerce", dayfirst=True
    )

    return df


def standardize_book_title(title):
    """
    Standardises book titles so that:
    - Each word starts with a capital letter
    - Common small words are lowercase unless they are the first word
    """

    # If the value is missing, return it unchanged
    if pd.isna(title):
        return title

    # Words that should remain lowercase (unless first)
    small_words = {"and", "the", "or", "an", "a"}

    # Split the title into individual words
    words = title.lower().split()
    cleaned_words = []

    # Capitalise words based on position and rules
    for i, word in enumerate(words):
        if i == 0 or word not in small_words:
            cleaned_words.append(word.capitalize())
        else:
            cleaned_words.append(word)

    # Rebuild the title as a single string
    return " ".join(cleaned_words)


def calculate_borrow_time(row):
    """
    Calculates how many days a book was borrowed for.
    Returns NA if either date is missing.
    """

    checkout = row["checkout_date"]
    returned = row["return_date"]

    # If either date is missing or invalid, return NA
    if pd.isna(checkout) or pd.isna(returned):
        return pd.NA

    # Calculate the difference in days between return and checkout
    borrow_time = (returned - checkout).days
    return borrow_time


def process_library_data(file_path):
    """
    Main processing function that:
    - Loads and cleans the raw data
    - Standardises book titles
    - Calculates borrowed time
    - Removes invalid records with negative borrowed time
    """

    # Load and clean the raw data
    df = load_and_clean_data(file_path)

    # Apply title standardisation to book titles
    df["book_title"] = df["book_title"].apply(standardize_book_title)

    # Calculate borrowed time for each record
    df["borrow_time"] = df.apply(calculate_borrow_time, axis=1)

    # Track how many rows are removed due to invalid borrowed time
    dropCount = 0

    # Keep rows where borrowed time is valid or missing
    valid_loan_data = df[df["borrow_time"].isna() | (df["borrow_time"] >= 0)]

    # Calculate how many rows were dropped
    dropCount += len(df) - len(valid_loan_data)

    # Log the number of dropped rows for data quality visibility
    print(f"Dropped rows due to negative borrowed time: {dropCount}")

    return valid_loan_data


if __name__ == "__main__":
    # Path to the raw input file
    file_path = "03_Library Systembook.csv"

    # Run the full data processing pipeline
    processed_data = process_library_data(file_path)

    # Save the cleaned dataset to a CSV file for reporting
    processed_data.to_csv("clean_library_data.csv", index=False)

    # Drop rows where all values are NaN
    df = df.dropna(how='all')
    
    # Rename columns for consistency
    df.rename(columns={'Id': 'id', 
                       'Books': 'book_title', 
                       'Book checkout': 'checkout_date',
                       'Book Returned': 'return_date', 
                       'Days allowed to borrow': 'time_allowed_to_barrow',
                       'Customer ID': 'customer_id'}, 
                       inplace=True)
    
    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop= True)

    for col in ["checkout_date", "return_date"]:
        df[col]= (
            df[col]
            .astype('string')
            .str.replace('"','', regex= False)
            .str.strip()
        )
    
    # Convert relevant columns to the appropriate data types
    df['id'] = df['id'].astype(str)
    df["book_title"] = df["book_title"].astype(str)
    df['customer_id'] = df['customer_id'].astype(str)


    df['checkout_date'] = pd.to_datetime(df['checkout_date'], errors='coerce', dayfirst=True)
    df['return_date'] = pd.to_datetime(df['return_date'], errors='coerce', dayfirst=True)
    
    return df


def standardize_book_title(title):

    if pd.isna(title):
        return title
    
    small_words = {"and", "the", "or", "an", "a"}
    words = title.lower().split()
    cleaned_words = []

 
    for i, word in enumerate(words):

        if i == 0 or word not in small_words:
            cleaned_words.append(word.capitalize())
        else:
            cleaned_words.append(word)
    
    return " ".join(cleaned_words)


def calculate_borrow_time(row):

        checkout = row["checkout_date"]
        returned = row["return_date"]

        if pd.isna(checkout) or pd.isna(returned):
            return pd.NA
        # Calculate the difference in days
        borrow_time = (returned - checkout).days
        return borrow_time



def process_library_data(file_path):

    # Load and clean the data
    df = load_and_clean_data(file_path)
    # Standardize the book titles
    df["book_title"] = df["book_title"].apply(standardize_book_title)
    
    # Calculate borrow time for each row
    df['borrow_time'] = df.apply(calculate_borrow_time, axis=1)
    dropCount = 0
    valid_loan_data = df[df["borrow_time"].isna() | (df["borrow_time"]>=0)]
    dropCount += len(df)- len(valid_loan_data)

    print (f"Dropped row due to negative borrowed time: {dropCount}")
    
    return valid_loan_data


if __name__ == "__main__":
    file_path = "03_Library Systembook.csv"
    
    # Process the library data
    processed_data = process_library_data(file_path)
    
    # save to csv
    processed_data.to_csv('clean_library_data.csv',index=False)
    
