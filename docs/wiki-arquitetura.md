# Arquitetura do Sistema

Este documento descreve em detalhes como o sistema é estruturado internamente.

---

## Visão Geral

O sistema é dividido em três camadas independentes que se comunicam entre si:

```
┌─────────────────────────────────────────────────────┐
│                    USUÁRIO                          │
│                  (Telegram)                         │
└───────────────────────┬─────────────────────────────┘
                        │ mensagem
                        ▼
┌─────────────────────────────────────────────────────┐
│             PONTE DE COMUNICAÇÃO                    │
│                                                     │
│  • Recebe a mensagem                                │
│  • Identifica o remetente                           │
│  • Encaminha ao Cérebro                             │
│  • Retorna a resposta ao usuário                    │
└───────────────────────┬─────────────────────────────┘
                        │ instrução
                        ▼
┌─────────────────────────────────────────────────────┐
│                 CÉREBRO DA IA                       │
│                                                     │
│   ┌──────────┐  ┌──────────┐  ┌──────────────┐    │
│   │ Intenção │  │ Comandos │  │  Modelo LLM  │    │
│   └──────────┘  └──────────┘  └──────────────┘    │
│                                                     │
│   ┌──────────────────────────────────────────┐     │
│   │             Memória (SQLite)             │     │
│   └──────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

---

## Camada 1 — Interface (Telegram)

Responsável pela comunicação com o usuário.

O Telegram foi escolhido como interface inicial pelos seguintes motivos:

- API oficial, gratuita e estável
- Sem risco de banimento de conta
- Suporte nativo a bots em Python (`python-telegram-bot`)
- Possibilidade de migrar para outras interfaces no futuro sem alterar o Cérebro

**Interfaces futuras planejadas:**
- WhatsApp
- Discord
- Aplicativo próprio
- Interface web local

---

## Camada 2 — Ponte de Comunicação

A ponte é o intermediário entre a interface e o Cérebro. Ela não toma decisões.

**Responsabilidades:**
1. Receber a mensagem do usuário
2. Identificar quem enviou (ID do usuário)
3. Formatar e encaminhar ao Cérebro
4. Receber a resposta do Cérebro
5. Enviar a resposta ao usuário no Telegram

**Implementação:** FastAPI + python-telegram-bot (webhook)

---

## Camada 3 — Cérebro da IA

Esta é a parte central do sistema. Toda a lógica fica aqui.

### Fluxo de Processamento

Quando uma mensagem chega, o Cérebro segue este fluxo:

```
Mensagem recebida
       │
       ▼
Identificar intenção
       │
       ├── É um comando? ──► Executar comando ──► Responder
       │
       └── É uma pergunta? ──► Consultar memória
                                      │
                                      ▼
                               Chamar modelo LLM
                                      │
                                      ▼
                               Gerar resposta
                                      │
                                      ▼
                               Registrar interação
                                      │
                                      ▼
                               Responder ao usuário
```

### Módulos do Cérebro

| Módulo | Arquivo | Função |
|---|---|---|
| Identificação de intenção | `brain/intent.py` | Classifica o tipo de mensagem |
| Execução de comandos | `brain/commands.py` | Executa ações específicas |
| Integração com LLM | `brain/ai.py` | Chama o modelo de linguagem |
| Banco de dados | `memory/database.py` | Lê e escreve na memória |

---

## Sistema de Memória

A memória é o que diferencia o assistente de um chatbot simples.

**Dados armazenados:**

```
memory/
├── conversas         → histórico completo de mensagens
├── atividades        → estudos, corridas, treinos registrados
├── tarefas           → lembretes e pendências
└── configurações     → preferências do usuário
```

**Banco de dados:** SQLite (fase inicial) → PostgreSQL (escala futura)

---

## Sistema de IA (LLM)

Duas opções de implementação, intercambiáveis sem alterar o restante do sistema:

### Opção A — API Externa

- **Exemplos:** Claude (Anthropic), Gemini (Google)
- **Vantagens:** qualidade superior, fácil implementação
- **Desvantagens:** custo, dependência de internet, dados saem da máquina

### Opção B — IA Local (preferida)

- **Ferramenta:** Ollama
- **Modelos:** Llama 3, Mistral, Gemma
- **Vantagens:** privacidade total, sem custos por uso
- **Desvantagens:** exige hardware (mínimo 8GB RAM), respostas mais lentas

> A arquitetura foi projetada para suportar a troca entre as duas opções sem reescrever o sistema.

---

## Hardware

| Máquina | Função |
|---|---|
| PC principal (Windows) | Desenvolvimento, testes, versionamento |
| Notebook servidor (Linux) | Rodar a IA continuamente, armazenar dados, hospedar a API |
