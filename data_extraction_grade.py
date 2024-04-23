import pandas as pd

# Read the Excel file
excel_file = "Dataset/Dataset1(7 sheets).xlsx"
xls = pd.ExcelFile(excel_file)

# Dictionary to store data frames for each sheet
sheet_dict = {}

# Loop through each sheet and extract required columns
for sheet_name in xls.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Remove rows where any cell contains "Weight", "Total", or "Sr.#"
    df = df[~df.apply(lambda row: any(row.isin(['Weight', 'Total', 'Sr.#'])), axis=1)]

    # Select required columns
    df = df[['Grade']]

    sheet_dict[sheet_name] = df

# Write the extracted data to a new CSV file
output_csv = "Extracted/grade.csv"
with open(output_csv, 'w', newline='') as csvfile:
    header_written = False
    for sheet_name, df in sheet_dict.items():
        if not header_written:
            df.to_csv(csvfile, mode='a', index=False, header=True)
            header_written = True
        else:
            df.to_csv(csvfile, mode='a', index=False, header=False)
