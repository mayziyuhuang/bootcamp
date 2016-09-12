def valid_secondary_structure(seq):
    """make sure the number of closed parentheses is equal to the number of open parentheses"""

    open_parenthese = seq.count('(')
    close_parenthese = seq.count(')')

    return open_parenthese == close_parenthese

#exercise solution
#def parens_count(struc):
#    """
#    Ensures there are equal number of open and closed parentheses
#    in structure.
#    """
#    return struc.count('(') == struc.count(')')

#def dotparen_to_bp(seq):
#    """converts the dot-parens notation to a tuple"""

#    i = seq.find('(')
#    j = seq.rfind(')')
#    bp = (seq.pop(i), seq.pop(j))

#    return bp

#exercise solution
def dot_parens_to_bp(struc):
    """
    Convert a dot-parens structure to a list of base pairs.
    Return False if the structure is invalid.
    """

    #if not parens_count(struc):
    if not valid_secondary_structure(struc):
        print('Error in input structure.')
        return False

    # Initialize list of open parens and list of base pairs
    open_parens = []
    bps = []

    # Scan through string
    for i, x in enumerate(struc):
        if x == '(':
            open_parens.append(i)
        elif x == ')':
            if len(open_parens) > 0:
                bps.append((open_parens.pop(), i))
            else:
                print('Error in input structure.')
                return False

    # Return the result as a tuple
    return tuple(sorted(bps))

#exercise solution
def hairpin_check(bps):
    """Check to make sure no hairpins are too short."""
    for bp in bps:
        if bp[1] - bp[0] < 4:
            print('A hairpin is too short.')
            return False

    # Everything checks out
    return True

#exercise solution
def rna_ss_validator(seq, sec_struc, wobble=True):
    """Validate and RNA structure"""

    # Convert structure to base pairs
    bps = dot_parens_to_bp(sec_struc)

    # If this failed, the structure was invalid
    if not bps:
        return False

    # Do the hairpin check
    if not hairpin_check(bps):
        return False

    # Possible base pairs
    if wobble:
        ok_bps = ('gc', 'cg', 'au', 'ua', 'gu', 'ug')
    else:
        ok_bps = ('gc', 'cg', 'au', 'ua')

    # Check complementarity
    for bp in bps:
        bp_str = (seq[bp[0]] + seq[bp[1]]).lower()
        if bp_str not in ok_bps:
            print('Invalid base pair.')
            return False

    # Everything passed
    return True
