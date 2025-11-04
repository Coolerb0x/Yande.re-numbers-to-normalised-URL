import re

def process_yande_re_links_specific():

    with open('yinput.txt', 'r', encoding='utf-8') as f_in, \
         open('youtput.txt', 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            # Ищем числа после "yande.re" с любым количеством пробелов\Looking for numbers after "yande.re"
            match = re.search(r'yande\.re\s*(\d{4,})', line)
            if match:
                number = match.group(1)
                f_out.write(f"https://yande.re/post/show/{number}\n")
                print(f"Найдено: {number}")  # Для отладки\showing results for debugging
        
        print("Обработка завершена!")

# Запуск функции
process_yande_re_links_specific()
