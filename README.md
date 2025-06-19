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

## 📝 Reports
- [Proposal](https://github.com/UBC-MDS/heymate-report/blob/main/proposal_report/proposal-report.pdf)
- [Final Report](https://github.com/UBC-MDS/heymate-report/blob/main/final_report/final-report.pdf)
- [Technical Report](https://github.com/UBC-MDS/heymate-report/blob/main/technical_report/technical-report.pdf)

## 🚀 How to Run the Recommender System
Follow these steps to test the recommender module locally.

### 1. Set up Credentials
You need to create the `credentials` folder and add the `.env` and `open_ai_token.txt` files.
You can refer to the templates in the `credentials_template` folder.

### 2. Install and Activate the Environment
To install the conda environment:
```bash
conda env create -f environment.yml
```
To activate the conda environment:
```bash
conda activate heymate-mds-data-clean-pipeline
```

### 3. Load more training data (if needed)
If you want to load and clean additional data, you can activate the local server and make HTTP requests to invoke the tasks.
```bash
cd script
python local_deploy.py
```
you can find more details in [task_invoker notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/task_invoker.ipynb).

### 4. Make recommendation

To generate recommendations for a given restaurant type, refer to the [visualization notebook](https://github.com/UBC-MDS/heymate-report/blob/main/script/visualization.ipynb).

You can choose up to three types: `type1`, `type2`, and `type3`.

This will output the top N recommended dishes based on popularity scores for the selected restaurant types and visualize the results in a bar chart.




