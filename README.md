# 🍽️ Heymate Menu Recommendation Project
  - Author: Hankun Xiao, Yasmin Hassan, Jiaxin Zhang, Zhiwei Zhang
## Motivation
This project aims to build a menu recommendation pipeline for Heymate's restaurant partners. By analyzing internal product, store, and category data along with external datasets we seek to provide insights into menu item popularity, pricing, and restaurant-specific recommendations. Our recommendations help partners optimize their offerings through data driven insights.
## Summary
We conduct comprehensive data validation, enrichment, and exploratory analysis on restaurant menu data. Key steps include:
- Cleaning inconsistent menu item names using LLMs
- Merging external datasets (e.g. Kaggle)
- Scoring menu item popularity
- Building a pipeline to deliver actionable insights to restaurant clients
## Getting Started
### 1. Clone the Repository
To get started, clone the repository to your local machine
link to the repository:[Heymate Repo](https://github.com/UBC-MDS/heymate-report)
You can use the following command in your terminal:
```shell script
git clone git@github.com:UBC-MDS/heymate-report.git
cd heymate-report
```
### 2. Set up Credentials
**Important:** Due to NDA agreements with Heymate, we cannot share the actual API keys publicly. However, the credentials have been privately shared with the course instructor.
Follow these steps to set up your credentials:
1. **Rename the credentials_template folder to credentials:**
   ```shell script
   mv credentials_template credentials
   ```
2. **Navigate to the credentials folder:**
   ```shell script
   cd credentials
   ```
3. **Rename the environment(.env.example) template to .env:**
   ```shell script
   mv .env.example .env
   ```
4. **Edit the credential files:**
   - Open `.env` file and replace the placeholder values with actual database credentials
   - Open `open_ai_token.txt` and replace the placeholder with your actual OpenAI API token
   
   **Example of what to fill in `.env`:**
   ```
   SQL_SERVER=your_sql_server_here
   SQL_USER=your_sql_user_here
   SQL_PASSWORD=your_sql_password_here
   SQL_DATABASE=your_sql_database_here
   ```
5. **Go back to the main directory:**
   ```shell script
   cd ..
   ```
### 3. Install and Activate the Environment
To install the conda environment:
```shell script
conda env create -f environment.yml
```
To activate the conda environment:
```shell script
conda activate heymate-mds-data-clean-pipeline
```
### 4. Load more training data (if needed)
If you want to load and clean additional data, you can activate the local server and make HTTP requests to invoke the tasks.
```shell script
cd script
python flask_deploy.py
```
you can find more details in [knowledge_base_update notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/knowledge_base_update.ipynb).
## :rocket: How to Run the Recommender System
Follow these steps to test the recommender module locally.
### 1. Navigate to the Script Directory
```shell script
cd script
```
### 2. Make sure you are in the conda environment
```shell script
conda activate heymate-mds-data-clean-pipeline
```
### 3. To generate the recommendation results via script run:
```shell script
python menu_recommender.py
```
## Visualize Recommendation Demo
### How to View Interactive Recommendation Charts
Follow these steps to generate and view interactive bar charts showing menu recommendations:
#### 1. Navigate to the Script Directory
```shell script
cd script
```
#### 2. Activate the Environment
```shell script
conda activate heymate-mds-data-clean-pipeline
```
#### 3. Open the Visualization Notebook
```shell script
open visualization_demo.ipynb
```
#### 4. Generate Recommendations
1. **Run all cells** in the notebook to generate the popularity-based recommendations
2. The output will display as an **interactive bar chart** showing the top recommended menu items for selected restaurant types
#### 5. Customize Restaurant Types (Optional)
To visualize recommendations for different cuisines:
1. **Locate the second cell** in the notebook
2. **Modify the function parameters** to select up to three restaurant types:
   ```python
   recommender_menu_items(type1="Italian", type2="Mexican", type3="Chinese")
   ```
3. **Re-run the cell** to generate updated recommendations

**Some of the available Restaurant Types:**
| Parameter  | Available Options|
|----------- |------------------|
| type1, type2, type3 | "Italian", "Mexican", "Chinese", "Japanese", "American", "Indian", "Mediterranean", "French", "Korean", "Vietnamese", "Greek", "Lebanese", "Spanish" |

**Example combinations:**
```python
# Compare Asian cuisines
recommender_menu_items(type1="Chinese", type2="Japanese", type3="Thai")
# Compare Mediterranean options
recommender_menu_items(type1="Italian", type2="Greek", type3="Mediterranean")
# Mix different cuisine types
recommender_menu_items(type1="Mexican", type2="Korean", type3="French")
```
#### Expected Output
- Interactive bar charts comparing menu item popularity across selected restaurant types
- Restaurant-specific recommendations with popularity scores
- Visual comparison of menu performance metrics
**Note:** Ensure you're in the correct conda environment (`heymate-mds-data-clean-pipeline`) before running the notebook.
For detailed instructions and examples, refer to the [visualization_demo notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/visualization_demo.ipynb).
## :memo: Reports and Reproducibility
### Available Reports
- [Proposal](https://github.com/UBC-MDS/heymate-report/blob/main/proposal_report/proposal-report.pdf)
- [Final Report](https://github.com/UBC-MDS/heymate-report/blob/main/final_report/final-report.pdf)
- [Technical Report](https://github.com/UBC-MDS/heymate-report/blob/main/technical_report/technical_report.pdf)
### How to Reproduce the Final Report
To generate the **final report** in PDF format using Quarto, follow these steps:
Remember to cd out of the `script` directory if you are still in it.
```shell script
cd ..
```
#### 1. Navigate to the Report Directory
```shell script
cd final_report
```
#### 2. Render the report in PDF format:
```shell script
quarto render final-report.qmd --to pdf
```
#### 3. View the generated report
You can find the generated PDF file in the `final_report/` directory.
To open the pdf report, double-click final-report.pdf in your file system or run:
```shell script
open final-report.pdf
```

Similarly, you can reproduce the **technical report** using
```shell script
cd technical_report
quarto render technical_report.qmd --to pdf
```

### Prerequisites
Ensure you have Quarto installed on your system if you haven't already. You can install it by following the instructions on the Quarto website:
[Link](https://quarto.org/docs/get-started/)
If you use conda, you can use this command:
```bash
conda install -c conda-forge -c quarto
```
## License
This project was developed as part of the UBC Master of Data Science (MDS) Capstone and is intended for academic purposes only.
Some components, including API credentials and internal datasets from Heymate!, are subject to Non-Disclosure Agreements (NDAs) and are **not open-sourced**.
Please do not reuse or redistribute any part of this project without written permission from the authors and Heymate!.
## Acknowledgements
We would like to thank our project partner, Heymate!, for providing the data and support necessary to complete this project.
We also appreciate the guidance and feedback from our course instructors and peers throughout the project.
## Contact
For any questions or inquiries about this project, please contact the authors:
- Hankun Xiao: [Github](https://github.com/hankunxiao)
- Yasmin Hassan: [Github](https://github.com/yasmin2424)
- Jiaxin Zhang: [Github](https://github.com/jessiezhang24)
- Zhiwei Zhang: [Github](https://github.com/gracez-20)