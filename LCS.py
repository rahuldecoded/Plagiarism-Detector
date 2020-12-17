import numpy as np


def lcs_engine(answer_text, source_text):
    """
    Computes the longest common subsequence of words in two texts; returns a normalized value.
    :param answer_text: The pre-processed text for an answer text
    :param source_text: The pre-processed text for an answer's associated source text
    :return: A normalized LCS value
    """

    # separate into list entries to simulate matrix
    answer_words = answer_text.split()
    source_words = source_text.split()

    n = len(answer_words)
    m = len(source_words)

    lcs_matrix = np.zeros((n + 1, m + 1))

    # iterate through words, finding longest common subsequence using dynamic programming
    i = j = 1
    for answer_word in answer_words:
        j = 1
        for source_word in source_words:
            if answer_word == source_word:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i][j - 1], lcs_matrix[i - 1][j])

            j += 1

        i += 1

    lcs_normalized = lcs_matrix[n][m] / n

    return lcs_normalized * 100


def lcs(main_content, other_content):
    user_string_list = []
    number_of_user_strings = 0
    for sentence in main_content:
        number_of_user_strings += 1
        user_string_list.append(" ".join(sentence))
    user_string = " ".join(user_string_list)

    available_string_list = []
    number_of_available_string = 0
    for sentence in other_content:
        number_of_available_string += 1
        available_string_list.append(" ".join(sentence))
    available_string = " ".join(available_string_list)

    return lcs_engine(user_string, available_string)
