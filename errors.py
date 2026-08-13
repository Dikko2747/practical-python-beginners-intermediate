def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        raise ValueError(f"Bad input: {e}") from e
    else:
        return result
    finally:
        print("Attempted division")


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
