import pandas as pd
import re
import os


def main():
    df = pd.read_csv("rosmap_batch2.csv")
    new_dict = {}
    for row in df.iterrows():
        row_data = row[1]  # Get the actual row data
        sample_name = re.split(".ba", row_data["file_name"])[0]
        # Get file extension more reliably
        file_type = os.path.splitext(row_data["file_name"])[1].lstrip('.')
        print(row_data["file_name"], sample_name, file_type)

        if sample_name not in new_dict:
            new_dict[sample_name] = {"mapped": "", "index": ""}
        if file_type == "bam":
            new_dict[sample_name]["mapped"] = f'syn://{row_data["syn_id"]}'
        elif file_type == "bai":
            new_dict[sample_name]["index"] = f'syn://{row_data["syn_id"]}'
        else:
            raise ValueError(f"File type {file_type} is not valid for {sample_name}")


    # Convert dictionary to DataFrame
    samples_df = pd.DataFrame.from_dict(new_dict, orient='index').reset_index()
    samples_df.columns = ['sample_id', 'mapped', 'index']
    
    # Add strandedness column with 'auto' values
    samples_df['file_type'] = 'bam'

    samples_df.to_csv("syn21188662_rosmap_batch2_samplesheet.csv", index=False)


if __name__ == "__main__":
    main()