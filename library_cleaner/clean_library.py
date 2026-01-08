import argparse
import pandas as pd
from datetime import datetime

def load_and_clean_data(file):

    # Load the CSV file
    df = pd.read_csv(file)
    
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

def main():
    parser =argparse.ArgumentParser(description="Clean library data CSV")
    parser.add_argument("--input", default= "03_Library Systembook.csv", help = "Input CSV path")
    parser.add_argument("--output", default= "clean_library_data.csv", help = "Output CSV path")
    args = parser.parse_args()

    processed_data  = process_library_data(args.input)
    processed_data.to_csv(args.output, index = False)
    print(f"Cleaned data: {args.output}")


if __name__ == "__main__":
    main()
    
