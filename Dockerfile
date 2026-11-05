FROM python:3.11-slim
LABEL maintainer="kwonhyck0110@gmail.com"
ENV APP_ENV=dev

WORKDIR /app
COPY app/ /app/
RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]