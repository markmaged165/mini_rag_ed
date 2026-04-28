# mini_rag_ed

this is minimal impementation of the RAG MODEL for the question answering 
### requirements
-python 3.8 or later
##### instal python  using miniconda 
1) down adn install mininconda 
2) create  a new env using the folowing comand 

```bash
$ ' conda -n mini-rag-app '
```

## install the required packages 

````bash
 $ pip install -r requirements.txt
``````
```bash
$ cp .env.example .env
```

set your env variablesin the `.env` file . like `openai_api _key`

## run the fastapi server 
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```