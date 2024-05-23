import csv
import matplotlib.pyplot as plt

# Функция для чтения данных из CSV-файла
def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовочную строку
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
    return data

# Функция для вычисления процента проданных товаров
def calculate_percentage_sold(data):
    total_quantity_sold = sum([int(row[4]) for row in data])
    percentage_sold = {}
    for row in data:
        product = row[2]
        quantity_sold = int(row[4])
        percentage = (quantity_sold / total_quantity_sold) * 100
        percentage_sold[product] = percentage
    return percentage_sold

# Функция для сохранения результатов в текстовом файле
def save_results(file_path, total_revenue, most_sold_product, highest_revenue_product, percentage_sold):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            file.write(f"Общий доход: ${total_revenue}\n")
            file.write(f"Самый продаваемый товар: {most_sold_product}\n")
            file.write(f"Товар с наибольшим доходом: {highest_revenue_product}\n")
            file.write("\n")
            file.write("Процент продажи каждого товара:\n")
            for product, percentage in percentage_sold.items():
                file.write(f"{product}: {percentage:.2f}%\n")
        print("Результаты сохранены в файл успешно.")
    except Exception as e:
        print(f"Ошибка при сохранении результатов в файле {file_path}: {e}")

# Путь к CSV-файлу
file_path = 'sales_data.csv'
# Путь к файлу результатов
output_file_path = 'results.txt'

try:
    # Чтение данных из CSV-файла
    data = read_csv_file(file_path)
    
    # Вычисление общего дохода
    total_revenue = sum(float(row[4]) * float(row[5]) for row in data)
    
    # Поиск самого продаваемого товара
    most_sold_product = max(data, key=lambda x: int(x[4]))[2]
    
    # Поиск товара с наибольшим доходом
    highest_revenue_product = max(data, key=lambda x: float(x[4]) * float(x[5]))[2]
    
    # Вычисление процента продажи каждого товара
    percentage_sold = calculate_percentage_sold(data)
    
    # Сохранение результатов в текстовом файле
    save_results(output_file_path, total_revenue, most_sold_product, highest_revenue_product, percentage_sold)

    # Построение графика
    products = list(percentage_sold.keys())
    percentages = list(percentage_sold.values())

    plt.figure(figsize=(8, 6))
    plt.bar(products, percentages, color='skyblue')
    plt.xlabel('Товар')
    plt.ylabel('Процент (%)')
    plt.title('Диаграмма процента продажи каждого товара')
    plt.xticks(rotation=45, ha='right')
    plt.show()

except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
