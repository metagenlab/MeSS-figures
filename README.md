# MeSS-figures

Supplemental code for reproducing MeSS paper figures

## Dependencies

### Install mamba

You need mamba to install jupyer notebooks dependencies:

```sh
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

### Create mamba env

```sh
mamba env create -n mess-notebook -f env.yaml
```

## Run jupyter lab

```sh
mamba activate mess-notebook
jupyter lab
```

## Figures

### Diversities

Use [`3_plot_diversities.ipynb`](3_plot_diversities.ipynb) to generate the figures below

#### Figure 1A

<img src="figures/species-jaccard-NMDS.png" width=55% height=55%>

#### Figure 1B

<img src="figures/species-bray-NMDS.png" width=55% height=55%>

#### Figure S1

<img src="figures/alpha-divs.png" width=55% height=55%>

### Benchmark

Use [`4_plot_resource_usage.ipynb`](4_plot_resource_usage.ipynb) to generate the figures below

#### Figure S2

<img src="figures/cpu-time.png" width=80% height=80%>

#### Figure S3

<img src="figures/ram-usage.png" width=80% height=80%>
