def total_salary(path: str) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Skipping invalid line: {line}")

        if count == 0:
            return (0, 0.0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Error: File not found.")
        return (0, 0.0)
    except OSError as e:
        print(f"Error reading file: {e}")
        return (0, 0.0)
    
result = total_salary("salaries.txt")
print(result)