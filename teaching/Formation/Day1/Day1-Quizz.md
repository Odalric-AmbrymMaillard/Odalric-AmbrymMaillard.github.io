## Mini-quizz:

**1. Pourquoi l'exploitation exclusive est-elle risquée dans les problèmes de bandit ?**
- a) Elle génère un regret linéaire en ignorant les options potentiellement optimales
- b) Elle augmente la variance des estimations
- c) Elle nécessite plus de ressources computationnelles

Réponse: a) 
Explication : Une politique purement exploitative converge prématurément vers des sous-optimums locaux, menant à un regret cumulé linéaire au lieu de logarithmique.


**2. Quelle différence fondamentale entre l'apprentissage séquentiel et offline dans les bandits ?**
- a) Le séquentiel adapte la stratégie en temps réel, contrairement à l'offline
- b) L'offline garantit toujours de meilleures performances
- c) Le séquentiel ignore les données historiques

Réponse a)
Explication : Les méthodes séquentielles comme Kernel-TS mettent à jour leur modèle après chaque feedback, permettant une adaptation dynamique impossible en batch.


**3. Pourquoi est-il crucial de vérifier la stationnarité de l'environnement avant de déployer un bandit manchot ?**
- a) Les algorithmes stationnaires garantissent toujours un regret sous-linéaire
- b) Les variations temporelles non détectées peuvent induire un regret linéaire irrécupérable
- c) L'initialisation des paramètres bayésiens devient instable

Réponse : b)
Explication :
Les bandits classiques (UCB, Thompson Sampling) supposent implicitement une distribution stationnaire des récompenses



## Quizz final:

### PARTIE I 

**1. Quel est l'objectif principal d'un algorithme de bandit manchot ?**
- a) Maximiser la récompense immédiate
- b) Équilibrer exploration et exploitation
- c) Minimiser le nombre d'essais

Réponse : b)

**2. Comment UCB (Upper Confidence Bound) sélectionne-t-il les actions ?**
- a) En choisissant toujours l'arme avec la moyenne empirique la plus élevée
- b) En ajoutant un terme d'exploration basé sur la variance des estimations
- c) En utilisant un intervalle de confiance supérieur pour chaque estimation

Réponse : c)

**3. Quelle inégalité mathématique est utilisée pour construire les intervalles de confiance dans UCB ?**
- a) Inégalité de Cauchy-Schwarz
- b) Inégalité de Hoeffding
- c) Inégalité de Markov

Réponse : b)

**4. Que représente le regret cumulé $R_T$ ?**
- a) La différence entre les récompenses optimales et celles obtenues
- b) La variance totale des récompenses observées
- c) Le nombre de mauvaises actions choisies

Réponse : a)

**5. Comment fonctionne le Thompson Sampling ?**
- a) En générant des échantillons des distributions postérieures des moyennes
- b) En maintenant une borne supérieure optimiste pour chaque bras
- c) En alternant périodiquement entre exploration et exploitation

Réponse : a)

**6. Quel avantage principal offre l'approche bayésienne dans les bandits ?**
- a) Une complexité computationnelle réduite
- b) Une intégration naturelle des connaissances a priori
- c) Des garanties de regret indépendantes des distributions

Réponse : b)

**7. Pourquoi doit-on explorer dans un problème de bandit ?**
- a) Pour éviter les convergences prématurées vers des sous-optimalités
- b) Pour satisfaire des contraintes réglementaires
- c) Pour augmenter la variance des observations

Réponse : a)

**8. Quelle relation existe entre le nombre de tirages d'un bras sous-optimal et son gap $\Delta_a$ ?**
- a) $N_t(a) \propto 1/\Delta_a$
- b) $N_t(a) \propto 1/\Delta_a^2$
- c) $N_t(a) \propto \ln(1/\Delta_a)$

Réponse : b)

**9. Que représente $m_t^+(a)$ dans UCB ?**
- a) La moyenne empirique pondérée
- b) La borne supérieure de l'intervalle de confiance
- c) La variance estimée des récompenses

Réponse : b)

**10. Quelle différence clé entre UCB et Thompson Sampling ?**
- a) UCB utilise une approche fréquentiste, TS une approche bayésienne
- b) UCB nécessite plus de mémoire
- c) TS garantit un regret logarithmique dans tous les cas

Réponse : a)


**11. Quelle approche est risquée ?**
- a) L'exploration: choisir des actions peu connues à l'instant courant.
- b) L'exploitation: choisir l'action qui semble la meilleur à l'instant courant.
- c) L'exploration et l'exploitation sont toutes deux risquées.

Réponse : c)


### PARTIE II

**1. Quel est l'avantage principal de Kernel-TS par rapport aux méthodes grid search en microscopie super-résolution ?**
- a) Meilleure précision numérique
- b) Adaptation dynamique aux feedbacks successifs
- c) Complexité computationnelle réduite

Réponse : b)

**2. Comment Kernel-TS modélise-t-il l'incertitude sur la fonction de récompense ?**
- a) Par des intervalles de confiance fréquentistes
- b) Par des distributions postérieures bayésiennes
- c) Par des bornes d'erreur fixes

Réponse : b)

**3. Que représente γ_T(λ) dans les bornes de regret de Kernel-TS ?**
- a) Le gain d'information cumulé
- b) La variance résiduelle moyenne
- c) Le nombre de paramètres optimaux

Réponse : a)

**4. Pourquoi utilise-t-on un RKHS (Reproducing Kernel Hilbert Space) dans cette application ?**
- a) Pour gérer des espaces d'actions continus
- b) Pour réduire la dimension des données
- c) Pour garantir la convexité du problème

Réponse : a)

**5. Comment évalue-t-on les performances de Kernel-TS dans l'application de microscopie ?**
- a) Par simulation via rééchantillonnage d'images pré-acquises
- b) Par comparaison avec des experts humains
- c) Par validation croisée classique

Réponse : a)

**6. Quelle métrique clé mesure l'efficacité de l'optimisation en ligne ?**
- a) L'erreur quadratique moyenne
- b) Le regret cumulé
- c) La vitesse de convergence asymptotique

Réponse : b)

**7. Comment Kernel-TS sélectionne-t-il les paramètres à tester ?**
- a) En maximisant l'espérance postérieure
- b) En échantillonnant de la distribution postérieure
- c) En minimisant la variance empirique

Réponse : b)

**8. Quelle est la complexité principale des méthodes kernelisées ?**
- a) Calcul matriciel en O(t²) à l'étape t
- b) Stockage des noyaux en mémoire
- c) Optimisation non convexe

Réponse : a)

**9. Que modélise la fonction noyau k(x,x') dans ce contexte ?**
- a) La similarité entre configurations de paramètres
- b) La probabilité a priori des récompenses
- c) Le bruit de mesure expérimental

Réponse : a)

**10. Pourquoi utilise-t-on plusieurs instances de Kernel-TS dans l'application ?**
- a) Pour modéliser simultanément plusieurs objectifs qualité
- b) Pour paralléliser les calculs
- c) Pour moyenner les prédictions

Réponse : a)

**11. Quelle affirmation est correcte?**
- a) Un algorithme de bandit apprend toujours plus vite avec un noyau complexe
- b) La régularisation et le choix du noyau ou des features sont cruciaux pour éviter le surapprentissage ou la sous-estimation de l’incertitude
- c) Il suffit d’augmenter la taille des données pour garantir la performance

Réponse : b)


