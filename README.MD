# 养老院探视预约系统

基于 Django + Vue 的养老院探视预约系统，包含老人信息管理、家属预约探视、探视记录和紧急通知模块。项目按前后端分离组织，后端按业务拆分 Django app，前端按页面、组件和 API 服务拆分。

## 功能模块

- 老人信息管理：维护姓名、年龄、房间号、护理等级、紧急联系人和健康备注。
- 家属预约探视：提交预约、记录家属信息、探视时间、人数、状态和备注。
- 探视记录：登记签到、签退、体温、接待员工和探视摘要。
- 紧急通知：发布面向家属、员工或全体的通知，支持普通、重要、紧急级别。

## 项目结构

```text
backend/
  appointments/      家属预约模块
  notifications/     紧急通知模块
  residents/         老人信息模块
  visits/            探视记录模块
  common/            通用 HTTP 和 CORS 工具
  config/            Django 项目配置
frontend/
  src/components/    复用表单与展示组件
  src/services/      前端 API 调用封装
  src/views/         业务页面
scripts/
  start-backend.sh   容器后端启动脚本
```

## Docker Compose 启动

```bash
docker compose up --build
```

启动后访问：

- 前端：http://127.0.0.1:19062
- 后端健康检查：http://127.0.0.1:8000/api/health/
- Django Admin：http://127.0.0.1:8000/admin/

后端容器启动时会自动执行数据库迁移并写入一组演示数据。

## 本地开发启动

后端：

```bash
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py seed_data
.venv\Scripts\python manage.py runserver 127.0.0.1:8000
```

前端：

```bash
cd frontend
npm install
npm run dev -- --host 127.0.0.1
```

## API 端点

- `GET/POST /api/residents/`
- `GET/PUT/DELETE /api/residents/<id>/`
- `GET/POST /api/appointments/`
- `GET/PUT/DELETE /api/appointments/<id>/`
- `GET/POST /api/visits/`
- `GET/PUT/DELETE /api/visits/<id>/`
- `GET/POST /api/notifications/`
- `GET/PUT/DELETE /api/notifications/<id>/`
