# Tamagotchi Game

Bienvenue dans le jeu Tamagotchi ! Il s'agit d'un jeu d'animaux virtuels dans lequel tu dois prendre soin de ton Tamagotchi en gérant sa satisfaction, sa santé, son ennui et ses besoins. Le jeu comprend une boutique pour acheter des objets, jouer à des mini-jeux et veiller au bien-être de ton animal.

## Tables des matières

- [Installation](#installation)
- [Gameplay](#gameplay)
- [Images](#images)
- [Caractéristiques](#caractéristiques)
- [Comment jouer](#jouer)
- [Librairies et dépendances](#dépendances)
- [Contribution](#contributiion)
- [License](#license)

## Installation

Pour commencer, cloner le repo Github et installer les dépendances et librairies Python requises.

```sh
git clone https://github.com/perazaf1/tamagotchi-game.git
cd tamagotchi-game
pip install -r requirements.txt
```

Assurez-vous que Python 3.x et Pygame sont installés.

## Gameplay
Le jeu commence dans un menu principal où vous pouvez choisir de commencer une nouvelle partie ou de reprendre une partie sauvegardée. Vous devez maintenir les indicateurs de votre Tamagotchi (satisfaction, santé, ennui et besoins) au-dessus de zéro pour continuer à jouer. Si l'un de ces indicateurs atteint zéro, c'est le game over.

## Quelques Images
- Menu d'accueil <img align="center" height = "250px" width = "400px" alt="Accueil" src = "https://cdn.discordapp.com/attachments/782529104502587404/1241412902624301056/preview1.png?ex=664a1b5c&is=6648c9dc&hm=64823d93f39b903e22dca1263481963ba2ecf3b490358bc04d43e24141087849&">
- Lobby <img align="center" height = "250px" width = "400px" alt="Lobby" src = "https://cdn.discordapp.com/attachments/782529104502587404/1241412902976618650/preview2.png?ex=664a1b5c&is=6648c9dc&hm=6e8f2a5910ba025127d0457de16c398438117ee9211cb1471306de5901e53e96&">
- Magasin <img align="center" height = "250px" width = "400px" alt="Magasin" src = "https://cdn.discordapp.com/attachments/782529104502587404/1241412902372774050/preview3.png?ex=664a1b5c&is=6648c9dc&hm=a11f56877f5ffae8f96f847a919c3a7c8fc6c20de03b4ed0550d19fd51c38e78&">



## Caractéristiques
- Gestion des besoins : Gardez votre Tamagotchi heureux et en bonne santé en surveillant ses besoins.
- Animations : Le Tamagotchi est animé pour une expérience plus immersive.
- Mini-jeux : Jouez à des mini-jeux pour gagner des récompenses et maintenir le bonheur de votre Tamagotchi.
- Boutique : Achetez des objets pour améliorer la vie de votre Tamagotchi.
- Sauvegarde et chargement : Sauvegardez votre progression et reprenez là où vous vous êtes arrêté.

## Jouer 

1. Lancer le jeu : Exécutez le fichier main.py pour lancer le jeu.
2. Menu principal : Choisissez de commencer une nouvelle partie ou de reprendre une partie sauvegardée.
3. Surveillez les indicateurs : Gardez un œil sur les indicateurs de satisfaction, santé, ennui et besoins de votre Tamagotchi.
4. Utilisez les boutons : Interagissez avec les boutons pour nourrir, jouer, soigner et envoyer votre Tamagotchi aux toilettes.
5. Mini-jeux et boutique : Jouez à des mini-jeux pour gagner des pièces et achetez des objets dans la boutique.
6. Sauvegarde automatique : Votre progression est automatiquement sauvegardée lorsque vous quittez le jeu.

## Dépendances

Le jeu utilise les bibliothèques suivantes :
pygame : pour les graphismes, les sons et les interactions du jeu.
json : pour la sauvegarde et le chargement des données de jeu.

Pour installer toutes les dépendances, exécutez :
```sh
pip install -r requirements.txt
```

## Contribution

Les contributions sont les bienvenues ! Veuillez suivre ces étapes pour contribuer :

- Fork le repository
- Créez votre branche de fonctionnalité (``` git checkout -b feature/AmazingFeature ```)
- Commitez vos changements (```git commit -m 'Add some AmazingFeature' ```)
- Poussez votre branche (```git push origin feature/AmazingFeature```)
- Ouvrez une Pull Request

## License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.