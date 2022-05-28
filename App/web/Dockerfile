FROM python:3.10.4
# Installing python version 3.10.4

EXPOSE 5555
# Expose port 5555

WORKDIR /app
# Set the working directory to the project directory

COPY . /app/
# Copy the project files to the container


COPY . .
# Copy the project files to the container

RUN pip install -r requirements.txt && pip3 install -r requirements.txt
# Update pip and install the requirements from the requirements.txt file

CMD python3 "app.py"




