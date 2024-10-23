# MeSS-figures

Supplemental code for reproducing MeSS paper figures

## Dependencies

### Install conda

You need a conda ([Miniforge](https://github.com/conda-forge/miniforge)) install to run the notebooks:

```sh
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

### Create conda env

```sh
mamba env create -n notebooks -f env.yaml
```

## Run jupyter lab

```sh
mamba activate notebooks
jupyter lab
```

## Figures

### Diversities

Use [`3_plot_diversities.ipynb`](3_plot_diversities.ipynb) to generate the figures below

#### Figure 1A
<p align="center">
<img src="figures/species-jaccard-NMDS.png" width=55% height=55%>
</p>

#### Figure 1B
<p align="center">
<img src="figures/species-bray-NMDS.png" width=55% height=55%>
</p>

#### Figure S1
<p align="center">
<img src="figures/alpha-divs.png" width=55% height=55%>
</p>

### Benchmark

Use [`4_plot_resource_usage.ipynb`](4_plot_resource_usage.ipynb) to generate the figures below

#### Figure S2
<p align="center">
<img src="figures/cpu-time.png" width=80% height=80%>
</p>

#### Figure S3
<p align="center">
<img src="figures/ram-usage.png" width=80% height=80%>
</p>