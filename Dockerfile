FROM python AS login-env

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    python3-pip \
    build-essential

RUN  mkdir /flask_app


ADD . /flask_app

COPY requirements.txt /flask_app

WORKDIR /flask_app


RUN pip3 install -r requirements.txt


CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "running_login:app", "--log-level=debug"]

FROM python AS login-authenticate-env

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    python3-pip \
    build-essential

RUN  mkdir /flask_app


ADD . /flask_app

COPY requirements.txt /flask_app

WORKDIR /flask_app



RUN pip3 install -r requirements.txt



CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "running_login_authenticate:app", "--log-level=debug"]


FROM python AS db-env

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    python3-pip \
    build-essential

RUN  mkdir /flask_app


ADD . /flask_app

COPY requirements.txt /flask_app

WORKDIR /flask_app


#Install requirements from project
RUN pip3 install -r requirements.txt


# Launch the Flask/Gunicorn app after executing Docker Run command
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "running_db_class:app", "--log-level=debug"]


FROM python AS app-env

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    python3-pip \
    build-essential

RUN  mkdir /flask_app


ADD . /flask_app

COPY requirements.txt /flask_app

WORKDIR /flask_app


#Install requirements from project
RUN pip3 install -r requirements.txt


# Launch the Flask/Gunicorn app after executing Docker Run command
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "running_app:app", "--log-level=debug"]