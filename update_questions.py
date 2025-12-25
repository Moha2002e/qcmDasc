
import json

existing_questions = [
    {
        "id": 1,
        "question": "Qu'est-ce qu'une socket ?",
        "options": [
            "Un câble physique",
            "Un point de communication bidirectionnel",
            "Un type de variable en C",
            "Un protocole Internet"
        ],
        "answer": 1,
        "explanation": "Une socket est un point de communication (endpoint) permettant l'échange de données entre processus."
    },
    {
        "id": 2,
        "question": "Quel mode de communication le protocole TCP utilise-t-il ?",
        "options": [
            "Mode non connecté (datagramme)",
            "Mode déconnecté",
            "Mode connecté (stream)",
            "Mode aléatoire"
        ],
        "answer": 2,
        "explanation": "TCP (Transmission Control Protocol) utilise le mode connecté (SOCK_STREAM), garantissant fiabilité et ordre."
    },
    {
        "id": 3,
        "question": "Quel couple identifie de manière unique une socket en mode connecté ?",
        "options": [
            "{Adresse MAC, Port}",
            "{Adresse IP, Protocole}",
            "{Adresse IP, Port}",
            "{Nom d'hôte, Adresse IP}"
        ],
        "answer": 2,
        "explanation": "En mode connecté, une socket est identifiée par le couple unique {Adresse IP, Port}."
    },
    {
        "id": 4,
        "question": "Quelle primitive crée une socket ?",
        "options": [
            "make_socket()",
            "create()",
            "open()",
            "socket()"
        ],
        "answer": 3,
        "explanation": "La fonction `socket()` est l'appel système permettant de créer une nouvelle socket."
    },
    {
        "id": 5,
        "question": "Quel paramètre de `socket()` spécifie IPv4 ?",
        "options": [
            "AF_INET6",
            "AF_UNIX",
            "AF_INET",
            "SOCK_INET"
        ],
        "answer": 2,
        "explanation": "`AF_INET` est la famille d'adresses correspondant aux adresses Internet IPv4."
    },
    {
        "id": 6,
        "question": "Quel type de socket correspond au mode UDP ?",
        "options": [
            "SOCK_STREAM",
            "SOCK_RAW",
            "SOCK_DGRAM",
            "SOCK_PACKET"
        ],
        "answer": 2,
        "explanation": "`SOCK_DGRAM` (Datagram) est utilisé pour le mode non connecté (UDP)."
    },
    {
        "id": 7,
        "question": "Que retourne `socket()` en cas d'erreur ?",
        "options": [
            "0",
            "NULL",
            "-1",
            "false"
        ],
        "answer": 2,
        "explanation": "La fonction retourne -1 en cas d'erreur et met à jour la variable globale `errno`."
    },
    {
        "id": 8,
        "question": "Après création par `socket()`, l'état initial de la socket est :",
        "options": [
            "Connectée",
            "Liée à un port 80",
            "Anonyme (ni IP ni port)",
            "En écoute"
        ],
        "answer": 2,
        "explanation": "Juste après `socket()`, la socket existe mais n'est attachée à aucune adresse ni port (elle est anonyme)."
    },
    {
        "id": 9,
        "question": "Quelle fonction associe une socket à une adresse IP et un port ?",
        "options": [
            "connect()",
            "link()",
            "bind()",
            "listen()"
        ],
        "answer": 2,
        "explanation": "`bind()` est utilisée pour 'lier' la socket à une adresse locale spécifique."
    },
    {
        "id": 10,
        "question": "Qui doit OBLIGATOIREMENT utiliser `bind()` ?",
        "options": [
            "Le Client",
            "Le Serveur",
            "Les deux",
            "Aucun des deux"
        ],
        "answer": 1,
        "explanation": "Le serveur doit utiliser `bind()` pour être joignable sur un port connu. Le client peut laisser le système choisir."
    },
    {
        "id": 12,
        "question": "Quel est le rôle du DNS ?",
        "options": [
            "Sécuriser la connexion",
            "Traduire un nom d'hôte en adresse IP",
            "Compresser les données",
            "Gérer les erreurs réseaux"
        ],
        "answer": 1,
        "explanation": "Le DNS (Domain Name System) permet de faire correspondre un nom d'hôte convivial à une adresse IP numérique."
    },
    {
        "id": 13,
        "question": "La fonction `listen(sockfd, count)` :",
        "options": [
            "Accepte une connexion immédiatement",
            "Attend des données",
            "Finit la connexion",
            "Met la socket en mode passif (attente)"
        ],
        "answer": 3,
        "explanation": "`listen()` indique au noyau d'accepter les demandes de connexion entrantes sur cette socket."
    },
    {
        "id": 14,
        "question": "Que représente le paramètre 'count' (ou backlog) dans `listen()` ?",
        "options": [
            "Le nombre maximum de sockets créables",
            "Le nombre maximum de connexions actives",
            "La taille de la file d'attente des connexions pendantes",
            "Le délai d'attente avant timeout"
        ],
        "answer": 2,
        "explanation": "Le backlog spécifie combien de connexions peuvent être en attente d'acceptation (handshake terminé mais pas encore accept()) avant d'être rejetées."
    },
    {
        "id": 15,
        "question": "Quelle erreur survient si on tente un `bind()` sur un port déjà pris ?",
        "options": [
            "ENOMEM",
            "EADDRNOTAVAIL",
            "EADDRINUSE",
            "ECONNREFUSED"
        ],
        "answer": 2,
        "explanation": "`EADDRINUSE` signifie que l'adresse (IP/Port) est déjà utilisée par une autre socket."
    },
    {
        "id": 16,
        "question": "Quelle fonction permet au CLIENT d'initier le handshake TCP ?",
        "options": [
            "accept()",
            "dial()",
            "connect()",
            "init()"
        ],
        "answer": 2,
        "explanation": "`connect()` lance la procédure d'établissement de connexion vers le serveur."
    },
    {
        "id": 17,
        "question": "Si un client n'appelle pas `bind()`, que se passe-t-il ?",
        "options": [
            "Erreur à la compilation",
            "Erreur à l'exécution",
            "Le noyau attribue une IP et un port éphémère",
            "Le client utilise le port 0 par défaut"
        ],
        "answer": 2,
        "explanation": "C'est le 'bind implicite'. Le système alloue automatiquement un port libre lorsque `connect()` est appelé."
    },
    {
        "id": 18,
        "question": "Les fonctions `send` et `recv` avec flags=0 sont équivalentes à :",
        "options": [
            "printf et scanf",
            "write et read",
            "put et get",
            "sendto et recvfrom"
        ],
        "answer": 1,
        "explanation": "Sous Unix, écrire sur une socket connectée revient à écrire dans un descripteur de fichier via `write`."
    },
    {
        "id": 19,
        "question": "Quelle primitive est bloquante par défaut ?",
        "options": [
            "socket()",
            "bind()",
            "listen()",
            "connect()"
        ],
        "answer": 3,
        "explanation": "`connect()` bloque le processus jusqu'à ce que la connexion soit établie ou échoue (timeout/refus)."
    },
    {
        "id": 20,
        "question": "Pourquoi faut-il fermer une socket avec `close()` ?",
        "options": [
            "Pour éteindre l'ordinateur",
            "Pour libérer le descripteur et les ressources noyau",
            "Pour envoyer les dernières données",
            "Ce n'est pas nécessaire"
        ],
        "answer": 1,
        "explanation": "Il faut libérer les ressources. Une socket non fermée peut laisser un port en état 'bloqué' (CLOSE_WAIT, etc.)."
    },
    {
        "id": 21,
        "question": "Analysez ce code. Que fait-il ?",
        "code": "int s = socket(AF_INET, SOCK_STREAM, 0);",
        "options": [
            "Crée une socket UDP IPv4",
            "Crée une socket TCP IPv6",
            "Crée une socket TCP IPv4",
            "Crée une socket brute (RAW)"
        ],
        "answer": 2,
        "explanation": "AF_INET = IPv4, SOCK_STREAM = TCP. Le 0 indique le protocole par défaut (TCP)."
    },
    {
        "id": 22,
        "question": "Trouvez l'erreur dans ce code serveur :",
        "code": "bind(sd, (struct sockaddr *)&addr, sizeof(addr));\n// Manque quelque chose ici...\naccept(sd, NULL, NULL);",
        "options": [
            "Il manque socket()",
            "Il manque connect()",
            "Il manque listen()",
            "Il manque close()"
        ],
        "answer": 2,
        "explanation": "Entre `bind` (attacher l'adresse) et `accept` (accepter les clients), il faut impérativement appeler `listen()` pour passer en mode passif."
    },
    {
        "id": 23,
        "question": "Que signifie un retour de -1 sur cet appel ?",
        "code": "if (connect(sockfd, &addr, len) == -1) { ... }",
        "options": [
            "La connexion est établie",
            "La connexion a échoué",
            "La socket est fermée",
            "Le serveur est en attente"
        ],
        "answer": 1,
        "explanation": "Comme la plupart des appels système Unix, -1 signale une erreur (serveur éteint, réseau coupé, etc.)."
    },
    {
        "id": 24,
        "question": "Ce code est-il valide pour envoyer une structure ?",
        "code": "struct Data d = {1, 2};\nsend(sock, &d, sizeof(d), 0);",
        "options": [
            "Non, on ne peut envoyer que des chaînes",
            "Oui, mais attention à l'endianness (ordre des octets)",
            "Non, sizeof() ne marche pas sur les structures",
            "Oui, c'est parfaitement portable tel quel"
        ],
        "answer": 1,
        "explanation": "C'est syntaxiquement valide en C (envoi d'octets bruts), mais risqué entre architectures différentes si on ne gère pas l'endianness (ntohl/htonl)."
    },
    {
        "id": 25,
        "question": "Dans quel état finit une socket si le serveur ferme mais pas le client ?",
        "code": "// Serveur fait close(s)\n// Client ne fait rien",
        "options": [
            "ESTABLISHED",
            "CLOSE_WAIT (côté Client)",
            "LISTEN",
            "CLOSED"
        ],
        "answer": 1,
        "explanation": "Le client reçoit un FIN, l'OS passe sa socket en CLOSE_WAIT, attendant que l'application cliente appelle `close()` explicitement."
    },
    {
        "id": 26,
        "question": "Quelle constante définit le backlog maximum possible ?",
        "code": "listen(sockfd, SOMAXCONN);",
        "options": [
            "MAX_CONN",
            "TCP_MAX",
            "SOMAXCONN",
            "LIMIT_BACKLOG"
        ],
        "answer": 2,
        "explanation": "`SOMAXCONN` est la constante système définissant la limite supérieure de la file d'attente."
    },
    {
        "id": 29,
        "question": "Quel est le problème potentiel ici ?",
        "code": "char buf[10];\nrecv(s, buf, 100, 0);",
        "options": [
            "Aucun problème",
            "Buffer overflow (débordement de tampon)",
            "Erreur de syntaxe",
            "La socket va se fermer"
        ],
        "answer": 1,
        "explanation": "On demande de lire jusqu'à 100 octets dans un buffer qui ne peut en contenir que 10. Risque critique de corruption mémoire."
    },
    {
        "id": 30,
        "question": "Quelle fonction permet de récupérer l'adresse IP d'un client qui vient de se connecter ?",
        "code": "int client_sock = accept(srv_sock, ...);",
        "options": [
            "getpeername() (ou via les arguments de accept)",
            "getsockname()",
            "ipconfig()",
            "whoami()"
        ],
        "answer": 0,
        "explanation": "Les arguments pointeurs de `accept()` (struct sockaddr *) ou la fonction `getpeername()` permettent d'obtenir l'IP et le port du client distant."
    },
    {
        "id": 31,
        "question": "Que retourne la fonction `accept()` en cas de succès ?",
        "options": [
            "0",
            "Le même descripteur que la socket d'écoute",
            "Un nouveau descripteur de fichier dédié à la connexion",
            "L'adresse IP du client"
        ],
        "answer": 2,
        "explanation": "`accept()` crée et retourne une *nouvelle* socket connectée spécifiquement à ce client. La socket d'écoute originale reste disponible pour d'autres connexions."
    },
    {
        "id": 32,
        "question": "L'appel à la fonction `listen()` est-il bloquant ?",
        "options": [
            "Oui, il attend une connexion",
            "Non, il retourne immédiatement",
            "Oui, mais avec un timeout",
            "Cela dépend des flags"
        ],
        "answer": 1,
        "explanation": "`listen()` est purement déclaratif : il informe l'OS que la socket acceptera des connexions. Il ne bloque pas le programme."
    },
    {
        "id": 33,
        "question": "Combien de canaux de communication conceptuels imagine-t-on pour une connexion TCP ?",
        "options": [
            "Un seul canal bidirectionnel mélangé",
            "Deux canaux unidirectionnels (un Emission, un Réception)",
            "Quatre canaux",
            "Aucun, c'est des paquets"
        ],
        "answer": 1,
        "explanation": "Bien que ce soit le même câble, on conceptualise TCP comme deux 'pipes' distincts : un flux allant du Client vers le Serveur, et un flux Serveur vers Client."
    },
    {
        "id": 34,
        "question": "Que signifie généralement l'erreur `ECONNREFUSED` lors d'un `connect()` ?",
        "options": [
            "Le câble réseau est débranché",
            "Le serveur n'est pas lancé ou n'écoute pas sur ce port",
            "Le pare-feu bloque la connexion",
            "L'adresse IP n'existe pas"
        ],
        "answer": 1,
        "explanation": "Cela indique qu'il n'y a 'personne au bout du fil' : aucune application n'a fait de `bind/listen` sur l'IP/Port ciblé."
    },
    {
        "id": 35,
        "question": "Pourquoi peut-on utiliser `read()` et `write()` sur une socket sous Unix ?",
        "options": [
            "C'est une spécificité du langage C",
            "Car 'Tout est fichier' dans la philosophie Unix",
            "C'est une erreur, on ne devrait pas le faire",
            "Car les sockets sont des fichiers textes"
        ],
        "answer": 1,
        "explanation": "Le descripteur de socket est un descripteur de fichier standard, permettant l'usage des outils génériques de manipulation de fichiers."
    },
    {
        "id": 36,
        "question": "Quel est l'ordre typique des appels système pour un SERVEUR TCP ?",
        "options": [
            "socket -> connect -> write",
            "socket -> bind -> listen -> accept",
            "socket -> accept -> listen -> bind",
            "connect -> send -> close"
        ],
        "answer": 1,
        "explanation": "Le serveur crée la socket, la lie à un port (bind), se met en attente (listen), puis accepte les clients (accept)."
    },
    {
        "id": 37,
        "question": "Dans `socket(domain, type, protocol)`, que signifie `protocol = 0` ?",
        "options": [
            "Pas de protocole",
            "Protocole expérimental",
            "Le système choisit le protocole par défaut pour le type (ex: TCP pour STREAM)",
            "Mode raw socket"
        ],
        "answer": 2,
        "explanation": "Mettre 0 demande au système d'utiliser le standard : TCP pour SOCK_STREAM et UDP pour SOCK_DGRAM."
    },
    {
        "id": 38,
        "question": "Qu'est-ce un 'port éphémère' ?",
        "options": [
            "Un port qui change toutes les secondes",
            "Un port temporaire attribué automatiquement par le système",
            "Un port > 65535",
            "Un port réservé à l'administrateur"
        ],
        "answer": 1,
        "explanation": "Lorsqu'un client ne fait pas de `bind()`, le système lui prête un port libre aléatoire (ex: 49152) pour la durée de la connexion."
    },
    {
        "id": 39,
        "question": "Quel appel système déclenche réellement le 'Handshake TCP' sur le réseau ?",
        "options": [
            "socket()",
            "bind()",
            "connect()",
            "listen()"
        ],
        "answer": 2,
        "explanation": "C'est au moment où le client appelle `connect()` que les paquets SYN sont envoyés pour établir la connexion."
    },
    {
        "id": 40,
        "question": "Quelle affirmation est vraie concernant le mode UDP (SOCK_DGRAM) ?",
        "options": [
            "Il garantit l'ordre d'arrivée des paquets",
            "Il nécessite une connexion préalable",
            "Il envoie des messages (datagrammes) indépendants sans garantie",
            "Il est plus lent que TCP"
        ],
        "answer": 2,
        "explanation": "UDP est un protocole 'fire and forget' : on envoie le paquet, mais on ne sait pas s'il arrive ni dans quel ordre."
    },
    {
        "id": 41,
        "question": "Que signifie la famille d'adresse `AF_INET6` ?",
        "options": [
            "Internet Protocol v4",
            "Internet Protocol v6",
            "Réseau local Unix",
            "Bluetooth"
        ],
        "answer": 1,
        "explanation": "AF_INET correspond à IPv4, tandis que AF_INET6 correspond aux adresses IPv6 (128 bits)."
    },
    {
        "id": 42,
        "question": "Où sont stockées les connexions en attente (backlog) gérées par `listen` ?",
        "options": [
            "Dans le disque dur",
            "Dans une file d'attente (FIFO) en mémoire noyau",
            "Dans l'application serveur",
            "Elles sont rejetées immédiatement"
        ],
        "answer": 1,
        "explanation": "Le noyau stocke les connexions 'prêtes' (handshake fini) dans une file jusqu'à ce que l'application les récupère via `accept()`."
    },
    {
        "id": 43,
        "question": "Quel est le type de retour de la fonction `socket()` ?",
        "options": [
            "void",
            "char *",
            "int (descripteur de fichier)",
            "struct socket"
        ],
        "answer": 2,
        "explanation": "Elle retourne un entier (int) qui est l'indice dans la table des descripteurs de fichier du processus."
    }
]

# Set 'chapterId': 1 for all existing questions
for q in existing_questions:
    q['chapterId'] = 1

# New Chapter 3 questions
new_questions = [
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
]

all_questions = existing_questions + new_questions

with open('c:/Users/moha4/Documents/qcmDasc/src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=4, ensure_ascii=False)
