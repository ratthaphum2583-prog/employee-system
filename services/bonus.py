from config import HIGH_SALARY_THRESHOLD, HIGH_BONUS_RATE, NORMAL_BONUS_RATE, INACTIVE_BONUS_RATE

def calculate_bonus(salary, active):
    if active and salary >= HIGH_SALARY_THRESHOLD:
        bonus = salary * HIGH_BONUS_RATE / 100
    elif active and salary < HIGH_SALARY_THRESHOLD:
        bonus = salary * NORMAL_BONUS_RATE / 100
    else:
        bonus = INACTIVE_BONUS_RATE

    return bonus

if __name__ == "__main__":
    print(calculate_bonus(32000, True))
    print(calculate_bonus(26000, True))
    print(calculate_bonus(40000, False))