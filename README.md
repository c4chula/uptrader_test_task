# Тестовое задание UPTRADER

[Ссылка на задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?usp=sharing)

Запуск проекта

Для того, чтобы запустить проект, вам необходимо создать env-файл (смотреть пример)

```bash
source .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
