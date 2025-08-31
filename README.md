Desafio Técnico Doc9 – RPA Challenge

Visão Geral
Esta aplicação é a solução do desafio técnico proposto pela Doc9. O objetivo é criar um fluxo de trabalho em Python que acessa o site RPA Challenge OCR, processa uma tabela de dados, baixa as faturas correspondentes e gera um arquivo CSV com as informações extraídas.

O projeto foi desenvolvido com foco em performance, boas práticas de desenvolvimento e código limpo, seguindo uma arquitetura modular. Para melhorar o desempenho, optei por utilizar asyncio e aiohttp, permitindo que as faturas sejam baixadas de forma assíncrona e simultânea, tornando o processo mais rápido e eficiente do que o tradicional web scraping.

A lógica de negócio foi organizada em três módulos principais:

1. fetch_invoice_data: responsável pela extração das informações via endpoint JSON e pelo filtro dos dados por data. A escolha do aiohttp permite que essa etapa seja realizada de forma assíncrona, aumentando a performance do processo.

2. download_invoices.py: contém a lógica de download das faturas e gerenciamento das tasks assíncronas.

3. write_csv: responsável pela geração do arquivo CSV. Para maior controle, o nome do arquivo é gerado dinamicamente com data e hora, garantindo histórico de execuções.

Além dos 3 componentes, também temos o main, que realiza a orquestração destes componentes.

Features
-Extração de Dados: Realiza uma requisição à API do site para obter a lista completa de faturas.

-Filtragem Inteligente: Processa apenas as faturas cuja data de vencimento seja igual ou anterior à data atual, conforme especificado no desafio.

-Download Paralelo: Baixa de forma assíncrona e simultânea todas as faturas filtradas, otimizando drasticamente o tempo de execução.

-Geração de Relatório: Salva os dados extraídos em um arquivo .csv formatado, dentro de uma pasta de resultados.

-Organização: Salva os arquivos de fatura e o relatório CSV em uma estrutura de pastas output/ limpa e organizada.

Decisões Técnicas e Arquitetura
Para atender aos critérios de avaliação, especialmente os de performance e qualidade de código, as seguintes decisões foram tomadas:

1. Arquitetura Modular (Princípio da Responsabilidade Única)
O código foi estruturado em três componentes principais, cada um com uma responsabilidade clara:

fetch_invoice_data.py: Responsável exclusivamente por se comunicar com a API e buscar os dados brutos.

download_invoices.py: Responsável pela lógica de download paralelo e salvamento dos arquivos.

write_csv.py: Responsável por gerar o arquivo de relatório final.

Essa separação, orquestrada pelo main.py, torna o código mais legível, testável e fácil de manter.

2. Performance: Programação Assíncrona (Async I/O)
Para atender ao requisito de alta performance (2s), a escolha principal foi utilizar programação assíncrona com as bibliotecas asyncio e aiohttp.

3. Qualidade do Código e Boas Práticas
Gerenciamento de Dependências: Todas as bibliotecas(no caso desse projeto somente uma) necessárias estão listadas no arquivo requirements.txt.

Configuração Centralizada: O arquivo src/config.py centraliza todas as constantes e caminhos, facilitando a manutenção e evitando "magic strings".

Logging: O módulo logging foi utilizado para fornecer feedback claro sobre cada etapa do processo, o que é mais robusto e flexível que o uso de print().

Type Hinting: O código utiliza anotações de tipo para melhorar a legibilidade e permitir a verificação estática, tornando o desenvolvimento mais seguro.

Manuseio de Caminhos: A biblioteca pathlib foi usada para lidar com caminhos de arquivos de forma moderna e independente de sistema operacional.

ESTRUTURA DE PASTAS
O projeto segue uma estrutura de src layout, que é um padrão comum para aplicações Python:

Resultado Esperado
Após a execução, você verá no terminal os logs de cada etapa do processo. Além disso, dentro da pasta output teremos os resultados exibidos da seguinte forma:

output/
├── Invoices/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ... 
└── Results/
    └── 25-08-2025_14-30-00.csv

Desenvolvido por Gustavo Regnel.


--------------------------------- INSTRUÇÕES PARA CONFIGURAÇÃO E EXECUÇÃO ----------------------------------------------

Siga os passos abaixo para configurar e executar a aplicação.

Pré-requisitos
Python 3.8+

Git

Passos


1. Clone o Repositório:


1.1 git clone https://github.com/GustRegnel/Teste_Tecnico_Doc9.git


1.2 cd Teste_Tecnico_Doc9


2. Crie e Ative o Ambiente Virtual:


# Para Windows


python -m venv venv


venv\Scripts\activate.bat


# Para macOS/Linux


python3 -m venv venv


source venv/bin/activate


# Instalação e execução


3. Instale as Dependências:


pip install -r requirements.txt


4. Execute a Aplicação:
O script deve ser executado como um módulo a partir do diretório raiz para garantir que as importações funcionem corretamente.

Para isso utilize o seguinte comando:


python -m src.main


Obrigado pela atenção!