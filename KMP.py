import re


def compute_lps_array(pattern):
    pattern_length = len(pattern)
    lps_array = [0] * pattern_length
    pattern_ptr = 0
    current = 1
    while current < pattern_length:
        if pattern[pattern_ptr] == pattern[current]:
            pattern_ptr += 1
            lps_array[current] = pattern_ptr
            current += 1
        else:
            if pattern_ptr != 0:
                pattern_ptr = lps_array[pattern_ptr-1]
            else:
                lps_array[current] = 0
                current += 1
    return lps_array


def kmp_engine(pattern, text, p):
    pattern_length = len(pattern)
    text_length = len(text)
    lps_array = compute_lps_array(pattern)
    i = 0
    j = 0
    while i < text_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == pattern_length:
            p += 1
            j = lps_array[j - 1]
            break
        elif i < text_length and pattern[j] != text[i]:
            if j != 0:
                j = lps_array[j - 1]
            else:
                i += 1
    return p


def kmp(main_content, other_content):
    user_string_list = []
    number_of_user_strings = 0
    for sentence in main_content:
        number_of_user_strings += 1
        user_string_list.append(" ".join(sentence))
    # user_string = " ".join(user_string_list)

    available_string_list = []
    number_of_available_string = 0
    for sentence in other_content:
        number_of_available_string += 1
        available_string_list.append(" ".join(sentence))
    available_string = " ".join(available_string_list)

    counter_matched = 0
    counter_total = 0
    p = 0
    for pattern in user_string_list:
        pattern = pattern.strip()

        if len(pattern) > 0:
            counter_total += 1
            counter_matched += kmp_engine(pattern, available_string, p)
    return (counter_matched * 100) / counter_total
