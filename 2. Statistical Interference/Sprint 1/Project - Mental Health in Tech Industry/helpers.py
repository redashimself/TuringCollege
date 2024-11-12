import math


def get_responses_by_question(df, question_text):
    """
    Get responses for a specific question grouped by year.

    Parameters:
    df (pandas.DataFrame): The dataframe containing survey responses
    question_text (str): The exact text of the question to analyze

    Returns:
    pandas.DataFrame: A pivot table with years as rows and responses as columns
    """
    responses = df[df['question_text'] == question_text]
    return responses.groupby(['year', 'answer_text']).size().unstack(fill_value=0)


def categorize_gender(text):
    """
    Categorize gender responses into Male, Female, or Other
    """
    text = str(text).lower().strip()

    if text in ['male', 'm', 'man', 'cis male', 'male.', 'masculine', 'cis man']:
        return 'Male'
    elif text in ['female', 'f', 'woman', 'cis female', 'female.', 'feminine', 'cis woman']:
        return 'Female'
    else:
        return 'Other'


def calculate_prevalence_ci(df, question_text, positive_responses='Yes'):
    """
    Calculate prevalence and 95% CI for a condition

    Parameters:
    df: DataFrame containing survey responses
    question_text: The question to analyze
    positive_responses: String or list of strings that indicate a positive response

    Returns:
    tuple: (prevalence, ci_lower, ci_upper)
    """
    # Get total respondents for this question
    total_responses = df[df['question_text'] == question_text]['user_id'].nunique()

    # Get positive responses
    condition_df = df[df['question_text'] == question_text]
    if isinstance(positive_responses, str):
        positive_responses = [positive_responses]

    positive_count = condition_df[condition_df['answer_text'].isin(positive_responses)]['user_id'].nunique()

    # Calculate prevalence
    prevalence = (positive_count / total_responses) * 100

    # Calculate Wilson score interval
    z = 1.96  # 95% confidence
    n = total_responses
    p = prevalence / 100

    denominator = 1 + (z ** 2 / n)
    center = (p + (z ** 2) / (2 * n)) / denominator
    error = z * math.sqrt((p * (1 - p) + (z ** 2) / (4 * n)) / n) / denominator

    return prevalence, (center - error) * 100, (center + error) * 100
