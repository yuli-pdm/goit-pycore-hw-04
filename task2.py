from pathlib import Path


def get_cats_info(path: str) -> list[dict]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Пропускаємо порожні рядки
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")

                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": int(age)
                    }

                    cats.append(cat_info)

                except ValueError:
                    # Якщо рядок має неправильний формат
                    print(f"Skipping invalid line: {line}")

    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as e:
        print(f"Error reading file: {e}")

    return cats

if __name__ == "__main__":
    cats = get_cats_info("cats.txt")
    print(cats)

