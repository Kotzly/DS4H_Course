import pandas as pd
from simpledbf import Dbf5
from pathlib import Path
import argparse

def dbf_to_csv(input_filepath, output_filepath):
    Dbf5(input_filepath)\
        .to_csv(output_filepath)

def process_dbfs(input_folder, output_folder):
    for filepath in input_folder.glob("*.dbf"):
        print("Processing", filepath)
        output_folder.mkdir(exist_ok=True, parents=True)
        save_filepath = output_folder / filepath.name.replace("dbf", "csv")
        dbf_to_csv(
            filepath,
            save_filepath
        )

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="DBF")
    parser.add_argument('input_folder', type=str, help="Input folder")
    parser.add_argument('output_folder', type=str, help="Output folder")
    args = parser.parse_args()

    input_folder = Path(args.input_folder)
    output_folder = Path(args.output_folder)

    process_dbfs(
        input_folder=input_folder,
        output_folder=output_folder
    )
