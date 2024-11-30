FROM python:3.13.0-bookworm

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    netcat-openbsd \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && export PATH="$HOME/.cargo/bin:$PATH" \
    && . $HOME/.cargo/env \
    && apt-get remove -y curl build-essential \
    && apt-get autoremove -y \
    && apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.cargo/bin:${PATH}"

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Make sure entrypoint is executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Expose port 8000 for the Django app
EXPOSE 8000

# Set the default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
