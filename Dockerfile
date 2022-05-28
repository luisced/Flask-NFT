FROM python:3.10.4
# Installing python version 3.10.4

COPY . /app
# Copy the project files to the container

WORKDIR /app
# Set the working directory to the project directory

COPY . .
# Copy the project files to the container

ENTRYPOINT ["python"]
# Run the python script
CMD ["app.py"]


RUN pip install --upgrade pip && pip3 install -r requirements.txt
# Update pip and install the requirements from the requirements.txt file
