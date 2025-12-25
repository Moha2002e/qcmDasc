
const fs = require('fs');
const path = require('path');

const questionsPath = path.join(__dirname, 'src/data/questions.json');
const existingQuestions = JSON.parse(fs.readFileSync(questionsPath, 'utf8'));

// Add chapterId: 1 to existing questions
const updatedExisting = existingQuestions.map(q => ({
    ...q,
    chapterId: 1
}));

// New Chapter 3 questions
const newQuestions = [
    {
        "id": 44,
        "chapterId": 3,
        "question": "Quel est le rôle principal de `Class.forName('driver...')` ?",
        "options": [
            "Créer la connexion à la BD",
            "Charger le driver JDBC en mémoire",
            "Exécuter des requêtes SQL",
            "Trier les résultats"
        ],
        "answer": 1,
        "explanation": "`Class.forName()` charge dynamiquement la classe du driver et déclenche son auto-enregistrement auprès du `DriverManager`."
    },
    {
        "id": 45,
        "chapterId": 3,
        "question": "Depuis JDBC 4, `Class.forName()` est-il obligatoire ?",
        "options": [
            "Oui, toujours",
            "Non, le chargement est souvent automatique",
            "Oui, si on utilise MySQL",
            "Non, JDBC ne nécessite plus de driver"
        ],
        "answer": 1,
        "explanation": "Les drivers modernes sont détectés automatiquement via le mécanisme SPI de Java."
    },
    {
        "id": 46,
        "chapterId": 3,
        "question": "Quelle classe gère la liste des drivers et fournit les connexions ?",
        "options": [
            "Connection",
            "Driver",
            "DriverManager",
            "DataSource"
        ],
        "answer": 2,
        "explanation": "`DriverManager` est la classe utilitaire qui sélectionne le bon driver en fonction de l'URL JDBC fournie."
    },
    {
        "id": 47,
        "chapterId": 3,
        "question": "`Connection` en JDBC est :",
        "options": [
            "Une classe",
            "Une interface",
            "Une méthode",
            "Une exception"
        ],
        "answer": 1,
        "explanation": "`Connection` est une interface définissant le contrat standard. L'implémentation réelle est fournie par le driver (ex: MySQL)."
    },
    {
        "id": 48,
        "chapterId": 3,
        "question": "Quel est le format typique d'une URL JDBC MySQL ?",
        "options": [
            "http://mysql/db",
            "jdbc:mysql://host:port/db",
            "sql:jdbc:mysql:db",
            "mysql:host:db"
        ],
        "answer": 1,
        "explanation": "Le format standard est `jdbc:<sous-protocole>:<détails>`."
    },
    {
        "id": 49,
        "chapterId": 3,
        "question": "Quelle méthode permet d'obtenir une connexion ?",
        "options": [
            "new Connection()",
            "DriverManager.getConnection()",
            "Statement.connect()",
            "Class.forName()"
        ],
        "answer": 1,
        "explanation": "On ne fait jamais `new Connection()`. C'est `DriverManager` qui fabrique l'objet."
    },
    {
        "id": 50,
        "chapterId": 3,
        "question": "Par défaut, le mode Auto-Commit d'une connexion est :",
        "options": [
            "Désactivé (false)",
            "Activé (true)",
            "Aléatoire",
            "Réservé à l'admin"
        ],
        "answer": 1,
        "explanation": "Par défaut, chaque requête SQL (INSERT/UPDATE...) est validée immédiatement."
    },
    {
        "id": 51,
        "chapterId": 3,
        "question": "Quand `rollback()` a-t-il un effet ?",
        "options": [
            "Toujours",
            "Jamais",
            "Seulement si Auto-Commit est désactivé (false)",
            "Seulement après un SELECT"
        ],
        "answer": 2,
        "explanation": "Si Auto-Commit est true, les transactions sont instantanées. Pour utiliser rollback, il faut gérer la transaction manuellement."
    },
    {
        "id": 52,
        "chapterId": 3,
        "question": "Quelle interface permet d'envoyer des requêtes SQL basiques ?",
        "options": [
            "ResultSet",
            "Statement",
            "Query",
            "Transaction"
        ],
        "answer": 1,
        "explanation": "`Statement` est l'interface de base pour l'exécution d'instructions SQL statiques."
    },
    {
        "id": 53,
        "chapterId": 3,
        "question": "Que retourne `stmt.executeUpdate(...)` ?",
        "options": [
            "Un ResultSet",
            "Un boolean",
            "Un int (nombre de lignes affectées)",
            "Une Connection"
        ],
        "answer": 2,
        "explanation": "Il retourne le nombre de lignes insérées, modifiées ou supprimées."
    },
    {
        "id": 54,
        "chapterId": 3,
        "question": "Que retourne `stmt.executeQuery(...)` ?",
        "options": [
            "Un ResultSet",
            "Un int",
            "Un boolean",
            "Un tableau"
        ],
        "answer": 0,
        "explanation": "Il est utilisé pour les SELECT et retourne toujours un objet `ResultSet`."
    },
    {
        "id": 55,
        "chapterId": 3,
        "question": "La méthode `execute(sql)` peut exécuter :",
        "options": [
            "Seulement des SELECT",
            "Seulement des UPDATE",
            "N'importe quel type de requête SQL",
            "Rien, elle n'existe pas"
        ],
        "answer": 2,
        "explanation": "`execute()` est générique. Elle retourne `true` si le résultat est un ResultSet, `false` sinon."
    },
    {
        "id": 56,
        "chapterId": 3,
        "question": "Pourquoi faut-il appeler `rs.next()` avant de lire des données ?",
        "options": [
            "Pour trier les données",
            "Car le curseur est initialement placé AVANT la première ligne",
            "C'est optionnel",
            "Pour se connecter à la base"
        ],
        "answer": 1,
        "explanation": "Le curseur démarre 'beforeFirst'. Le premier appel à `next()` le place sur la première ligne réelle."
    },
    {
        "id": 57,
        "chapterId": 3,
        "question": "En JDBC, les index des colonnes commencent généralement à :",
        "options": [
            "0",
            "1",
            "-1",
            "Cela dépend du driver"
        ],
        "answer": 1,
        "explanation": "Dans l'API JDBC standard, les index de colonnes sont 1-based (commencent à 1)."
    },
    {
        "id": 58,
        "chapterId": 3,
        "question": "Quel est le risque principal de `Statement` classique ?",
        "options": [
            "Il est trop rapide",
            "L'injection SQL",
            "Il ne supporte pas les SELECT",
            "Il utilise trop de mémoire"
        ],
        "answer": 1,
        "explanation": "En concaténant des chaînes pour créer la requête, on est vulnérable aux injections SQL."
    },
    {
        "id": 59,
        "chapterId": 3,
        "question": "Quelle est la version sécurisée et précompilée de `Statement` ?",
        "options": [
            "SecureStatement",
            "PreparedStatement",
            "CompiledQuery",
            "FocusStatement"
        ],
        "answer": 1,
        "explanation": "`PreparedStatement` permet de séparer le code SQL des données (paramètres), empêchant l'injection."
    },
    {
        "id": 60,
        "chapterId": 3,
        "question": "Dans `PreparedStatement`, par quoi sont remplacés les paramètres ?",
        "options": [
            "Des %",
            "Des $",
            "Des points d'interrogation (?)",
            "Des étoiles (*)"
        ],
        "answer": 2,
        "explanation": "Les placeholders sont des `?`. Exemple : `SELECT * FROM users WHERE id = ?`."
    },
    {
        "id": 61,
        "chapterId": 3,
        "question": "Que signifie DAO ?",
        "options": [
            "Data Access Object",
            "Direct Access Output",
            "Driver Auto Open",
            "Database Abstract Organization"
        ],
        "answer": 0,
        "explanation": "DAO est un motif de conception (pattern) encapsulant l'accès aux données."
    },
    {
        "id": 62,
        "chapterId": 3,
        "question": "Quelle méthode permet d'obtenir les métadonnées (noms des colonnes...) ?",
        "options": [
            "rs.getMetaData()",
            "con.getInfo()",
            "stmt.getDetails()",
            "System.getMeta()"
        ],
        "answer": 0,
        "explanation": "`ResultSetMetaData` s'obtient via `rs.getMetaData()` et décrit la structure des résultats."
    },
    {
        "id": 63,
        "chapterId": 3,
        "question": "Quelle classe Java correspond au type SQL `DATE` ?",
        "options": [
            "java.util.Date",
            "java.sql.Date",
            "java.time.Instant",
            "String"
        ],
        "answer": 1,
        "explanation": "`java.sql.Date` est le wrapper JDBC standard pour les dates (sans partie heure)."
    },
    {
        "id": 64,
        "chapterId": 3,
        "question": "Pourquoi utiliser `Integer` au lieu de `int` dans une classe entité ?",
        "options": [
            "C'est plus rapide",
            "Pour autoriser la valeur `null`",
            "C'est obligatoire en Java",
            "Pour faire des calculs"
        ],
        "answer": 1,
        "explanation": "Les types primitifs (`int`) ne peuvent pas être null. Les bases de données acceptant NULL, les wrappers (`Integer`) sont préférables."
    },
    {
        "id": 65,
        "chapterId": 3,
        "question": "Si `executeUpdate` retourne 0, cela signifie :",
        "options": [
            "Une erreur SQL",
            "Aucune ligne n'a été affectée",
            "La base est vide",
            "La requête est invalide"
        ],
        "answer": 1,
        "explanation": "Cela signifie que la requête a réussi techniquement, mais qu'elle n'a modifié aucune ligne (ex: UPDATE avec WHERE introuvable)."
    },
    {
        "id": 66,
        "chapterId": 3,
        "question": "Que doit-on faire absolument après avoir utilisé une Connection ?",
        "options": [
            "La laisser ouverte pour gagner du temps",
            "La fermer (`close()`)",
            "La supprimer",
            "Redémarrer le serveur"
        ],
        "answer": 1,
        "explanation": "Les connexions sont des ressources limitées et coûteuses. Il faut les libérer pour éviter les fuites."
    },
    {
        "id": 67,
        "chapterId": 3,
        "question": "Dans le pattern DAO, que contient la classe DAO ?",
        "options": [
            "L'interface graphique",
            "Les requêtes SQL et la gestion de connexion",
            "Les règles CSS",
            "Le code HTML"
        ],
        "answer": 1,
        "explanation": "Le DAO isole la couche persistance. L'UI ne doit pas contenir de SQL."
    },
    {
        "id": 68,
        "chapterId": 3,
        "question": "Quelle méthode permet de passer un entier à un PreparedStatement ?",
        "options": [
            "setId()",
            "putInt()",
            "setInt(index, valeur)",
            "addParam()"
        ],
        "answer": 2,
        "explanation": "On utilise les setters typés comme `setInt`, `setString`, etc. en précisant l'index du `?`."
    },
    {
        "id": 69,
        "chapterId": 3,
        "question": "Comment vérifier si un ResultSet contient encore des lignes ?",
        "options": [
            "rs.hasNext()",
            "rs.next() retourne true",
            "rs.isEmpty()",
            "rs.check()"
        ],
        "answer": 1,
        "explanation": "La méthode `next()` déplace le curseur et indique (boolean) s'il y a une ligne valide à lire."
    },
    {
        "id": 70,
        "chapterId": 3,
        "question": "Dans le modèle SearchVM (ViewModel), si un champ est null :",
        "options": [
            "On plante le programme",
            "On cherche les valeurs NULL en base",
            "On ignore ce critère de recherche",
            "On cherche une chaine vide"
        ],
        "answer": 2,
        "explanation": "C'est une convention courante : un champ null dans un filtre de recherche signifie 'peu importe cette valeur'."
    },
    {
        "id": 71,
        "chapterId": 3,
        "question": "`ResultSet` permet-il de revenir en arrière par défaut ?",
        "options": [
            "Oui, avec previous()",
            "Non, c'est un curseur forward-only par défaut",
            "Oui, toujours",
            "Oui, avec back()"
        ],
        "answer": 1,
        "explanation": "Par défaut, le ResultSet est TYPE_FORWARD_ONLY."
    },
    {
        "id": 72,
        "chapterId": 3,
        "question": "Quel objet contient les données d'une ligne de la table 'Car' ?",
        "options": [
            "L'objet Car (Entité)",
            "L'objet Connection",
            "L'objet Driver",
            "L'objet String"
        ],
        "answer": 0,
        "explanation": "L'entité (Entity) est une classe Java simple (POJO) qui mappe la structure de la table."
    },
    {
        "id": 73,
        "chapterId": 3,
        "question": "Quelle exception principale les méthodes JDBC lèvent-elles ?",
        "options": [
            "IOException",
            "SQLException",
            "DatabaseException",
            "NullPointerException"
        ],
        "answer": 1,
        "explanation": "La quasi-totalité des opérations JDBC déclarent lancer `SQLException` (checked exception)."
    },
    {
        "id": 74,
        "chapterId": 3,
        "question": "Peut-on avoir plusieurs `Statement` ouverts sur une même `Connection` ?",
        "options": [
            "Non, un seul à la fois",
            "Oui, c'est possible",
            "Oui, mais seulement en lecture",
            "Non, risque de crash"
        ],
        "answer": 1,
        "explanation": "Une connexion peut fabriquer plusieurs Statements distincts."
    },
    {
        "id": 75,
        "chapterId": 3,
        "question": "Quelle méthode permet de convertir une date SQL en LocalDate ?",
        "options": [
            "toLocalDate()",
            "getDate()",
            "parse()",
            "convert()"
        ],
        "answer": 0,
        "explanation": "Depuis Java 8, `java.sql.Date` possède la méthode de commodité `toLocalDate()`."
    },
    {
        "id": 76,
        "chapterId": 3,
        "question": "Dans le code `Class.forName('xyz')`, quel est le but du bloc `static` du driver ?",
        "options": [
            "Afficher un message",
            "S'enregistrer auprès du DriverManager",
            "Ouvrir la connexion",
            "Créer la table"
        ],
        "answer": 1,
        "explanation": "Le bloc statique du Driver contient l'appel à `DriverManager.registerDriver(new Driver())`."
    },
    {
        "id": 77,
        "chapterId": 3,
        "question": "Si j'utilise `statement.executeQuery` pour un INSERT, que se passe-t-il ?",
        "options": [
            "Cela fonctionne normalement",
            "Une SQLException est levée",
            "Rien ne se passe",
            "La base est supprimée"
        ],
        "answer": 1,
        "explanation": "L'API JDBC lève souvent une exception si on utilise la mauvaise méthode (bien que certains drivers soient permissifs, la spec dit que executeQuery doit retourner un ResultSet)."
    },
    {
        "id": 78,
        "chapterId": 3,
        "question": "SOLID : Quel principe le DAO respecte-t-il particulièrement ?",
        "options": [
            "Single Responsibility Principle (SRP)",
            "Liskov Substitution",
            "Interface Segregation",
            "None"
        ],
        "answer": 0,
        "explanation": "Le DAO isole la responsabilité de l'accès aux données, laissant la logique métier aux autres classes."
    },
    {
        "id": 79,
        "chapterId": 3,
        "question": "Mapping : Une table 'cars' et une table 'engines' liée. L'entité `Car` aura :",
        "options": [
            "Un champ `int engine_id`",
            "Un champ `Engine engine` (objet)",
            "Rien",
            "Une méthode SQL"
        ],
        "answer": 1,
        "explanation": "En POO, on préfère mapper les relations par des références d'objets (composition) plutôt que par des ID étrangers bruts."
    },
    {
        "id": 80,
        "chapterId": 3,
        "question": "Quel est l'avantage de `PreparedStatement` pour la maintenance ?",
        "options": [
            "Le code est plus court",
            "Il sépare la structure de la requête des données variables, améliorant la lisibilité",
            "Il supprime le besoin de connexion",
            "Il génère du HTML"
        ],
        "answer": 1,
        "explanation": "C'est plus propre que la concaténation de chaînes de caractères."
    },
    {
        "id": 81,
        "chapterId": 3,
        "question": "Comment savoir combien de colonnes contient un ResultSet ?",
        "options": [
            "rs.size()",
            "rs.getMetaData().getColumnCount()",
            "rs.length",
            "rs.count()"
        ],
        "answer": 1,
        "explanation": "Il faut passer par les métadonnées."
    },
    {
        "id": 82,
        "chapterId": 3,
        "question": "Que fait `Statement.execute()` si le résultat est un update count ?",
        "options": [
            "Elle retourne true",
            "Elle retourne false",
            "Elle retourne l'entier",
            "Elle plante"
        ],
        "answer": 1,
        "explanation": "Elle retourne `false` si le résultat n'est PAS un ResultSet."
    },
    {
        "id": 83,
        "chapterId": 3,
        "question": "Quelle est la bonne pratique pour gérer les exceptions JDBC ?",
        "options": [
            "Les ignorer (catch vide)",
            "Utiliser try-with-resources pour fermer automatiquement",
            "Ne pas utiliser de try-catch",
            "Relancer en RuntimeException sans logger"
        ],
        "answer": 1,
        "explanation": "`try(Connection c = ...) { ... }` garantit la fermeture propre des ressources même en cas d'erreur."
    }
];

const allQuestions = [...updatedExisting, ...newQuestions];

fs.writeFileSync(questionsPath, JSON.stringify(allQuestions, null, 4), 'utf8');
