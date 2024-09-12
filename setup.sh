#!/bin/bash

echo "executando o docker-compose e subindo o container..."
docker-compose -f "docker-compose.yml" up -d --build &&

echo "Criando imagem do container..."
docker tag django:latest registry.pop-pa.rnp.br:5000/django &&

echo "Enviando imagem para o registry..."
docker push registry.pop-pa.rnp.br:5000/django &&

echo "Encerrando o container"
docker-compose down &&

echo "Apagando imagem..."
docker image rm registry.pop-pa.rnp.br:5000/django &&

echo "Finalizado!"