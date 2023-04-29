FROM python:3.8

WORKDIR /FastAPI_Manage

COPY requirements.txt /FastAPI_Manage/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastAPI_Manage/requirements.txt

COPY . /FastAPI_Manage

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
