# Task Manager API

هذا مشروع بسيط سويته باستخدام **FastAPI** لإدارة المهام.

المشروع بيه:

* Register و Login
* JWT Authentication
* User و Admin
* إضافة وتعديل وحذف المهام
* إكمال المهمة
* عرض المهام
* PostgreSQL و SQLModel
* Docker

## التشغيل

أول شي ثبت المكتبات:

```bash
pip install -r requirements.txt
```

شغل PostgreSQL باستخدام Docker:

```bash
docker compose up -d
```

سوي ملف اسمه `.env` وحط بيه إعدادات قاعدة البيانات:

```env
DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/taskdb
SECRET_KEY=Computiqmuntezer
المفتاح للتجربة فقط
APP_NAME=Task Manager API
```


بعدين شغل المشروع:

```bash
uvicorn main:app --reload
```

وافتح:

```text
http://127.0.0.1:8000/docs
```

من Swagger تكدر تجرب الـAPI.

## User Registration

حتى تسوي User جديد، استخدم:

```text
POST /auth/register
```

المعلومات المطلوبة:

* Username
* Email
* Password

بعد التسجيل، الحساب يكون **User** بشكل افتراضي.

## Admin Creation

حتى تسوي Admin جديد، شغل:

```bash
python create_admin.py
```

راح يطلب منك:

* Admin username
* Admin email
* Admin password

بعدها ينشئ الحساب بصلاحية **Admin**.

الـAdmin يكدر يشوف ويدير كل المهام، بينما الـUser يتعامل فقط مع مهامه.

## Database

المشروع كان يستخدم **SQLite**، وتم تحويل قاعدة البيانات إلى **PostgreSQL**.

تم استخدام **Docker** لتشغيل PostgreSQL وحفظ البيانات.

## Updates

* تم تصليح خطأ **500** عند إنشاء Task وتحديثها.
* تم تحويل قاعدة البيانات من **SQLite** إلى **PostgreSQL**.
* تم إضافة إعداد PostgreSQL باستخدام **Docker**.
