#!/usr/bin/env python3

import sys
import pandas as pd
import glob
import os

if len(sys.argv) != 3:
    exit("Usage: concat_tables.py <dir> <out>")


files = glob.glob(f"{sys.argv[1]}/*.tsv")
dfs = []
for file in files:
    sample = os.path.basename(file).split(".tsv")[0]
    df = pd.read_csv(file, sep="\t")
    df["sample"] = [sample] * len(df)
    dfs.append(df)
dfs = pd.concat(dfs)

# drop non filtered mess and camisim read counts
index_drop = (
    dfs["sample"].str.contains("mess") & ~dfs["sample"].str.contains("filtered")
) | (dfs["sample"].str.contains("camisim") & ~dfs["sample"].str.contains("filtered"))

df = dfs[~index_drop]
mdf = pd.pivot_table(df, values="reads", columns="sample", index="taxon").fillna(0)
mdf = mdf.sort_values(by=list(mdf.columns), ascending=False).reset_index().astype(int)
mdf.to_csv(f"{sys.argv[2]}/otus.tsv", sep="\t", index=False)
mdf["taxon"].drop_duplicates().to_csv(
    f"{sys.argv[2]}/uniq_taxids.tsv", sep="\t", header=False, index=False
)
