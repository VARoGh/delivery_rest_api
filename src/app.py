"""
Module: app.py

Description:
    Точка входа FastAPI-приложения.
    Отвечает за:
    - инициализацию API
    - загрузку обученной ML-модели
    - приём HTTP-запросов
    - возврат предсказаний модели
"""

import os

# FastAPI — фреймворк для создания REST API
from fastapi import FastAPI, HTTPException

# Pydantic используется FastAPI для валидации входных и выходных данных
from pydantic import BaseModel

import pandas as pd

# Loguru — удобный логгер для логирования событий приложения
from loguru import logger

# Импорт функций инференса:
# load_model — загрузка сохранённой модели
# predict — получение предсказаний
from src.inference import load_model, predict
from src.preprocessing import feature_engineering, preprocess
from catboost import CatBoostRegressor

# Создаём экземпляр FastAPI-приложения
app = FastAPI()


# ====== Pydantic-модели ======

class DeliveryFeatures(BaseModel):
    """
    Схема входных данных для модели.

    Используется FastAPI для:
    - валидации входного JSON
    - автогенерации Swagger-документации
    """
    order_datetime: str
    items_count: int
    distance_km: float
    precip_mm: float
    prep_time_avg: float
    distance_km: float
    base_speed_kmh: float
    vehicle_type: str
    traffic_level: int
    is_fast_food: int
    is_express_delivery: int


class DeliveryPrediction(BaseModel):
    """
    Схема ответа API.

    Гарантирует, что клиент всегда получит
    предсказанный время доставки.
    """
    predicted: float


# ====== Загрузка модели ======

# Логируем старт загрузки модели
logger.info("Loading model")

# Путь до сохранённой модели
MODEL_PATH = os.path.join("models", "model_cbr_delivery.pkl")

# Загружаем модель один раз при старте приложения,
# а не при каждом запросе (важно для производительности)
MODEL = load_model(MODEL_PATH)

logger.info("Model loaded successfully")


# ====== Endpoints ======

# Декоратор @app.get("/") регистрирует функцию как обработчик GET-запросов по корневому пути "/"
# GET-запросы обычно используются для получения данных (без изменения состояния сервера)
@app.get("/")
def health_check():
    """
    Health-check endpoint.

    Используется для проверки, что сервис жив
    (например, в Docker, Kubernetes, monitoring).
    """
    return {"status": "ok"}


# @app.post указывает, что это endpoint для обработки POST-запросов
# POST обычно используется для отправки данных на сервер (как в нашем случае - признаков для предсказания)
# response_model=DeliveryPrediction - указывает FastAPI на формат выходных данных
# Это обеспечивает автоматическую валидацию и документацию в Swagger
@app.post("/predict", response_model=DeliveryPrediction)
def get_prediction(features: DeliveryFeatures):
    """
    Endpoint для получения предсказания ML-модели.

    Parameters
    ----------
    features : DeliveryFeatures
        Признаки, переданные в JSON.

    Returns
    -------
    DeliveryPrediction
        Предсказанное время доставки.
    """
    try:
        # Преобразуем входные данные в DataFrame,
        # т.к. большинство sklearn-моделей ожидают именно такой формат
        data = pd.DataFrame([features.model_dump()])
        data['order_datetime'] = pd.to_datetime(data['order_datetime'])

        # Обработка и преобразование данных
        data = feature_engineering(data)
        if data is None:
            raise 
        data = preprocess(data)
        if data is None:
            raise

        # Получаем предсказание модели
        print(MODEL)
        predicted = predict(MODEL, data)

        logger.info(f"Predicted = {predicted}" )

    except Exception as e:
        # Логируем ошибку и возвращаем HTTP 500
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )

    # Возвращаем результат в формате Pydantic-модели
    return DeliveryPrediction(predicted=predicted)
