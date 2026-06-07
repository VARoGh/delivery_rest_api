# 🚀 Model as a Service (FastAPI)

Пример реализации подхода **Model as a Service (MaaS)** для задач машинного обучения.
Проект демонстрирует, как обученную ML-модель обернуть в REST API с использованием **FastAPI**.

Модель принимает параметры доставки и возвращает предсказанное время доставки.

---

## 📁 Структура проекта

```text
SIM-DS-MODEL-AS-A-SERVICE/
├── models/
│   ├── .gitkeep
│   └── model.joblib          # Сохранённая ML-модель
│
├── src/
│   ├── __init__.py
│   ├── app.py                # FastAPI-приложение (entrypoint)
│   ├── inference.py          # Загрузка модели и инференс
│   └── preprocessing.py      # Препроцессинг данных
│
├── tests/                    # (опционально) тесты
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Архитектура

**Pipeline:**

1. `preprocessing.py` — подготовка данных
2. `model.joblib` — сохранённая модель

**Inference / API:**

* `inference.py` — загрузка модели и предсказание
* `app.py` — REST API (FastAPI)

---

## 🛠️ Установка и запуск

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/VARoGh/delivery_rest_api.git
```

---

### 2️⃣ Создание виртуального окружения

#### 🪟 Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> ⚠️ Если PowerShell ругается на политику выполнения:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

#### 🍎 macOS / 🐧 Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 🚀 Запуск FastAPI

```bash
uvicorn src.app:app --reload --port 8890
```

API будет доступно по адресу:

👉 [http://127.0.0.1:8890](http://127.0.0.1:8890)

---

## 📚 Swagger / OpenAPI

FastAPI автоматически генерирует документацию:

* Swagger UI:
  👉 [http://127.0.0.1:8890/docs](http://127.0.0.1:8890/docs)

* OpenAPI schema:
  👉 [http://127.0.0.1:8890/redoc](http://127.0.0.1:8890/redoc)

---

## 🔮 Пример запроса

### POST `/predict`

**Request body:**

```json
{
    "order_datetime": "2025-03-13 20:27:00",
    "items_count": 2,
    "distance_km": 3.5,
    "precip_mm": 2.5,
    "prep_time_avg": 5.7,
    "base_speed_kmh": 55,
    "vehicle_type": "car",
    "traffic_level": 4,
    "is_fast_food": 1,
    "is_express_delivery": 0
}
```

**Response:**

```json
{
  "predicted": 58.5
}
```

---

## 🧩 Используемые технологии

* Python 3.12+
* FastAPI
* Pydantic
* Scikit-learn
* Pandas
* Joblib
* Uvicorn
* Loguru

---

## 🎯 Цель проекта

Проект демонстрирует:

* деплой ML-модели как сервиса
* best practices структуры ML-проекта
* работу с FastAPI и Swagger