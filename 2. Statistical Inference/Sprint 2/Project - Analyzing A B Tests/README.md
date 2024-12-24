# A/B Testing Analysis Projects

This repository contains analysis of A/B tests for two different business cases:

## Projects

### Fast Food Marketing Campaign
- `fast_food_marketing_campaign.ipynb`: Analysis of three promotional strategies
- `fastfood_dashboard_data.csv`: Raw sales and promotion data
- `promotion_summary_stats.csv`: Aggregated statistics
- [Dashboard](https://lookerstudio.google.com/reporting/04502a29-37c4-41de-b5cb-9b7300bb5763)

#### Key Findings
- Promotion 1 significantly outperformed Promotion 2 (+10.77k sales, p<0.001)
- Promotion 1 showed better but not statistically significant results vs Promotion 3
- Recommendation: Implement Promotion 1 due to consistent performance and higher sales
- Sample size was well-balanced across 137 locations (43/47/47 split)

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
