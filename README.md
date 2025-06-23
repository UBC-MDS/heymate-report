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
link to the repository:[Heymate Report](https://github.com/UBC-MDS/heymate-report)
You can use the following command in your terminal:
```bash
git clone git@github.com:UBC-MDS/heymate-report.git
cd heymate-report
```

### 2. Set up Credentials
You need to create the `credentials` folder and add the `.env` and `open_ai_token.txt` files.
You can refer to the templates in the `credentials_template` folder. Edit the files with the appropriate API keys and tokens. **Folder name should be `credentials` and not `credentials_template` and files should be named `.env` and `open_ai_token.txt` respectively.**

 **Note on Credentials**  
Due to NDA agreements with Heymate, we are unable to share the actual API keys or `.env` contents publicly.  
However, we have privately shared the `credentials/` folder with the course instructor (via Slack/email), as it is necessary to run the full pipeline.


### 3. Install and Activate the Environment
To install the conda environment:
```bash
conda env create -f environment.yml
```
To activate the conda environment:
```bash
conda activate heymate-mds-data-clean-pipeline
```
### 4. Load more training data (if needed)
If you want to load and clean additional data, you can activate the local server and make HTTP requests to invoke the tasks.
```bash
cd script
python flask_deploy.py
```
you can find more details in [knowledge_base_update notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/knowledge_base_update.ipynb).

## 🚀 How to Run the Recommender System
Follow these steps to test the recommender module locally.
### 1. Navigate to the Script Directory
```bash
cd script
```   
### 2. Make sure you are in the conda environment
```bash
conda activate heymate-mds-data-clean-pipeline
```
### 3. To generate the recommendation results via script run:
```bash
python menu_recommender.py
```

### Visualize recommendation demo

To generate and visualize recommendations for a given restaurant type, refer to the [visualization_demo notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/visualization_demo.ipynb).

You can choose up to three types: `type1`, `type2`, and `type3`.

This will output the top N recommended dishes based on popularity scores for the selected restaurant types and visualize the results in a bar chart.

## 📝 Reports and Reproducibility

### Available Reports
- [Proposal](https://github.com/UBC-MDS/heymate-report/blob/main/proposal_report/proposal-report.pdf)
- [Final Report](https://github.com/UBC-MDS/heymate-report/blob/main/final_report/final-report.pdf)
- [Technical Report](https://github.com/UBC-MDS/heymate-report/blob/main/technical_report/technical-report.pdf)


### How to Reproduce the Final Report

To generate the **final report** in PDF format using Quarto, follow these steps:

#### 1. Navigate to the Report Directory
```bash
cd final_report
```

#### 2. Render the report in PDF format:
```bash 
quarto render final-report.qmd --to pdf
``` 
#### 3. View the generated report
You can find the generated PDF file in the `final_report/` directory.
To open the pdf report, double-click final-report.pdf in your file system or run:
```bash
open final-report.pdf
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





