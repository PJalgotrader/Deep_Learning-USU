"""Check that your local PyCaret environment for the Deep Learning course works.

Run from the repository root. With uv:

    uv run python scripts/check_environment.py

With conda:

    conda activate dl_pycaret
    python scripts/check_environment.py

It checks the Python version, imports the key packages, then runs one tiny classification
experiment and one tiny time series experiment. It takes about a minute.
"""
import importlib
import sys
import warnings

warnings.filterwarnings("ignore")
problems = []


def step(title):
    print(f"\n--- {title}")


def fail(message):
    problems.append(message)
    print(f"  [FAIL] {message}")


step("Python")
print(f"  {sys.version.split()[0]}  ({sys.executable})")
if sys.version_info[:2] != (3, 13):
    fail("Expected Python 3.13. Run `uv sync` at the repository root and use `uv run`, "
         "or create the conda environment from environment.yml and activate it.")

step("Packages")
for name in ["pycaret", "numpy", "pandas", "sklearn", "scipy", "statsmodels", "sktime",
             "matplotlib", "lightgbm", "xgboost", "catboost", "shap"]:
    try:
        module = importlib.import_module(name)
        print(f"  {name:<12} {getattr(module, '__version__', '?')}")
    except Exception as e:
        fail(f"cannot import {name}: {type(e).__name__}: {e}")

if "pycaret" in sys.modules and not sys.modules["pycaret"].__version__.startswith("3.5"):
    fail("Expected PyCaret 3.5.x from the pycaret-core package. "
         "Run: pip uninstall -y pycaret  then  pip install pycaret-core==3.5.0")

if "statsmodels" in sys.modules:
    major, minor = (int(x) for x in sys.modules["statsmodels"].__version__.split(".")[:2])
    if (major, minor) >= (0, 15):
        fail('statsmodels 0.15+ breaks the ETS forecaster. Run: pip install "statsmodels<0.15"')

if not problems:
    step("Classification experiment (Module 3 and the PyCaret demos)")
    try:
        from pycaret.classification import ClassificationExperiment
        from pycaret.datasets import get_data

        data = get_data("juice", verbose=False)
        exp = ClassificationExperiment()
        exp.setup(data, target="Purchase", session_id=123, fold=3, verbose=False)
        available = set(exp.models().index)
        for booster in ["lightgbm", "xgboost", "catboost"]:
            if booster not in available:
                fail(f"{booster} is missing from models()")
        exp.create_model("lr", verbose=False)
        print("  setup, models and create_model('lr') work")
    except Exception as e:
        fail(f"classification experiment: {type(e).__name__}: {e}")

    step("Time series experiment (the forecasting notebooks)")
    try:
        from pycaret.datasets import get_data
        from pycaret.time_series import TSForecastingExperiment

        y = get_data("airline", verbose=False)
        ts = TSForecastingExperiment()
        ts.setup(y, fh=12, fold=2, session_id=123, verbose=False)
        available = set(ts.models().index)
        for booster in ["lightgbm_cds_dt", "xgboost_cds_dt", "catboost_cds_dt"]:
            if booster not in available:
                fail(f"{booster} is missing from models()")
        # ETS is the model that breaks when statsmodels 0.15 sneaks in
        ets = ts.create_model("ets", verbose=False)
        ts.predict_model(ets, verbose=False)
        print("  setup, models, create_model('ets') and predict_model work")
    except Exception as e:
        fail(f"time series experiment: {type(e).__name__}: {e}")

print()
if problems:
    print(f"{len(problems)} problem(s) found:")
    for message in problems:
        print(f"  - {message}")
    sys.exit(1)
print("Your course environment is ready.")
