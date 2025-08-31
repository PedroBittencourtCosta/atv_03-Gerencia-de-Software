# Atividade Prática de Gerência de Configuração de Software

Este repositório foi criado para a atividade prática da disciplina de GCS. O objetivo é simular um fluxo de trabalho básico de desenvolvimento de software utilizando Git e GitHub.

## Software
O projeto consiste em um script Python (`app.py`) simples que exibe uma mensagem de saudação e um menu.

## Histórico de Commits (Branch `main`)

O desenvolvimento inicial foi realizado em três commits principais:

1.  **`Initial commit: Adiciona a versão 1.0 do software`**: Criação do arquivo inicial com uma mensagem de "Hello, World!".
2.  **`Feat: Adiciona nome do autor na mensagem`**: O software foi atualizado para incluir o nome do autor.
3.  **`Feat: Implementa função de saudação`**: Foi adicionada uma função para saudar o usuário de forma mais dinâmica.

## Desenvolvimento de Funcionalidade (Branching)

Para adicionar uma nova funcionalidade (um menu), foi utilizado o seguinte fluxo de branching:

1.  Um novo branch chamado `feature/adiciona-menu` foi criado a partir do branch `main`.
2.  O desenvolvimento do menu foi realizado e "commitado" neste branch.
3.  Após a finalização, o branch `feature/adiciona-menu` foi integrado (merged) de volta ao branch `main`.

## Como Executar
Para rodar o software, basta executar o seguinte comando em seu terminal (requer Python instalado):
```bash
python app.py
```