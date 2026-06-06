# 🚀 Model as a Service (FastAPI)

Пример реализации подхода **Model as a Service (MaaS)** для задач машинного обучения.
Проект демонстрирует, как обученную ML-модель обернуть в REST API с использованием **FastAPI**.

Модель принимает признаки ириса и возвращает предсказанный класс.

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
│   ├── pipeline.py           # Обучение и сохранение модели
│   ├── preprocessing.py      # Препроцессинг данных
│   └── train.py              # Логика обучения модели
│
├── tests/                    # (опционально) тесты
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Архитектура

**Pipeline:**

1. `pipeline.py` — запуск обучения
2. `train.py` — обучение модели
3. `preprocessing.py` — подготовка данных
4. `model.joblib` — сохранённая модель

**Inference / API:**

* `inference.py` — загрузка модели и предсказание
* `app.py` — REST API (FastAPI)

---

## 🛠️ Установка и запуск

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/totiela/sim-ds-model-as-a-service
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

## 🏋️ Обучение модели

Перед запуском API необходимо обучить модель:

```bash
python -m src.pipeline
```

После этого файл модели сохранится в:

```text
models/model.joblib
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
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**

```json
{
  "predicted_class": "setosa"
}
```

---

## 🧩 Используемые технологии

* Python 3.10+
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
* разделение обучения и инференса
* best practices структуры ML-проекта
* работу с FastAPI и Swagger

