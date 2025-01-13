FROM amazon/aws-sam-cli-build-image-python3.9

# Create the app directory
RUN mkdir /app

# Copy application files into the container
ADD . /app

# Set the working directory
WORKDIR /app

# Install virtualenv and create a virtual environment
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install virtualenv \
    && python3 -m virtualenv env

# Install dependencies inside the virtual environment
RUN source env/bin/activate && pip install flask beautifulsoup4 requests  -q -U google-generativeai

# Expose the application port
EXPOSE 5000

# Activate the virtual environment and run the application
CMD ["/bin/bash", "-c", "source env/bin/activate && python3 app.py"]
