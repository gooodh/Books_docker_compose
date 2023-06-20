FROM python:3.10 

SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update
RUN apt -qy install gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8

RUN useradd -rms /bin/bash bookm && chmod 77 /opt /run

WORKDIR /code
RUN mkdir /code/ctatic && mkdir /code/media && chown -R bookm:bookm /code && chmod 755 /code

COPY --chown=bookm:bookm . .

RUN pip install -r requirements.txt

USER bookm

CMD gunicorn config.wsgi -b 0.0.0.0:8000



