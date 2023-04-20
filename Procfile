release: python manage.py migrate
web: uvicorn aurochs.asgi:application --host 0.0.0.0 --port $PORT --workers=5
# beat: celery --app aurochs beat 
# worker: celery  --app aurochs worker --beat -Q celery
# worker: celery  --app aurochs worker --beat -c 4 -Q celery
