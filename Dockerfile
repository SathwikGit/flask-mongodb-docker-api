# for running
FROM python:3.13

# dir for container
WORKDIR /app

# copy all files to the docker image
COPY . .

# for dependencies
RUN pip install -r requirements.txt

# port where application runs
EXPOSE 9000

# to start running the container
CMD ["python","app.py"]