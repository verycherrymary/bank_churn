1) Автор проекта - Сучкова Мария
2) Проект - приложение на streamlit предсказывает - уйдет клиент из банка или нет.
3) Датасет взят с соревнования на Kaggle (Binary Classification with a Bank Churn Dataset
Playground Series - Season 4, Episode 1)

Набор данных об оттоке клиентов банка — это часто используемый набор данных для прогнозирования оттока клиентов в банковской сфере. Содержит информацию о клиентах банка, которые либо покинули банк, либо продолжают оставаться его клиентами. 
Набор данных включает в себя следующие атрибуты:

- Customer ID: A unique identifier for each customer - уникальный номер клиента
- Surname: The customer's surname or last name - ФИО клиента
- Credit Score: A numerical value representing the customer's credit score - значение кредитного скоринга
- Geography: The country where the customer resides (France, Spain or Germany) - страна резидентства клиента
- Gender: The customer's gender (Male or Female) -пол клиента
- Age: The customer's age. - возраст клиента
- Tenure: The number of years the customer has been with the bank - сколько лет данный клиент обслуживается в банке
- Balance: The customer's account balance - баланс на счете клиента
- NumOfProducts: The number of bank products the customer uses (e.g., savings account, credit card) -кол-во продуктов банка, которыми пользуется клиент
- HasCrCard: Whether the customer has a credit card (1 = yes, 0 = no) - есть ли кредитная карта банка
- IsActiveMember: Whether the customer is an active member (1 = yes, 0 = no) - активный участник или нет
- EstimatedSalary: The estimated salary of the customer - примерная зарплата клиента
- Exited: Whether the customer has churned (1 = yes, 0 = no) - таргет- клиент покинет банк или нет

Прогноз делает модель Catboost,обученная на этих данных 
