```text
+----------------------------------------------------------+
|                                                          |
| ░█░█░█▀█░█░░░█░░░█▀▀░▀█▀░░░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░ |
| ░█▄█░█▀█░█░░░█░░░█▀▀░░█░░░░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░ |
| ░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀ |
|                                                          |
+----------------------------------------------------------+
```

Software desenvolvido em **Python** para o gerenciamento financeiro, onde os dados são armazenados em um banco SQLite e exportados em planilhas do Excel.

O projeto foi desenvolvido para automatizar o processo de organização financeira em uma planilha. Inicialmente o projeto era para o gerenciamento de despesas, mas o software possui diferentes funcionalidades para ajudar o usuário com o gerenciamento financeiro.

**A estrutura do README.md**:

- [Estrutura do projeto](#estrutura-do-projeto);
- [Tecnologias utilizadas](#tecnologias-utilizdas);
- [Instalação](#instalação);
- [Funcionamento](#funcionamento);
- [Autores](#autores);
- [Como contribuir?](#como-contribuir);

---

# Estrutura do projeto
```
Wallet_Control/
│
├── data/               # Banco de dados SQLite
├── database/           # Operações do banco
├── services/           # Regras de negócio
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Tecnologias utilizdas
- Linguagens:
    - Python 3
- Bibliotecas:
    - OpenPyXL
- Banco de dados: SQLite
- Empacotamento: **PyInstaller**

---

# Instalação
Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/Wallet_Control.git
cd Wallet_Control
```
Instale as depedências:

```bash
pip install -r requirements.txt
```
Execute o programa:
```bash
python main.py
```

---

# Funcionamento
O arquivo `main` é o menu para o uso de todo o software, e cada seleção é um módulo python diferente. Tem um módulo para a registro de **despesas**, módulo para **entrada financeira**, módulo para **conexão com o banco** de dados.

Após a utilização do softwate com os registros financeiros feitos e armazenados no banco de dados, localizado na pasta `data/financeiro.db` (localizado na mesma pasta onde se encontra o software executável), a exportação da planilha `.xslx` se encontra na pasta `export/` (localizado na mesma pasta onde se encontra o software executável).

---

# Autores
- [@pedroh288](https://www.github.com/pedroh288)

---

# Como contribuir?
1. Faça fork do repositório
2. Crie uma branch da feature (`git checkou -b ...`)
3. Faça commit das suas mudanças (`git commit -m "..."`)
4. Faça push para a branch criada (`git push origin ...`)
5. Abra um Pull Request