import tkinter as tk
from tkinter import ttk

rules = [
    {
        "condition": lambda facts: facts["long_absence"] == "Да",
        "action": lambda facts: "Рекомендация: Перейти в режим максимального энергосбережения: выключить все некритичные электроприборы, установить минимально допустимую температуру отопления/кондиционирования. Отключить освещение, отключить подогрев воды (если есть)."
    },
    {
        "condition": lambda facts: facts["time_of_day"] == "Утро" and facts["weather_conditions"] == "Солнечно" and facts["people_in_house"] == "Никого (0)" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Уменьшить яркость освещения до минимума или выключить свет, снизить интенсивность кондиционирования/отопления. Закрыть жалюзи (если есть). Отключить неиспользуемую технику."
    },
    {
        "condition": lambda facts: facts["time_of_day"] in ["День", "Вечер"] and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Поддерживать комфортное освещение и температуру. Использовать энергосберегающие лампы. Настроить кондиционер/отопление на поддержание оптимальной температуры. Закрыть жалюзи (если жарко и солнечно). Убедиться, что неиспользуемая техника выключена."
    },
    {
        "condition": lambda facts: facts["time_of_day"] == "Ночь" and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Включить ночной режим освещения (приглушенный свет). Снизить температуру отопления на 1-2 градуса (для комфортного сна). Отключить некритичные электроприборы."
    },
    {
        "condition": lambda facts: facts["temperature_outside"] in ["Холодно (от -10°C до 0°C)", "Очень холодно (ниже -10°C)"] and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["elderly_children"] == "Да" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Увеличить температуру отопления, убедиться, что обогрев достаточен для пожилых людей и детей. Использовать дополнительные обогреватели (при необходимости). Проверить отсутствие сквозняков."
    },
        {
        "condition": lambda facts: facts["time_of_day"] == "Утро" and facts["weather_conditions"] == "Пасмурно" and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Включить умеренное освещение, настроить температуру на комфортный уровень. Использовать энергосберегающие лампы."
    },
    {
        "condition": lambda facts: facts["time_of_day"] == "День" and facts["weather_conditions"] == "Дождь" and facts["people_in_house"] == "Никого (0)" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Снизить освещение до минимума, отключить электроприборы, кроме систем безопасности."
    },
    {
        "condition": lambda facts: facts["temperature_outside"] in ["Тепло (от +20°C до +30°C)", "Жарко (выше +30°C)"] and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Использовать кондиционирование воздуха эффективно. Закрыть жалюзи/шторы в солнечной стороне. Отключить неиспользуемые электроприборы."
    },
    {
        "condition": lambda facts: facts["temperature_outside"] == "Комфортно (от +10°C до +20°C)" and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Поддерживать текущую температуру, использовать естественное освещение по возможности."
    },
    {
        "condition": lambda facts: facts["time_of_day"] == "Вечер" and facts["weather_conditions"] == "Ветер" and facts["people_in_house"] == "Никого (0)" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Убедиться, что все окна закрыты. Уменьшить температуру отопления."
    },
    {
        "condition": lambda facts: facts["time_of_day"] == "Ночь" and facts["weather_conditions"] == "Холодно (от -10°C до 0°C)" and facts["people_in_house"] in ["Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Использовать обогреватель с таймером. Проверить утепление окон."
    },
    {
        "condition": lambda facts:  facts["people_in_house"] == "Один человек (1)" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Использовать зональное освещение и обогрев. Отключать неиспользуемые электроприборы."
    },

    {
        "condition": lambda facts: facts["elderly_children"] == "Да" and facts["temperature_outside"] == "Жарко (выше +30°C)" and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Обеспечить прохладу и достаточное увлажнение воздуха. Избегать прямых солнечных лучей."
    },
    {
        "condition": lambda facts: facts["weather_conditions"] in ["Снег", "Дождь"] and facts["temperature_outside"] in ["Холодно (от -10°C до 0°C)", "Очень холодно (ниже -10°C)"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Проверить систему отопления. Убедиться в отсутствии утечек тепла."
    },
        {
        "condition": lambda facts: facts["people_in_house"] == "Много людей (4 и более)" and facts["time_of_day"] in ["День", "Вечер"] and facts["long_absence"] == "Нет",
        "action": lambda facts: "Рекомендация: Использовать энергосберегающие приборы. Следить за разумным использованием электроэнергии."
    }
]

questions = [
    {
        "question": "Текущее время суток:",
        "options": ["Утро", "День", "Вечер", "Ночь"],
        "fact_key": "time_of_day"
    },
    {
        "question": "Погодные условия на улице:",
        "options": ["Солнечно", "Облачно", "Пасмурно", "Дождь", "Снег", "Ветер"],
        "fact_key": "weather_conditions"
    },
    {
        "question": "Примерная температура на улице:",
        "options": ["Очень холодно (ниже -10°C)", "Холодно (от -10°C до 0°C)", "Прохладно (от 0°C до +10°C)", "Комфортно (от +10°C до +20°C)", "Тепло (от +20°C до +30°C)", "Жарко (выше +30°C)"],
        "fact_key": "temperature_outside"
    },
    {
        "question": "Сколько людей в доме:",
        "options": ["Никого (0)", "Один человек (1)", "Несколько человек (2-3)", "Много людей (4 и более)"],
        "fact_key": "people_in_house"
    },
    {
        "question": "Присутствуют ли пожилые люди или маленькие дети?:",
        "options": ["Да", "Нет"],
        "fact_key": "elderly_children"
    },
    {
        "question": "Планируется ли длительное отсутствие дома (более 4 часов)?:",
        "options": ["Да", "Нет"],
        "fact_key": "long_absence"
    }
]

def optimize_energy(facts, rules):
    """Применяет правила к фактам и возвращает рекомендации."""
    recommendations = []
    for rule in rules:
        if rule["condition"](facts):
            recommendations.append(rule["action"](facts))
            break  # Apply only the first matching rule
    if not recommendations:
        return "Рекомендаций по оптимизации энергопотребления на основе введенных данных нет."
    else:
        return "\n".join(recommendations)

def get_recommendations():
    """Gets user facts from GUI and displays recommendations."""
    facts = {}
    for q in questions:
        facts[q["fact_key"]] = q["variable"].get()

    recommendation_result = optimize_energy(facts, rules)
    recommendation_label.config(text=recommendation_result)

# --- Tkinter GUI ---
root = tk.Tk()
root.title("Оптимизация энергопотребления умного дома")

# Create variables to store user's choices
for q in questions:
    q["variable"] = tk.StringVar(value=q["options"][0])

# Create and place labels and option menus
for i, q in enumerate(questions):
    label = tk.Label(root, text=q["question"], anchor="w")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    option_menu = ttk.OptionMenu(root, q["variable"], q["options"][0], *q["options"])
    option_menu.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

# Create and place the button
button = ttk.Button(root, text="Получить рекомендации", command=get_recommendations)
button.grid(row=len(questions), column=0, columnspan=2, pady=10)

#Create and place the label for results
recommendation_label = tk.Label(root, text="", wraplength=500, justify='left')
recommendation_label.grid(row=len(questions) + 1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

root.mainloop()