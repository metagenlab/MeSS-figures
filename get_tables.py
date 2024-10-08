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
mdf = pd.pivot_table(df, values="reads", columns="sample", index="taxon").reset_index().fillna(0)
mdf.apply(lambda col: sorted(col, reverse=True), axis=0).to_csv("data/otus.tsv", sep="\t",index=False)
mdf["taxon"].drop_duplicates().to_csv("data/uniq_taxids.tsv", sep="\t", header=False, index=False)