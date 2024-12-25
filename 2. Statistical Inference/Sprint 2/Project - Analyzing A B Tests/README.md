# A/B Testing Analysis Projects

This repository contains analysis of A/B tests for two different business cases:

## Projects

### Fast Food Marketing Campaign
- `fast_food_marketing_campaign.ipynb`: Analysis of three promotional strategies
- `fastfood_dashboard_data.csv`: Raw sales and promotion data
- `promotion_summary_stats.csv`: Aggregated statistics 
- [Dashboard](https://lookerstudio.google.com/reporting/04502a29-37c4-41de-b5cb-9b7300bb5763)

#### Key Findings
Raw Performance:
- Promotion 1 maintained highest stable sales (~55-60K)
- Promotion 2 consistently underperformed (~40K)
- Promotion 3 performed similarly to Promotion 1 but with more variability

Statistical Results:
- Significant difference between Promotion 1 vs 2 (+10.77K, p<0.001)
- No significant difference between Promotion 1 vs 3 (+2.73K, p=0.128)
- Well-balanced sample across 137 locations (43/47/47 split)

Market Size Impact:
- Performance gaps narrowed after market size weighting
- Promotions 1 and 3 showed similar weighted performance
- Recommendation: Implement Promotion 1, with Promotion 3 as viable alternative

### Cookie Cats Mobile Game
- `analysis.py`: Core analysis functions
- `visualization.py`: Data visualization code
- `cookie_cats_mobile_game.ipynb`: Main analysis notebook

#### Key Findings
- Gate 30 outperformed Gate 40 for player retention
- 1-day retention: -1.32% relative decrease with Gate 40 (not significant)
- 7-day retention: -4.31% relative decrease with Gate 40 (p < 0.01) (significant)
- Recommendation: Keep Gate 30 as standard due to better long-term retention

## Setup
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```
