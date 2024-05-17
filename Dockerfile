FROM python:3.11

# Install git
RUN apt-get update && apt-get install -y git

# Set up the working directory
#WORKDIR /app

# Clone the repository
RUN git clone https://github.com/JAlcocerT/openai-chatbot

WORKDIR /openai-chatbot

# Install Python requirements
RUN pip install -r requirements.txt #all at once

#RUN sed -i 's/numpy==1\.26\.4/numpy==1.24.4/; s/pandas==2\.2\.2/pandas==2.0.2/' requirements.txt

# Set the entrypoint to a bash shell
CMD ["/bin/bash"]