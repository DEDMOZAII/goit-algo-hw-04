def total_salary(path):  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(float(salary))

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, average

    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None
total, average = total_salary("HM2\salarys.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")