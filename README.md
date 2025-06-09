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

## 🚀 How to Run the Recommender System
Follow these steps to test the recommender module locally.
### 1. Activate the Environment
Make sure you are in the correct conda environment:
```bash
conda activate heymate-mds-data-clean-pipeline
```

### 2. Run the Recommendation Script (CLI)
To test the recommender logic for a given restaurant type:

```bash
cd script
python menu_recommender.py
```
This will output the top N recommended dishes based on popularity scores for the selected restaurant types. You can modify type1, type2, and type3 in menu_recommender.py to test different use cases.





