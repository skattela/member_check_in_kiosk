#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker pull skattela/epc_qr_code_app
docker stop epc_qr_code_app
docker rm epc_qr_code_app
docker run --name epc_qr_code_app -d -p 80:80 skattela/epc_qr_code_app