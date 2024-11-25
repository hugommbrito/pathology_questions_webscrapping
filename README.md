🩺 Pathology Questions Scraper

This project is a Python web scraper designed to automatically collect answered questions from the Pathology Outlines website and save them into a CSV file. This file can be easily imported into tools like Notion, Excel, Google Sheets or other organization and data analysis software.

The code is heavlily commented to make it easy to understand and modify because it is intended to be interpreted by pathologists, not only developers. 🤓

✨ Features

	•	Fetches and collects answered questions from the pathology website.
	•	Organizes questions and answers in a tabular format.
	•	Exports the data to a CSV file, ready for use in spreadsheets or databases.

🛠️ Technologies Used

	•	Python 3.9+
	•	Selenium for browser automation.
	•	Python’s csv module for data handling and export.
	•	Seleniom WebDriver (compatible with Chrome).

🚀 How to Use

Follow these steps to set up and run the script on your machine:

1. Prerequisites

	•	Python 3.9 or later.
	•	Google Chrome installed.
	•	Selenium Lib

2. Installation

	1.	Clone this repository available in https://github.com/hugommbrito/pathology_questions_webscrapping:

git clone git@github.com:hugommbrito/pathology_questions_webscrapping.git
cd pathology-questions-scraper


	2.	Create a virtual environment (optional, but recommended):

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


	3.	Install the required dependencies:

pip install -r requirements.txt


	4.	Ensure the WebDriver (Chrome) is correctly set up in your system’s PATH.

3. Configuration

Open the main.py file and adjust the settings if necessary:
	•	driver_path: Path to your browser’s WebDriver.
	•	output_file: Name of the CSV file where questions will be saved (default is pathologyDB.csv).

4. Running the Script

Run the script with the following command:

python main.py

The script will:
	1.	Open the browser and navigate to the pathology questions website.
	2.	Collect all available questions and answers.
	3.	Save the data into the pathologyDB.csv file.

5. Output

The generated CSV file will have the following structure with sample data:

Index	Subspecialty	Question Number	Question Text	Question Images	Alternatives	Correct Alternative	Explanation	Reference	Question Link
1	Bone, joints & soft tissue	1	A 30-year-old woman presented with a painful mass in the femur. What is it?	https://img.link/1.png	A: Osteosarcoma, B: Chondrosarcoma, C: Ewing	A	Most common in young adults.	https://pathologyoutlines.com/bonecase123	https://pathologyoutlines.com/question1
2	GI / Liver	2	What is the most common primary liver tumor in adults?	None	A: Hepatoblastoma, B: HCC, C: Angiosarcoma	B	Hepatocellular carcinoma is the most common.	https://pathologyoutlines.com/livercase456	https://pathologyoutlines.com/question2
3	Thoracic	3	A 65-year-old smoker presents with hemoptysis. Which mutation is most likely?	https://img.link/2.png	A: EGFR, B: ALK, C: KRAS	C	Common in smoking-associated lung adenocarcinoma.	https://pathologyoutlines.com/lungcase789	https://pathologyoutlines.com/question3

Explanation of Fields:

	•	Index: Numerical order of the questions in the dataset.
	•	Subspecialty: The medical subspecialty of the question (e.g., Bone, joints & soft tissue).
	•	Question Number: The ID or number of the question in that subspecialty.
	•	Question Text: The main text of the question.
	•	Question Images: Links to any images associated with the question (if available).
	•	Alternatives: Answer options, prefixed by their corresponding letters (e.g., A, B, C).
	•	Correct Alternative: The letter corresponding to the correct answer.
	•	Explanation: Explanation for the correct answer.
	•	Reference: URL for further reading or reference about the question.
	•	Question Link: The direct link to the question on the website.

You can open the file in Excel, Google Sheets, or import it into databases like Notion.

🧪 Testing the Script

If you’d like to test the script before fetching all questions, limit the number of pages to scrape and the number of questionas to be extracted from each page by adjusting the logic in the script.

⚠️ Disclaimer

	•	Ethical Use: This script was developed for personal and educational purposes. Make sure to respect the terms of use of the website when using this scraper.
	•	Performance: To avoid overloading the website, the script includes delays between requests.

📝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author

Created by https://github.com/hugommbrito.
