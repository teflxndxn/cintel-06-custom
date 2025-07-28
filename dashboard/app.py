from shiny import App, ui, render, reactive, req
import pandas as pd

# ---------------------------
# Reactive File Reader
# ---------------------------
@reactive.file_reader("flights.csv")
def read_flights():
    return pd.read_csv("flights.csv")

# ---------------------------
# UI Layout
# ---------------------------
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("year", "Select Year", choices=[], selected=None),
        ui.input_checkbox_group("months", "Select Months", choices=[], selected=[]),
    ),
    ui.layout_column_wrap(
        ui.h2("Flights Dashboard"),
        ui.output_text("selection_text"),
        ui.output_data_frame("filtered_table"),
        ui.output_plot("passenger_plot"),
    ),
)

# ---------------------------
# Server Logic
# ---------------------------
def server(input, output, session):

    @reactive.Effect
    def update_inputs():
        df = read_flights()
        years = sorted([str(int(y)) for y in df["year"].unique()])
        months = sorted(df["month"].unique())

        ui.update_select("year", choices=years, selected=years[0])
        ui.update_checkbox_group("months", choices=months, selected=months)

    @reactive.Calc
    def filtered_data():
        df = read_flights()
        req(input.year())
        req(input.months())

        return df[
            (df["year"] == int(input.year())) &
            (df["month"].isin(input.months()))
        ]

    @output
    @render.text
    def selection_text():
        return f"Showing data for year {input.year()} and months {', '.join(input.months())}"

    @output
    @render.data_frame
    def filtered_table():
        return filtered_data()

    @output
    @render.plot
    def passenger_plot():
        import matplotlib.pyplot as plt
        df = filtered_data()

        fig, ax = plt.subplots()
        ax.bar(df["month"], df["passengers"])
        ax.set_title(f"Passengers in {input.year()}")
        ax.set_xlabel("Month")
        ax.set_ylabel("Passengers")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

# ---------------------------
# App Entry Point
# ---------------------------
app = App(app_ui, server)
