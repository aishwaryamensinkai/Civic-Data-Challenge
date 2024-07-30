# Civic-Data-Challenge

Civic Data Challenge is a month-long contest where members of the community get the chance to use datasets from Open Data Syracuse to build an interesting data visualization, website application, data analysis, map, chatbot, or any other type of project that uses the featured dataset.

## Project Description
This project analyzes and visualizes crime data in Syracuse using datasets from Open Data Syracuse. It includes an interactive web application that allows users to explore crime trends, visualize geographical distributions of crimes, and generate crime summaries using a custom ChatGPT model.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app/app.py`.
5. Open your web browser and go to `http://localhost:5000`.

## Usage
- Enter a location to generate a crime summary.
- View the crime map to explore crime distributions.

## Project Structure
- `data/`: Contains the dataset.
- `app/`: Contains the Flask web application.
- `scripts/`: Contains Python scripts for data analysis and cleaning.
- `README.md`: Contains a description of the project, setup instructions, and usage information.
- `requirements.txt`: Lists the dependencies required for the project.
- `crime_map.html`: The HTML file generated for the map visualization.

https://data.syr.gov/pages/data-challenge


# Final Steps

1. Populate the data/ directory with your Part1.csv file.
2. Run the data cleaning script:
  ```bash
  python scripts/data_cleaning.py
  ```
3. Run the data analysis script:
  ```bash
  python scripts/data_analysis.py
  ```
4. Start the Flask application by running:
  ```bash
  python app/app.py
  ```
5. Test your web application to ensure everything is working as expected.
6. Prepare your submission by compiling your results, code, and description.
7. Submit your project to opendata@syrgov.net with all required details.
