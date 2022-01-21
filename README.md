# learning
Repository used for self-learning and personal development

# Deeplearning Env
```bash
virtualenv -p python3.8 deep_learning_env
printf "\n# Adding this command to read local .env file" >> deep_learning_env/bin/activate
printf "\nexport \$(grep -v '^#' .env | xargs)" >> deep_learning_env/bin/activate
source deep_learning_env/bin/activate
```


# Env
```bash
virtualenv -p python3.8 env
printf "\n# Adding this command to read local .env file" >> deep_learning_env/bin/activate
printf "\nexport \$(grep -v '^#' .env | xargs)" >> deep_learning_env/bin/activate
source deep_learning_env/bin/activate
```


# Download key from kaggle and store it in kaggle  folder