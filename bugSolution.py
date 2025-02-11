def function_with_uncommon_error(x):
    try:
        if x == float('inf') or x == float('nan'):
            return 0.0 if x == float('inf') else float('nan')
        result = 10 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return result
    finally:
        print("Execution completed")

print(function_with_uncommon_error(2))  # Output: 5.0, Execution completed
print(function_with_uncommon_error(0))  # Output: Error: Cannot divide by zero, Execution completed
print(function_with_uncommon_error('a')) # Output: Error: Invalid input type, Execution completed
print(function_with_uncommon_error(float('inf'))) #Output: 0.0, Execution completed
print(function_with_uncommon_error(float('nan'))) #Output: nan, Execution completed