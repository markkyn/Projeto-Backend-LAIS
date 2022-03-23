![logomarca LAIS - Laboratório de Inovação Tecnológica em saúde](https://regulacao.lais.ufrn.br/static/assets/images/lais-topbar.png)

# 👋🏽 Introdução
 Repositório do projeto Back-End do processo Seletivo edição 10.

Durante o processo seletivo desse projeto foram definidas certas orientações para o desenvolvimento de um mini-sistema de Agendamento de exame de covid.

As orientações podem ser encontradas [aqui](https://lais.huol.ufrn.br/wp-content/uploads/2022/03/Edital-10_2022-Orientacoes-para-a-Fase-2.pdf)
# 🔧 Instalação
### Instalação de Ambiente Virtual
- Baixe esse repositório e Entre no diretório respectivo
- Utilize um VirtualEnvironment
`python -m venv venv`
- Instale as dependências necessárias
`pip install -r requirements.txt`

### Passos Iniciais para Funcionamento do Projeto
 - Crie e Execute de migrations para o banco de dados
`python ./manage.py makemigrations`
`python ./manage.py migrate`

- É recomendado criar um SuperUsuário, mas não obrigatório
`python ./manage.py createsuperuser`
	- Dados necessários:
		- CPF Válido ( [Gerador de CPF](https://www.4devs.com.br/gerador_de_cpf) )
		- Data de Nascimento
		- Senha
- Carrege os dados de Grupos e Estabelecimentos
`python ./manage.py loaddata grupos_de_atendimento.json`
`python ./manage.py add_estabelecimentos`

# Informações sobre o Projeto:
## URL's
- Página Inicial
- Página de Login
- Página de Cadastro
- Página de Agendamento
- Página de Listagem de Exames
## Estrutura de Pastas
### Apps:
- core
- users
- pages
- agendamento
- 

	|..core/ ( Diretório de Projeto )
		|..__init__.py
		|..settings.py
		|..urls.py
		|..asgi.py
		|..wsgi.py
		|..management/
			|..__init__.py
			|..commands/
				|..__init__.py
				|.. add_estabelecimentos.py
		( Command de adição de Estabelecimento)
	|.. pages/ (App de Paginas[Login,Signup])
		|..__init__.py
		|..apps.py
		|..urls.py (URLS de todo Projeto)
		|..validators.py
		|..forms/ (Diretorio Modulazirado)
			|..__init__.py
			|..loginForm.py
			|..signupFrm.py
		|..views/ (Diretório Modularizado)
			|..__init__.py
			|..homeView.py
			|..loginView.py
			|..signupView.py
			|..dropdownView.py
	|..users (App de CustomUser)
		|..__init__.py
		|..apps.py
		|..admin.py
		|..models.py
		|..validators.py
		|.. migrations/
	|..agendamento (App de Agendamento e Listagem)
		|..__init__.py
		|..apps.py
		|..admin.py
		|..models.py
		|..validators.py
		|..views/ (Diretório Modularizado)
			|..__init__.py
			|..agendamentoView.py
			|..listagemView.py
		|..forms/ (Diretorio Modularizado)
			|..__init__.py
			|..agendamentoForm.py
		|..migrations/
	|..templates (Diretórios de HTML's)
	
	...etc...
		
		


# 🧾Suporte de Avaliação

## Obrigatórias
### História de Usuário #1 - Página Inicial *

 - [x] CA#01 - Informações de Usuário Autenticado
 - [x] CA#02 - Botão de Encerrar Botão
 - [x] CA#03 - Realizar Agendamento para Usuários Aptos a agendamento
 - [x] CA#04 - Opção de Login e AutoCadastro para Usuários não-autenticados
### História de Usuário #2 - AutoCadastro *
 - [x] CA#01 - Campos de Formulário de AutoCadastro
 - [x] CA#02 - Validação de Idade
 - [x] CA#03 - Adição de Grupos ao Banco de Dados ( loaddata )
 - [x] CA#04 - Validação de CPF
 - [x] CA#05 - Unicidade de CPF
 - [x] CA#06 - Mensagem de Confirmação
 - [x] CA#07 - Aptidão de Usuário
### História de Usuário #3 - Página de Login *
 - [x] CA#01 - Campos de Login
 - [x] CA#02 - Validação de Campos
 - [x] CA#03 - Redirecionamento de Login
 - [x] CA#04 - Utilização do Sistema de Autenticação Django(UserCreationForm)

### História de Usuário #6 - Agendamento de Exame
 - [x] CA#01 - Limite de Agendamento por Usuário
 - [x] CA#02 - Campos de Agendamento
 - [x] CA#03 - Limite de Usuários por Agendamento
 - [x] CA#04 - Validação de Horário de Agendamento
 - [x] CA#05 - Validação de Data de Agendamento
 - [x] CA#06 - Validação de Idade de Usuário por Horário de Agendamento
 - [x] CA#07 - Formato de Campo de Estabelecimento
 - [x] CA#08 - Formato de Campo de Horário
 - [x] CA#09 - Validação de Horário de Agendamento Futura
 - [x] CA#10 - Redirecionamento de Agendamento

## Não-Obrigatórias
### História de Usuário#4 - Administração da plataforma

 - [x] CA#01 -   Command para inserir Estabelecimentos
 - [x] CA#02 - Listagem de Estabelecimento
 - [x] CA#03 - Filtragem de Estabelecimento

### História de Usuário#5 - Listagem de Exames
 - [x] CA#01 - Requerimento de Usuário Autenticado
 - [x] CA#02 - Campos da Tabela de Listagem
 - [x] CA#03 - Horário Expirado
### História de Usuário#7 - Painel Administrativo
- [ ] CA#01 - Gráfico de Barras de Agendamento por Estabelecimento
 - [ ] CA#02 - Gráfico Pizza de Aptidão de Usuários
 - [x] CA#03 - Redirecionamento para Usuários Não-Autorizados
