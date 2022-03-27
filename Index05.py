def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum_digit=0
    if s[0].isdigit():
        sum_digit+=1
    if s[1].isdigit():
        sum_digit+=1
    if s[2].isdigit():
        sum_digit+=1
    if s[3].isdigit():
        sum_digit+=1
    if s[4].isdigit():
        sum_digit+=1            
    return sum_digit