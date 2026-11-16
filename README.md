# AI-Molecular-Analyst-

**Assistente de quimioinformática baseado em inteligência artificial, integrando modelos de linguagem locais, Python e RDKit para análise molecular e cálculo de propriedades físico-químicas.**

## Sobre o Projeto

O AI Molecular Analyst é um projeto independente voltado à integração entre Inteligência Artificial e química computacional, com o objetivo de simplificar e automatizar processos de análise molecular.

A proposta é permitir que usuários interajam com ferramentas de química computacional por meio de linguagem natural, tornando as análises moleculares mais acessíveis, intuitivas e eficientes.

## Nota sobre a Versão Demonstrativa

Este repositório apresenta uma versão demonstrativa (*Demo*) do AI Molecular Analyst, desenvolvida para apresentar os conceitos fundamentais, as tecnologias utilizadas e as integrações iniciais do projeto.

**Esta não representa a versão final do projeto.** A solução completa contempla capacidades mais amplas, com foco especial na autonomia do usuário, na facilidade de interação e na automação de processos computacionais e científicos.

O repositório público não inclui a implementação completa nem os materiais proprietários do projeto.

## Tecnologias e Bibliotecas

- **Python 3.12** – Linguagem de programação principal.
- **RDKit** – Processamento de estruturas moleculares e cálculo de descritores moleculares.
- **Ollama** – Execução local de modelos de linguagem.
- **Qwen 2.5 3B** – Modelo de linguagem utilizado nos testes iniciais.
- **LangChain** – Integração e orquestração de modelos de linguagem.
- **Pandas e NumPy** – Manipulação e processamento de dados.
- **Plotly, Matplotlib e Seaborn** – Visualização de dados.
- **Streamlit** – Desenvolvimento de interfaces interativas.
- **ReportLab, OpenPyXL e python-docx** – Geração de documentos e relatórios.

## Funcionalidades Implementadas

- Integração entre Python e RDKit.
- Leitura de estruturas moleculares a partir de representações SMILES.
- Cálculo de descritores moleculares:
  - Massa molecular (MW);
  - Coeficiente de partição octanol/água (LogP);
  - Área de superfície polar topológica (TPSA);
  - Doadores de ligações de hidrogênio (HBD);
  - Aceitadores de ligações de hidrogênio (HBA).
- Integração com modelos de linguagem executados localmente por meio do LangChain e Ollama.
- Validação inicial dos cálculos moleculares e das respostas geradas pela inteligência artificial.

## Arquitetura do Projeto

O projeto segue uma abordagem modular, integrando diferentes componentes:

1. **Processamento de Linguagem Natural:** interpretação das solicitações do usuário por um modelo de linguagem local.
2. **Orquestração:** o LangChain coordena a interação entre o modelo de linguagem e as ferramentas computacionais.
3. **Química Computacional:** o RDKit realiza cálculos moleculares e processamento de estruturas químicas.
4. **Processamento de Dados:** bibliotecas Python organizam e processam os resultados analíticos.
5. **Geração de Resultados:** produção de tabelas, visualizações e relatórios científicos.

*A arquitetura representa a direção de desenvolvimento do projeto; nem todos os componentes estão implementados nesta versão demonstrativa.*

## Desenvolvimento Futuro

- Análise de múltiplas moléculas.
- Geração automatizada de DataFrames.
- Filtragem molecular baseada em propriedades físico-químicas.
- Avaliação pelas regras de Lipinski, Egan e Veber.
- Análise BOILED-Egg.
- Geração de fingerprints moleculares.
- Visualização interativa de dados.
- Geração automatizada de relatórios científicos.
- Execução autônoma de fluxos de análise por meio de comandos em linguagem natural.

## Instalação e Execução

**Requisitos:**

- Python 3.12;
- Ollama instalado e em execução;
- Modelo Qwen 2.5 3B disponível localmente.

**Instalação das dependências:**

```bash
pip install -r requirements.txt
```

**Execução da demonstração:**

```bash
python teste.py
```

## Status do Projeto

**Em desenvolvimento — Protótipo inicial validado.**

A versão pública atual demonstra a integração entre RDKit, LangChain e Ollama, servindo como apresentação inicial da proposta tecnológica do AI Molecular Analyst.

## Direitos Autorais

Copyright © 2026. Todos os direitos reservados.

Este repositório está disponível publicamente para consulta e demonstração em portfólio. Não é concedida autorização para copiar, modificar, redistribuir ou utilizar comercialmente seu conteúdo sem autorização prévia do autor.
