import scipy.stats as stats
import numpy as np
import pandas as pd


def check_sample_ratio_mismatch(df, variant_column='version', expected_ratio=0.5):
    """
    Check for Sample Ratio Mismatch using Chi-square test

    Parameters:
    df: DataFrame containing the experiment data
    variant_column: Column name containing variant information
    expected_ratio: Expected proportion of users in treatment group

    Returns:
    dict containing observed counts, expected counts, chi-square statistic, and p-value
    """
    # Get observed counts
    observed = df[variant_column].value_counts()
    total_samples = len(df)

    # Calculate expected counts
    expected = pd.Series({
        observed.index[0]: total_samples * expected_ratio,
        observed.index[1]: total_samples * (1 - expected_ratio)
    })

    # Perform chi-square test
    chi2, p_value = stats.chisquare(observed, expected)

    return {
        'observed_counts': observed,
        'expected_counts': expected,
        'chi2_statistic': chi2,
        'p_value': p_value
    }


def analyze_binary_metric(df, metric_column, variant_column='version'):
    """
    Analyze binary metric using Chi-square test

    Parameters:
    df: DataFrame containing the experiment data
    metric_column: Column name of the binary metric to analyze
    variant_column: Column name containing variant information

    Returns:
    dict containing contingency table and test results
    """
    # Create contingency table
    contingency = pd.crosstab(df[variant_column], df[metric_column])

    # Perform chi-square test
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

    return {
        'contingency_table': contingency,
        'chi2_statistic': chi2,
        'p_value': p_value,
        'dof': dof
    }


def analyze_continuous_metric(df, metric_column, variant_column='version', use_parametric=True):
    """
    Analyze continuous metric using either t-test or Mann-Whitney U test

    Parameters:
    df: DataFrame containing the experiment data
    metric_column: Column name of the continuous metric to analyze
    variant_column: Column name containing variant information
    use_parametric: If True, use t-test; if False, use Mann-Whitney U test

    Returns:
    dict containing test results and basic statistics
    """
    # Split data by variant
    variants = df[variant_column].unique()
    group1 = df[df[variant_column] == variants[0]][metric_column]
    group2 = df[df[variant_column] == variants[1]][metric_column]

    # Perform statistical test
    if use_parametric:
        statistic, p_value = stats.ttest_ind(group1, group2)
        test_name = "Student's t-test"
    else:
        statistic, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')
        test_name = "Mann-Whitney U test"

    # Calculate effect size (Cohen's d for parametric)
    if use_parametric:
        effect_size = (group1.mean() - group2.mean()) / np.sqrt((group1.var() + group2.var()) / 2)
    else:
        effect_size = statistic / (len(group1) * len(group2))  # normalized U statistic

    return {
        'test_name': test_name,
        'statistic': statistic,
        'p_value': p_value,
        'effect_size': effect_size,
        'group1_mean': group1.mean(),
        'group2_mean': group2.mean(),
        'group1_std': group1.std(),
        'group2_std': group2.std()
    }
