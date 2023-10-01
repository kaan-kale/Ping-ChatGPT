# Ping-ChatGPT

- Install the openai package and add you openai api key to the environment

```bash
pip install openai
export OPENAI_API_KEY="YOUR_API_KEY"
```

When you run the "main.py" file, the results will be written in "results.txt". The prompt is "Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ..." to ensure same answer every time and solely get the response delay based on time, location etc. We do not want different answer lengths to affect our results.
