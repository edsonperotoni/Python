#!/bin/bash

# 1. Definir o nome do ambiente
VENV_NAME=".venv"

echo "--- 🛠️ Iniciando configuração do ambiente Python ---"

# 2. Criar o ambiente virtual se não existir
if [ ! -d "$VENV_NAME" ]; then
    echo "> Criando ambiente virtual em $VENV_NAME..."
    python -m venv $VENV_NAME
else
    echo "> Ambiente $VENV_NAME já existe. Pulando criação."
fi

# 3. Atualizar o pip e instalar as bibliotecas necessárias
echo "> Instalando dependências (Matplotlib, Numpy, PyQt5)..."
./$VENV_NAME/bin/pip install --upgrade pip
./$VENV_NAME/bin/pip install matplotlib numpy PyQt5

echo "--- ✅ Tudo pronto! ---"
echo "Para ativar no Fish, use: source $VENV_NAME/bin/activate.fish"
echo "Para ativar no Bash, use: source $VENV_NAME/bin/activate"

echo "No Arch Linux ou CachyOS Linux, podes criar uma abreviação para o comando de ativação:"
echo "abbr --add venv_start 'source $VENV_NAME/bin/activate.fish'"
