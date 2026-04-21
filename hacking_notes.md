# Notes de cours Hacking - EPITA

## SQL Injection (CH41)

### Exemples d'injection via JavaScript
```javascript
// Variante avec #
document.getElementById("username").value = "admin' #";

// Ou sans connaître le username exact
document.getElementById("username").value = "' OR '1'='1' --";
```

### Pourquoi l'injection peut échouer (même si la console dit "OK")

Si la console confirme que l'entrée est valide mais que l'accès n'est pas accordé, voici les pistes à explorer :

1. **Syntaxe des commentaires** : 
   - `#` est spécifique à **MySQL**.
   - `-- ` (notez l'espace après les tirets) est utilisé pour **PostgreSQL, SQLite, et MS SQL Server**. Sans l'espace, l'injection peut échouer.
   - `/*` peut aussi être utilisé pour fermer la requête.

2. **Équilibrage des parenthèses** : 
   - La requête SQL d'origine peut ressembler à `SELECT * FROM users WHERE (username = '...')`.
   - Dans ce cas, il faut fermer la parenthèse : `admin') #` ou `admin') OR ('1'='1' -- `.

3. **Protection Backend vs Frontend** :
   - Le message "bon" de la console peut venir d'une validation JavaScript simple qui n'indique pas si la base de données a réellement accepté l'injection.
   - Le serveur peut utiliser des **Prepared Statements** (requêtes préparées) qui neutralisent l'injection même si la syntaxe semble correcte.

4. **WAF / Filtrage** :
   - Un Pare-feu Applicatif (WAF) peut détecter les mots-clés `OR` ou `1=1` et bloquer silencieusement la requête ou renvoyer une réponse neutre.

## Structure du CTF Ranku 1 (Exegide)

### Fonctionnement de l'Auth
Le site utilise un **Token JWT** stocké dans les cookies.
- **Extraction du Token** : `getCookie('token')`
- **Décodage** : Le client décode le JWT pour afficher le `username`.
- **Récupération des données** : Une fois "connecté", le site appelle :
  - `data/points?username=...` pour le score.
  - `data/challenges` pour la liste des épreuves.

### Analyse du bouton "Terminer"
Attention : Le bouton avec l'ID `terminate-btn` effectue en fait une requête **POST** vers `/logout`.
- Si l'injection SQL réussit à vous connecter, cliquer sur ce bouton vous déconnectera immédiatement et vous renverra vers `/account`.
- **Piège potentiel** : Si la console affiche "success" après avoir cliqué sur Terminer, cela signifie simplement que la déconnexion a réussi, pas forcément que le challenge est validé.

### Catégories de Challenges
- Authentification 1 & 2
- Stéganographie
- Injection SQL
- Binaire
- OSINT
- MATHS

