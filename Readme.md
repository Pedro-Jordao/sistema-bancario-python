# Banco Digital - Projeto de Estudos

O repositório a seguir foi criado por mim como parte de um projeto de Bootcamp da [Digital Innovation One - DIO](https://web.dio.me/home) para fins de avaliação e aprovação. Embora a tarefa envolva etapas e configurações básicas, a implementação foi realizada de acordo com os requisitos descritos na Descrição do Desafio.

Ao concluir este desafio, você será capaz de:

✅ Implementar um sistema simples de operações bancárias em Python.  
✅ Gerenciar depósitos e saques com controle de limites e quantidade de operações.  
✅ Modularizar funções, tornando o código mais organizado e reutilizável.  
✅ Adicionar funcionalidades para criar usuários (com validação de CPF) e contas correntes vinculadas.  
✅ Listar todas as contas criadas com seus respectivos usuários.

## 🚀 Alterações e Melhorias Realizadas

Este projeto foi dividido em duas versões principais:

🔹 **Versão Original**  
- Toda a lógica de depósito, saque e extrato estava diretamente dentro do loop principal.  
- Não havia separação de responsabilidades por funções.  
- Apenas funcionalidades básicas de depósito, saque e extrato estavam implementadas.  

🔹 **Versão Otimizada (Atual)**  
- O código foi refatorado para utilizar funções dedicadas para depósito, saque e extrato, promovendo maior organização e reaproveitamento.  
- Foram criadas funções adicionais para cadastrar usuários (com CPF único) e contas correntes vinculadas a usuários.  
- O menu foi expandido para incluir operações de cadastro de usuário, conta corrente e listagem de contas.  
- Foi aplicado o uso de argumentos posicionais e nomeados para as funções, de acordo com as melhores práticas apresentadas no módulo.  
- O projeto agora permite múltiplas contas por usuário, respeitando os requisitos de CPF único e validação de dados.

## 📌 Funcionalidades Principais

✅ Depositar valores na conta.  
✅ Sacar valores com limite diário de saques e valor máximo por operação.  
✅ Visualizar extrato das operações realizadas, incluindo saldo final.  
✅ Criar usuários com CPF único, nome, data de nascimento e endereço.  
✅ Criar contas correntes vinculadas a usuários existentes, com numeração sequencial de contas.  
✅ Listar todas as contas cadastradas com informações de usuário e agência.
## 🧾 Notas Finais

Este README é um modelo padrão reutilizável para projetos desenvolvidos em bootcamps da DIO.
Adapto conforme o desafio proposto, mantendo a estrutura clara e objetiva.
