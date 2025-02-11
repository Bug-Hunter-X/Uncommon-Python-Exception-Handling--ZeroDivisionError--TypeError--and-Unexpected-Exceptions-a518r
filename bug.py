def function_with_uncommon_error(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input type")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        return result
    finally:
        print("Execution completed")

print(function_with_uncommon_error(2))  # Output: 5.0, Execution completed
print(function_with_uncommon_error(0))  # Output: Error: Cannot divide by zero, Execution completed
print(function_with_uncommon_error('a')) # Output: Error: Invalid input type, Execution completed
print(function_with_uncommon_error(float('inf'))) #Output: 0.0, Execution completed
print(function_with_uncommon_error(float('nan'))) #Output: nan, Execution completed
