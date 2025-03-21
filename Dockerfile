# 1. Base Image
FROM python:3.12

# 2. install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# 3. set working directory
WORKDIR /app

# 4. Copy files to working directory
COPY pyproject.toml uv.lock* ./

# 5. Install dependencies
RUN uv sync

# 6. command to run on container start
CMD ["sleep", "infinity"]