# RSP Accounting Bill Comparison

A Streamlit application for comparing accounting bills using CSV files.

## Setup

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
cd src
streamlit run app.py
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

- `src/`: Source code
  - `app.py`: Main Streamlit application
  - `utils/`: Utility functions
  - `pages/`: Additional pages
- `tests/`: Unit tests
- `requirements.txt`: Project dependencies

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.