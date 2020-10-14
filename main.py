from itertools import combinations

def normalize_username(username):
    '''
    Returns username after normalizing username given by user input.
    Normalizing involves lowercasing email and removing dots user may have entered.
    '''
    username = username.lower()
    return ''.join(filter(lambda c: c != '.', username))

def email_variations_helper(username, dot_count, mail_server, res):
    insertion_idxs = combinations([i for i in range(1, len(username))], dot_count)

    for point in insertion_idxs:
        i = 0
        new_username = list(username)

        for idx in point:
            new_username.insert(idx+i, '.')
            i += 1

        res.append(''.join(new_username)+'@'+mail_server)


def email_variations(email=None):
    '''
    Generates all combinations of valid email variations that redirect to email.
    '''
    main_email = input('What email do you want all variations for? ') if not email else email

    username, mail_server = main_email.split('@')
    username = normalize_username(username)

    max_dots = len(username) - 1

    res = []
    for i in range(1, max_dots+1):
        email_variations_helper(list(username), i, mail_server, res)

    return res
