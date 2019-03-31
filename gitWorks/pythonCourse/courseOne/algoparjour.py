from random import randint
# from time import time




tab0 = ['bleu', 'super', 'autre', 'bizarre', 'difficile', 'drôle', 'étrange', 'facile', 'grave', 'impossible', 'jeune', 'juste', 'libre', 'malade', 'même', 'pauvre', 'possible', 'propre', 'rouge', 'sale', 'simple', 'tranquille', 'triste', 'vide', 'bonne', 'toute', 'doux', 'faux', 'français', 'gros', 'heureux', 'mauvais', 'sérieux', 'vieux', 'vrai', 'ancien', 'beau', 'blanc', 'certain', 'chaud', 'cher', 'clair', 'content', 'dernier', 'désolé', 'différent', 'droit', 'entier', 'fort', 'froid', 'gentil', 'grand', 'haut', 'humain', 'important', 'joli', 'léger', 'long', 'meilleur', 'mort', 'noir', 'nouveau', 'pareil', 'petit', 'plein', 'premier', 'prêt', 'prochain', 'quoi', 'seul', 'tout', 'vert', 'vivant', 'Noms communs', 'aide', 'chef', 'enfant', 'garde', 'gauche', 'geste', 'gosse', 'livre', 'merci', 'mort', 'ombre', 'part', 'poche', 'professeur', 'tour', 'madame', 'fois', 'paix', 'voix', 'affaire', 'année', 'arme', 'armée', 'attention', 'balle', 'boîte', 'bouche', 'carte', 'cause', 'chambre', 'chance', 'chose', 'classe', 'confiance', 'couleur', 'cour', 'cuisine', 'dame', 'dent', 'droite', 'école', 'église', 'envie', 'épaule', 'époque', 'équipe', 'erreur', 'espèce', 'face', 'façon', 'faim', 'famille', 'faute', 'femme', 'fenêtre', 'fête', 'fille', 'fleur', 'force', 'forme', 'guerre', 'gueule', 'habitude', 'heure', 'histoire', 'idée', 'image', 'impression', 'jambe', 'joie', 'journée', 'langue', 'lettre', 'lèvre', 'ligne', 'lumière', 'main', 'maison', 'maman', 'manière', 'marche', 'merde', 'mère', 'minute', 'musique', 'nuit', 'odeur', 'oreille', 'parole', 'partie', 'peau', 'peine', 'pensée', 'personne', 'peur', 'photo', 'pièce', 'pierre', 'place', 'police', 'porte', 'présence', 'prison', 'putain', 'question', 'raison', 'reponse', 'robe', 'route', 'salle', 'scène', 'seconde', 'sécurité', 'semaine',
'situation', 'soeur', 'soirée', 'sorte', 'suite', 'table', 'terre', 'tête', 'vérité', 'ville', 'voiture', 'bois', 'bras', 'choix', 'corps', 'cours', 'gars', 'mois',
'pays', 'prix', 'propos', 'sens', 'temps', 'travers', 'vieux', 'accord', 'agent', 'amour', 'appel', 'arbre', 'argent', 'avenir', 'avion', 'bateau', 'bébé', 'besoin', 'bonheur', 'bonjour', 'bord', 'boulot', 'bout', 'bruit', 'bureau', 'café', 'camp', 'capitaine', 'chat', 'chemin', 'chéri', 'cheval', 'cheveu', 'chien', 'ciel', 'client', 'cœur', 'coin', 'colonel', 'compte', 'copain', 'côté', 'coup', 'courant', 'début', 'départ', 'dieu', 'docteur', 'doigt', 'dollar', 'doute', 'droit', 'effet', 'endroit', 'ennemi', 'escalier', 'esprit', 'état', 'être', 'exemple', 'fait', 'film', 'flic', 'fond', 'français', 'frère', 'front ', 'garçon', 'général', 'genre', 'goût', 'gouvernement', 'grand', 'groupe', 'haut', 'homme', 'honneur', 'hôtel', 'instant', 'intérêt ', 'intérieur', 'jardin ', 'jour ', 'journal ', 'lieu ', 'long ', 'maître ', 'mari ', 'mariage ', 'matin ', 'médecin ', 'mètre ', 'milieu ', 'million ', 'moment ', 'monde ', 'monsieur', 'mouvement', 'moyen ', 'noir ', 'nouveau ', 'numéro ', 'oeil ', 'oiseau ', 'oncle ', 'ordre ', 'papa ', 'papier ', 'parent ', 'passage ', 'passé ', 'patron ', 'père ', 'petit ', 'peuple ', 'pied ', 'plaisir ', 'plan ', 'point ', 'pouvoir ', 'premier ', 'présent ', 'président ', 'prince ', 'problème', 'quartier', 'rapport ', 'regard ', 'reste ', 'retard ', 'retour ', 'rêve ', 'revoir ', 'salut ', 'sang ', 'secret ', 'seigneur', 'sentiment', 'service ', 'seul ', 'siècle ', 'signe ', 'silence ', 'soir ', 'soldat ', 'soleil ', 'sourire ', 'souvenir', 'sujet ', 'téléphone', 'tout ', 'train ', 'travail ', 'trou ', 'truc ', 'type ', 'vent ', 'ventre ', 'verre ', 'village ', 'visage ', 'voyage ', 'fils  ', 'gens  ', 'abandonner ', 'accepter ', 'accompagner ', 'acheter     ', 'adorer     ', 'agir     ', 'aider     ', 'aimer     ', 'ajouter ', 'aller ', 'amener ', 'amuser ', 'annoncer', 'apercevoir', 'apparaître', 'appeler ', 'apporter', 'apprendre', 'approcher', 'arranger', 'arrêter ', 'arriver ', 'asseoir ', 'assurer ', 'attaquer', 'atteindre', 'attendre', 'avancer ', 'avoir ', 'baisser ', 'battre ', 'boire ', 'bouger ', 'brûler ', 'cacher ', 'calmer ', 'casser ', 'cesser ', 'changer ', 'chanter ', 'charger ', 'chercher ', 'choisir     ', 'commencer ', 'comprendre ', 'compter     ', 'conduire ', 'connaître ', 'continuer ', 'coucher ', 'couper ', 'courir ', 'couvrir ', 'craindre', 'crier ', 'croire ', 'danser ', 'décider ', 'découvrir', 'dégager ', 'demander ', 'descendre ', 'désoler ', 'détester', 'détruire', 'devenir ', 'deviner ', 'devoir ', 'dire ', 'disparaître', 'donner ', 'dormir ', 'échapper', 'écouter ', 'écrire ', 'éloigner', 'embrasser', 'emmener ', 'empêcher', 'emporter', 'enlever ', 'entendre', 'entrer ', 'envoyer ', 'espérer ', 'essayer ', 'être ', 'éviter ', 'excuser ', 'exister ', 'expliquer', 'faire ', 'falloir ', 'fermer', 'filer ', 'finir ', 'foutre ', 'frapper ', 'gagner ', 'garder ', 'glisser ', 'habiter ', 'ignorer ', 'imaginer ', 'importer ', 'inquiéter ', 'installer ', 'intéresser ', 'inviter ', 'jeter ', 'jouer ', 'jurer ', 'lâcher ', 'laisser ', 'lancer ', 'lever ', 'lire ', 'maintenir', 'manger ', 'manquer ', 'marcher ', 'marier ', 'mener ', 'mentir ', 'mettre ', 'monter ', 'montrer ', 'mourir ', 'naître ', 'obliger ', 'occuper ', 'offrir ', 'oser ', 'oublier ', 'ouvrir ', 'paraître', 'parler ', 'partir ', 'passer ', 'payer ', 'penser ', 'perdre ', 'permettre', 'plaire ', 'pleurer ', 'porter ', 'poser ', 'pousser ', 'pouvoir ', 'préférer', 'prendre ', 'préparer ', 'présenter ', 'prévenir ', 'prier     ', 'promettre ', 'proposer ', 'protéger ', 'quitter     ', 'raconter ', 'ramener     ', 'rappeler ', 'recevoir ', 'reconnaître ', 'réfléchir ', 'refuser     ', 'regarder', 'rejoindre', 'remarquer', 'remettre', 'remonter', 'rencontrer', 'rendre', 'rentrer', 'répéter', 'répondre', 'reposer', 'reprendre', 'ressembler', 'rester', 'retenir', 'retirer', 'retourner', 'retrouver', 'réussir', 'réveiller', 'revenir', 'rêver', 'revoir', 'rre', 'risqer', 'rouer', 'sauer', 'sauer', 'savir', 'sember', 'senir', 'séparer', 'serrer', 'servir', 'sortir', 'souffrir', 'sourire', 'souvenir', 'suffire', 'suivre', 'taire', 'tendre', 'tenir', 'tenter', 'terminer', 'tirer', 'tomber', 'toucher', 'tourner', 'traîner', 'traiter', 'travailler', 'traverser', 'tromper', 'trouver', 'tuer', 'utiliser',
'valoir', 'vendre', 'venir', 'vivre', 'voir', 'voler', 'vouloir']
# for x in tab0:
#     tab01.append(len(x))
# # print(tab01)
tab01=[4, 5, 5, 7, 9, 5, 7, 6, 5, 10, 5, 5, 5, 6, 4, 6, 8, 6, 5, 4, 6, 10, 6, 4, 5, 5, 4, 4, 8, 4, 7, 7, 7, 5, 4, 6, 4, 5, 7, 5, 4, 5, 7, 7, 6, 9, 5, 6, 4, 5, 6, 5, 4, 6,
9, 4, 5, 4, 8, 4, 4, 7, 6, 5, 5, 7, 4, 8, 4, 4, 4, 4, 6, 12, 4, 4, 6, 5, 6, 5, 5, 5, 5, 4, 5, 4, 5, 10, 4, 6, 4, 4, 4, 7, 5, 4, 5, 9, 5, 5, 6, 5, 5, 7, 6, 5, 6, 9, 7, 
4, 7, 4, 4, 6, 5, 6, 5, 6, 6, 6, 6, 6, 4, 5, 4, 7, 5, 5, 7, 4, 5, 5, 5, 5, 6, 6, 8, 5, 8, 4, 5, 10, 5, 4, 7, 6, 6, 5, 5, 7, 4, 6, 5, 7, 6, 5, 4, 6, 7, 4, 5, 7, 6,
6, 4, 5, 6, 8, 4, 5, 5, 6, 5, 6, 5, 8, 6, 6, 8, 6, 7, 4, 5, 5, 5, 7, 8, 7, 9, 5, 6, 5, 5, 5, 5, 4, 6, 5, 7, 4, 4, 5, 5, 5, 4, 4, 4, 4, 6, 4, 5, 7, 5, 6, 5, 5, 5, 5,
6, 6, 5, 6, 4, 6, 7, 7, 4, 6, 4, 5, 6, 4, 4, 9, 4, 6, 5, 6, 6, 5, 4, 6, 4, 4, 7, 6, 6, 4, 4, 7, 5, 6, 4, 7, 5, 6, 5, 5, 5, 7, 6, 8, 6, 4, 4, 7, 4, 4, 4, 4, 8, 5, 6,
6, 7, 5, 4, 12, 5, 6, 4, 5, 7, 5, 7, 8, 9, 7, 5, 8, 5, 5, 7, 5, 8, 6, 8, 6, 7, 8, 7, 6, 8, 9, 6, 5, 8, 7, 5, 7, 6, 6, 5, 7, 7, 8, 6, 7, 5, 6, 7, 5, 8, 5, 6, 8, 8, 8, 
10, 7, 8, 8, 8, 7, 6, 7, 7, 5, 7, 6, 5, 7, 8, 9, 8, 5, 7, 6, 8, 5, 7, 7, 8, 8, 6, 9, 5, 6, 8, 5, 5, 5, 5, 7, 6, 8, 7, 7, 6, 6, 11, 9, 12, 12, 11, 9, 10, 10, 8, 6, 7, 
7, 8, 10, 10, 8, 8, 9, 9, 8, 8, 8, 8, 8, 8, 9, 8, 8, 6, 8, 7, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9, 12, 10, 11, 12, 9, 10, 10, 8, 7, 7, 8, 8, 6, 7, 7, 8, 9, 8, 9, 10, 8,
8, 8, 8, 8, 7, 5, 11, 7, 7, 8, 8, 7, 8, 9, 8, 8, 8, 8, 8, 7, 8, 8, 8, 5, 7, 8, 8, 9, 6, 8, 6, 6, 6, 7, 8, 7, 7, 8, 8, 8, 9, 9, 10, 10, 11, 8, 6, 6, 6, 7, 8, 7, 6,
5, 9, 7, 8, 8, 7, 6, 7, 7, 7, 8, 7, 7, 8, 8, 7, 5, 8, 7, 8, 7, 7, 7, 6, 7, 7, 9, 7, 8, 7, 6, 8, 8, 8, 8, 9, 10, 9, 10, 10, 9, 9, 12, 9, 12, 9, 9, 12, 10, 12, 8, 9, 9,
8, 8, 10, 6, 7, 7, 8, 7, 9, 10, 6, 7, 7, 9, 9, 7, 9, 7, 5, 6, 3, 6, 5, 5, 5, 5, 6, 5, 7, 6, 6, 6, 8, 7, 8, 7, 6, 5, 6, 5, 6, 8, 5, 6, 7, 7, 7, 7, 10, 9, 7, 7, 4, 8, 6, 6, 5, 5, 4, 5, 7]

tab012={'bleu': 4, 'super': 5, 'autre': 5, 'bizarre': 7, 'difficile': 9, 'drôle': 5, 'étrange': 7, 'facile': 6, 'grave': 5, 'impossible': 10,
'jeune': 5, 'juste': 5, 'libre': 5, 'malade': 6, 'même': 4, 'pauvre': 6, 'possible': 8, 'propre': 6, 'rouge': 5, 'sale': 4, 'simple': 6,
'tranquille': 10, 'triste': 6, 'vide': 4, 'bonne': 5, 'toute': 5, 'doux': 4, 'faux': 4, 'français': 8, 'gros': 4, 'heureux': 7,
'mauvais': 7, 'sérieux': 7, 'vieux': 5, 'vrai': 4, 'ancien': 6, 'beau': 4, 'blanc': 5, 'certain': 7, 'chaud': 5, 'cher': 4,
'clair': 5, 'content': 7, 'dernier': 7, 'désolé': 6, 'différent': 9, 'droit': 5, 'entier': 6, 'fort': 4, 'froid': 5,
'gentil': 6, 'grand': 5, 'haut': 4, 'humain': 6, 'important': 9, 'joli': 4, 'léger': 5, 'long': 4, 'meilleur': 8, 'mort': 4,
'noir': 4, 'nouveau': 7, 'pareil': 6, 'petit': 5, 'plein':5, 'premier': 7, 'prêt': 4, 'prochain': 8, 'quoi': 4, 
'seul': 4, 'tout': 4, 'vert': 4, 'vivant': 6, 'Noms communs': 12, 'aide': 4,'chef': 4, 'enfant': 6, 'garde': 5,
'gauche': 6, 'geste': 5, 'gosse': 5, 'livre': 5, 'merci': 5, 'ombre': 5, 'part': 4, 'poche': 5,
'professeur': 10, 'tour': 4, 'madame': 6, 'fois': 4, 'paix': 4, 'voix': 4, 'affaire': 7, 'année': 5,
'arme': 4, 'armée': 5, 'attention': 9, 'balle': 5, 'boîte': 5, 'bouche': 6, 'carte': 5, 'cause': 5, 'chambre': 7,
'chance': 6, 'chose': 5, 'classe': 6, 'confiance': 9, 'couleur': 7, 'cour': 4, 'cuisine': 7, 'dame': 4, 'dent': 4,
'droite': 6, 'école': 5, 'église': 6, 'envie': 5, 'épaule': 6, 'époque': 6, 'équipe': 6, 'erreur': 6, 'espèce': 6,
'face': 4, 'façon': 5, 'faim': 4, 'famille': 7, 'faute': 5, 'femme': 5, 'fenêtre': 7, 'fête': 4, 'fille': 5, 'fleur': 5,
'force': 5, 'forme': 5, 'guerre': 6, 'gueule': 6, 'habitude': 8, 'heure': 5, 'histoire': 8, 'idée': 4, 'image': 5,
'impression': 10,'jambe': 5, 'joie': 4, 'journée': 7, 'langue': 6, 'lettre': 6, 'lèvre': 5, 'ligne': 5, 'lumière': 7,
'main': 4, 'maison': 6,'maman': 5, 'manière': 7, 'marche': 6, 'merde': 5, 'mère': 4, 'minute': 6, 'musique': 7, 'nuit': 4,
'odeur': 5, 'oreille': 7,'parole': 6, 'partie': 6, 'peau': 4, 'peine': 5, 'pensée': 6, 'personne': 8, 'peur': 4, 'photo': 5,
'pièce': 5, 'pierre': 6,'place': 5, 'police': 6, 'porte': 5, 'présence': 8, 'prison': 6, 'putain': 6, 'question': 8,
'raison': 6, 'reponse': 7,'robe': 4, 'route': 5, 'salle': 5, 'scène': 5, 'seconde': 7, 'sécurité': 8, 'semaine': 7, 'situation': 9,
'soeur': 5, 'soirée': 6, 'sorte': 5, 'suite': 5, 'table': 5, 'terre': 5, 'tête': 4, 'vérité': 6, 'ville': 5, 'voiture': 7, 'bois': 4,
'bras': 4, 'choix': 5, 'corps': 5, 'cours': 5, 'gars': 4, 'mois': 4, 'pays': 4, 'prix': 4, 'propos': 6, 'sens': 4, 'temps': 5,
'travers': 7, 'accord': 6, 'agent': 5, 'amour': 5, 'appel': 5, 'arbre': 5, 'argent': 6, 'avenir': 6, 'avion': 5, 'bateau': 6,
'bébé': 4, 'besoin': 6, 'bonheur': 7, 'bonjour': 7, 'bord': 4, 'boulot': 6, 'bout': 4, 'bruit': 5, 'bureau': 6, 'café': 4, 
'camp': 4, 'capitaine': 9, 'chat': 4, 'chemin': 6, 'chéri': 5, 'cheval': 6, 'cheveu': 6, 'chien': 5, 'ciel': 4, 'client': 6, 
'cœur': 4, 'coin': 4, 'colonel': 7, 'compte': 6, 'copain': 6, 'côté': 4, 'coup': 4, 'courant': 7, 'début': 5, 'départ': 6,
'dieu': 4, 'docteur': 7, 'doigt': 5, 'dollar': 6, 'doute': 5, 'effet': 5, 'endroit': 7, 'ennemi': 6, 'escalier': 8,
'esprit': 6, 'état': 4, 'être': 4, 'exemple': 7, 'fait': 4, 'film': 4, 'flic': 4, 'fond': 4, 'frère': 5, 'front ': 6,
'garçon': 6, 'général': 7, 'genre': 5, 'goût': 4, 'gouvernement': 12, 'groupe': 6, 'homme': 5, 'honneur': 7, 'hôtel': 5,
'instant': 7, 'intérêt ': 8, 'intérieur': 9, 'jardin ': 7, 'jour ': 5, 'journal ': 8, 'lieu ': 5, 'long ': 5, 'maître ': 7,
'mari ': 5, 'mariage ': 8, 'matin ': 6, 'médecin ': 8, 'mètre ': 6, 'milieu ': 7, 'million ': 8, 'moment ': 7, 'monde ': 6,
'monsieur': 8, 'mouvement': 9, 'moyen ': 6, 'noir ': 5, 'nouveau ': 8, 'numéro ': 7, 'oeil ': 5, 'oiseau ': 7, 'oncle ': 6,
'ordre ': 6, 'papa ': 5, 'papier ': 7, 'parent ': 7, 'passage ': 8, 'passé ': 6, 'patron ': 7, 'père ': 5, 'petit ': 6,
'peuple ': 7, 'pied ': 5, 'plaisir ': 8, 'plan ': 5, 'point ': 6, 'pouvoir ': 8, 'premier ': 8, 'présent ': 8,
'président ': 10, 'prince ': 7, 'problème': 8, 'quartier': 8, 'rapport ': 8, 'regard ': 7, 'reste ': 6, 'retard ': 7,
'retour ': 7, 'rêve ': 5, 'revoir ': 7, 'salut ': 6, 'sang ': 5, 'secret ': 7, 'seigneur': 8, 'sentiment': 9,
'service ': 8, 'seul ': 5, 'siècle ': 7, 'signe ': 6, 'silence ': 8, 'soir ': 5, 'soldat ': 7, 'soleil ': 7, 
'sourire ': 8, 'souvenir': 8, 'sujet ': 6, 'téléphone': 9, 'tout ': 5, 'train ': 6, 'travail ': 8, 'trou ': 5,
'truc ': 5, 'type ': 5, 'vent ': 5, 'ventre ': 7, 'verre ': 6, 'village ': 8, 'visage ': 7, 'voyage ': 7, 'fils  ': 6,
'gens  ': 6, 'abandonner ': 11, 'accepter ': 9, 'accompagner ': 12, 'acheter': 12, 'adorer ': 11, 
'agir': 9, 'aider': 10, 'aimer': 10, 'ajouter ': 8, 'aller ': 6, 'amener ': 7, 'amuser ': 7, 'annoncer': 8,
'apercevoir': 10,'apparaître': 10, 'appeler ':8, 'apporter': 8, 'apprendre': 9, 'approcher': 9, 'arranger': 8, 'arrêter ': 8,
'arriver ': 8, 'asseoir ': 8, 'assurer ': 8,'attaquer': 8, 'atteindre': 9, 'attendre': 8, 'avancer ': 8, 'avoir ': 6, 'baisser ': 8,
'battre ': 7, 'boire ': 6, 'bouger ': 7,'brûler ': 7, 'cacher ': 7, 'calmer ': 7, 'casser ': 7, 'cesser ': 7, 'changer ': 8,
'chanter ': 8, 'charger ': 8, 'chercher ': 9, 'choisir     ': 12, 'commencer ': 10, 'comprendre ': 11, 'compter': 12,
'conduire ': 9, 'connaître ': 10, 'continuer ': 10, 'coucher ': 8, 'couper ': 7, 'courir ': 7, 'couvrir ': 8, 'craindre': 8,
'crier ': 6, 'croire ': 7, 'danser ': 7, 'décider ': 8, 'découvrir': 9,
'dégager ': 8, 'demander ': 9, 'descendre ': 10, 'désoler ': 8, 'détester': 8, 'détruire': 8, 'devenir ': 8, 'deviner ': 8,
'devoir ': 7, 'dire ': 5, 'disparaître':11, 'donner ': 7, 'dormir ': 7, 'échapper': 8, 'écouter ': 8, 'écrire ': 7, 'éloigner': 8,
'embrasser': 9, 'emmener ': 8,'empêcher': 8, 'emporter': 8, 'enlever ': 8, 'entendre': 8, 'entrer ': 7, 'envoyer ': 8, 'espérer ': 8,
'essayer ': 8, 'être ': 5, 'éviter ': 7, 'excuser ': 8, 'exister ': 8, 'expliquer': 9, 'faire ': 6, 'falloir ': 8, 'fermer': 6,
'filer ': 6, 'finir ': 6, 'foutre ': 7, 'frapper ': 8, 'gagner ': 7, 'garder ': 7, 'glisser ': 8, 'habiter ': 8, 'ignorer ': 8,
'imaginer ':9, 'importer ': 9, 'inquiéter ': 10, 'installer ': 10, 'intéresser ': 11, 'inviter ': 8, 'jeter ': 6, 'jouer ': 6,
'jurer ': 6,'lâcher ': 7, 'laisser ': 8, 'lancer': 7, 'lever ': 6, 'lire ': 5, 'maintenir': 9, 'manger ': 7, 'manquer ': 8,
'marcher ': 8,'marier ': 7, 'mener ': 6, 'mentir ': 7, 'mettre ': 7, 'monter ': 7, 'montrer ': 8, 'mourir ': 7, 'naître ': 7,
'obliger ': 8,'occuper ': 8, 'offrir ': 7, 'oser ': 5, 'oublier ': 8, 'ouvrir ': 7, 'paraître': 8, 'parler ': 7, 'partir ': 7,
'passer ': 7,'payer ': 6, 'penser ': 7, 'perdre ': 7, 'permettre': 9, 'plaire ': 7, 'pleurer ': 8, 'porter ': 7, 'poser ': 6,
'pousser ': 8,'préférer': 8, 'prendre ': 8, 'préparer ': 9, 'présenter ': 10, 'prévenir ': 9, 'prier     ': 10, 'promettre ': 10,
'proposer ': 9, 'protéger ': 9, 'quitter     ': 12, 'raconter ': 9, 'ramener     ': 12, 'rappeler ': 9, 'recevoir ': 9,
'reconnaître ': 12, 'réfléchir ': 10, 'refuser     ': 12, 'regarder': 8, 'rejoindre': 9, 'remarquer': 9, 'remettre': 8,
'remonter': 8, 'rencontrer': 10, 'rendre': 6, 'rentrer': 7, 'répéter': 7, 'répondre': 8, 'reposer': 7, 'reprendre': 9,
'ressembler': 10, 'rester': 6, 'retenir':7, 'retirer': 7, 'retourner': 9, 'retrouver': 9, 'réussir': 7, 'réveiller': 9,
'revenir': 7, 'rêver': 5, 'revoir': 6, 'rre': 3, 'risqer': 6, 'rouer': 5, 'sauer': 5,
'savir': 5, 'sember': 6, 'senir': 5, 'séparer': 7, 'serrer': 6, 'servir': 6, 'sortir': 6, 'souffrir': 8, 'sourire': 7,
'suffire': 7, 'suivre': 6, 'taire': 5, 'tendre': 6, 'tenir': 5, 'tenter': 6, 'terminer': 8, 'tirer': 5, 'tomber': 6,
'toucher': 7, 'tourner': 7, 'traîner': 7, 'traiter': 7, 'travailler': 10, 'traverser': 9, 'tromper': 7, 'trouver': 7,
'tuer': 4, 'utiliser': 8, 'valoir': 6, 'vendre': 6, 'venir': 5, 'vivre': 5, 'voir': 4, 'voler': 5, 'vouloir': 7}
# {tab0[i]: tab01[i] for i in range(0,len(tab0))}

# print(tab012)

# print(len(tab0))
# print(len(tab012))
# print(tab012)
print(dict.sort())


tab1=["Abdallah","Abdel","Abdelaziz","Abdelkader","Alexander","Alexandra","Alexandre","Alexandrine","Andrée","Andrew",
"Andy","Ange","Angel","Angie","Antonin","Antonio","Apolline","Ariane","Benedicte","Benjamin","Bryan","Calie","Calvin",
"Camélia","Cyrielle","Cyril","Daisy","Dalila","Damien","Eline","Elio","Eliott","Elisa","Emmie","Emmy","Emre","Enes",
"Frédéric","Frédérique","Gabin","Gwenola","Habib","Issam","Jacky","Jacqueline","Kylian","Laetitia","Laly","Muhammed",
"Muriel","Mustapha","Nour","Noura","Océane","Pascaline","Patrice","Patricia","Patrick","Paul","Paula","Paule","Paulette",
"Paulin","Pauline","Paulo","Pedro","Ruben","Rudy","Ruth","Ryad","Ryan","Sabah","Vivien","Vladimir","Wael","Walid",
"Walter","Xx","Yvonne","Zacharie","Zahra","Zakaria"]
tab12=[8, 5, 9, 10, 9, 9, 9, 11, 6, 6, 4, 4, 5, 5, 7, 7, 8, 6, 9, 8, 5, 5, 6, 7, 8, 5, 5, 6, 6, 5, 4, 6, 5, 5,
4, 4, 4, 8, 10, 5, 7, 5, 5, 5, 10, 6, 8, 4, 8, 6, 8, 4, 5, 6, 9, 7, 8, 7, 4, 5, 5, 8, 6, 7, 5, 5, 5, 4,
4, 4, 4, 5, 6, 8, 4, 5, 6, 2, 6, 8, 5, 7]


# print(tab2)
# # tab3={}.fromkeys(tab1,tab2[i+1])
# searcher = "rudy"











# n=[10,100,1000,10000,100000]
# times = {'quick': []}
# samples = 5


# for size in n:
#     tot_time = 0.0
#     for v in range(samples):
#         b = create_array(size, size)
#         t0 = time()
#         s = quicksort(b)
#         t1= time()
#         tot_time+=(t1-t0)
#     times['quick'].append(tot_time/float(samples))

# print("n\t Quicksort \t Autres")
# print(40*"--")
# for i, size in enumerate(n):
#     print(f"{size}\t{(times['quick'][i])%0.5}")