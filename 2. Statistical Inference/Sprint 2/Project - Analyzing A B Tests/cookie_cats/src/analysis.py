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

    def get_sample_stats(self) -> Dict[str, pd.DataFrame]:
        total_size = len(self.df)
        variant_sizes = self.df['version'].value_counts()
        variant_props = variant_sizes / total_size

        # Create DataFrame with both sizes and proportions
        stats_df = pd.DataFrame({
            'Size': variant_sizes,
            'Proportion': variant_props
        })

        stats_df.loc['Total'] = [total_size, 1.0]

        return {
            'total_size': total_size,
            'stats': stats_df
        }

    def check_sample_ratio_mismatch(self) -> Dict[str, pd.DataFrame]:
        observed = self.df['version'].value_counts()
        expected = pd.Series({
            self.control_name: len(self.df) * 0.5,
            self.treatment_name: len(self.df) * 0.5
        })

        # Chi-square test for SRM
        stat, pval = stats.chisquare(observed, expected)

        # Binomial test for proportion difference
        n = len(self.df)
        count = observed.iloc[0]  # count of first group
        binom_result = stats.binomtest(count, n, p=0.5)
        proportion_difference = (binom_result.statistic - 0.5) * 100  # Changed from .proportion to .statistic

        # Create DataFrame
        srm_df = pd.DataFrame({
            'Observed': observed,
            'Expected': expected,
            'Statistic': [stat, None],
            'P-value': [pval, None],
            'Proportion_Difference_%': [proportion_difference, -proportion_difference]
        })

        return {
            'srm_stats': srm_df
        }

    def analyze_game_rounds(self) -> Dict[str, pd.DataFrame]:
        control_data = self.df[self.df['version'] == self.control_name]['sum_gamerounds']
        treatment_data = self.df[self.df['version'] == self.treatment_name]['sum_gamerounds']

        # Mann-Whitney U test
        statistic, p_value = stats.mannwhitneyu(
            control_data, treatment_data, alternative='two-sided'
        )

        # Create summary statistics DataFrame
        stats_summary = pd.DataFrame({
            'median': [control_data.median(), treatment_data.median()],
            'mean': [control_data.mean(), treatment_data.mean()],
            'count': [len(control_data), len(treatment_data)],
            'MWU_Statistic': [statistic, None],
            'P-value': [p_value, None]
        }, index=[self.control_name, self.treatment_name])

        return {
            'rounds_stats': stats_summary
        }

    def analyze_retention(self, metric: str) -> AnalysisResults:
        """Analyze retention metrics (retention_1 or retention_7) returning both DataFrame and original structure"""
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

        # Create both DataFrame and original structure
        retention_df = pd.DataFrame({
            'Retention_Rate': [control_rate, treatment_rate],
            'Sample_Size': [n_control, n_treatment],
            'Effect_Size': [effect, None],
            'Relative_Effect_%': [relative_effect, None],
            'CI_Lower': [ci[0], None],
            'CI_Upper': [ci[1], None],
            'Chi_Square': [chi2, None],
            'P_value': [p_value, None]
        }, index=[self.control_name, self.treatment_name])

        # Return both the DataFrame and the original structure for visualization
        results = AnalysisResults(
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

        results.stats_df = retention_df  # Add DataFrame as an attribute
        return results
