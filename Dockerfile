FROM python:3.10

RUN mkdir /FASTAPP/

WORKDIR  /FASTAPP/

COPY ./requirements.txt  /FASTAPP/requirements.txt


RUN pip install --upgrade pip

RUN pip install -r /FASTAPP/requirements.txt


COPY . /FASTAPP/


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



# FROM python:3.10

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
