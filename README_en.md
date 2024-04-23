# 🌐 ScrapingClub Parser 🕸️

## 📝 Description
This script parses data from [ScrapingClub](https://scrapingclub.com/exercise/list_basic/) website and saves it in CSV format. The script also visualizes the number of products on each page using a bar chart.

## 🛠️ Installation
1. Make sure you have Python 3.x installed.
2. Install the required libraries by running the `pip install -r requirements.txt` command if the requirements.txt file is present in the repository.

## ▶️ Usage
1. Run the script by passing the number of pages you want to spar as a command line argument (default is 1 page).
   Example: `python main.py 5` - parses data from the first 5 pages.
2. After the script is executed, a `data.csv` file containing the parsed data will be created and the number of products on each page will be displayed as a bar chart.

## 📂 Project structure
- `main.py`: Main script for parsing data, creating DataFrame and visualization.
- `requirements.txt`: The file with the project dependencies.
- `data.csv`: File with saved data.
- `README.md`: File with project description and usage instructions in Russian.
- `README_en.md`: File with project description and instructions for use in English.

## 📦 Dependencies
- requests
- beautifulsoup4
- pandas
- matplotlib

## 👨‍💻 Author
Damir Ainetdinov
`damir2002-ms`