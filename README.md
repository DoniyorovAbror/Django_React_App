### Fullstack ( Backend - Django ) - ( Frontend - React.js )

### Запуск проекта локально

### Backend:

- Требование для Backendа Python=3.10
- Заходим в папку Backend и в консоле наберем команду ниже:

    ```sh
python3 -m venv venv
venv/bin/activate
pip3 install -r requirements.txt
cd menu
    ```

- Создайте .env файл внутрь папки menu_api и напишите SECRET_KEY = ' API_KEY ' - ключ сгенерированный джанго после наберите в консоль:

    ```sh
    py manage.py runserver
    ```

- Откройте любой браузер и адресной строке наберите
    ```
http://127.0.0.1:8000/api/v1/receipt
    ```
- Вся документация по API находятся по адресам:
    ```
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/swagger
http://127.0.0.1:8000/swagger.json
http://127.0.0.1:8000/swagger.yaml
    ```
- Backend Сервер запустили.

### Frontend:

- Откройте новый консоль и переходите в папку Frontend и наберите:
    ```sh
npm i
npm start
    ```

- Откройте новую вкладку в браузере и наберите:
    ```sh
http://localhost:3000
    ```