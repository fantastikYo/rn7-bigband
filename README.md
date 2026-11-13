# Site du RN7 Big Band — mise en ligne sur GitHub Pages

## 1. Mettre le site en ligne (10 minutes, gratuit)
1. Créez un compte sur https://github.com (ou utilisez le vôtre).
2. Cliquez sur **New repository**, nommez-le `rn7bigband`, en **Public**, puis **Create**.
3. Cliquez sur **uploading an existing file** et déposez `index.html`, puis **Commit changes**.
4. Allez dans **Settings → Pages** : Source = **Deploy from a branch**, Branch = `main` / `(root)`, puis **Save**.
5. Après environ 1 minute, le site est en ligne sur `https://VOTRE-PSEUDO.github.io/rn7bigband/`.

## 2. Brancher votre nom de domaine (ex. rn7bigband.fr)
1. Achetez le domaine chez un registrar (OVH, Gandi, Namecheap…).
2. Dans la zone DNS du registrar, ajoutez :
   - 4 enregistrements **A** pour `@` : `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - 1 enregistrement **CNAME** pour `www` → `VOTRE-PSEUDO.github.io`
3. Sur GitHub, dans **Settings → Pages → Custom domain**, saisissez `rn7bigband.fr`, puis **Save**.
4. Quand la vérification est passée, cochez **Enforce HTTPS**. La propagation DNS peut prendre quelques heures.

## 3. Mettre à jour le contenu
Tout se trouve en bas de `index.html`, dans la **ZONE À MODIFIER** :
- **ACTUALITÉS** : copiez un bloc `{ ... }`, collez-le en haut de la liste, puis changez la date, le titre, le lieu et le texte.
- **VIDÉOS** : collez le lien YouTube complet et un titre. La vignette s'affiche toute seule.
- **CONFIG** : l'e-mail de contact et le lien de la chaîne YouTube.

Sur GitHub : ouvrez `index.html`, cliquez sur le crayon ✏️, modifiez, puis **Commit changes**. Le site se met à jour en environ 1 minute.

## 4. (Optionnel) Recevoir les messages du formulaire directement
Par défaut, le bouton « Envoyer » ouvre la messagerie du visiteur.
Pour recevoir les messages sans passer par là : créez un formulaire gratuit sur https://formspree.io et copiez son identifiant (ex. `xyzabcd`) dans `formspree: ""`.
