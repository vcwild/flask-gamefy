# Use an official Python runtime as an image
FROM python:3.8

# Expose Flask port
EXPOSE 5000

# Using pipenv to install project dependencies
RUN pip install pipenv
COPY Pipfile* ./app/
RUN pipenv lock --requirements > ./app/requirements.txt
RUN pip install -r ./app/requirements.txt

COPY . ./app/
# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist

# Run app.py when the container launches
# RUN ./app/data/write_db.py
WORKDIR /app
CMD ./app.py
ENTRYPOINT [ "python" ]