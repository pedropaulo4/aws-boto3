📦 Projeto Básico com Boto3 (AWS SDK para Python)

Este repositório tem como objetivo servir como introdução ao uso do boto3, o SDK oficial da AWS para Python.
Aqui você encontrará uma base organizada para trabalhar com os principais serviços da AWS de forma simples e didática.

Serviços abordados neste projeto:

EC2

S3

Lambda

DynamoDB

Este projeto é indicado para quem está começando com AWS e automação usando Python.

🎯 Objetivo do Projeto

Aprender a configurar o boto3

Entender como se conectar aos serviços da AWS

Criar uma base reutilizável para projetos futuros

Organizar o código por serviço da AWS

🛠️ Pré-requisitos

Antes de iniciar, você precisa ter:

Python 3.8 ou superior

Conta ativa na AWS

AWS CLI instalada

Credenciais AWS configuradas corretamente

Permissões adequadas (IAM)

📦 Instalação

Instale as dependências do projeto:

pip install -r requirements.txt


Ou instale diretamente o boto3:

pip install boto3

🔐 Configuração da AWS

As credenciais da AWS devem estar configuradas localmente usando o AWS CLI:

aws configure


Será necessário informar:

Access Key ID

Secret Access Key

Região padrão

Formato de saída

⚠️ Nunca versionar credenciais no repositório.

📁 Estrutura do Projeto

Estrutura simples e organizada por serviço:

.
├── ec2.py          # Funções relacionadas ao EC2
├── s3.py           # Funções relacionadas ao S3
├── lambda_fn.py    # Funções relacionadas ao AWS Lambda
├── dynamodb.py     # Funções relacionadas ao DynamoDB
├── requirements.txt
└── README.md


Cada arquivo contém funções responsáveis por interagir com um serviço específico da AWS.

☁️ Serviços Utilizados
EC2

Utilizado para gerenciamento de instâncias de máquinas virtuais na AWS.

S3

Utilizado para armazenamento de arquivos e objetos na nuvem.

Lambda

Utilizado para execução de funções serverless sem gerenciamento de servidores.

DynamoDB

Banco de dados NoSQL totalmente gerenciado pela AWS.

📌 Boas Práticas

Utilize IAM Roles sempre que possível

Evite usar credenciais diretamente no código

Use variáveis de ambiente para configurações

Aplique o princípio do menor privilégio

Separe responsabilidades por arquivo/módulo

📚 Referências Úteis

Documentação oficial do boto3
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

Documentação AWS
https://docs.aws.amazon.com/

🧑‍💻 Finalidade

Este repositório é voltado para estudo e aprendizado, podendo ser usado como base para projetos maiores que utilizem serviços da AWS com Python.

