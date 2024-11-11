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
