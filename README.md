# Cookiecutter Data Science in Snowflake

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work in Snowflake._

## [Project homepage](https://bitbucket.org/mvfglobal/mvfdata-cc-dsml-template/src/main/)

### Requirements to use the cookiecutter template:

- Python 3.9 or 3.10
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

```bash
pip install cookiecutter
```

or

```bash
conda config --add channels conda-forge
conda install cookiecutter
```

### To start a new project, run:

- Clone this repo
- Move to the Athena project
- Run:

```bash
cookiecutter -c v1 path/to_folder/mvfdata-cc-dsml-template
```

1. Follow the prompts (choose Auth0 as method to connect to SF)
2. `cd` into the new project folder created.
3. add `.env` to `.gitignore` and commit the change
4. Run `make create_environment`
5. Activate your new conda environment
6. Run `make requirements`
7. Go to `.env` and update the file with your snowflake credentials

### Add a new package

> Note: make sure you're using your project conda environment

1. Add new required package to environment.yml
1. Run step 6 again.

### New version of Cookiecutter Data Science

---

Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.

### The resulting directory structure

---

The directory structure of your new project looks like this:

```bash
├── Makefile                            <- Makefile with commands like `make create_environment` or `make requirements`
├── README.md                           <- The top-level README for developers using this project.
├── docs                                <- A default Sphinx project; see sphinx-doc.org for details
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── environment.yml
├── models                              <- Trained and serialized models, model predictions, or model summaries
├── notebooks                           <- Jupyter notebooks. Naming convention is a number (for ordering),
│   │                                      the creator's initials, and a short `-` delimited description, e.g.
│   │                                      `1.0-jqp-initial-data-exploration`.
│   ├── data                            <- sample data for pandas cheatsheet notebook
│   │   └── credit_risk.csv
│   ├── pandas_cheatsheet.ipynb         <- notebook with common pandas operations
│   └── starter_template.ipynb          <- template for creating snowflake ready connected notebooks
├── reports                             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── commercial_report_template.md
│   ├── figures                         <- Generated graphics and figures to be used in reporting
│   └── technical_report_template.md
└── src                                 <- Source code for use in this project.
    ├── __init__.py                     <- Makes src a Python module
    ├── common
    │   ├── __init__.py
    │   └── snowflake_connector.py
    ├── data
    │   ├── __init__.py
    │   └── make_dataset.py             <- Scripts to generate/reference data in snowflake
    ├── features
    │   ├── __init__.py
    │   └── build_features.py           <- Scripts to turn raw data into features for modeling
    └── models                          <- Scripts to train models and then use trained models to make predictions
        ├── __init__.py
        ├── predict_model.py
        └── train_model.py
```
