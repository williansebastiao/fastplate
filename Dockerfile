FROM python:3.10

# WORKING ON DIR
WORKDIR /code

# INSTALL PACKAGES
RUN apt-get update \
    && pip install poetry

# COPY FILES TO PATH
COPY . /code

# INSTALL REQUIREMENTS ON DOCKER
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# EXPOSE PORT
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]