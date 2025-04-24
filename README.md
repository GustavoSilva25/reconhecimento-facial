# Reconhecimento facial com Python

Este projeto realiza o reconhecimento facial usando a webcam, com base no rostos previamente cadastrados em uma pasta local 'known_faces/'.

## Funcionalidades
  
  - Reconhecimento facial ao vivo.
  - Identificação com base em imagens cadastradas.
  - Detecção com redimensionamento.

## Tecnologias utilizadas

- Python.
- OpenCV.
- face_recognition.

## Estrutura

- `known_faces/`: pasta com imagens dos rostos conhecidos. O nome do arquivo é usado como identificador.
- `main.py`: script principal para executar o projeto.

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
2. Executar o script:
   ```bash
   python main.py
