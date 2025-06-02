# Gerenciador de Salas

**Conteúdo da Disciplina**: Algoritmos  

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/2006196  |  Wallyson Paulo Costa Souza |
| 22/2006893  |  Kaio Macedo Santana |

## Sobre 
Essa aplicação simula o agendamento de uma Sala Multiuso para várias atividades diferentes (como Artes, Música, Ballet, etc.).
Ela recebe vários pedidos de reserva com horários diferentes, e o objetivo é aceitar o maior número possível desses pedidos sem que os horários das atividades se sobreponham — ou seja, só uma atividade pode usar a sala por vez. O algoritmo usado é o Interval Scheduling (Escalonamento de Intervalos).

## Instalação 
**Linguagem**: Python<br>
**Framework**: XXXXXX<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.

1. Clone este repositório:
   ```bash
    https://github.com/projeto-de-algoritmos-2025/Gerenciador_de_Salas.git
   ```
3.Acesse o diretório do Projeto:   
   ```bash
   cd gerenciador_salas.py
   ```
4.Execute o arquivo principal:
   ```bash
  python gerenciador_salas.py
   ```
    

## Como ela funciona?

 Gerar pedidos de reserva:
    O programa cria vários pedidos aleatórios para usar a sala, com horários de início e fim dentro de um dia de 24 horas.
    
 Escolher quais aceitar:
    Ele usa um algoritmo chamado Interval Scheduling que seleciona o maior número possível de atividades que não se sobrepõem, ou seja, não tem conflito de horário.
    
 Mostrar os resultados:
Na primeira tabela, você vê todos os pedidos gerados, com as atividades e seus horários (no formato AM/PM).

 Na segunda tabela, aparecem apenas os pedidos que foram aceitos (os que não conflitavam).

 No gráfico, fica fácil visualizar quais horários estão ocupados e quais foram aprovados (em azul) ou recusados (em cinza).

## Apresentação
Link da apresentação:





