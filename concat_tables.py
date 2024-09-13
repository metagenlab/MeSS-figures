#!/usr/bin/env python3

import sys
import pandas as pd
import glob
import os

if len(sys.argv) != 2:
    exit("Usage: concat_tables.py <dir>")


files = glob.glob(f"{sys.argv[1]}/*.tsv")
dfs = []
for file in files:
    sample = os.path.splitext(os.path.basename(file))[0]
    df = pd.read_csv(file, sep="\t")
    df["sample"] = [sample] * len(df)
    dfs.append(df)
dfs = pd.concat(dfs)

