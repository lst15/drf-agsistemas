# Teste de Desenvolvimento para AGSistemas - API Rest com DRF

Este é um projeto de teste desenvolvido para a empresa AGSistemas, focado na construção de uma API Rest utilizando o Django Rest Framework (DRF) em Python e um banco de dados SQLite. Este projeto não segue a arquitetura MVT (Model-View-Template) do Django, mas sim a arquitetura de API Restful.

## Descrição do Projeto

O projeto consiste em um sistema de controle de veículos, incluindo o cadastro de veículos e motoristas, bem como a capacidade de rastrear qual motorista está utilizando um veículo em um determinado período.

### Funcionalidades

- **Página Inicial:** Retorna à página principal do sistema.
- **Veículos:** Permite o cadastro de veículos.
- **Motoristas:** Permite o cadastro de motoristas.
- **Consulta por Data:** Um campo de pesquisa para filtrar os registros por data.
- **Lista de Movimentação dos Veículos:** Exibe a movimentação de veículos ordenada por data de saída, do mais novo ao mais antigo.
- **Botões (Visualizar, Editar, Excluir):** Ações disponíveis em cada registro da lista de movimentação de veículos.

### Cadastro de Veículos

- **Próxima Troca de Óleo:** Um campo que indica quando a próxima troca de óleo é devida. Quando o quilometragem registrada no controle de veículos atingir o quilometragem especificado para a próxima troca de óleo, uma mensagem será exibida na tela.

## Como Executar o Projeto

Siga as instruções abaixo para executar o projeto:

1. **Clonar o Repositório: Clone este repositório em seu sistema local usando o seguinte comando:**

   ```bash
   git clone git@github.com:lst15/mvt-agsistemas.git
   cd mvt-agsistemas
   ``` 

2. **Configuração do Ambiente Virtual (venv):** Crie um ambiente virtual para o projeto usando o seguinte comando:

   ```bash
   python -m venv venv

3. **Ativar o Ambiente Virtual: Ative o ambiente virtual:**
    * Windows
      
   ```bash
   venv\Scripts\activate
   ```
   
   * MacOS e Linux
     
   ```bash
   source venv/bin/activate
   ```  

4. **Execute o seguinte comando para instalar as dependências necessárias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure as configurações de banco de dados no arquivo settings.py de acordo com suas configurações do MySQL.**
    * Execute as migrações para criar as tabelas do banco de dados
      
   ```bash
   python manage.py migrate
   ```
6. **Inicie o servidor Django com o seguinte comando:**

   ```bash
   python manage.py runserver
   ```

Acesse o aplicativo em seu navegador em http://localhost:8000.

## Conclusão
Este projeto foi desenvolvido como um teste para a AGSistemas e implementa um sistema de controle de veículos em conformidade com os requisitos fornecidos. Ele inclui funcionalidades de cadastro, listagem, edição e exclusão de veículos e motoristas, bem como um sistema de alerta para a troca de óleo.
   
