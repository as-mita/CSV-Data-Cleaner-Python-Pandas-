import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows with null values
    df = df.dropna()

    # Convert column types if needed
    for col in df.columns:
        try:
            df[col] = df[col].astype(float)
        except:
            pass

    df.to_csv(output_file, index=False)
    print("Data cleaned and saved successfully.")

if __name__ == "__main__":
    clean_csv("raw_data.csv", "cleaned_data.csv")
