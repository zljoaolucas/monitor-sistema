# Monitor de Sistema em Tempo Real

Monitor de recursos do sistema (CPU, RAM, disco e rede) no terminal, com interface
em tempo real construída com [Rich](https://github.com/Textualize/rich) e dados
coletados via [psutil](https://github.com/giampaolo/psutil).

![status](https://img.shields.io/badge/status-ativo-brightgreen)

## Preview

O monitor exibe um painel com:

- **CPU** — uso percentual, colorido por faixa (verde/amarelo/vermelho)
- **RAM** — uso percentual, MB usados e disponíveis
- **Disco** — uso percentual da partição raiz e GB livres
- **Rede** — total enviado e recebido (MB) desde o boot

## Requisitos

- Python 3.8+
- Linux ou macOS (a leitura de disco usa o caminho `/`; para Windows, ajuste
  para algo como `C:\\` em `ps.disk_usage(...)`)

## Instalação

```bash
git clone https://github.com/zljoaolucas/monitor-sistema.git
cd monitor-sistema
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

Pressione `Ctrl+C` para encerrar.

## Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
