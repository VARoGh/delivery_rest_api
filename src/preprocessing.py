import numpy as np
import pandas as pd
from loguru import logger

CFG = {}
CFG['all_features'] = ['items_count',
                       'distance_km',
                       'precip_mm',
                       'prep_time_avg',
                       'delivery_time_minutes_base',
                       'vehicle_type',
                       'time_of_day',
                       'traffic_level',
                       'is_fast_food',
                       'is_express_delivery']

CFG['log_features'] = ['distance_km',
                       'precip_mm',
                       'delivery_time_minutes_base']


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame | None:
    """
    Формирование новых кастомных признаков
    """
    try:
        # Читаем сырые данные из предыдущей задачи

        if df['base_speed_kmh'].item() <= 0:
            logger.warning(f"Найдены строки с некорректной скоростью в base_speed_kmh")
            raise ValueError("base_speed_kmh меньше или равно нулю")

        # Базовое время доставки - distance_km / base_speed_kmh
        df['delivery_time_minutes_base'] = df['distance_km'] * 60 / df['base_speed_kmh']

        # День недели
        df['day_of_week'] = df['order_datetime'].dt.day_name()

        # Время суток - утро, день, вечер, ночь
        bins = [0, 6, 12, 18, 24]
        labels = ['Ночь', 'Утро', 'День', 'Вечер']
        hours = df['order_datetime'].dt.hour
        df['time_of_day'] = pd.cut(hours, bins=bins, labels=labels, right=False, include_lowest=True)
        return df

    except Exception as e:
        logger.exception(f"Ошибка в feature_engineering: {e}")


def preprocess(df: pd.DataFrame) -> pd.DataFrame | None:
    """
    Предобработка данных
    Применяет те же преобразования, что использовались при обучении модели.
    """

    try:
        # Логарифмическое преобразование c проверкой больше нуля, так как при отр. значении логирифм log1p - RuntimeWarning
        for col in CFG["log_features"]:
            invalid = (df[col] < 0).sum()
            if invalid:
                logger.warning(f"В столбце {col} имеются отрицательные значения: {invalid}")
            df = df[~(df[col] < 0)]
            df[col] = np.log1p(df[col])

        return df

    except Exception as e:
        logger.exception(f"Ошибка в preprocess: {e}")
