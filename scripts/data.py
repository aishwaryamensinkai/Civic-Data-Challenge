import os
import pandas as pd  # type: ignore

def merge_csv_files(input_folder, output_file):
    # Check if the input directory exists
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"The directory '{input_folder}' does not exist.")

    data_frames = []
    for file in os.listdir(input_folder):
        if file.endswith('.csv'):
            file_path = os.path.join(input_folder, file)
            df = pd.read_csv(file_path)
            df.drop(columns=['X', 'Y', 'LAT', 'LONG', 'Attempt'], errors='ignore', inplace=True)
            data_frames.append(df)
    merged_df = pd.concat(data_frames, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f'Merged {len(data_frames)} CSV files into {output_file}')

input_folder = '../raw_data'  # Ensure this path is correct
output_file = '../data/Part1.csv'

try:
    merge_csv_files(input_folder, output_file)
except FileNotFoundError as e:
    print(e)
