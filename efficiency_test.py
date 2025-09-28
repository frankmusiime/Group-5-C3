#!/usr/bin/python3
"""
DSA Integration with SMS Transactions
Compare Linear Search vs Dictionary Lookup on sample transaction records.
Includes reflection explaining why dictionary lookup is faster.
Uses ANSI escape codes for colored output.
"""

import time

# --- ANSI Color Codes ---
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BRIGHT = "\033[1m"

# --- Sample Data: 20 Transactions ---
transactions = [{"id": i, "amount": i * 100} for i in range(1, 21)]
transactions_dict = {tx["id"]: tx for tx in transactions}


# --- 1. Linear Search (List-Based) ---
def linear_search(transactions_list, search_id):
    """Scan the list one by one until the record is found."""
    for tx in transactions_list:
        if tx["id"] == search_id:
            return tx
    return None


# --- 2. Dictionary Lookup ---
def dict_lookup(transactions_map, search_id):
    """Directly fetch the record using its key (id)."""
    return transactions_map.get(search_id, None)


# --- 3. Efficiency Measurement ---
def compare_efficiency(search_id):
    """Measure time taken for linear search vs dictionary lookup."""
    # Linear Search Timing
    start = time.time()
    result_linear = linear_search(transactions, search_id)
    end = time.time()
    linear_time = end - start

    # Dictionary Lookup Timing
    start = time.time()
    result_dict = dict_lookup(transactions_dict, search_id)
    end = time.time()
    dict_time = end - start

    # Print Results
    print(f"{CYAN}{BRIGHT}=== Search Efficiency Comparison ==={RESET}")
    print(f"{YELLOW}Searching for ID: {search_id}{RESET}")
    print(
        f"{WHITE}Linear Search Result: {result_linear}, "
        f"{GREEN}Time: {linear_time:.10f} seconds{RESET}"
    )
    print(
        f"{WHITE}Dictionary Lookup Result: {result_dict}, "
        f"{RED}Time: {dict_time:.10f} seconds{RESET}"
    )
    print(f"{MAGENTA}{'-' * 50}{RESET}")


# --- 4. Reflection ---
def reflection():
    """Explain why dictionary lookup is faster and suggest alternatives."""
    print(f"{MAGENTA}{BRIGHT}\nReflection\n{RESET}")
    print(f"{WHITE}Linear search goes through each record stepby step.{RESET}")
    print(
        f"{WHITE}Dictionary lookup is faster because it uses a hash function "
        f"to jump directly to the record without scanning all items.{RESET}"
    )
    print(
        f"{CYAN}This makes it much more efficient,"
        "especially for large datasets.{RESET}"
    )


# --- 5. Run Tests ---
if _name_ == "_main_":
    # Try with multiple IDs
    compare_efficiency(5)   # early in the list
    compare_efficiency(15)  # middle of the list
    compare_efficiency(20)  # last in the list

    # Print reflection
    reflection()