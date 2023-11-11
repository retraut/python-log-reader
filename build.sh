cat ~/.github_token | docker login ghcr.io -u retraut --password-stdin
docker build . -t ghcr.io/retraut/python-log-reader:latest
docker push ghcr.io/retraut/python-log-reader:latest
