total_test_runs = 0
failed_test_count = 0

def eq(actual, expected):
    return actual == expected

def not_eq(actual, expected):
    return actual != expected

def expected_to(func, actual, expected):
    def with_message(message):
        if not func(actual, expected):
            global failed_test_count
            failed_test_count += 1
            quick_print(message)
            quick_print("  Test failed. Expected:", expected, "Actual:", actual)
        global total_test_runs
        total_test_runs += 1
    return with_message

def test(message, expected_to):
    return expected_to(message)

def report():
    quick_print("Total tests run:", total_test_runs)
    quick_print("Total tests failed:", failed_test_count)
    if failed_test_count == 0:
        quick_print("All tests passed!")
