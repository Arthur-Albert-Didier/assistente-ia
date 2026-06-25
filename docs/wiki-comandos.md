# Comandos do Assistente

Lista de todos os comandos planejados e implementados.

---

## Status dos Comandos

| Símbolo | Significado |
|---|---|
| ✅ | Implementado |
| 🔄 | Em desenvolvimento |
| ⏳ | Planejado |

---

## Registro de Atividades

Comandos para registrar eventos no banco de dados.

| Comando | Exemplo | Status |
|---|---|---|
| Registrar estudo | `Estudei Python por 1 hora` | ⏳ |
| Registrar corrida | `Registre uma corrida de 20 minutos` | ⏳ |
| Registrar treino | `Fiz 30 minutos de treino` | ⏳ |
| Registrar tarefa concluída | `Conclui a tarefa X` | ⏳ |

**Exemplo de fluxo:**

```
Usuário: "Registre uma corrida de 20 minutos."

IA identifica: comando → categoria: corrida → duração: 20min
IA salva no banco de dados
IA responde: "Corrida de 20 minutos registrada. ✅"
```

---

## Consultas

Comandos para recuperar informações da memória.

| Comando | Exemplo | Status |
|---|---|---|
| Resumo do dia | `O que fiz hoje?` | ⏳ |
| Resumo da semana | `Quanto estudei esta semana?` | ⏳ |
| Histórico de corridas | `Quantas corridas fiz este mês?` | ⏳ |
| Tarefas pendentes | `Quais tarefas estão pendentes?` | ⏳ |
| Progresso de projetos | `Como está o projeto X?` | ⏳ |

---

## Lembretes

Comandos para criar e gerenciar lembretes.

| Comando | Exemplo | Status |
|---|---|---|
| Criar lembrete | `Me lembre de revisar matemática amanhã` | ⏳ |
| Listar lembretes | `Quais são meus lembretes?` | ⏳ |
| Remover lembrete | `Cancela o lembrete de matemática` | ⏳ |

---

## Automações

Comandos para controlar o computador e executar scripts.

| Comando | Exemplo | Status |
|---|---|---|
| Abrir programa | `Abra o VS Code` | ⏳ |
| Executar script | `Rode o script de backup` | ⏳ |
| Gerar relatório | `Gere um relatório semanal` | ⏳ |

> ⚠️ Automações só funcionam quando o assistente está rodando no mesmo computador que será controlado, ou via rede local.

---

## Comandos de Sistema

Comandos internos para gerenciar o próprio assistente.

| Comando | Exemplo | Status |
|---|---|---|
| Status do sistema | `/status` | ⏳ |
| Ajuda | `/ajuda` | ⏳ |
| Limpar histórico | `/limpar` | ⏳ |

---

## Como Novos Comandos São Adicionados

1. Definir o padrão de linguagem natural que aciona o comando
2. Adicionar a lógica em `brain/commands.py`
3. Registrar no banco se necessário
4. Documentar aqui

A identificação de intenção (em `brain/intent.py`) é responsável por classificar cada mensagem e decidir qual comando executar.
