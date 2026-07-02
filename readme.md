# 1. Navigate to the project directory
cd ai-engineering

# 2. Activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Start the FastAPI server
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000 --reload