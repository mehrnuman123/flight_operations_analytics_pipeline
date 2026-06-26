import pandas as pd
from pathlib import Path
from source_data import dataset_path


input_path=Path(dataset_path)
output_path=Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)


all_dfs=[]

count=0


# there are 8 csv files with 5.5 million rows ad 35 columns in datset

for file in input_path.glob("*.csv"):
    print("Processing:", file.name)

    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.lower()

    df.to_parquet(output_path / f"{file.stem}.parquet", index=False)

    del df


# below line breaking my remote wsl connection because my vm is getting out of memory, it crashed wsl
#final_df = pd.concat(all_dfs, ignore_index=True)



