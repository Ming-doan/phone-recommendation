## Phone Recommendation API!

Creator: `BaoSena Team` - Quy Nhon AI Hackathon 2023.

## 📖 Documentation

1. API for Webhook

```bash
POST: {domain}/api/recommend
```

```json
// Request object
{
  "message": "prompt message"
}
```

```json
// Response object
{
  "message": "Answers for AI",
  "recommends": ["url_1", "url_2"]
}
```

## 💻 Tech stack

1. APIs: `FastAPI`.
2. AI libraries: `Pytorch`.
3. Pretrain models: `Transformers`.

## ⚡ How to run this project.

```bash
# Download dependencies
pip install -r requirements.txt

# Start API
uvicorn main:app

# Start with development mode
uvicorn main:app --reload
```
