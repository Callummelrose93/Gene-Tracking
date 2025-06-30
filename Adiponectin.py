# The 3 genes realted to Adiponectin are:
# 1. ADIPOQ - rs1501299
# 2. ADIPOR1 - rs2241766
# 3. ADIPOR2 - rs17300539
# The following code will extract the data from the 1000 Genomes Project and create a dataframe with the relevant information.  

import pandas as pd
import numpy as np
import os
import gzip
import shutil

import json
import time

import urllib.parse
import urllib.request
import urllib.error



def download_file(url, filename):
    """
    Download a file from a URL and save it to a local file.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while downloading {filename}: {e}")


def extract_gzip(gzip_file, output_file):
    """
    Extract a gzip file to a specified output file.
    """
    try:
        with gzip.open(gzip_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Extracted {gzip_file} to {output_file}")
    except Exception as e:
        print(f"Error extracting {gzip_file}: {e}")


def get_1000_genomes_data():
    """
    Download and extract the 1000 Genomes Project data for the specified genes.
    """
    # Define the URLs for the 1000 Genomes Project data
    urls = {
        "ADIPOQ": "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/GRCh37_positions/ADIPOQ.vcf.gz",
        "ADIPOR1": "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/GRCh37_positions/ADIPOR1.vcf.gz",
        "ADIPOR2": "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/GRCh37_positions/ADIPOR2.vcf.gz"
    }

    # Create a directory to store the downloaded files
    os.makedirs("1000_genomes_data", exist_ok=True)

    # Download and extract each file
    for gene, url in urls.items():
        filename = os.path.join("1000_genomes_data", f"{gene}.vcf.gz")
        output_file = os.path.join("1000_genomes_data", f"{gene}.vcf")
        download_file(url, filename)
        extract_gzip(filename, output_file)
        # Remove the gzip file after extraction
        os.remove(filename)

