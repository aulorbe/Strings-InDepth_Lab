import re

def say_hello(name):
    print(f"Hi my name is {name}")

def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace,str_to_insert)

def remove_duplicate_punctuation(string):
    spec_chars = list(set(re.findall('[^A-Z^a-z\s]', s)))
    for spec in spec_chars:
        s = re.sub('[' + spec + ']+', spec, s)
    return s

def validate_email_format(email):
    regex = '\w+\@\w+.com'
    output = re.match(regex,email)
    if output:
        return True
    else:
        return False
validate_email_format('aulorbegmail.com')


def anonymize_credit_card_number(cc):
    all_x = ''

    for c in cc:
        if c.isdigit():
            all_x += ('X')
        else:
            all_x += (c)

    return ((all_x[:-4]) + cc[-4:])
