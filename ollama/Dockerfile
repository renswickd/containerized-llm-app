FROM ollama/ollama:latest

# Tools for healthchecks / scripting
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl bash && rm -rf /var/lib/apt/lists/*

COPY ./pull-model.sh /pull-model.sh
RUN chmod +x /pull-model.sh
