# coding: utf-8
a= ['ac', 'bv', 'de', 'er', 'fb', 'gg', 'hv', 'kc', 'ls', 'lu', 'nc', 'oh', 'oj', 'pt', 'ux', 'wt', 'xi', 'yd']

# sort
# print(len(a)//2)#9
# print(a[:9])#['ac', 'bv', 'de', 'er', 'fb', 'gg', 'h', 'kc', 'ls']
# print(a[9:])#['lu', 'nc', 'oh', 'oj', 'pt', 'ux', 'wt', 'xi', 'yd']
# print(a[len(a)//2])#lu

# for i in range(0,len(a)//2):
#     b = a.index(a[:len(a)//2][i+1])
#     v= a.index(a[len(a)//2])
#     print({i},{a.index(a[:len(a)//2][i+1])},{a.index(a[len(a)//2:][i-1])}, {i +v}, {1+i+v})

# 0 1 17 9 10
# 1 2 9 10 11
# 2 3 10 11 12
# 3 4 11 12 13
# 4 5 12 13 14
# 5 6 13 14 15
# 6 7 14 15 16
# 7 8 15 16 17


# tab0 = ['bleu', 'super', 'autre', 'bizarre', 'difficile', 'drôle', 'étrange', 'facile', 'grave', 'impossible', 'jeune', 'juste', 'libre', 'malade', 'même', 'pauvre', 'possible', 'propre', 'rouge', 'sale', 'simple', 'tranquille', 'triste', 'vide', 'bonne', 'toute', 'doux', 'faux', 'français', 'gros', 'heureux', 'mauvais', 'sérieux', 'vieux', 'vrai', 'ancien', 'beau', 'blanc', 'certain', 'chaud', 'cher', 'clair', 'content', 'dernier', 'désolé', 'différent', 'droit', 'entier', 'fort', 'froid', 'gentil', 'grand', 'haut', 'humain', 'important', 'joli', 'léger', 'long', 'meilleur', 'mort', 'noir', 'nouveau', 'pareil', 'petit', 'plein', 'premier', 'prêt', 'prochain', 'quoi', 'seul', 'tout', 'vert', 'vivant', 'Noms communs', 'aide', 'chef', 'enfant', 'garde', 'gauche', 'geste', 'gosse', 'livre', 'merci', 'mort', 'ombre', 'part', 'poche', 'professeur', 'tour', 'madame', 'fois', 'paix', 'voix', 'affaire', 'année', 'arme', 'armée', 'attention', 'balle', 'boîte', 'bouche', 'carte', 'cause', 'chambre', 'chance', 'chose', 'classe', 'confiance', 'couleur', 'cour', 'cuisine', 'dame', 'dent', 'droite', 'école', 'église', 'envie', 'épaule', 'époque', 'équipe', 'erreur', 'espèce', 'face', 'façon', 'faim', 'famille', 'faute', 'femme', 'fenêtre', 'fête', 'fille', 'fleur', 'force', 'forme', 'guerre', 'gueule', 'habitude', 'heure', 'histoire', 'idée', 'image', 'impression', 'jambe', 'joie', 'journée', 'langue', 'lettre', 'lèvre', 'ligne', 'lumière', 'main', 'maison', 'maman', 'manière', 'marche', 'merde', 'mère', 'minute', 'musique', 'nuit', 'odeur', 'oreille', 'parole', 'partie', 'peau', 'peine', 'pensée', 'personne', 'peur', 'photo', 'pièce', 'pierre', 'place', 'police', 'porte', 'présence', 'prison', 'putain', 'question', 'raison', 'reponse', 'robe', 'route', 'salle', 'scène', 'seconde', 'sécurité', 'semaine',
# 'situation', 'soeur', 'soirée', 'sorte', 'suite', 'table', 'terre', 'tête', 'vérité', 'ville', 'voiture', 'bois', 'bras', 'choix', 'corps', 'cours', 'gars', 'mois',
# 'pays', 'prix', 'propos', 'sens', 'temps', 'travers', 'vieux', 'accord', 'agent', 'amour', 'appel', 'arbre', 'argent', 'avenir', 'avion', 'bateau', 'bébé', 'besoin', 'bonheur', 'bonjour', 'bord', 'boulot', 'bout', 'bruit', 'bureau', 'café', 'camp', 'capitaine', 'chat', 'chemin', 'chéri', 'cheval', 'cheveu', 'chien', 'ciel', 'client', 'cœur', 'coin', 'colonel', 'compte', 'copain', 'côté', 'coup', 'courant', 'début', 'départ', 'dieu', 'docteur', 'doigt', 'dollar', 'doute', 'droit', 'effet', 'endroit', 'ennemi', 'escalier', 'esprit', 'état', 'être', 'exemple', 'fait', 'film', 'flic', 'fond', 'français', 'frère', 'front ', 'garçon', 'général', 'genre', 'goût', 'gouvernement', 'grand', 'groupe', 'haut', 'homme', 'honneur', 'hôtel', 'instant', 'intérêt ', 'intérieur', 'jardin ', 'jour ', 'journal ', 'lieu ', 'long ', 'maître ', 'mari ', 'mariage ', 'matin ', 'médecin ', 'mètre ', 'milieu ', 'million ', 'moment ', 'monde ', 'monsieur', 'mouvement', 'moyen ', 'noir ', 'nouveau ', 'numéro ', 'oeil ', 'oiseau ', 'oncle ', 'ordre ', 'papa ', 'papier ', 'parent ', 'passage ', 'passé ', 'patron ', 'père ', 'petit ', 'peuple ', 'pied ', 'plaisir ', 'plan ', 'point ', 'pouvoir ', 'premier ', 'présent ', 'président ', 'prince ', 'problème', 'quartier', 'rapport ', 'regard ', 'reste ', 'retard ', 'retour ', 'rêve ', 'revoir ', 'salut ', 'sang ', 'secret ', 'seigneur', 'sentiment', 'service ', 'seul ', 'siècle ', 'signe ', 'silence ', 'soir ', 'soldat ', 'soleil ', 'sourire ', 'souvenir', 'sujet ', 'téléphone', 'tout ', 'train ', 'travail ', 'trou ', 'truc ', 'type ', 'vent ', 'ventre ', 'verre ', 'village ', 'visage ', 'voyage ', 'fils  ', 'gens  ', 'abandonner ', 'accepter ', 'accompagner ', 'acheter     ', 'adorer     ', 'agir     ', 'aider     ', 'aimer     ', 'ajouter ', 'aller ', 'amener ', 'amuser ', 'annoncer', 'apercevoir', 'apparaître', 'appeler ', 'apporter', 'apprendre', 'approcher', 'arranger', 'arrêter ', 'arriver ', 'asseoir ', 'assurer ', 'attaquer', 'atteindre', 'attendre', 'avancer ', 'avoir ', 'baisser ', 'battre ', 'boire ', 'bouger ', 'brûler ', 'cacher ', 'calmer ', 'casser ', 'cesser ', 'changer ', 'chanter ', 'charger ', 'chercher ', 'choisir     ', 'commencer ', 'comprendre ', 'compter     ', 'conduire ', 'connaître ', 'continuer ', 'coucher ', 'couper ', 'courir ', 'couvrir ', 'craindre', 'crier ', 'croire ', 'danser ', 'décider ', 'découvrir', 'dégager ', 'demander ', 'descendre ', 'désoler ', 'détester', 'détruire', 'devenir ', 'deviner ', 'devoir ', 'dire ', 'disparaître', 'donner ', 'dormir ', 'échapper', 'écouter ', 'écrire ', 'éloigner', 'embrasser', 'emmener ', 'empêcher', 'emporter', 'enlever ', 'entendre', 'entrer ', 'envoyer ', 'espérer ', 'essayer ', 'être ', 'éviter ', 'excuser ', 'exister ', 'expliquer', 'faire ', 'falloir ', 'fermer', 'filer ', 'finir ', 'foutre ', 'frapper ', 'gagner ', 'garder ', 'glisser ', 'habiter ', 'ignorer ', 'imaginer ', 'importer ', 'inquiéter ', 'installer ', 'intéresser ', 'inviter ', 'jeter ', 'jouer ', 'jurer ', 'lâcher ', 'laisser ', 'lancer ', 'lever ', 'lire ', 'maintenir', 'manger ', 'manquer ', 'marcher ', 'marier ', 'mener ', 'mentir ', 'mettre ', 'monter ', 'montrer ', 'mourir ', 'naître ', 'obliger ', 'occuper ', 'offrir ', 'oser ', 'oublier ', 'ouvrir ', 'paraître', 'parler ', 'partir ', 'passer ', 'payer ', 'penser ', 'perdre ', 'permettre', 'plaire ', 'pleurer ', 'porter ', 'poser ', 'pousser ', 'pouvoir ', 'préférer', 'prendre ', 'préparer ', 'présenter ', 'prévenir ', 'prier     ', 'promettre ', 'proposer ', 'protéger ', 'quitter     ', 'raconter ', 'ramener     ', 'rappeler ', 'recevoir ', 'reconnaître ', 'réfléchir ', 'refuser     ', 'regarder', 'rejoindre', 'remarquer', 'remettre', 'remonter', 'rencontrer', 'rendre', 'rentrer', 'répéter', 'répondre', 'reposer', 'reprendre', 'ressembler', 'rester', 'retenir', 'retirer', 'retourner', 'retrouver', 'réussir', 'réveiller', 'revenir', 'rêver', 'revoir', 'rre', 'risqer', 'rouer', 'sauer', 'sauer', 'savir', 'sember', 'senir', 'séparer', 'serrer', 'servir', 'sortir', 'souffrir', 'sourire', 'souvenir', 'suffire', 'suivre', 'taire', 'tendre', 'tenir', 'tenter', 'terminer', 'tirer', 'tomber', 'toucher', 'tourner', 'traîner', 'traiter', 'travailler', 'traverser', 'tromper', 'trouver', 'tuer', 'utiliser',
# 'valoir', 'vendre', 'venir', 'vivre', 'voir', 'voler', 'vouloir']

value  = "sens"
print(40*"-")

# print(len(tab0))#600
# tab0.sort()
# print(tab0)

tab0= ['Noms communs', 'abandonner ', 'accepter ', 'accompagner ', 'accord', 'acheter     ', 'adorer     ', 'affaire', 'agent', 'agir     ', 'aide', 'aider     ', 'aimer     ', 'ajouter ', 'aller ', 'amener ', 'amour', 'amuser ', 'ancien', 'annoncer', 'année', 'apercevoir', 'apparaître', 'appel', 'appeler ', 'apporter', 'apprendre', 'approcher', 'arbre', 'argent', 'arme', 'armée', 'arranger', 'arriver ', 'arrêter ', 'asseoir ', 'assurer ', 'attaquer', 'atteindre', 'attendre', 'attention', 'autre', 'avancer ', 'avenir', 'avion', 'avoir ', 'baisser ', 'balle', 'bateau', 'battre ', 'beau', 'besoin', 'bizarre', 'blanc', 'bleu', 'boire ', 'bois', 'bonheur', 'bonjour', 'bonne', 'bord', 'bouche', 'bouger ', 'boulot', 'bout', 'boîte', 'bras', 'bruit', 'brûler ', 'bureau', 'bébé', 'cacher ', 'café', 'calmer ', 'camp', 'capitaine', 'carte', 'casser ', 'cause', 'certain', 'cesser ', 'chambre', 'chance', 'changer ', 'chanter ', 'charger ', 'chat', 'chaud', 'chef', 'chemin', 'cher', 'chercher ', 'cheval', 'cheveu', 'chien', 'choisir     ', 'choix', 'chose', 'chéri', 'ciel', 'clair', 'classe', 'client', 'coin', 'colonel', 'commencer ', 'comprendre ', 'compte', 'compter     ', 'conduire ', 'confiance', 'connaître ', 'content', 'continuer ', 'copain', 'corps', 'coucher ', 'couleur', 'coup', 'couper ', 'cour', 'courant', 'courir ', 'cours', 'couvrir ', 'craindre', 'crier ', 'croire ', 'cuisine', 'côté', 'cœur', 'dame', 'danser ', 'demander ', 'dent', 'dernier', 'descendre ', 'devenir ', 'deviner ', 'devoir ', 'dieu', 'difficile', 'différent', 'dire ', 'disparaître', 'docteur', 'doigt', 'dollar', 'donner ', 'dormir ', 'doute', 'doux', 'droit', 'droit', 'droite', 'drôle', 'début', 'décider ', 'découvrir', 'dégager ', 'départ', 'désoler ', 'désolé', 'détester', 'détruire', 'effet', 'embrasser', 'emmener ', 'emporter', 'empêcher', 'endroit', 'enfant', 'enlever ', 'ennemi', 'entendre', 'entier', 'entrer ', 'envie', 'envoyer ', 'erreur', 'escalier', 'esprit', 'espèce', 'espérer ', 'essayer ', 'excuser ', 'exemple', 'exister ', 'expliquer', 'face', 'facile', 'faim', 'faire ', 'fait', 'falloir ', 'famille', 'faute', 'faux', 'façon', 'femme', 'fenêtre', 'fermer', 'filer ', 'fille', 'film', 'fils  ', 'finir ', 'fleur', 'flic', 'fois', 'fond', 'force', 'forme', 'fort', 'foutre ', 'français', 'français', 'frapper ', 'froid', 'front ', 'frère', 'fête', 'gagner ', 'garde', 'garder ', 'gars', 'garçon', 'gauche', 'genre', 'gens  ', 'gentil', 'geste', 'glisser ', 'gosse', 'gouvernement', 'goût', 'grand', 'grand', 'grave', 'gros', 'groupe', 'guerre', 'gueule', 'général', 'habiter ', 'habitude', 'haut', 'haut', 'heure', 'heureux', 'histoire', 'homme', 'honneur', 'humain', 'hôtel', 'idée', 'ignorer ', 'image', 'imaginer ', 'important', 'importer ', 'impossible', 'impression', 'inquiéter ', 'installer ', 'instant', 'intéresser ', 'intérieur', 'intérêt ', 'inviter ', 'jambe', 'jardin ', 'jeter ', 'jeune', 'joie', 'joli', 'jouer ', 'jour ', 'journal ', 'journée', 'jurer ', 'juste', 'laisser ', 'lancer ', 'langue', 'lettre', 'lever ', 'libre', 'lieu ', 'ligne', 'lire ', 'livre', 'long', 'long ', 'lumière', 'lâcher ', 'lèvre', 'léger', 'madame', 'main', 'maintenir', 'maison', 'malade', 'maman', 'manger ', 'manière', 'manquer ', 'marche', 'marcher ', 'mari ', 'mariage ', 'marier ', 'matin ', 'mauvais', 'maître ', 'meilleur', 'mener ', 'mentir ', 'merci', 'merde', 'mettre ', 'milieu ', 'million ', 'minute', 'mois', 'moment ', 'monde ', 'monsieur', 'monter ', 'montrer ', 'mort', 'mort', 'mourir ', 'mouvement', 'moyen ', 'musique', 'mère', 'mètre ', 'médecin ', 'même', 'naître ', 'noir', 'noir ', 'nouveau', 'nouveau', 'nuit', 'numéro ', 'obliger ', 'occuper ', 'odeur', 'oeil ', 'offrir ', 'oiseau ', 'ombre', 'oncle ', 'ordre ', 'oreille', 'oser ', 'oublier ', 'ouvrir ', 'paix', 'papa ', 'papier ', 'paraître', 'pareil', 'parent ', 'parler', 'parole', 'part', 'partie', 'partir ', 'passage ', 'passer ', 'passé ', 'patron ', 'pauvre', 'payer ', 'pays', 'peau', 'peine', 'penser ', 'pensée', 'perdre ', 'permettre', 'personne', 'petit', 'petit ', 'peuple ', 'peur', 'photo', 'pied ', 'pierre', 'pièce', 'place', 'plaire ', 'plaisir ', 'plan ', 'plein', 'pleurer ', 'poche', 'point ', 'police', 'porte', 'porter ', 'poser ', 'possible', 'pousser ', 'pouvoir ', 'pouvoir ', 'premier', 'premier ', 'prendre ', 'prier     ', 'prince ', 'prison', 'prix', 'problème', 'prochain', 'professeur', 'promettre ', 'propos', 'proposer ', 'propre', 'protéger ', 'préférer', 'préparer ', 'présence', 'présent ', 'présenter ', 'président ', 'prévenir ', 'prêt', 'putain', 'père ', 'quartier', 'question', 'quitter     ', 'quoi', 'raconter ', 'raison', 'ramener     ', 'rappeler ', 'rapport ', 'recevoir ', 'reconnaître ', 'refuser     ', 'regard ', 'regarder', 'rejoindre', 'remarquer', 'remettre', 'remonter', 'rencontrer', 'rendre', 'rentrer', 'reponse', 'reposer', 'reprendre', 'ressembler', 'reste ', 'rester', 'retard ', 'retenir', 'retirer', 'retour ', 'retourner', 'retrouver', 'revenir', 'revoir', 'revoir ', 'risqer', 'robe', 'rouer', 'rouge', 'route', 'rre', 'réfléchir ', 'répondre', 'répéter', 'réussir', 'réveiller', 'rêve ', 'rêver', 'sale', 'salle', 'salut ', 'sang ', 'sauer', 'sauer', 'savir', 'scène', 'seconde', 'secret ', 'seigneur', 'semaine', 'sember', 'senir', 'sens', 'sentiment', 'serrer', 'service ', 'servir', 'seul', 'seul ', 'signe ', 'silence ', 'simple', 'situation', 'siècle ', 'soeur', 'soir ', 'soirée', 'soldat ', 'soleil ', 'sorte', 'sortir', 'souffrir', 'sourire', 'sourire ', 'souvenir', 'souvenir', 'suffire', 'suite', 'suivre', 'sujet ', 'super', 'sécurité', 'séparer', 'sérieux', 'table', 'taire', 'temps', 'tendre', 'tenir', 'tenter', 'terminer', 'terre', 'tirer', 'tomber', 'toucher', 'tour', 'tourner', 'tout', 'tout ', 'toute', 'train ', 'traiter', 'tranquille', 'travail ', 'travailler', 'travers', 'traverser', 'traîner', 'triste', 'tromper', 'trou ',
'trouver', 'truc ', 'tuer', 'type ', 'téléphone', 'tête', 'utiliser', 'valoir', 'vendre', 'venir', 'vent ', 'ventre ', 'verre ', 'vert', 'vide', 'vieux', 'vieux', 'village ', 'ville', 'visage ', 'vivant', 'vivre', 'voir', 'voiture', 'voix', 'voler', 'vouloir', 'voyage ', 'vrai', 'vérité', 'échapper', 'école', 'écouter ', 'écrire ', 'église', 'éloigner', 'épaule', 'époque', 'équipe', 'état', 'étrange', 'éviter ', 'être', 'être ']

print(tab0[len(tab0)//4])
print(tab0[6])
print(len(tab0[6]))




















# if len(a[9]) == len(value) or  len(a[]) == len(value):
#     if a[9][1] == value[1]:
         


# c = a[len(a)//2][1],0
# d = a[len(a)//2+1:][1],0

# print(b ,'low')#
# print(c ,'mid')
# print(d ,'high')#

# print(40*"-")
# b = a[:len(b)//2]
# c = a[len(c)//2]
# d = a[len(d)//2+1:]

# print(40*"-")

# print(b ,'low')#
# print(c ,'mid')
# print(d ,'high')#

# print(40*"-")
