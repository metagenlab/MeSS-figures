#!/usr/bin/env python3

import sys
import pandas as pd

if len(sys.argv) != 4:
    exit("Usage: filter_bracken.py <threshold> <report> <sample>")

nb = int(sys.argv[1])
df = pd.read_csv(sys.argv[2], sep="\t")
sample = sys.argv[3]
subset_df = df[["taxonomy_id", "new_est_reads"]]
subset_df.sort_values("new_est_reads", ascending=False, inplace=True)
subset_df.columns = ["taxon", "reads"]
subset_df.to_csv(
    f"{sample}.tsv",
    sep="\t",
    index=False,
)
subset_df[subset_df.reads >= nb].to_csv(f"{sample}_filtered.tsv", sep="\t", index=False)
