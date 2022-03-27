def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    s=0
    if s[0].isdigit():
        s+=1
    if s[1].isdigit():
        s+=1
    if s[2].isdigit():
        s+=1
    if s[3].isdigit():
        s+=1
    if s[4].isdigit():
        s+=1            
    return s