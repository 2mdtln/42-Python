# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_different_errors.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/18 12:12:31 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/21 22:22:03 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def garden_operations(op: str, string: str = "str", integer: int = 42,
                      file: str = "file.txt", key: str = "name"):
    return_val = 0
    if op in ("int", "all"):
        return_val = int(string)
    if op in ("100/", "all"):
        return_val = 100 / integer
    if op in ("open", "all"):
        f = open(file)
        f.close()
    if op in ("key", "all"):
        plants = {"cherry": "pink", "sunflower": "yellow"}
        print(plants[key])
    return return_val


def test_error_types():
    print("\nTesting ValueError...")
    try:
        garden_operations(op="int", string="aaa")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        print(garden_operations(op="100/", integer=0))
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(op="open", file="missing.txt")
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: No such file '{err.filename}'")
    print("\nTesting KeyError...")
    try:
        garden_operations(op="key", key="missing_plant")
    except KeyError as err:
        print(f"Caught KeyError: '{err.args[0]}'")
    print("\nTesting multiple errors together...")
    try:
        garden_operations(op="all", string=4, integer=3,
                          file="missing.txt", key="missing_plant")
    except Exception:
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
