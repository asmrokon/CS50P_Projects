def generate_varied_code(filename, total_lines=2058):
    with open(filename, "w") as f:
        lines_written = 0
        func_id = 0

        while lines_written < total_lines:
            # Write a function with a loop and some logic (7 lines each)
            func_id += 1
            f.write(f"def func_{func_id}(n):\n")
            f.write(f"    total = 0\n")
            f.write(f"    for i in range(n):\n")
            f.write(f"        if i % 2 == 0:\n")
            f.write(f"            total += i\n")
            f.write(f"        else:\n")
            f.write(f"            total -= i\n")
            f.write(f"    return total\n")
            lines_written += 8

            # Write 2 usage lines per function
            f.write(f"result_{func_id} = func_{func_id}(100)\n")
            f.write(f"print(result_{func_id})\n")
            lines_written += 2

        print(f"{lines_written} lines of code written to {filename}")

generate_varied_code("realistic_code_2058_lines.py")
