import pandas as pd
import re


def main():
    df = pd.read_csv("rosmap_batch4.txt")
    new_dict = {}
    for row in df.iterrows():
        row_data = row[1]  # Get the actual row data
        sample_name = re.split("_R[0-9]_", row_data["file_name"])[0]
        read_match = re.search("_R([0-9])_", row_data["file_name"])
        read_number = read_match.group(1) if read_match else None
        if sample_name not in new_dict:
            new_dict[sample_name] = {"fastq_1": "", "fastq_2": ""}
        if read_number == "1":
            new_dict[sample_name]["fastq_1"] = f'syn://{row_data["syn_id"]}'
        elif read_number == "2":
            new_dict[sample_name]["fastq_2"] = f'syn://{row_data["syn_id"]}'
        else:
            raise ValueError(f"Read number {read_number} is not valid for {sample_name}")

    # Convert dictionary to DataFrame
    samples_df = pd.DataFrame.from_dict(new_dict, orient='index').reset_index()
    samples_df.columns = ['sample', 'fastq_1', 'fastq_2']
    
    # Add strandedness column with 'auto' values
    samples_df['strandedness'] = 'auto'

    samples_df.to_csv("syn24175555_rosmap_batch4_samplesheet.csv", index=False)


if __name__ == "__main__":
    main()