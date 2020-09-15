docker build -t server:latest .
helm upgrade server ./deploy/server --install -f ./deploy/server/values.yaml