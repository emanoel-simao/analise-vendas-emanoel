# 📊 Projeto de Análise de Vendas com Streamlit

Este é um projeto simples de análise de dados de vendas desenvolvido com **Python** e **Streamlit**. Ele permite carregar arquivos `.xlsx` contendo dados de vendas e visualizar métricas de forma interativa e visual.

## 🚀 Acesse a aplicação online

Você pode testar a aplicação diretamente pelo navegador no link abaixo:

🔗 [Clique aqui para testar no Streamlit](https://mg2hirll5q9cgxadd3p8f2.streamlit.app/)

## 🧰 Tecnologias utilizadas

- Python 3.10+
- Pandas
- Streamlit
- openpyxl (para leitura de arquivos `.xlsx`)

## 📁 Estrutura do projeto

```
📦 analise-vendas-emanoel
├── analisador.py              # Script principal da aplicação
├── exemplo_streamlit.xlsx     # Arquivo de exemplo para testes
├── requirements.txt           # Dependências do projeto
└── .devcontainer/             # Configuração do Dev Container (opcional)
```

## ▶️ Como rodar localmente

1. **Clone o repositório**:
```bash
git clone https://github.com/emanoel-simao/analise-vendas-emanoel.git
cd analise-vendas-emanoel
```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**:
```bash
streamlit run analisador.py
```

## 📌 Observações

- O aplicativo aceita arquivos `.xlsx` como entrada. Certifique-se de que o arquivo está formatado corretamente.
- Um exemplo de planilha está incluído no repositório: `exemplo_streamlit.xlsx`.

## 📬 Contato

Feito por **Emanoel Simão** – sinta-se à vontade para entrar em contato ou contribuir!
