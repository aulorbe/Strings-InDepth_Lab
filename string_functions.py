def say_hello(name):
    def say_hello(name):
    print(f"Hi my name is {name}")

def replace_given_substring(str_to_replace, str_to_insert, string):
    def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace,str_to_insert)

def remove_duplicate_punctuation(string):
    spec_chars = list(set(re.findall('[^A-Z^a-z\s]', s)))
    for spec in spec_chars:
        s = re.sub('[' + spec + ']+', spec, s)
    return s


def validate_email_format(email):
    def validate_email_format(email):
    regex = '\w+\@\w+.com'
    output = re.match(regex,email)
    if output:
        return True
    else:
        return False


def anonymize_credit_card_number(credit_card_number):
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    pass
