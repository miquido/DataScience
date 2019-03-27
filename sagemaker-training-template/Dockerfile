FROM microsoft/mmlspark

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

ADD . /opt/program
WORKDIR /opt/program

USER root

ENTRYPOINT ["python", "main.py"]
