![Deep Learning course cover](https://user-images.githubusercontent.com/19335954/210499958-e1230059-4b9c-4ea4-a5af-9901bd02ba18.png)

# DATA 5610-6610: Deep Learning — Fall 2026

Public course repository for **DATA 5610-6610: Deep Learning**, owned and maintained by Professor Pedram Jahangiry at Utah State University.

Fall 2026 covers **Modules 1–7**. Modules 8 and 9 are not taught this semester.

## Getting started

1. Create a GitHub account and install GitHub Desktop, or use Git from the command line.
2. Clone this repository:

   ```bash
   git clone https://github.com/PJalgotrader/Deep_Learning-USU.git
   ```

3. Find the lecture slides and course notebooks in [`Lectures and codes/`](./Lectures%20and%20codes/).
4. Pull regularly so your local copy stays current:

   ```bash
   git pull
   ```

See the [Fall 2026 course schedule](https://docs.google.com/spreadsheets/d/1qzFDl0lkPwIBZ52VgE3VbEL4Scet9OGJW2DVeQLQOrA/edit?gid=416110313#gid=416110313) for the detailed sequence of topics and assignments.

## Repository map

| Path | Contents |
| --- | --- |
| [`Lectures and codes/`](./Lectures%20and%20codes/) | Module slides, notebooks, papers, and supporting examples |
| [`Platforms and tools/`](./Platforms%20and%20tools/) | Google Colab, PyCaret, uv (student quick start, cheat sheet, ten-second test) and development-tool resources |
| [`data/`](./data/) | Course datasets used by selected notebooks and examples |
| [`images/`](./images/) | Images used by this README and other repository materials |
| [`pyproject.toml`](./pyproject.toml) + [`uv.lock`](./uv.lock) | The local **uv** environment (Python 3.13) for the PyCaret and scikit-learn notebooks. `requirements.txt` is an export of the same versions |
| [`environment.yml`](./environment.yml) | The same environment for **conda** users (`dl_pycaret`) |
| [`scripts/`](./scripts/) | `check_environment.py`, which confirms that the local environment works |

## How to run the notebooks

**One rule:** if a notebook trains a neural network (Keras 3 / TensorFlow: Modules 4 to 7), run it on **Google Colab with a GPU** (Runtime > Change runtime type > GPU). Keras and TensorFlow are preinstalled there; nothing to set up. Everything else (Module 3, the Module 6 PyCaret forecasting notebook, and the demos in [`Platforms and tools/PyCaret/`](./Platforms%20and%20tools/PyCaret/)) runs on Colab **or** on your own computer, in one local environment that you build with **uv** (recommended) or **conda**. Same three options as the Machine Learning and Deep Forecasting courses, same commands.

| Notebooks | Where |
| --- | --- |
| Modules 4 to 7 (NN, CNN, RNN/LSTM, Transformers) | Google Colab, GPU runtime |
| Module 3 (ML review, scikit-learn + PyCaret) and the PyCaret demos | Colab, or your computer (uv or conda) |

The PyCaret notebooks use PyCaret 3.5.0 from the `pycaret-core` package (the old `pycaret` package does not run on Python 3.12 or newer, including Colab's). Their first cell installs it on Colab and does nothing on your own machine.

### Option 1: Google Colab (nothing to install)

Open the notebook with its Colab badge and run it from the top, in a fresh runtime (**Runtime > Disconnect and delete runtime** if you already imported PyCaret in that session).

### Option 2: your own computer with uv (recommended)

[uv](https://docs.astral.sh/uv/) downloads Python 3.13, creates a `.venv` inside this repository and installs the exact versions recorded in `uv.lock`. It does not touch any Python or Anaconda you already have. New to uv? Start with [`Platforms and tools/uv/`](./Platforms%20and%20tools/uv/) (quick start, conda-to-uv cheat sheet, ten-second test).

1. Install uv ([instructions](https://docs.astral.sh/uv/getting-started/installation/)), then reopen the terminal and check `uv --version`.

   Windows (PowerShell):
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   macOS / Linux:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Clone into a normal local folder (not inside Google Drive or OneDrive) and build the environment:
   ```bash
   git clone https://github.com/PJalgotrader/Deep_Learning-USU.git
   cd Deep_Learning-USU
   uv sync
   ```
3. Check it:
   ```bash
   uv run python scripts/check_environment.py
   ```
   The last line must be `Your course environment is ready.`
4. Start Jupyter:
   ```bash
   uv run jupyter lab
   ```

**VS Code:** register the environment once as a Jupyter kernel, then pick it with **Select Kernel > Jupyter Kernel > Python 3.13 (Deep Learning)**:

```bash
uv run python -m ipykernel install --user --name deep-learning --display-name "Python 3.13 (Deep Learning)"
```

### Option 3: your own computer with conda

```bash
git clone https://github.com/PJalgotrader/Deep_Learning-USU.git
cd Deep_Learning-USU
conda env create -f environment.yml
conda activate dl_pycaret
python scripts/check_environment.py
jupyter lab
```

In VS Code, `dl_pycaret` shows up under **Select Kernel > Python Environments**.

The full guide and troubleshooting table are in the [PyCaret setup guide](./Platforms%20and%20tools/PyCaret/README.md).

## Fall 2026 course modules

| Module | Topic |
| --- | --- |
| 1 | Introduction to Deep Learning |
| 2 | Setting Up the Deep Learning Environment |
| 3 | Machine Learning Review: Fundamentals and Models |
| 4 | Deep Neural Networks: NN and DNN |
| 5 | Deep Computer Vision: CNN, R-CNN, YOLO, and FCN |
| 6 | Deep Sequence Modeling: RNN and LSTM |
| 7 | Transformers: Attention Is All You Need |

> **Fall 2026 scope:** Modules 8 and 9 are not part of this semester’s course delivery.

## Using this repository responsibly

- Course materials may be revised during the semester. Pull updates regularly and follow Canvas for official announcements, assignments, deadlines, and grades.
- Do not commit passwords, API keys, access tokens, student records, or other private information.
- Do not publish homework solutions, answer keys, or restricted team work unless the instructor explicitly permits it.
- Review notebook cells and outputs before committing or sharing them publicly.

## About the instructor

[Pedram Jahangiry, CFA](https://huntsman.usu.edu/directory/jahangiry-pedram) is a Professional Practice Assistant Professor of Data Analytics and Information Systems in the Jon M. Huntsman School of Business at Utah State University. Before joining the Huntsman School in 2018, he was a research associate in BlackRock’s Financial Modeling Group in New York. His teaching and applied research focus on machine learning, deep learning, and time-series forecasting.

Pedram is also a project mentor with the [Analytics Solutions Center](https://huntsman.usu.edu/asc/index), which provides experiential learning opportunities through analytics projects with organizational partners.

## Links

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedram-jahangiry-cfa-5778015a)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCNDElcuuyX-2pSatVBDpJJQ)
[![X](https://img.shields.io/twitter/url/https/twitter.com/PedramJahangiry.svg?style=social&label=Follow%20%40PedramJahangiry)](https://twitter.com/PedramJahangiry)

<img src="images/Jahangirylogo.png" width="150" align="right" alt="Pedram Jahangiry logo">
