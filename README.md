# 📃 document-me

**Automatic Python function docstring generator** using [Langchain](https://www.langchain.com/), [Prefect](https://www.prefect.io/), and [Ollama](https://ollama.com/).

This project watches a folder of `.py` scripts, detects when one is modified, and automatically inserts Google-style docstrings into undocumented functions using a locally running LLaMA3 model via Ollama.

---

## 🚀 Features

- 📂 Watches `scripts/` for changes
- 🤖 Detects undocumented functions via AST and Watchdog
- 🧠 Uses LLaMA3 (via Ollama) to generate docstrings
- 📝 Saves output into `documented_scripts/` (non-destructive)
- ⚙️ Integrated with Prefect 2 for observability
- 📈 Optional Prefect Cloud integration

---

## 📁 Project structure

```bash
document-me/
├── document_me/        
│   ├── flows.py
│   ├── llm.py
│   ├── parser.py
│   ├── utils.py
│   └── watcher.py
├── scripts/           
│   └── example.py 
├── documented_scripts/           
│   └── example.py 
├── Makefile
└── requirements.txt        
```

---

## ⚙️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running locally
- A llama model downloaded: (Recomendation Llama3)
  ```bash
  ollama run [Llama-Model]
  ```

---

## 📦 Setup

### 1. Clone the repo 
```bash
git clone https://github.com/pablodieaco/document-me.git
cd document-me
```

### 2. Create virtual environment and install dependencies

```bash
make setup
```

### 3. (Optional) Log in to Prefect Cloud to see the executions.

```bash
make cloud-login
```

And follow the instructions.


---

## 🛠 Usage

### 1. Initialize your Ollama model

```bash
ollama run llama3
```

### 2. Run the Wathcer

```bash
make watcher 
```

By default it is suppose to be running `llama3`, if you want to use another, pass it as an argument

```bash
make watcher MODEL_NAME=llama2
```

This will:
- Continously monitor the `scripts/` folder
- On any `.py` file change detected, it will:
  - Extract functions without docstring
  - Ask your `llama3` model for docstring (via Langchain)
  - Save the result into `documented_scripts`

## 🧠 Powered by

- [Langchain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Prefect](https://prefect.io/)
- [AST + astor](https://docs.python.org/3/library/ast.html)

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for details.

---

## 🙋‍♂️ Author

Made with ❤️ by **Pablo Diego Acosta**

- 💼 LinkedIn: [linkedin.com/in/pablodiegoacosta](https://www.linkedin.com/in/pablodiegoacosta)

---

## ✨ Todo / Ideas

- [ ] Rewrite the original file (with caution).
- [ ] Use any LLM hosted on a public hub.
- [ ] Extend the functionality to support classes and complete scripts.

## 🤝 Contributing

Whether you're a researcher, developer, or enthusiast — feel free to contribute!  
You're welcome to suggest improvements.

✨ Open a pull request, start a discussion, or simply share your ideas.
