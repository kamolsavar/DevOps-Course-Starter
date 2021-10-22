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

FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
RUN apt-get install ./chrome.deb -y
RUN rm ./chrome.deb
# Install Chromium WebDriver
# firefox driver has been deleted
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE`
RUN echo "Installing chromium webdriver version ${LATEST}"
RUN curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip 
RUN apt-get install unzip -y
RUN unzip ./chromedriver_linux64.zip



