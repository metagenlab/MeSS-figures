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
