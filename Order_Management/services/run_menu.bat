@echo off

uvicorn menu_service.main:app --host 0.0.0.0 --port 8002 --reload