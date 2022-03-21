![logomarca LAIS - Laboratório de Inovação Tecnológica em saúde](https://regulacao.lais.ufrn.br/static/assets/images/lais-topbar.png)

# 👋🏽 Introdução
 Repositório do projeto Back-End do processo Seletivo edição 10.

Durante o processo seletivo desse projeto foram definidas certas orientações para o desenvolvimento de um mini-sistema de Agendamento de exame de covid.

As orientações podem ser encontradas [aqui](https://lais.huol.ufrn.br/wp-content/uploads/2022/03/Edital-10_2022-Orientacoes-para-a-Fase-2.pdf)
# 🔧 Instalação


# 🧾Suporte de Avaliação

## Obrigatórias
### História de Usuário #1 - Página Inicial *

 - [x] CA#01 - Informações de Usuário Autenticado
	 - URL : '/home'
	 - Arquivo: templates/home.html
 - [x] CA#02 - Botão de Encerrar Botão
 - [x] CA#03 - Realizar Agendamento para Usuários Aptos a agendamento
 - [x] CA#04 - Opção de Login e AutoCadastro para Usuários não-autenticados
### História de Usuário #2 - AutoCadastro *
 - [x] CA#01 - Campos de Formulário de AutoCadastro
	 - URL : '/home'
	 - Arquivo: templates/home.html
 - [x] CA#02 - Validação de Idade
 - [x] CA#03 - Adição de Grupos ao Banco de Dados ( loaddata )
 - [x] CA#04 - Validação de CPF
 - [x] CA#05 - Unicidade de CPF
 - [ ] CA#06 - Mensagem de Confirmação
 - [ ] CA#07 - Aptidão de Usuário
### História de Usuário #3 - Página de Login *
 - [x] CA#01 - Campos de Login
 - [ ] CA#02 - Validação de Campos
 - [x] CA#03 - Redirecionamento de Login
 - [x] CA#04 - Utilização do Sistema de Autenticação Django(UserCreationForm)

### História de Usuário #6 - Agendamento de Exame
 - [ ] CA#01 - Limite de Agendamento por Usuário
 - [x] CA#02 - Campos de Agendamento
 - [x] CA#03 - Limite de Usuários por Agendamento
 - [x] CA#04 - Validação de Horário de Agendamento
 - [x] CA#05 - Validação de Data de Agendamento
 - [ ] CA#06 - Validação de Idade de Usuário por Horário de Agendamento
 - [x] CA#07 - Formato de Campo de Estabelecimento
 - [x] CA#08 - Formato de Campo de Horário
 - [x] CA#09 - Validação de Horário de Agendamento Futura
 - [x] CA#10 - Redirecionamento de Agendamento

## Não-Obrigatórias
### História de Usuário#4 - Administração da plataforma

 - [ ] CA#01 -   Command para inserir Estabelecimentos
 - [ ] CA#02 - Listagem de Estabelecimento
 - [ ] CA#03 - Filtragem de Estabelecimento

### História de Usuário#5 - Listagem de Exames
 - [x] CA#01 - Requerimento de Usuário Autenticado
 - [x] CA#02 - Campos da Tabela de Listagem
 - [x] CA#03 - Horário Expirado
### História de Usuário#7 - Painel Administrativo
- [ ] CA#01 - Gráfico de Barras de Agendamento por Estabelecimento
 - [ ] CA#02 - Gráfico Pizza de Aptidão de Usuários
 - [ ] CA#03 - Redirecionamento para Usuários Não-Autorizados
