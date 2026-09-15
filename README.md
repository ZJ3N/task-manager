# Task Manager API

هذا مشروع بسيط سويته باستخدام **FastAPI** لإدارة المهام.

المشروع بيه:

* Register و Login
* JWT Authentication
* User و Admin
* إضافة وتعديل وحذف المهام
* إكمال المهمة
* عرض المهام
* SQLite و SQLModel

## التشغيل

أول شي ثبت المكتبات:

```bash
pip install -r requirements.txt
```

سوي ملف اسمه `.env` وحط بيه:

```env
DATABASE_URL=sqlite:///./tasks.db
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

المشروع يستخدم **SQLite** لحفظ المستخدمين والمهام.
