import re


def boyer_moore_engine(other_content, main_content, no_other, no_main):
    """
    :param other_content: is the available content is web
    :param main_content: user's content
    :param no_other: number of sentences in other's content
    :param no_main: number of sentences in user's content
    :return: returns the amount of plagiarism.
    """
    counter_matched = 0;
    ready_data = re.split(r'[.]', other_content)
    for pattern in ready_data:
        pattern = pattern.strip()
        if len(pattern) > 0:
            pattern_start_pos = 0
            found = 0
            while pattern_start_pos + len(pattern) <= len(main_content):
                # select a substring of the text of equal length to the pattern,
                # and search from right to left
                j = pattern_start_pos + len(pattern)
                for i in range(0, len(pattern))[::-1]:
                    # print(test)
                    # if the characters in text and pattern match -
                    if pattern[i].lower() == main_content[j - 1].lower():
                        j = j - 1
                        if j == pattern_start_pos:
                            found = 1
                            break
                        else:
                            continue

                    # if the characters in text and pattern do not match -
                    else:
                        # if the 'mismatched' character does not appear in the pattern,
                        # move the pattern 'n' characters ahead
                        if pattern[0:i].rfind(main_content[j - 1]) == -1:
                            pattern_start_pos = pattern_start_pos + len(pattern)
                            break

                        # if the 'mismatched' character appears in the pattern,
                        # move the pattern so that the matching characters are aligned
                        else:
                            pattern_start_pos = pattern_start_pos + len(pattern) - pattern[0:i].rfind(
                                main_content[j - 1]) - 1
                            break

                # the first if statement in the for loop above has found the complete pattern in the text
                if found == 1:
                    counter_matched = counter_matched + 1
                    break
    # return 2 * counter_matched * 100 / (no_other + no_main)
    return counter_matched * 100 / no_main


def boyer_moore(main_content, other_content):
    user_string_list = []
    number_of_user_strings = 0
    for sentence in main_content:
        number_of_user_strings += 1
        user_string_list.append(" ".join(sentence))
    user_string = ".".join(user_string_list)

    available_string_list = []
    number_of_available_string = 0
    for sentence in other_content:
        number_of_available_string += 1
        available_string_list.append(" ".join(sentence))
    available_string = ".".join(available_string_list)
    return boyer_moore_engine(available_string, user_string,
                              number_of_available_string, number_of_user_strings)

