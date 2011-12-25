import string
import copy
import math

#http://www.pythonchallenge.com/pc/def/map.html
data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def letter_shift(letter, shift, alpha_list):
    # get index number of char in normal alphabetical list, for the provided letter
    i = string.index(string.ascii_lowercase, letter)
    # shift every character in the list
    shifted_alpha_list = rotate_list(alpha_list, shift)
    return shifted_alpha_list[i]

# http://bigbaldguy.livejournal.com/69844.html
def rotate_list(l, offset):
    """
    Rotate a list by (offset) elements. Elements which fall off
    one side are provided again on the other side.
    Returns a rotated copy of the list. If (offset) is 0,
    returns a copy of (l).
    
    Examples:
        >>> rotate_list([1, 2, 3, 4, 5, 6], 2)
        [3, 4, 5, 6, 1, 2]
        >>> rotate_list([1, 2, 3, 4, 5, 6], -2)
        [5, 6, 1, 2, 3, 4]
    """
    if len(l) == 0:
        raise ValueError("Must provide a list with 1 or more elements")
    if offset == 0:
        rv = copy.copy(l)
    else:
        real_offset = offset % int(math.copysign(len(l), offset))
        rv = (l[real_offset:] + l[:real_offset])
    return rv

def simple_decode(code, alpha_list, shift):
    out = []
    for l in code:
        if l in alpha_list:
            out.append(letter_shift(l, shift, alpha_list))
        else:
            out.append(l)
    return ''.join(out)

# turn the given data into an array of letters
data_list = list(data)

# get a list of lowercase alphabet characters
alpha_list = list(string.ascii_lowercase)

# decode the data (the long way)
print simple_decode(data, alpha_list, 2)

print "==========================="

# use `string.maketrans()` as suggested
roseta = string.maketrans("".join(alpha_list), "".join(rotate_list(alpha_list, 2)))
print data.translate(roseta)

