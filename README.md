# 🤖 Assistente Pessoal com IA

> Um assistente digital privado, acessível pelo Telegram, rodando no seu próprio hardware.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## O que é este projeto?

Este projeto é um **assistente pessoal inteligente** que centraliza informações, automatiza tarefas e ajuda a organizar estudos, projetos e rotina — tudo via mensagens de texto, hospedado no próprio notebook.

Não é apenas um chatbot. É um sistema pessoal que aprende sua rotina, registra hábitos, executa comandos e responde perguntas com base no seu histórico.

**Exemplos de uso:**

```
"O que devo estudar hoje?"
"Registre uma corrida de 20 minutos."
"Quanto tempo estudei esta semana?"
"Me lembre de revisar matemática amanhã."
```

---

## Arquitetura

```
[Telegram] ──► [Ponte de Comunicação] ──► [Cérebro da IA]
                                               │
                                    ┌──────────┼──────────┐
                                 [Memória]  [Comandos]  [IA/LLM]
                                 (SQLite)               (Local/API)
```

O sistema é dividido em três camadas:

| Camada | Responsabilidade |
|---|---|
| **Interface** | Comunicação com o usuário via Telegram |
| **Ponte** | Recebe mensagens, identifica remetente, encaminha e retorna respostas |
| **Cérebro** | Interpreta intenções, executa ações, consulta memória, gera respostas |

---

## Funcionalidades Planejadas

- [x] Estrutura base do projeto
- [ ] Bot no Telegram funcional
- [ ] Integração com modelo de IA
- [ ] Sistema de memória (histórico de conversas)
- [ ] Registro de atividades (estudo, corrida, treino)
- [ ] Consultas ao histórico
- [ ] Sistema de lembretes
- [ ] Automações locais (abrir programas, scripts)
- [ ] Sugestões personalizadas com base em hábitos

---

## Stack Tecnológica

| Componente | Tecnologia |
|---|---|
| Linguagem | Python 3.11+ |
| Backend | FastAPI |
| Interface | Telegram Bot (python-telegram-bot) |
| Banco de dados | SQLite → PostgreSQL (futuro) |
| IA (inicial) | API externa (Claude / Gemini) |
| IA (futura) | Ollama + Llama / Mistral (local) |

---

## Estrutura do Repositório

```
assistente-ia/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
│
├── app/
│   ├── main.py              # Ponto de entrada
│   ├── bot/
│   │   └── telegram.py      # Integração com Telegram
│   ├── brain/
│   │   ├── intent.py        # Identificação de intenção
│   │   ├── commands.py      # Execução de comandos
│   │   └── ai.py            # Integração com LLM
│   ├── memory/
│   │   ├── database.py      # Conexão com banco
│   │   └── models.py        # Modelos de dados
│   └── config.py            # Configurações gerais
│
├── docs/
│   ├── arquitetura.md
│   ├── comandos.md
│   └── roadmap.md
│
└── scripts/
    └── setup.sh             # Script de instalação
```

---

## Como Rodar (em breve)

A documentação de instalação será adicionada conforme o projeto avança.

Consulte a [Wiki](../../wiki) para documentação detalhada.

---

## Roadmap

| Fase | Descrição | Status |
|---|---|---|
| Fase 1 | Assistente básico — recebe e responde mensagens | 🔄 Em andamento |
| Fase 2 | Sistema de comandos — registros e consultas | ⏳ Planejado |
| Fase 3 | Memória persistente — histórico organizado | ⏳ Planejado |
| Fase 4 | Automações — controle do computador | ⏳ Planejado |
| Fase 5 | IA avançada — sugestões e análise de hábitos | ⏳ Planejado |

---

## Motivação

Este projeto nasceu com dois objetivos: criar uma ferramenta útil para o dia a dia e aprender programação, APIs, bancos de dados e arquitetura de software na prática.

---

## Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.
