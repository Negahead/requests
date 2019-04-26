import sys

# This code exists for backwards compatibility reasons.
# I don't like it either. Just look the other way. :)

for package in ('urllib3', 'idna', 'chardet'):
    # __import__ is a function to import modules specifically for the python interpreter
    # locals(): Return a dictionary containing the current scope's local variables.
    # updates to this dictionary will affect name lookups in the local scope
    locals()[package] = __import__(package)
    # This traversal is apparently necessary such that the identities are
    # preserved (requests.packages.urllib3.* is urllib3.*)

    # sys.modules contains all the modules available currently
    for mod in list(sys.modules):  # `mod` is of str type
        if mod == package or mod.startswith(package + '.'):
            sys.modules['requests.packages.' + mod] = sys.modules[mod]

# Kinda cool, though, right?
