# Mon premier container

Ma toute première intéraction avec des containers.

Homelab utilisé : v1

## Commandes

1. Charger et lancer l'image : `podman run -it debian:12 bash`

Jouer avec l'image : 
```bash
python --version # Devrait renvoyer une erreur car rien n'est installé

apt update -y
apt install python3 python-pip python3-venv

source .venv/bin/activate

(.venv) pip install cowsay
(.venv) echo "import cowsay; cowsay.cow('Hello world !')" > script.py
(.venv) python -m script.py 
```

2. Détacher l'image : `CTRL + Q` puis `CTRL + P`

3. Voir l'état du container en cours : `podman ps`

4. Stopper le container : `podman stop <nom container>`

5. Supprimer le conteneur : `podman rm <nom conteneur>`