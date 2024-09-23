# izagent

A minimal implementation API for the MRKL algorithm.

dependencies
    - openai
    - fastapi
    - aiohttp
    - concurrent-log-handler


```bash
$ brew install rye
```

provide the following secrets in .env file
```bash
GOOGLESEARCH_BASE_URL=${GOOGLESEARCH_BASE_URL}
GOOGLESEARCH_CSE_ID=${GOOGLESEARCH_CSE_ID}
GOOGLESEARCH_API_KEY=${GOOGLESEARCH_API_KEY}

OPENAI_API_KEY=${OPENAI_API_KEY}
```

run server

```bash
$ rye sync
$ rye run dev
```

swagger
http://127.0.0.1:8000/docs#/

you could compare the difference between api/v0/mrkl and api/v0/plain 
