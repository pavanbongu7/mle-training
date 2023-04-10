# start with base image as miniconda
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the source code and environment.yml to the container
COPY . .

# Create the Conda environment from environment.yml
RUN conda create -n mle-dev && \
    conda clean --all --yes

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Activate the Conda environment
ENV PATH /opt/conda/envs/mle-dev/bin:$PATH

# store the command in bashrc so that whenecer decoker starts any bash cell , 
#the command will run automatically
RUN echo "source activate mle-dev" > ~/.bashrc

RUN pip install -r requirements.txt

# Start the application
CMD ["python", "flask_app/app.py"]
