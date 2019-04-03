import sys


def is_palindrome(string):
    return string == string[::-1]


def find_longest_palindrome(string):
    longest = str()

    for start_idx in range(0, len(string)):
        for end_idx in range(start_idx + 1, len(string) + 1):
            sub_string = string[start_idx:end_idx]

            if is_palindrome(sub_string) and len(sub_string) > len(longest):
                longest = sub_string

    return longest


# Example:
# $ python longest_palindrome.py "raaaaaaabcbaaaaaaar blanavolimilovanahablahabla raaaaaaacaaaaaaar"
# raaaaaaabcbaaaaaaar

def main(argv):
    check_input_arg(argv)

    string = argv[1]
    longest_palindrome = find_longest_palindrome(string)

    print(longest_palindrome)


def check_input_arg(argv):
    if len(argv) != 2:
        print("Usage: $ python longest_palindrome.py <some string>")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
