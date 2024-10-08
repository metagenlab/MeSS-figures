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
Use `3_plot_diversities.ipynb` to generate the figures below

#### Figure 1A

![fig1a](figures/species-jaccard-NMDS.png)

#### Figure 1B

![fig1b](figures/species-bray-NMDS.png)

#### Figure S1

![figs1](figures/alpha-divs.png)

### Benchmark

Use `4_plot_resource_usage.ipynb` to generate the figures below

#### Figure S2

![figs2](figures/cpu-time.png)

#### Figure S3

![figs3](figures/ram-usage.png)