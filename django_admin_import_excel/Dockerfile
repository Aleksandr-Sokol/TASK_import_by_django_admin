# образ на основе которого создаём контейнер
FROM python:3.10

# рабочая директория внутри проекта
WORKDIR /usr/src/app

## переменные окружения для python
## чтобы Python не писал файлы .pyc при импорте исходных модулей
#ENV PYTHONDONTWRITEBYTECODE 1
## гарантирует, что выходные данные python будут отправлены прямо в терминал (например, журнал вашего контейнера)
## без предварительной буферизации и что вы сможете просматривать выходные данные вашего приложения
## (например, журналы django) в режиме реального времени.
#ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

# устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]