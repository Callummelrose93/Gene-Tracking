import numpy as np
import pandas as pd
import os

class DataTracking:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data_files = []
        self.data_dict = {}
        self.load_data()

    def load_data(self):
        """Load all data files from the specified directory."""
        for file in os.listdir(self.data_dir):
            if file.endswith('.csv'):
                file_path = os.path.join(self.data_dir, file)
                self.data_files.append(file_path)
                self.data_dict[file] = pd.read_csv(file_path)

    def get_data_summary(self):
        """Return a summary of the loaded data files."""
        summary = {}
        for file, df in self.data_dict.items():
            summary[file] = {
                'shape': df.shape,
                'columns': df.columns.tolist(),
                'head': df.head().to_dict(orient='records')
            }
        return summary

#     # Download and extract the data files
#     for gene, url in urls.items():
#         file_name = os.path.join("1000_genomes_data", f"{gene}.vcf.gz")