import re
import string

def sum_of_letters_a1(word):
    return sum([ord(c.upper())-64 for c in word])

def base26(word):
    word = word.upper()
    table = string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789ABCDEFGHIJKLMNOP")
    return int(word.translate(table), 26)

RANGE_RE = re.compile(r"between (\d*) and (\d*) \(inclusive\)")
PERCENTAGE_RE = re.compile(r"exactly (.*)% of the letters")
PERCENT_RANGE_RE = re.compile(r"between (.*)% and (.*)% \(inclusive\) of the letters")
def value_matches(description, value, wordlen):
    """Returns True if value fits the provided description string.

    Args:
      description: A string that describes the value. One of:
         #: An exact numerical value to match.
         between # and # (inclusive): A range of values to match.
         exactly #% of the letters: An exact percentage of the length to match.
         between #% and #% (inclusive) of the letters: A range of percentages to match.
      value: A value to check against the description.
      wordlen: The length of the word, for use in calculating percentages.

    Returns: True if the value fits."""
    ran = RANGE_RE.match(description)
    if ran:
        low = int(ran.group(1))
        high = int(ran.group(2))
        return value >= low and value <= high

    percentage = PERCENTAGE_RE.match(description)
    if percentage:
        pct = float(percentage.group(1))
        if 0.1 > abs(pct - value / wordlen):
            return True
        return False
    
    percent_range = PERCENT_RANGE_RE.match(description)
    if percent_range:
        low = float(percent_range.group(1))
        high = float(percent_range.group(2))
        pct = float(value) * 100 / wordlen
        return pct >= low and pct <= high

    return value == int(description)
