def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
            return cats_info
        
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None
cats_info = get_cats_info(r"cats.txt")
if cats_info:
    print(*cats_info, sep='\n') 


