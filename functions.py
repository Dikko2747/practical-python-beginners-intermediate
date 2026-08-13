def average(scores):
    """Mean of a list; 0 if empty."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def grade(avg, pass_mark=50):
    return "PASS" if avg >= pass_mark else "FAIL"


print(grade(average([48, 65, 71])))
