# Site du RN7 Big Band — mise en ligne sur GitHub Pages

## 1. Mettre le site en ligne (10 minutes, gratuit)
1. Créez un compte sur https://github.com (ou utilisez le vôtre).
2. Cliquez sur **New repository**, nommez-le `rn7bigband`, en **Public**, puis **Create**.
3. Cliquez sur **uploading an existing file** et déposez `index.html`, puis **Commit changes**.
4. Allez dans **Settings → Pages** : Source = **Deploy from a branch**, Branch = `main` / `(root)`, puis **Save**.
5. Après environ 1 minute, le site est en ligne sur `https://VOTRE-PSEUDO.github.io/rn7bigband/`.

## 2. Brancher votre nom de domaine (rn7bigband.org, chez Namecheap)
1. Achetez le domaine chez un registrar (OVH, Gandi, Namecheap…).
2. Dans la zone DNS du registrar, ajoutez :
   - 4 enregistrements **A** pour `@` : `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - 1 enregistrement **CNAME** pour `www` → `VOTRE-PSEUDO.github.io`
3. Sur GitHub, dans **Settings → Pages → Custom domain**, saisissez `rn7bigband.org`, puis **Save**.
4. Quand la vérification est passée, cochez **Enforce HTTPS**. La propagation DNS peut prendre quelques heures.

## 3. Mettre à jour le contenu
Tout se trouve en bas de `index.html`, dans la **ZONE À MODIFIER** :
- **ACTUALITÉS** : copiez un bloc `{ ... }`, collez-le en haut de la liste, puis changez la date, le titre, le lieu et le texte.
- **VIDÉOS** : collez le lien YouTube complet et un titre. La vignette s'affiche toute seule.
- **CONFIG** : l'e-mail de contact et le lien de la chaîne YouTube.

Sur GitHub : ouvrez `index.html`, cliquez sur le crayon ✏️, modifiez, puis **Commit changes**. Le site se met à jour en environ 1 minute.

## 4. Formulaire de contact
Le formulaire passe par **Web3Forms** (gratuit, 250 messages/mois) : les messages arrivent directement sur l'e-mail associé à la clé `web3forms` de `CONFIG`.
Pour changer d'adresse de réception, créez une nouvelle clé sur https://web3forms.com et remplacez-la dans `CONFIG`. Clé vide = le bouton ouvre la messagerie du visiteur.

## 5. Espace musiciens (page protégée par mot de passe)
`espace-musiciens.html` est chiffrée : son contenu ne s'affiche qu'avec le mot de passe, et ne peut pas être lu dans le code source.
Elle affiche en direct les fichiers du dossier Google Drive partagé : chaque MP3 devient une vignette qui s'écoute sur place, les autres fichiers (PDF…) s'ouvrent en aperçu. Les sous-dossiers deviennent des rubriques.
**Ajouter un fichier dans le Drive suffit** : il apparaît tout seul sur la page.

La lecture passe par une clé d'API Google Drive (Google Cloud Console, projet « RN7 site »), restreinte à l'API Drive et aux adresses du site (rn7bigband.org, www.rn7bigband.org, fantastikyo.github.io). Si le site change d'adresse, ajoutez-la dans les restrictions de la clé.

Pour changer le texte, le dossier, la clé ou le mot de passe (sur un ordinateur avec Python et le module `cryptography`) :
1. modifiez `outils/espace-musiciens.contenu.html` (fichier en clair, **non publié** : il est exclu par `.gitignore`) ;
2. lancez `python3 outils/chiffrer-espace.py` et saisissez le mot de passe ;
3. commitez le nouveau `espace-musiciens.html`.

Le mot de passe n'est enregistré nulle part : notez-le de votre côté.

## 6. Référencement
- Titre, description, adresse canonique, balises de partage (Open Graph, image `assets/partage.jpg`) et données structurées (`MusicGroup`) sont dans l'en-tête de `index.html`.
- Les concerts **à venir** de `ACTUALITES` sont déclarés automatiquement à Google comme événements (`MusicEvent`) : renseignez bien `lieu` sous la forme « Salle — Ville ».
- `robots.txt` et `sitemap.xml` sont à la racine. Inscrivez le site dans Google Search Console (https://search.google.com/search-console) et soumettez `https://rn7bigband.org/sitemap.xml`.
