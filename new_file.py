import pandas as pd
from datetime import datetime

def load_and_clean_data(file):

    # Load the CSV file
    df = pd.read_csv(file)
    
    # Drop rows where all values are NaN
    df = df.dropna(how='all')
    
    # Rename columns for consistency
    df.rename(columns={'Id': 'id', 'Books': 'book_title', 'Book checkout': 'checkout_date',
                       'Book Returned': 'return_date', 'Days allowed to borrow': 'time_allowed_to_barrow',
                       'Customer ID': 'customer_id'}, inplace=True)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert relevant columns to the appropriate data types
    df['id'] = df['id'].astype(str)
    df["book_title"] = df["book_title"].astype(str)
    df['customer_id'] = df['customer_id'].astype(str)
    df['checkout_date'] = pd.to_datetime(df['checkout_date'], errors='coerce', dayfirst=False)
    df['return_date'] = pd.to_datetime(df['return_date'], errors='coerce', dayfirst=False)
    
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


def calculate_borrow_time(return_date,checkout_date):
   
        # Calculate the difference in days
        borrow_time = (return_date - checkout_date).days
        return borrow_time



def process_library_data(file_path):

    # Load and clean the data
    df = load_and_clean_data(file_path)
    
    # Standardize the book titles
    df["book_title"] = df["book_title"].apply(standardize_book_title)
    
    # Calculate borrow time for each row
    df['borrow_time'] = df.apply(calculate_borrow_time, axis=1)
    
    return df


if __name__ == "__main__":
    file = "03_Library Systembook.csv"
    
    # Process the library data
    processed_data = process_library_data(file)
    
    # Print the processed data to check the output
    print(processed_data.head())
