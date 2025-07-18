






## MINIQUIZZ (3 Questions):


#### **Q1.** Quelle est la principale différence entre l’approximation linéaire et non linéaire dans la représentation des fonctions de valeur ?

- A. L’approximation linéaire utilise des réseaux de neurones profonds
- B. L’approximation linéaire combine les entrées de façon linéaire, la non linéaire utilise des fonctions complexes comme les réseaux de neurones
- C. La non linéaire est toujours plus rapide
- D. L’approximation linéaire ne nécessite pas de données d’entraînement

✅ **Réponse attendue : B)**


#### **Q2.** Quel est le principe de l’algorithme REINFORCE ?

- A. Utiliser la différence temporelle pour mettre à jour la valeur
- B. Utiliser des réseaux de neurones convolutifs
- C. Mettre à jour la politique en fonction du gradient estimé à partir des trajectoires complètes
- D. Appliquer des bonus de récompense

✅ **Réponse attendue : C)**




#### **Q3.** Qu’est-ce que PPO (Proximal Policy Optimization) cherche à résoudre ?

- A. L’exploration dans les bandits manchots
- B. Les mises à jour de politique trop brutales qui déstabilisent l’apprentissage
- C. L’approximation de fonction linéaire
- D. La planification dans les arbres

✅ **Réponse attendue : B)**


## QUIZZ FINAL (21 Questions):


#### **Q0.** Qu’est-ce que l’approximation de fonction en apprentissage par renforcement, et pourquoi est-elle nécessaire ?

- a) Pour accélérer l’entraînement des réseaux de neurones
- b) Pour représenter efficacement des fonctions dans des espaces d’états vastes ou continus
- c) Pour garantir la convergence de tous les algorithmes
- d) Pour éviter l’utilisation de récompenses négatives

✅ **Réponse attendue : b)**


#### **Q1.** Quel est le principe de LSTD (Least-Squares Temporal Difference) ?

- a) Utiliser la descente de gradient pour mettre à jour les politiques
- b) Maximiser l’entropie de la politique
- c) Résoudre un système d’équations pour estimer les valeurs de façon optimale
- d)  Appliquer des bonus de récompense pour explorer

✅ **Réponse attendue : c)**

---


#### **Q2.** Quelle est la limite principale de LSTD ?

- a) Ne fonctionne qu’avec des réseaux de neurones profonds
- b) Nécessite de stocker et d’inverser de grandes matrices, ce qui devient coûteux
- c) Ne peut s’appliquer qu’aux environnements déterministes
- d) N’est pas compatible avec l’apprentissage hors ligne

---
✅ **Réponse attendue : b)**

#### **Q3.** Dans un algorithme acteur/critique, quel est le rôle du **critique** ?

- a) Générer l'action optimale
- b) Estimer le gradient de la politique
- c) Apprendre la fonction de valeur
- d) Explorer de nouvelles actions

✅ **Réponse attendue : c)**

---

#### **Q4.** Et le rôle de l’**acteur** dans ce même cadre ?

- a) Optimiser la fonction de valeur
- b) Mettre à jour la politique en suivant un gradient
- c) Réduire la variance du gradient
- d) Interroger un modèle de dynamique

✅ **Réponse attendue : b)**

---

#### **Q5.** Quelle est la formule générale du **Policy Gradient Theorem** ?

- a) ∇J(θ) ≈ Esp[∇_θ log π_θ(a|s) \* Q_π(s,a)]
- b) ∇J(θ) ≈ ∇θ Vπ(s)
- c) ∇J(θ) ≈ ∇θ Aπ(s,a)
- d) ∇J(θ) ≈ Qπ(s,- a) \* πθ(a|s)

✅ **Réponse attendue : a)**

---

#### **Q6.** Quelle est une limitation majeure de l’algorithme REINFORCE ?

- a) Il nécessite un modèle
- b) Il ne fonctionne que pour des états discrets
- c) Il présente une variance élevée
- d) Il est instable à cause du replay buffer

✅ **Réponse attendue : c)**

---

#### **Q7.** Quelle est la principale différence entre REINFORCE et un algorithme acteur/critique ?

- a) REINFORCE nécessite un replay buffer
- b) L’acteur/critique utilise une estimation de la valeur pour réduire la variance
- c) REINFORCE est déterministe
- d) L’acteur/critique est hors-ligne uniquement

✅ **Réponse attendue : b)**

---

#### **Q8.** DQN (Deep Q-Network) combine apprentissage Q-Learning et réseau de neurones. Quelle technique est utilisée pour **stabiliser** l’apprentissage ?

- a) L’utilisation de modèles dynamiques
- b) Un réseau critique auxiliaire
- c) Le replay buffer et un target network figé
- d) Un estimateur bayésien de Q

✅ **Réponse attendue : c)**

---

#### **Q9.** Quelle est la différence entre DQN et Double DQN ?

- a) Double DQN utilise deux replay buffers
- b) Double DQN évite la surestimation de Q en séparant sélection et évaluation
- c) DQN est stochastique, Double DQN est déterministe
- d) Double DQN ne nécessite pas de réseau de neurones

✅ **Réponse attendue : b)**

---

#### **Q10.** PPO (Proximal Policy Optimization) cherche à éviter :

- a) La divergence causée par un pas d’apprentissage trop faible
- b) L’oubli catastrophique des politiques anciennes
- c) Les mises à jour trop brutales de la politique
- d) L’explosion du nombre d’actions

✅ **Réponse attendue : c)**

---

#### **Q11.** Quelle est la fonction de perte caractéristique de PPO ?

- a) Bellman residual
- b) Loss = − min(r(θ)A, clip(r(θ), 1−ε, 1+ε)A)
- c) Loss = TD²
- d) − log πθ(a|s) \* Gt

✅ **Réponse attendue : b)**

---

#### **Q12.** Quelle technique suivante permet **d’encourager l’exploration** dans les algorithmes de policy gradient ?

- a) La pénalisation L2
- b) La régularisation par entropie
- c) L’utilisation de replay buffer
- d) La normalisation des observations

✅ **Réponse attendue : b)**

---

#### **Q13.** Qu’est-ce qu’un “advantage” (avantage) en RL ?

- a) Le gain entre une politique ancienne et la nouvelle
- b) La différence entre valeur d’action et valeur d’état : A(s,- a) = Q(s,- a) – V(s)
- c) Une régularisation de la fonction de politique
- d) Une méthode d’optimisation stochastique

✅ **Réponse attendue : b)**

---

#### **Q14.** Pourquoi l’utilisation de réseaux de neurones dans le RL pose-t-elle des problèmes ?

- a) Car ils convergent trop rapidement
- b) Car ils ne sont pas compatibles avec des données séquentielles
- c) Car les données sont non i.i.d. et la cible bouge
- d) Car ils nécessitent trop de mémoire

✅ **Réponse attendue : c)**

---

#### **Q15.** Quel problème peut survenir si la **politique change trop rapidement** pendant l’apprentissage ?

- a) La variance du gradient chute
- b) L’exploration devient optimale
- c) La distribution de données change, rendant les updates incohérents
- d) L’algorithme converge vers le maximum global

✅ **Réponse attendue : c)**

---

#### **Q16.** Quel est un exemple de d'heuristique souvent utilisée dans les algos Deep RL ?

- a) Régularisation par noyau de Parzen
- b) Scheduler de température de Softmax
- c) Clipping des gradients
- d) Lissage gaussien des récompenses

✅ **Réponse attendue : c)**

---

#### **Q17.** Quelle méthode vise à **compenser l'instabilité** causée par le non-stationnaire dans le Deep RL ?

- a) L’utilisation d’un grand pas d’apprentissage
- b) Le recalcul fréquent du replay buffer
- c) La target network mise à jour lentement
- d) La désactivation du Critique pendant l'entraînement

✅ **Réponse attendue : c)**

---

#### **Q18.** Quel type d’approximation est **inadapté** à des états continus et complexes ?

- a) Tabulaire
- b) RBF (Radial Basis Functions)
- c) Approximation linéaire
- d) Réseaux de neurones profonds

✅ **Réponse attendue : a)**

---

#### **Q19.** Quel est un **avantage des réseaux convolutifs** dans le contexte du Deep RL, par exemple pour des jeux Atari ?

- a) Ils réduisent la taille des actions
- b) Ils permettent de mémoriser les politiques anciennes
- c) Ils extraient efficacement des caractéristiques visuelles
- d) Ils remplacent la fonction de valeur par la politique

✅ **Réponse attendue : c)**

---


####  **Q20.**  Qu’est-ce qu’un bonus d'exploration et comment peut-il favoriser l'apprentissage ?

- a) Une récompense supplémentaire pour inciter l’agent à visiter des états peu visités
- b) Une pénalité pour éviter les états dangereux
- c) Une augmentation de la taille du réseau
- d) Un changement du taux d’apprentissage

✅ **Réponse attendue : a)**

