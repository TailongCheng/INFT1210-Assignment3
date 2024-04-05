# Import the python module
FROM python:3.8-slim
 
# Set the working directory
WORKDIR /flaskapp
 
# Copy the source python file to my current working directory.
COPY *.py ./
 
# Run command to ensure the Flask framework is present in the container.
RUN pip install Flask
 
# Expose port 8080 for the application
EXPOSE 80
CMD ["python", "flaskapp.py"]
