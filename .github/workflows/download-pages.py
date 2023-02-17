import gdown
import os
import argparse

# Create parser for CLI
parser = argparse.ArgumentParser()
parser.add_argument(
    '--url', type=str, default='https://drive.google.com/drive/folders/1nfG7TJ3_9_GK90xTEsjxrVMmzNO_dCQI')
parser.add_argument('--output', type=str, default='data/pages')

# Parse arguments:
args = parser.parse_args()

# Download the folder from `url`:
gdown.download_folder(args.url, args.output)
