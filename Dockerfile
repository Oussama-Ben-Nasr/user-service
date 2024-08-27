FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY api/main.py /code/

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "80"]