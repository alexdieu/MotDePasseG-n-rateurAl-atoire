# MotDePasseGénérateurAléatoire
Générateur de mot de passe aléatoire
Il n'y a pas d'autentificateur . Ce n'est pas un outil prévu pour le vol.
Pour utiliser, il suffit de taper python password.py ou python password.py -n 8. Le script n’a qu’un seul argument, -n (ou --num), qui est le nombre de mots à générer. En ajoutant plus de mots, un mot de passe sera plus difficile à BruteForce. La valeur par défaut est de 5 mots, alors que j’utilise personnellement 8 mots pour mon mot de passe.
L’entropie d’un mot de passe est une mesure de la force qu’il est.
L’entropie est liée au nombre de suppositions qu’un attaquant devrait tenter afin de forcer le mot de passe de quelqu’un.
La définition précise de l’entropie est la base de journal 2 de l’espace de recherche.
Par exemple, si un mot de passe était un numéro aléatoire à 5 chiffres, l’espace de recherche aurait 10 à 5 mots de passe possibles, et se connecter2(10 à 5) - 16,61 bits d’entropie.
Si un mot de passe figurait sur la liste des [1000 mots de passe les plus courants] (http://www.passwordrandom.com/most-popular-passwords) (tels que '"123456"), il aurait tout au plus log2(1000) = 9,97 bits d’entropie.
JE NE SUIS RESPONSABLE D'AUCUNE UTILISATION QUI VISERAIT à ENFREINDRE LA LOI FRANCAISE OU AUTRE PAYS MERCI 
VOUS L'UTILISEZ COMME VOUS VOULEZ JE NE SERAIT PAS RESPONSABLE DE VOS ACTES !
