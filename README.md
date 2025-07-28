# cintel-06-custom
Custom PyShiny app with interactive filters and visualizations
# Flights Dashboard - Module 6 Custom PyShiny App

## Project Overview

This project is a custom interactive dashboard built with **PyShiny** to explore airline passenger data (`flights.csv`). Users can filter data by **year** and **months** and visualize passenger counts dynamically. It demonstrates reactive programming and continuous intelligence concepts using the `reactive.file_reader` feature.

---

## Features

- Dynamic selection of **Year** (dropdown)
- Multiple **Months** selection (checkbox group)
- Text output showing current filters
- Data table showing filtered records
- Bar chart visualizing monthly passenger counts
- Automatic data reloading when the `flights.csv` file changes on disk

---

## Data Source

- The dataset is sourced from the [Seaborn flights dataset](https://github.com/mwaskom/seaborn-data/blob/master/flights.csv).
- The data contains monthly passenger numbers from 1949 to 1960.

---

## How to Run

1. Clone or download this repository.
2. Ensure `flights.csv` is in the same directory as `app.py`.
3. Create and activate a Python virtual environment.
4. Install required packages:

```bash
   pip install -r requirements.txt
```
Run the app:
python app.py
Open your browser and go to http://localhost:8000

## Files in this Repository

app.py — Main PyShiny application script
flights.csv — Data file with flights passenger information
requirements.txt — Python dependencies
README.md — This documentation file
docs/ — Optional exported app assets for static hosting



## API References

PyShiny Input Select
PyShiny Checkbox Group
PyShiny Render Plot
PyShiny reactive.file_reader
