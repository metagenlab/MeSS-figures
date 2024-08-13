#!/usr/bin/env python3

import sys
import pandas as pd

if len(sys.argv) != 4:
    exit("Usage: filter_bracken.py <threshold> <report> <output>")

nb = int(sys.argv[1])
df = pd.read_csv(sys.argv[2], sep="\t")
output = sys.argv[3]
subset_df = df[df.new_est_reads >= nb][["taxonomy_id", "new_est_reads"]]
subset_df["seq_abundance"] = [
    reads / subset_df.new_est_reads.sum() for reads in subset_df.new_est_reads
]
subset_df.sort_values("new_est_reads", ascending=False)
subset_df.columns = ["taxon", "reads", "seq_abundance"]
subset_df.to_csv(
    output,
    sep="\t",
    index=False,
)