def save_clean_data(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for record in data:
            file.write(str(record) + "\n")
