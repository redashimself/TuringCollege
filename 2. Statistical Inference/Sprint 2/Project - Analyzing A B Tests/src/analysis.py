from dataclasses import dataclass
from typing import Dict, Any

import pandas as pd
import numpy as np
from scipy import stats


@dataclass
class AnalysisResults:
    """Container for analysis results"""
    test_results: Dict[str, float]
    effect_size: Dict[str, float]
    rates: Dict[str, float]


class ABTestAnalysis:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path + "/cookie_cats.csv")
        self.control_name = 'gate_30'
        self.treatment_name = 'gate_40'

    def get_sample_stats(self) -> Dict[str, Any]:
        total_size = len(self.df)
        variant_sizes = self.df['version'].value_counts()
        variant_props = variant_sizes / total_size

        return {
            'total_size': total_size,
            'variant_sizes': variant_sizes,
            'variant_props': variant_props
        }

    def check_sample_ratio_mismatch(self) -> tuple:
        observed = self.df['version'].value_counts()
        expected = pd.Series({
            self.control_name: len(self.df) * 0.5,
            self.treatment_name: len(self.df) * 0.5
        })
        return stats.chisquare(observed, expected)

    def analyze_game_rounds(self) -> Dict[str, Any]:
        control_data = self.df[self.df['version'] == self.control_name]['sum_gamerounds']
        treatment_data = self.df[self.df['version'] == self.treatment_name]['sum_gamerounds']

        statistic, p_value = stats.mannwhitneyu(
            control_data, treatment_data, alternative='two-sided'
        )

        stats_summary = pd.DataFrame({
            self.control_name: {
                'median': control_data.median(),
                'mean': control_data.mean(),
                'count': len(control_data)
            },
            self.treatment_name: {
                'median': treatment_data.median(),
                'mean': treatment_data.mean(),
                'count': len(treatment_data)
            }
        }).T

        return {
            'test_results': {'statistic': statistic, 'p_value': p_value},
            'summary': stats_summary
        }

    def analyze_retention(self, metric: str) -> AnalysisResults:
        """Analyze retention metrics (retention_1 or retention_7)"""
        contingency = pd.crosstab(self.df['version'], self.df[metric])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency)

        control_rate = self.df[self.df['version'] == self.control_name][metric].mean()
        treatment_rate = self.df[self.df['version'] == self.treatment_name][metric].mean()

        effect = treatment_rate - control_rate
        relative_effect = effect / control_rate * 100

        n_control = len(self.df[self.df['version'] == self.control_name])
        n_treatment = len(self.df[self.df['version'] == self.treatment_name])

        se = np.sqrt((control_rate * (1 - control_rate)) / n_control +
                     (treatment_rate * (1 - treatment_rate)) / n_treatment)

        ci = (effect - 1.96 * se, effect + 1.96 * se)

        return AnalysisResults(
            test_results={'chi2': chi2, 'p_value': p_value},
            effect_size={
                'absolute': effect,
                'relative': relative_effect,
                'confidence_interval': ci
            },
            rates={
                'control': control_rate,
                'treatment': treatment_rate
            }
        )