def say_hello(name):
    def say_hello(name):
    print(f"Hi my name is {name}")

def replace_given_substring(str_to_replace, str_to_insert, string):
    def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace,str_to_insert)

def remove_duplicate_punctuation(string):
    # should remove all duplicate punctuation marks in a given string
    # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
    # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"
    pass


def validate_email_format(email):
    # should make sure there are no special characters (i.e. *,~,#,$,%,&,(,),`,",',:,;,/,>,<)
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise
    pass


def anonymize_credit_card_number(credit_card_number):
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    pass
