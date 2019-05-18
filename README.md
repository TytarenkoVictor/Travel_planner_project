# Travel planner project

### Курсова робота Титаренко Віктора на тему: "Розроблення засобів для планування подорожей."

## Короткий опис:
Travel planner має на меті допомогти молоді спланувати подорож та заощадити час і кошти. Він забезпечує користувача надійним та оптимально складеним маршрутом подорожі, який мінімізує витрати та максимізує враження та користь від подорожі. 
## Вимоги до введених даних:
Користувач повинен ввести дату початку подорожі у форматі dd/mm/yy.
<br>Користувач повинен ввести дату закінчення подорожі у форматі dd/mm/yy.
<br>Мінімальна тривалість подорожі 3 дні, максимальна 21 день.
<br>Можливість планування подорожі до 31/12/19 у зв'язку з відсутністю або недостатньою кількістю перельотів на 2020р.
## Результат виконання Travel planner:
Результатом виконання є web-додаток, який містить 4 поля для вводу даних: місто виїзду, місто призначення, дата виїзду та кінцева дата.
<br>У разі коректного вводу даних користувач отримує детальний маршрут подорожі, ціни в кожному місті, найпопулярніші туристичні місця, розгорнутий ціновий аналіз, прогноз загальних витрат на подорож та їх візуалізацію, посилання на бронювання перельотів та на туристичні місця.
## Реалізація Travel planner:
Система реалізована на основі LinkedQueue ADT, завдяки якому створено маршрут, кожен елемент якого є елементом LinkedQueue ADT.
<br>Окрім того, реалізовані класи Search для пошуку перельотів, CheckDate для перевірки введених даних, Time для визначення часових проміжків, CostOfLiving для аналізу цін на харчування та транспорт, TravelPlan для створення фінального маршруту.
## Опис даних Travel planner:
Дані отримані із сайтів kiwi.com, numbeo.com та wikitravel.com шляхом парсингу за допомогою BeautifulSoup4 та API.
## Запуск Travel planner:
Для запуску системи потрібно скористатися файлом connect.py та завантажити бібліотеки datetime, bs4, urllib, re, json, flask.
<br>Або перейти за посиланням: TytarenkoViktor.pythonanywhere.com
