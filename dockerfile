
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /buza-website



WORKDIR /buza-website


# Copy the current directory contents into the container
ADD . /buza-website

# Install packages in the piplockfile
RUN pip install pipenv
# RUN yarn
RUN cp -p .env.example .env
RUN pipenv install --upgrade setuptools
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv run django-admin migrate
RUN pipenv run django-admin loaddata examples/example-data.json
 EXPOSE 8000
