from django.conf import settings
from random import choice
from string import ascii_letters, digits
from django.core.exceptions import ObjectDoesNotExist

# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits


#-------------------another way by random, the problem is that the same compination can be choosen infinity times--------------------------
def create_random_code(chars=AVAIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    """
    option1: generate shortened URL until there is no duplicates (its ok because the probability is to large)
    """
    random_code = create_random_code()
    # Gets the model class
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code
#---------------------------------------------------------------------------------------------------------------------------------------------

def make_first_random_code():
    return "".join([AVAIABLE_CHARS[0] for _ in range(SIZE)])

def add_more_options(pre_shortener_url):
    """
    if we finished all the option (default is 62 ^ 7 ) so add another block of option (*62 options)
    for example: if we have just one letters the options are ('a' to 'z') + ('A' to 'Z') + (0 to 9) = 62
    62 options. if we add another block of option we got 62 * 62 = 3844
    and etc...

    We start with 7 blocks of options (62^7)
    """
    new_shortener_url = list(pre_shortener_url)
    for letter in new_shortener_url:
        if letter is not AVAIABLE_CHARS[len(AVAIABLE_CHARS) - 1]:  # check if all the chars are the last option and we have no more options
            return pre_shortener_url
    for i in range(len(new_shortener_url) - 1, -1, -1):  # run backwards on pre_shortener_url
        new_shortener_url[i] = AVAIABLE_CHARS[0]  # reset the blocks
    new_shortener_url.insert(0, AVAIABLE_CHARS[0])  # add first block
    return "".join(new_shortener_url)


def increase_by_one(pre_shortener_url):
    """
    in this method we add one step to our generate code
    """
    carry = 0
    pre_shortener_url = add_more_options(pre_shortener_url)
    new_shortener_url = list(pre_shortener_url)
    for i in range(len(new_shortener_url) - 1, -1, -1):  # run backwards on pre_shortener_url
        letter_index = AVAIABLE_CHARS.find(new_shortener_url[i])  # get the index from 62base
        if i == len(new_shortener_url) - 1:  # add one to first letter
            letter_index += 1
        letter_index += carry  # add carry if exist
        if letter_index >= len(AVAIABLE_CHARS):  # create carry if needs
            carry = 1
            new_shortener_url[i] = AVAIABLE_CHARS[0]  # return the letter to first letter of our 62base
        else:
            carry = 0
            new_shortener_url[i] = AVAIABLE_CHARS[letter_index]  # change letter or keep like it was
    return "".join(new_shortener_url)


def create_shortened_url(model_instance):
    model_class = model_instance.__class__
    try:
        shortener_url_object = model_class.objects.latest('created')
        return increase_by_one(shortener_url_object.short_url)
    except ObjectDoesNotExist:
        return make_first_random_code()
