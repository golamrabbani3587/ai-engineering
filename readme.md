echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc

pip install --upgrade pip
pip install virtualenv
pip install jupyter

mkdir ai-engineering
cd ai-engineering

python -m venv venv
source venv/bin/activate

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic email-validator