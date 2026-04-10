# Mon premier container

Ma toute première intéraction avec des containers.

Source : [TP1 - Image Docker basique avec Debian 12 - Stéphane Robert](https://github.com/stephrobert/containers-training/blob/main/00-Docker/01-debian12-basique/01-contruction-1ere-image.md) 

Homelab utilisé : [v1](https://github.com/petoulemonde/homelab/releases/tag/v1)

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

## Ce que j'ai appris
**Connaissances** : 
- Conteneur : 
    - Intéragir avec les containers via le CLI

**Compétences** : 
- Podman
    - Commandes de base : 
    ```bash
    podman ps # lister les containers en cours
    podman ps -a # lister les container en cours ou arretés
    podman stop # arreter un container
    podman start # redémarrer un container
    ```
    - Détacher un container : `CTRL + P puis CTRL + Q`
