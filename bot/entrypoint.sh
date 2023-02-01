export $(grep -v '^#' .env | xargs -d '\n')
source ./venv/bin/activate
python ./src/bot.py