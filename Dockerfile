FROM python:3.10

# WORKING ON DIR
WORKDIR /code

# INSTALL PACKAGES
RUN apt-get update \
    && pip install poetry

# INSTALL DOPPLER CLI
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && \
    apt-get -y install doppler

# COPY FILES TO PATH
COPY . /code

# INSTALL REQUIREMENTS ON DOCKER
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# EXECUTE ENTRYPOINT AND CMD
ENTRYPOINT ["doppler", "run", "--"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
