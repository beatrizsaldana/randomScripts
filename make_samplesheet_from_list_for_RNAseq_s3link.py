import pandas as pd
import re


def main():
    df = pd.read_csv("syn4164376_rosmap_batch1_samplesheet_syn.csv")
    s3_url = "s3://diverse-cohorts-project-tower-scratch/RNAseq_sample_exchanges/bamtofastq_results/rosmap_batch1/reads/"
    new_dict = {}
    for row in df.iterrows():
        row_data = row[1]  # Get the actual row data
        sample_id = row_data["sample_id"]
        new_dict[sample_id] = {"fastq_1": f"{s3_url}{sample_id}_1.merged.fastq.gz", "fastq_2": f"{s3_url}{sample_id}_2.merged.fastq.gz"}

    # Convert dictionary to DataFrame
    samples_df = pd.DataFrame.from_dict(new_dict, orient='index').reset_index()
    samples_df.columns = ['sample', 'fastq_1', 'fastq_2']
    
    # Add strandedness column with 'auto' values
    samples_df['strandedness'] = 'auto'

    samples_df.to_csv("rosmap_batch1_rnaseq_samplesheet.csv", index=False)


if __name__ == "__main__":
    main()