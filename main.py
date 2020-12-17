# Import Required packages
from preprocessing import preprocessing
from BoyerMoore import boyer_moore
from RabinKarp import rabin_karp
from KMP import kmp
from LCS import lcs

# Read the user's file
with open('Sample1.txt', 'r') as reader:
    user_file = reader.read()
user_file = preprocessing(user_file)


# Read the available file
with open('Sample2.txt', 'r') as reader:
    available_file = reader.read()
available_file = preprocessing(available_file)


rabin_karp_value = rabin_karp(user_file, available_file)
print("Rabin Karp:", rabin_karp_value)

boyer_moore_value = boyer_moore(user_file, available_file)
print("Boyer Moore:", boyer_moore_value)

kmp_value = kmp(user_file, available_file)
print("KMP:", kmp_value)

lcs_value = lcs(user_file, available_file)
print("LCS:", lcs_value)


if __name__ == '__main__':
    pass

