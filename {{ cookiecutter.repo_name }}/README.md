# {{cookiecutter.project_name}}

{{cookiecutter.description}}

> STEP 1: add the `.env` file to `.gitignore` to avoid committing secrets to the repo

## Reports

- EDA and technical report should be saved in the reports folder using one of the following formats: `HTML` or `PDF`

## Project Organization

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
