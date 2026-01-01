- env variable: value stored by OS

1. set env variable (lasts until you close the terminal)
- export OPEN_AI_KEY=""

2. verify it exists
- echo $OPENAI_API_KEY

3. use in code
- import os
api_key = os.environ["OPENAI_API_KEY"]

To get key:

1. OpenAI Platform: https://platform.openai.com
2. Quickstart: https://platform.openai.com/docs/quickstart
3. Create and view keys: https://platform.openai.com/api-keys