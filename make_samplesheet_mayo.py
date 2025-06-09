import pandas as pd

def process_mayo_data(file_path):
    # Read the text file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Initialize lists to store data
    sample_ids = []
    mapped_ids = []
    index_ids = []
    
    # Process the file line by line
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.endswith('.bam'):
            # Extract sample ID (everything before .bam)
            sample_id = line[:-4]
            
            # Get the mapped ID (Synapse ID for .bam file)
            mapped_id = None
            for j in range(i, min(i+4, len(lines))):
                if lines[j].strip().startswith('syn'):
                    mapped_id = lines[j].strip()
                    break
            
            # Get the index ID (Synapse ID for .bai file)
            index_id = None
            for j in range(i+4, min(i+8, len(lines))):
                if lines[j].strip().startswith('syn'):
                    index_id = lines[j].strip()
                    break
            
            if mapped_id and index_id:
                # Add to lists
                sample_ids.append(sample_id)
                mapped_ids.append(mapped_id)
                index_ids.append(index_id)
            
            # Move to next entry
            i += 8
        else:
            i += 1
    
    # Create DataFrame
    df = pd.DataFrame({
        'sample_id': sample_ids,
        'mapped': mapped_ids,
        'index': index_ids,
        'file_type': ['bam'] * len(sample_ids)
    })
    
    return df

def main():
    # Process the data
    df = process_mayo_data('sequenced_at_Mayo.txt')
    
    # Save to CSV
    df.to_csv('sequenced_at_mayo_sample_file.csv', index=False)
    print(f"Created samplesheet with {len(df)} entries")

if __name__ == "__main__":
    main()