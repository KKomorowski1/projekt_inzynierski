FROM python:3.11.0

WORKDIR /projekt_inzynierski

COPY . /projekt_inzynierski

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT behave features/
