# testeUnitarios
Trabalho de Engenharia de Software 1 - Realizar teste unitário de uma aplicação (calculadora), de 3 a 5 unidades<br />
Nome: João Paulo Migliatti - 802534

# Descrição da aplicação:
A aplicação é uma calculadora básica, que realiza as operações de adição, subtração, multiplicação e divisão.
Foi necessário dividir a aplicação nos arquivos calculadora.py e logica_calculadora.py, pois quando os dois estavam juntos o pytest executava o menu da calculadora junto com os testes.

# Descrição dos testes:
Os testes procuram testar 4 classes da parte lógica da calculadora (arquivo logica_calculadora), sendo elas adicao, subtracao, multiplicacao e divisao. Os testes procuram falhas como divisão por 0 e divisão com dizima periódica. Basicamente todos eles inserem dois numeros em uma certa operação matemática com um resultado já predeterminado e comparam com o que a calculadora retornou, para analisar se os resultados estão corretos.

# Como rodar a aplicação e os testes:
Clonar o repositório:<br />
Utilizar o comando: git clone https://github.com/Jmigliatti/testeUnitarios.git<br />
Executar a aplicação:<br />
Vá até o diretório do repositório clonado<br />
Execute o arquivo calculadora.py com o comando: python calculadora.py<br />
Executar os testes:<br />
É necessário ter o Pytest instalado. Se não tiver, instale usando o seguinte comando: pip install pytest<br />
Vá até o diretório do repositório clonado<br />
Execute o Pytest, com o comando: python -m pytest -s teste_calculadora.py<br />
(pelo menos no windows este foi o comando correto)<br />
Isso executará os testes unitários e mostrará os resultados no terminal.<br />



