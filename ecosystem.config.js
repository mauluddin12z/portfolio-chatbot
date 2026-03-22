module.exports = {
  apps: [
    {
      name: "portfolio-chatbot",
      script: "venv/bin/uvicorn",
      args: "main:app --host 0.0.0.0 --port 8000 --reload",
      interpreter: "python3",
      watch: true
    }
  ]
};