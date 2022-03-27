def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sd=0
    if s[0].isdigit():
        sd+=int(s[0])
    if s[1].isdigit():
        sd+=int(s[1])
    if s[2].isdigit():
        sd+=int(s[2])
    if s[3].isdigit():
        sd+=int(s[3])  
    if s[4].isdigit():
        sd+=int(s[4])
    return sd
                    