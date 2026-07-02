# 1. Navigate to the project directory
cd ai-engineering

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Start the FastAPI server
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
