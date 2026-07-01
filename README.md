# verificar usuario conectado
git config --list

# pasta e arquivos que estão no git
Get-ChildItem -Force 

Get-ChildItem -Force backend

Remove-Item -Recurse -Force .git

git status

git init

git add .

git commit -m "Initial commit"

git log

git rev-parse --show-toplevel

git diff

git diff --cached

git branch


# Renomear branch para o padrão main
git branch -M main

# Conectar ao GitHub

## Criar o repositório no GitHub e depois:
git remote add origin https://github.com/Xandy_mm/meu-projeto.git

## Verificar
git remote -v

## Enviar o projeto
git push -u origin main

## se errar
git remote remove origin

## quando já existe arquivo (merge)
git pull origin main --allow-unrelated-histories

## Conflitos de arquivos
git status

git add README.md
git commit -m "Merge remote README"
git push -u origin main

## Opção alternativa: sobrescrever o GitHub com seu projeto local
### Use somente se você não se importa em apagar o README inicial do GitHub:
git push -u origin main --force
