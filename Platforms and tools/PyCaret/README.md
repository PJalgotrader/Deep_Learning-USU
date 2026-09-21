Here is the link to my YouTube playlist for PyCaret! https://youtube.com/playlist?list=PL2GWo47BFyUOqCAj_16yeNspfeM0nfA6q

**Topics**: 
1. PyCaret introduction
2. PyCaret regression
3. PyCaret classification
4. PyCaret timeseries

## PyCaret setup

We use **PyCaret 3.5.0 from the `pycaret-core` package**. The original `pycaret` package stopped at 3.3.2, which only supports Python 3.9 to 3.11, so `pip install pycaret` fails on Google Colab and on any current Python. `pycaret-core` is the maintained continuation of PyCaret 3: same `import pycaret`, same functions, and it runs on Python 3.13.

These are the notebooks in this course that use PyCaret. The same setup works for all of them:

| Notebook | PyCaret module |
| --- | --- |
| [Module 3- ML PyCaret-Classification](../../Lectures%20and%20codes/Module%203-%20Machine%20Learning%20Review/Module%203-%20ML%20PyCaret-Classification.ipynb) | classification |
| [Predictiong_stock_returns_PyCaret](../../Lectures%20and%20codes/Module%206-%20Deep%20Sequence%20Modeling/python/univariate_ts/Predictiong_stock_returns_PyCaret.ipynb) (Module 6) | time series |
| [PyCaret-ClassificationDemo](./PyCaret-ClassificationDemo.ipynb) | classification |
| [PyCaret-RegressionDemo](./PyCaret-RegressionDemo.ipynb) | regression |
| [PyCaret-timeseries](./PyCaret-timeseries.ipynb) | time series |
| [Predictiong_stock_price_PyCaret](./Predictiong_stock_price_PyCaret.ipynb) | time series |

### Option 1: Google Colab (nothing to install on your computer)

Open the notebook with its "Open in Colab" badge and run it from the top. The first code cell detects Colab and installs what the notebook needs. Run that cell **first, in a fresh runtime**, before importing PyCaret. No runtime restart is needed afterwards.

### Option 2: your own machine, with uv (recommended)

[uv](https://docs.astral.sh/uv/) downloads Python 3.13 and installs the exact package versions locked in the repository's `uv.lock`, inside a `.venv` folder in the repo. New to uv? Read [`Platforms and tools/uv/`](../uv/) first (quick start, conda-to-uv cheat sheet, ten-second test). From the root of your cloned copy of this repo:

```bash
uv sync
```

```bash
uv run python scripts/check_environment.py
```

```bash
uv run jupyter lab
```

For VS Code, register the environment once as a named kernel and pick it under **Select Kernel** ▸ **Jupyter Kernel**:

```bash
uv run python -m ipykernel install --user --name deep-learning --display-name "Python 3.13 (Deep Learning)"
```

### Option 3: your own machine, with conda

You need [Miniconda](https://docs.anaconda.com/miniconda/) or Anaconda. From the root of your cloned copy of this repo:

```bash
conda env create -f environment.yml
```

```bash
conda activate dl_pycaret
```

```bash
python scripts/check_environment.py
```

The check script prints your package versions, runs one tiny classification experiment and one tiny time series experiment, and should end with `Your course environment is ready.`

Then open the notebook:

- **JupyterLab:** run `jupyter lab` with `dl_pycaret` activated.
- **VS Code:** open the notebook, click **Select Kernel** ▸ **Python Environments** ▸ `dl_pycaret`.

The install cell at the top of each notebook does nothing on your own machine, so you can simply Run All.

Both local options use **Python 3.13** on purpose. It matches Colab, and on Python 3.12 or older `pycaret-core` falls back to old versions of numpy, pandas and scikit-learn that clash with PyTorch and TensorFlow. [`pyproject.toml`](../../pyproject.toml) (uv) and [`environment.yml`](../../environment.yml) (conda) list the same packages; uv additionally pins every version in `uv.lock`.

To remove the environment later: delete the `.venv` folder (uv) or run `conda env remove -n dl_pycaret` (conda).

### Troubleshooting

| Symptom | Fix |
| --- | --- |
| `RuntimeError: Pycaret only supports python 3.9, 3.10, 3.11 ... Please DOWNGRADE` | You installed the old `pycaret` package. Run `pip uninstall -y pycaret`, then `pip install pycaret-core==3.5.0`. |
| pip tries to build numpy from source and fails | Same cause: `pip install pycaret` on Python 3.13. Install `pycaret-core` instead. |
| `ValueError: Estimator catboost_cds_dt Not Available` (or `xgboost`, `lightgbm`, `catboost`) | The library was installed after PyCaret had already been imported. On Colab: Runtime ▸ Disconnect and delete runtime, then run from the top. Locally: restart the kernel. |
| `ETSResults.simulate() got an unexpected keyword argument 'random_state'`, or `ets` missing from `compare_models()` | statsmodels 0.15 is installed. Run `pip install "statsmodels<0.15"` and restart the kernel. |
| The version cell does not show `3.5.0`, or the notebook cannot find `pycaret` | The notebook is running on the wrong kernel. Select `Python 3.13 (Deep Learning)` (uv) or `dl_pycaret` (conda) and run `import sys; print(sys.executable)` to confirm. |
| `DLL load failed` on Windows inside a uv environment | The environment was built on top of Anaconda's Python. Delete the `.venv` folder and run `uv sync` again. This repository tells uv to use its own Python. |
| All models score like a coin flip after `setup()` with preprocessing | A PyCaret 3.5.0 bug with pandas ≥ 2.2. Keep `data_split_shuffle=False` as explained inside the classification and regression notebooks. |

## 🔗 Links

[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedram-jahangiry-cfa-5778015a)

[![Youtube](https://img.shields.io/badge/youtube_channel-1DA1F2?style=for-the-badge&logo=youtube&logoColor=white&color=FF0000)](https://www.youtube.com/channel/UCNDElcuuyX-2pSatVBDpJJQ)

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/PedramJahangiry.svg?style=social&label=Follow%20%40PedramJahangiry)](https://twitter.com/PedramJahangiry)
