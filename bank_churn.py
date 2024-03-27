from pathlib import Path
import pickle
import streamlit as st
from PIL import Image
import pandas as pd


# ====================== главная страница ============================
# параметры главной страницы
# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
# 1 control
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="bank_churn_project",
    page_icon="🧊",
)
# ----------- функции -------------------------------------

# функция для загрузки картинки с диска
# кэшируем, иначе каждый раз будет загружаться заново
@st.cache_data
def load_image(image_path):
    image = Image.open(image_path)
    # обрезка до нужного размера с сохранением пропорций
    MAX_SIZE = (800,600)
    image.thumbnail(MAX_SIZE)
    return image

# функция загрузки модели
# кэшируем, иначе каждый раз будет загружаться заново
@st.cache_data
def load_model(model_path):
    # загрузка сериализованной модели
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model


# ------------- загрузка картинки для страницы и модели ---------

# путь до картинки
image_path = Path.cwd() / 'hqdefault.jpg'
image = load_image(image_path)

# путь до модели
model_path = Path.cwd() / 'cat.pkl'
model_cat = load_model(model_path)


# ---------- отрисовка текста и картинки ------------------------
# 2 control
st.write(
    """
    # Прогноз оттока клиентов из банка
    Введите данные и получите результат
    """
)

# отрисовка картинки на странице
# 3 control
st.image(image)


# ====================== боковое меню для ввода данных ===============
# 4 control
st.sidebar.header('Введите данные')

# кнопки - слайдеры для ввода данных человека
# 5 control
def sidebar_input_features():
    gender = st.sidebar.selectbox("Пол клиента", ("Мужской", "Женский"))
    geo = st.sidebar.selectbox("Страна резидентства", (
    "Франция", "Германия", "Испания"))
    age = st.sidebar.slider("Возраст клиента", min_value=16, max_value=100, value=16,
                            step=1)

    credit = st.sidebar.slider("Кредитный скоринг клиента",min_value=0, max_value=1000, value=1, step=1)

    ten = st.sidebar.slider("Срок обслуживания клиента",
                               min_value=0, max_value=20, value=1, step=1)
    bal = st.sidebar.slider("Баланс счета клиента",
                               min_value=0, max_value=500000, value=1, step=1)
    sal = st.sidebar.slider("Зарплата клиента",
                               min_value=0, max_value=500000, value=1, step=1)
    numprod = st.sidebar.slider("Количество сервисов банка у клиента",
                               min_value=0, max_value=10, value=1, step=1)
    translatetion = {
        "Мужской": "Male",
        "Женский": "Female",
        "Франция": "France",
        "Германия": "Germany",
        "Испания": "Spain",
       }

    data = {
        "CreditScore": credit,
        "Geography": translatetion[geo],
        "Gender": gender,
        "Age": age,
        "Tenure": ten,
        "Balance": bal,
        "NumOfProducts": numprod,
        "EstimatedSalary": sal,
    }

    df = pd.DataFrame(data, index=[0])

    return df

    
x_test=sidebar_input_features()
prediction = model_cat.predict_proba(x_test)
pred_churn=prediction[:,1]
pred_churn=int(pred_churn*100)

# вывести предсказание модели
st.write("## Вероятность ухода клиента из банка:")
st.write(pred_churn, '%')

