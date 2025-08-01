# AviatorGuru (OCR + ML Prediction Web App)

## 🛠 Setup Instructions for Render

### ✅ Backend Deployment
1. Upload `backend/` as a Python Web Service.
2. Use Python 3.11+.
3. Add `requirements.txt`.
4. Use this start command:

```
gunicorn main:app -k uvicorn.workers.UvicornWorker
```

---

### ✅ Frontend Deployment
1. Upload `frontend/` as a Static Site.
2. Connect to backend API at `/predict` and `/upload`.

---

Enjoy your AI-powered Aviator predictions! 🚀