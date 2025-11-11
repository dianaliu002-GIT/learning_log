#!/usr/bin/env bash
set -o errexit

echo "=== 开始构建过程 ==="

echo "1. 安装依赖..."
pip install -r requirements.txt

echo "2. 列出所有迁移文件..."
find . -name "*.py" -path "*/migrations/*" | grep -v __pycache__

echo "3. 显示迁移状态（应用前）..."
python manage.py showmigrations

echo "4. 创建静态文件目录..."
mkdir -p staticfiles

echo "5. 收集静态文件..."
python manage.py collectstatic --noinput

echo "6. 应用数据库迁移..."
python manage.py migrate --noinput

echo "7. 显示迁移状态（应用后）..."
python manage.py showmigrations

echo "8. 验证Topic模型..."
python manage.py shell -c "
from learning_logs.models import Topic
from django.contrib.auth.models import User
print('Topic模型字段:', [f.name for f in Topic._meta.get_fields()])
print('验证完成')
"

echo "=== 构建完成 ==="
