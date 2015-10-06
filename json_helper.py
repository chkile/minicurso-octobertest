import logging

def compare(expected, actual):
    """
    Checks each key from the expected json in the actual json.
    If all values checked match, returns True. Otherwise, returns False.
    """
    all_match = True
    for key, value in expected.iteritems():
        if not value==actual.get(key):
            logging.error("'%s' key did not match. Expected '%s', got '%s'" % (key, value, actual.get(key)))
            all_match = False
    return all_match
