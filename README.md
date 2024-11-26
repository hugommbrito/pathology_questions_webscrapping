<h1 align="center">🩺 Pathology Question Scraper</h1>

<p align="center">
	This project is a Python web scraper designed to automatically collect answered questions from the <a href="https://www.pathologyoutlines.com/review-questions">Pathology Outlines website</a> and save them into a CSV file. This file can be easily imported into tools like Notion, Excel, Google Sheets or other organization and data analysis software.
</p>

<p align="center">
The code is heavlily commented to make it easy to understand and modify because it is intended to be interpreted by pathologists, not only developers. 🤓
</p>

---

<h2>✨ Features</h2>
<ul>
  <li>Scrapes multiple pages of pathology questions.</li>
  <li>Extracts question text, images, alternatives, answers, and references.</li>
  <li>Exports the data to a CSV file, ready for use in spreadsheets or databases.</li>
  <li>Allows customization of the number of pages and questions to scrape.</li>
</ul>

---

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python 3.9+</li>
  <li>Selenium for browser automation.</li>
	<li>Seleniom WebDriver (compatible with Chrome).</li>
  <li>Python’s csv module for data handling and export.</li>
</ul>

---

<h2>🚀 How to Use</h2>
<p>Follow these steps to set up and run the script on your machine:</p>

<h3>Prerequisites</h3>
<ol>
	<li>Python 3.9 or later.</li>
	<li>Google Chrome installed.</li>
	<li>Selenium Lib</li>
</ol>

<ol>
  <h3><li>Clone the <a href="https://github.com/hugommbrito/pathology_questions_webscrapping:">Repository</a>:</li></h3>
  <pre><code>git clone git@github.com:hugommbrito/pathology_questions_webscrapping.git</code></pre>
  <pre><code>cd pathology-questions-scraper</code></pre>
	
  <h3><li>Create a virtual environment (optional, but recommended):</li></h3>
  <pre><code>python3 -m venv venv</code></pre>
  <pre><code>
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
	</code></pre>
	
 
  <h3><li>Install the required dependencies:</li></h3>
  <pre><code>pip install -r requirements.txt</code></pre>
	
  <h3><li>Ensure the Browser (Chrome) is correctly instaled in your OS.</li></h3>
  
  <h3><li>Configuration</li></h3>
	<p>Open the main.py file and adjust the settings if necessary:</p>
	<ul>
		<li>Scraping Volume: Adjust the amount of pages and questions per page that you whant to get.</li>
		<li>Driver Path: Path to your browser’s WebDriver.</li>
		<li>Output File: Name of the CSV file where questions will be saved (default is pathologyDB.csv).</li>
	</ul>
 
  <h3><li>Running the Script</li></h3>
	<p>Run the script with the following command:</p>
  <pre><code>python3 main.py</code></pre>

 <p>The script will:<br/>
	1.	Open the browser and navigate to the pathology questions website.<br/>
	2.	Collect all available questions and answers.<br/>
	3.	Save the data into the pathologyDB.csv file.</p>
	
</ol>

---

<h2>📊 CSV Structure</h2>
<p>The CSV file includes the following columns:</p>
<table>
  <thead>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>index</code></td>
      <td>Unique identifier for each question.</td>
    </tr>
    <tr>
      <td><code>Subspecialty</code></td>
      <td>Pathology subspecialty related to the question.</td>
    </tr>
    <tr>
      <td><code>Question Number</code></td>
      <td>Question number on the page.</td>
    </tr>
    <tr>
      <td><code>Question Text</code></td>
      <td>The main text of the question.</td>
    </tr>
    <tr>
      <td><code>Question Images</code></td>
      <td>Links to any images associated with the question (if available).</td>
    </tr>
    <tr>
      <td><code>Alternatives</code></td>
      <td>Possible answers with letters (e.g., A, B, C).</td>
    </tr>
    <tr>
      <td><code>Correct Alternative</code></td>
      <td>The letter of the correct answer.</td>
    </tr>
    <tr>
      <td><code>Explanation</code></td>
      <td>Detailed explanation of the answer.</td>
    </tr>
    <tr>
      <td><code>Reference</code></td>
      <td>Link to supporting reference.</td>
    </tr>
    <tr>
      <td><code>Question Link</code></td>
      <td>URL of the question page.</td>
    </tr>
  </tbody>
</table>

<p>You can open the file in Excel, Google Sheets, or import it into databases like Notion.</p>

---

<h2>🧪 Testing</h2>
<p>
If you’d like to test the script before fetching all questions, limit the number of pages to scrape and the number of questionas to be extracted from each page by adjusting the logic in the script.</p>

<h2>⚠️ Disclaimer</h2>

  •	Ethical Use: This script was developed for personal and educational purposes. Make sure to respect the terms of use of the website when using this scraper.
	•	Performance: To avoid overloading the website, the script includes delays between requests.
---

<h2>📝 Contributing</h2>
<p>Feel free to submit issues or pull requests. Contributions are welcome!</p>

<h2>📄 License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<h2>👨‍💻 Author</h2>

<p>Created by <a href="https://github.com/hugommbrito">HugoMMBrito</a>.</p>
