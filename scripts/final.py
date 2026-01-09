import pandas as pd


def load_and_clean_books(file_path: str) -> pd.DataFrame:
    print("\n--- Cleaning BOOKS dataset ---")

    df = pd.read_csv(file_path)
    rows_loaded = len(df)

    # Blank rows (all columns empty)
    blank_rows = df.isna().all(axis=1).sum()
    df = df.dropna(how="all")

    # Rename columns
    df = df.rename(
        columns={
            "Id": "id",
            "Books": "book_title",
            "Book checkout": "checkout_date",
            "Book Returned": "return_date",
            "Days allowed to borrow": "time_allowed_to_borrow",
            "Customer ID": "customer_id",
        }
    )

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()
    df = df.drop_duplicates().reset_index(drop=True)

    # Clean date strings (remove quotes, whitespace)
    for col in ["checkout_date", "return_date"]:
        df[col] = (
            df[col]
            .astype("string")
            .str.replace('"', "", regex=False)
            .str.strip()
        )

    # Convert to strings & trim
    df["id"] = df["id"].astype("string").str.strip()
    df["book_title"] = df["book_title"].astype("string").str.strip()
    df["customer_id"] = df["customer_id"].astype("string").str.strip()

    # Parse dates (UK format)
    df["checkout_date"] = pd.to_datetime(df["checkout_date"], errors="coerce", dayfirst=True)
    df["return_date"] = pd.to_datetime(df["return_date"], errors="coerce", dayfirst=True)

    # Extra metrics
    missing_customer_ids = df["customer_id"].isna().sum()
    invalid_checkout_dates = df["checkout_date"].isna().sum()
    invalid_return_dates = df["return_date"].isna().sum()

    # Borrow time + overdue (> 14 days)
    df["borrowed_days"] = (df["return_date"] - df["checkout_date"]).dt.days
    books_due_over_2_weeks = (df["borrowed_days"] > 14).sum()

    # Print metrics
    print(f"Rows loaded: {rows_loaded}")
    print(f"Blank rows removed: {blank_rows}")
    print(f"Duplicate rows removed: {duplicate_rows}")
    print(f"Missing customer IDs: {missing_customer_ids}")
    print(f"Invalid checkout dates: {invalid_checkout_dates}")
    print(f"Invalid return dates: {invalid_return_dates}")
    print(f"Books due (> 14 days borrowed): {books_due_over_2_weeks}")
    print(f"Rows after cleaning: {len(df)}")

    return df
def load_and_clean_customers(file_path: str) -> pd.DataFrame:
    print("\n--- Cleaning CUSTOMERS dataset ---")

    df = pd.read_csv(file_path)
    rows_loaded = len(df)

    blank_rows = df.isna().all(axis=1).sum()
    df = df.dropna(how="all")

    df = df.rename(columns={"Customer ID": "customer_id", "Customer Name": "customer_name"})

    duplicate_rows = df.duplicated().sum()
    df = df.drop_duplicates().reset_index(drop=True)

    df["customer_id"] = df["customer_id"].astype("string").str.strip()
    df["customer_name"] = df["customer_name"].astype("string").str.strip()

    missing_customer_ids = df["customer_id"].isna().sum()

    print(f"Rows loaded: {rows_loaded}")
    print(f"Blank rows removed: {blank_rows}")
    print(f"Duplicate rows removed: {duplicate_rows}")
    print(f"Missing customer IDs: {missing_customer_ids}")
    print(f"Rows after cleaning: {len(df)}")

    return df

if __name__ == "__main__":
    file_path = "03_Library Systembook.csv"
    customers_file = "03_Library SystemCustomers.csv"
    cleaned_customers = load_and_clean_customers(customers_file)
    cleaned_customers.to_csv("clean_library_customers.csv", index=False)

    cleaned_books = load_and_clean_books(file_path)
    cleaned_books.to_csv("clean_library_books.csv", index=False)

    print("\nSaved: clean_library_books.csv")
