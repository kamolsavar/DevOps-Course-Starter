FROM python:3.8 as base

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH

WORKDIR /DEVOPS-COURSE-STARTER

# Install Dependencies
COPY ./pyproject.toml .
RUN poetry install

# Copying over files
COPY todo_app ./todo_app/
# COPY .env .
# EXPOSE 8080
FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as production
ENTRYPOINT poetry run gunicorn  --bind=0.0.0.0:5000 "todo_app.app:create_app()"

# testing stage
FROM base as test
#.....

# Build it
$ docker build --target test --tag my-test-image .
# Run tests in the "tests" directory
$ docker run my-test-image tests
# Maybe your e2e tests are somewhere else? Run them:
$ docker run my-test-image <path_to_other_tests>



