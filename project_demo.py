import gradio as gr
from datetime import datetime

# Sample data (replace this with your actual data)
data = [
    ["2024-08-07", 1.1, 1.2, 1.3, 1.4, 11.1, "Very Good"],
    ["2024-08-08", 2.1, 2.2, 2.3, 2.4, 22.2, "Good"],
    ["2024-08-09", 3.1, 3.2, 3.3, 3.4, 33.3, "Bad"],
    # Add more data rows as needed
]


def search_by_date(date_input):
    date_str = datetime.fromtimestamp(date_input).strftime("%Y-%m-%d")
    for row in data:
        if row[0] == date_str:
            return row[1], row[2], row[3], row[4], row[5], row[6]
    return "No data found", "", "", "", "", ""


iface = gr.Interface(
    fn=search_by_date,
    inputs=gr.DateTime(label="Select Date", include_time=False),
    outputs=[
        gr.Textbox(label="NO2"),
        gr.Textbox(label="O3"),
        gr.Textbox(label="PM2.5"),
        gr.Textbox(label="PM10"),
        gr.Textbox(label="Air quality index"),
        gr.Textbox(label="Air quality"),
    ],
    title="Air Quality Prediction",
    description="Enter a date to retrieve air quality information.",
)

iface.launch()
