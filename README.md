# PostedAPI

## Установка и запуск

1. Склонируйте репозиторий
```bash
git clone https://github.com/cosmic-onyx/PostedAPI.git
```
2. Настройте переменные окружения
скопируйте содержимое .env.example и вставьте в новый созданный вами файл .env

3. Запустите проект
```bash
docker compose up -d --build
```

## Админ панель
Уже создан пользователь

login - root,
password - root

или те значения, которые вы указали в .env (ADMIN_LOGIN, ADMIN_PASSWORD)


## Запуск тестов

```bash
cd drf

python -m pytest
```

## Аутентификация

API использует JWT токены для аутентификации. После регистрации или входа вы получите JWT токен, который нужно передавать в заголовке `Authorization`:

```
Authorization: Bearer YOUR_JWT_TOKEN
```

## API Эндпоинты

### Аутентификация

#### Регистрация
- **POST** `/auth/register`
- **Описание**: Регистрация нового пользователя
- **Тело запроса**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Ответ**: `201 Created`
  ```json
  {
    "id": 1,
    "username": "testuser"
  }
  ```

#### Вход в систему
- **POST** `/auth/login`
- **Описание**: Вход в систему существующего пользователя
- **Тело запроса**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Ответ**: `200 OK`
  ```json
  {
    "id": 1,
    "username": "testuser"
  }
  ```

#### Выход из системы
- **POST** `/auth/logout`
- **Описание**: Выход из системы (удаление JWT токена)
- **Ответ**: `200 OK`
  ```json
  {
    "detail": "Успешный выход из системы."
  }
  ```

### Статьи (Articles)

#### Получить список всех статей
- **GET** `/api/v1/article/`
- **Описание**: Получить список всех статей
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "title": "Заголовок статьи",
      "content": "Содержание статьи",
      "category": 1,
      "user": 1,
      "created_at": "2024-01-01T12:00:00Z"
    }
  ]
  ```

#### Создать новую статью
- **POST** `/api/v1/article/`
- **Описание**: Создать новую статью
- **Заголовки**: 
  - `Authorization: Bearer YOUR_JWT_TOKEN`
  - `Content-Type: application/json`
- **Тело запроса**:
  ```json
  {
    "title": "Заголовок статьи",
    "content": "Содержание статьи",
    "category_id": 1
  }
  ```
- **Ответ**: `201 Created`
  ```json
  {
    "id": 1,
    "title": "Заголовок статьи",
    "content": "Содержание статьи",
    "category": 1,
    "user": 1,
    "created_at": "2024-01-01T12:00:00Z"
  }
  ```

#### Получить конкретную статью
- **GET** `/api/v1/article/{id}/`
- **Описание**: Получить конкретную статью по ID
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `200 OK`
  ```json
  {
    "id": 1,
    "title": "Заголовок статьи",
    "content": "Содержание статьи",
    "category": 1,
    "user": 1,
    "created_at": "2024-01-01T12:00:00Z"
  }
  ```

#### Обновить статью
- **PUT** `/api/v1/article/{id}/`
- **Описание**: Обновить существующую статью (только владелец)
- **Заголовки**: 
  - `Authorization: Bearer YOUR_JWT_TOKEN`
  - `Content-Type: application/json`
- **Тело запроса**:
  ```json
  {
    "title": "Обновленный заголовок",
    "content": "Обновленное содержание",
    "category_id": 1
  }
  ```
- **Ответ**: `200 OK`
  ```json
  {
    "id": 1,
    "title": "Обновленный заголовок",
    "content": "Обновленное содержание",
    "category": 1,
    "user": 1,
    "created_at": "2024-01-01T12:00:00Z"
  }
  ```
- **Ошибка**: `403 Forbidden` - если вы не владелец статьи
  ```json
  {
    "detail": "Вы не можете удалять/редактировать это"
  }
  ```

#### Удалить статью
- **DELETE** `/api/v1/article/{id}/`
- **Описание**: Удалить статью (только владелец)
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `204 No Content`
- **Ошибка**: `403 Forbidden` - если вы не владелец статьи
  ```json
  {
    "detail": "Вы не можете удалять/редактировать это"
  }
  ```

### Комментарии (Comments)

#### Получить список всех комментариев
- **GET** `/api/v1/comment/`
- **Описание**: Получить список всех комментариев
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "user": 1,
      "article": {
        "id": 1,
        "title": "Заголовок статьи",
        "content": "Содержание статьи",
        "category": 1,
        "user": 1,
        "created_at": "2027-01-01T12:00:00Z"
      },
      "content": "Текст комментария",
      "created_at": "2027-01-01T12:30:00Z"
    }
  ]
  ```

#### Создать новый комментарий
- **POST** `/api/v1/comment/`
- **Описание**: Создать новый комментарий
- **Заголовки**: 
  - `Authorization: Bearer YOUR_JWT_TOKEN`
  - `Content-Type: application/json`
- **Тело запроса**:
  ```json
  {
    "article_id": 1,
    "content": "Текст комментария"
  }
  ```
- **Ответ**: `201 Created`
  ```json
  {
    "id": 1,
    "user": 1,
    "article": {
      "id": 1,
      "title": "Заголовок статьи",
      "content": "Содержание статьи",
      "category": 1,
      "user": 1,
      "created_at": "2024-01-01T12:00:00Z"
    },
    "content": "Текст комментария",
    "created_at": "2024-01-01T12:30:00Z"
  }
  ```

#### Получить конкретный комментарий
- **GET** `/api/v1/comment/{id}/`
- **Описание**: Получить конкретный комментарий по ID
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `200 OK`
  ```json
  {
    "id": 1,
    "user": 1,
    "article": {
      "id": 1,
      "title": "Заголовок статьи",
      "content": "Содержание статьи",
      "category": 1,
      "user": 1,
      "created_at": "2024-01-01T12:00:00Z"
    },
    "content": "Текст комментария",
    "created_at": "2024-01-01T12:30:00Z"
  }
  ```

#### Обновить комментарий
- **PUT** `/api/v1/comment/{id}/`
- **Описание**: Обновить существующий комментарий (только автор)
- **Заголовки**: 
  - `Authorization: Bearer YOUR_JWT_TOKEN`
  - `Content-Type: application/json`
- **Тело запроса**:
  ```json
  {
    "article_id": 1,
    "content": "Обновленный текст комментария"
  }
  ```
- **Ответ**: `200 OK`
  ```json
  {
    "id": 1,
    "user": 1,
    "article": {
      "id": 1,
      "title": "Заголовок статьи",
      "content": "Содержание статьи",
      "category": 1,
      "user": 1,
      "created_at": "2024-01-01T12:00:00Z"
    },
    "content": "Обновленный текст комментария",
    "created_at": "2024-01-01T12:30:00Z"
  }
  ```
- **Ошибка**: `403 Forbidden` - если вы не автор комментария
  ```json
  {
    "detail": "Вы не можете удалять/редактировать это"
  }
  ```

#### Удалить комментарий
- **DELETE** `/api/v1/comment/{id}/`
- **Описание**: Удалить комментарий (только автор)
- **Заголовки**: `Authorization: Bearer YOUR_JWT_TOKEN`
- **Ответ**: `204 No Content`
- **Ошибка**: `403 Forbidden` - если вы не автор комментария
  ```json
  {
    "detail": "Вы не можете удалять/редактировать это"
  }
  ```