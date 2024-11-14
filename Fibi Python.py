def extract_gene_stable_ids(input_file, output_file):
    with open(input_file, 'r') as infile:
        gene_ids = []

        # Read the first line to skip the header
        header = infile.readline()  # Read and ignore the header line

        # Iterate through each line of the file
        for line in infile:
            # Split each line by the comma delimiter
            parts = line.strip().split(',')
            if parts:  # Check if there are parts after splitting
                gene_ids.append(parts[0])  # Append only the Gene stable ID (first part)

    # Write the Gene stable IDs to the output file
    with open(output_file, 'w') as outfile:
        for gene_id in gene_ids:
            outfile.write(gene_id + '\n')

def main():
    # Update the input and output file paths
    input_file = r'C:\Users\agujo\Downloads\mart_export.txt'  # Path to your input file
    output_file = r'C:\Users\agujo\Downloads\gene_stable_ids.txt'  # Desired output file for Gene stable IDs

    extract_gene_stable_ids(input_file, output_file)
    print(f"Extracted Gene stable IDs saved to {output_file}")


if __name__ == "__main__":
    main()
