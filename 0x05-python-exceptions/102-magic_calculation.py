def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result += b + a
            break
        return result

    if __name__ == "__main__":
        # Example usage
        result = magic_calculation(3, 2)
        print("Result:", result)
