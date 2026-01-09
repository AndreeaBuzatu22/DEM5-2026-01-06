import pandas as pd
from datetime import datetime


def load_and_clean_books(file_path: str):
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

    # Metrics: missing / invalid
    missing_customer_ids = df["customer_id"].isna().sum()
    invalid_checkout_dates = df["checkout_date"].isna().sum()
    invalid_return_dates = df["return_date"].isna().sum()

    # Borrow time + overdue (> 14 days)
    df["borrowed_days"] = (df["return_date"] - df["checkout_date"]).dt.days
    books_due_over_2_weeks = (df["borrowed_days"] > 14).sum()

    # More useful simple metrics (distribution + on time vs overdue)
    avg_borrowed_days = df["borrowed_days"].mean(skipna=True)
    median_borrowed_days = df["borrowed_days"].median(skipna=True)

    on_time_count = (df["borrowed_days"].notna() & (df["borrowed_days"] <= 14)).sum()
    overdue_count = (df["borrowed_days"].notna() & (df["borrowed_days"] > 14)).sum()
    returned_with_dates = df["borrowed_days"].notna().sum()
    overdue_rate = (overdue_count / returned_with_dates) if returned_with_dates > 0 else 0

    # Print metrics
    print(f"Rows loaded: {rows_loaded}")
    print(f"Blank rows removed: {blank_rows}")
    print(f"Duplicate rows removed: {duplicate_rows}")
    print(f"Missing customer IDs: {missing_customer_ids}")
    print(f"Invalid checkout dates: {invalid_checkout_dates}")
    print(f"Invalid return dates: {invalid_return_dates}")
    print(f"Books due (> 14 days borrowed): {books_due_over_2_weeks}")
    print(f"Avg borrowed days: {avg_borrowed_days}")
    print(f"Median borrowed days: {median_borrowed_days}")
    print(f"On time returns (<=14d): {on_time_count}")
    print(f"Overdue returns (>14d): {overdue_count}")
    print(f"Overdue rate: {overdue_rate:.2%}")
    print(f"Rows after cleaning: {len(df)}")

    metrics = {
        "run_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset": "books",
        "rows_loaded": int(rows_loaded),
        "blank_rows_removed": int(blank_rows),
        "duplicate_rows_removed": int(duplicate_rows),
        "rows_after_cleaning": int(len(df)),
        "missing_customer_ids": int(missing_customer_ids),
        "invalid_checkout_dates": int(invalid_checkout_dates),
        "invalid_return_dates": int(invalid_return_dates),
        "books_due_over_2_weeks": int(books_due_over_2_weeks),
        "avg_borrowed_days": float(avg_borrowed_days) if pd.notna(avg_borrowed_days) else None,
        "median_borrowed_days": float(median_borrowed_days) if pd.notna(median_borrowed_days) else None,
        "on_time_returns": int(on_time_count),
        "overdue_returns": int(overdue_count),
        "overdue_rate": float(overdue_rate),
    }

    return df, metrics


def load_and_clean_customers(file_path: str):
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

    metrics = {
        "run_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset": "customers",
        "rows_loaded": int(rows_loaded),
        "blank_rows_removed": int(blank_rows),
        "duplicate_rows_removed": int(duplicate_rows),
        "rows_after_cleaning": int(len(df)),
        "missing_customer_ids": int(missing_customer_ids),
    }

    return df, metrics


if __name__ == "__main__":
    books_file = "03_Library Systembook.csv"
    customers_file = "03_Library SystemCustomers.csv"

    # Clean customers
    cleaned_customers, customers_metrics = load_and_clean_customers(customers_file)
    cleaned_customers.to_csv("clean_library_customers.csv", index=False)

    # Clean books
    cleaned_books, books_metrics = load_and_clean_books(books_file)
    cleaned_books.to_csv("clean_library_books.csv", index=False)

    # Save metrics as a single CSV (2 rows: books + customers)
    metrics_df = pd.DataFrame([books_metrics, customers_metrics])
    metrics_df.to_csv("data_quality_metrics.csv", index=False)

    print("\nSaved: clean_library_books.csv")
    print("Saved: clean_library_customers.csv")
    print("Saved: data_quality_metrics.csv")
