# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to ensure non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install prerequisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends nmap \
    ca-certificates \
    apt-transport-https \
    gnupg \
    wget \
    software-properties-common && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add deadsnakes PPA to install Python
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a symbolic link for python3
RUN ln -s /usr/bin/python3.10 /usr/bin/python
RUN ls

# Copy the requirements file into the container

COPY requirements.txt .
RUN python3.10 -m venv /opt/venv
# Install Python dependencies
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of your application code into the container
COPY . /app
WORKDIR /app

# Expose any necessary ports (if applicable)
EXPOSE 5000

# Set the default command to run your application (modify as needed)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
