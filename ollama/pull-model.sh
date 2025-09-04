set -euo pipefail

# Config via env (can be set in compose)
: "${OLLAMA_MODEL:=smollm2:latest}"
: "${OLLAMA_HOST:=0.0.0.0}"

# Start the Ollama server in the background
# (no stray space — just 'ollama serve')
ollama serve &
pid=$!

# Wait for the daemon to be ready
echo "Waiting for ollama daemon..."
for i in {1..30}; do
  if curl -sSf http://127.0.0.1:11434/api/tags >/dev/null; then
    echo "Ollama is up."
    break
  fi
  echo "  ...still starting ($i)"
  sleep 1
done

# Pull the model (with one retry)
echo "Pulling model: ${OLLAMA_MODEL}"
if ! ollama pull "${OLLAMA_MODEL}"; then
  echo "Initial pull failed, retrying in 5s..."
  sleep 5
  ollama pull "${OLLAMA_MODEL}"
fi

# Keep the container attached to the daemon
wait "${pid}"
