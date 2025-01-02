FROM python:3.11.9-slim 
WORKDIR /usr/src/app 
COPY . . 
RUN pip install -r requirements.txt 

ENV FLASK_APP=dashboard 
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV API_KEY=API_KEY
ENV DATABASE_URL=DATABASE_URL

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]

