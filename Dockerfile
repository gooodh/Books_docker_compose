FROM python:3.10

SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update
RUN apt -qy install gcc libjpeg-dev libxslt-dev libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8

RUN useradd -rms /bin/bash book
RUN chmod 777 /opt /run

WORKDIR /book
RUN mkdir /book/staticfiles
RUN mkdir /book/media
RUN chown -R book:book /book && chmod 755 /book

COPY requirements.txt /book/

RUN pip install -r requirements.txt

COPY --chown=book:book . .
USER book
RUN python ./manage.py collectstatic --noinput








