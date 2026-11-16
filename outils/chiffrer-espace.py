#!/usr/bin/env python3
"""Génère espace-musiciens.html : le contenu est chiffré (AES-256-GCM, clé dérivée
du mot de passe par PBKDF2-SHA256) et ne s'affiche qu'avec le bon mot de passe.

Usage : python3 outils/chiffrer-espace.py
  - lit le contenu en clair dans outils/espace-musiciens.contenu.html (non versionné)
    (la liste des fichiers du Drive est chargée en direct par la page, via la clé
    d'API Google Drive indiquée dans ce fichier : inutile de relancer le script
    quand on ajoute des fichiers dans le Drive)
  - demande le mot de passe (jamais enregistré)
  - écrit espace-musiciens.html à la racine du site
"""
import base64, getpass, os, pathlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 600_000
ici = pathlib.Path(__file__).resolve().parent
racine = ici.parent
contenu = (ici / "espace-musiciens.contenu.html").read_text(encoding="utf-8")
mdp = os.environ.get("RN7_MDP") or getpass.getpass("Mot de passe : ")
if not os.environ.get("RN7_MDP") and getpass.getpass("Confirmer : ") != mdp:
    raise SystemExit("Les mots de passe ne correspondent pas.")
sel, iv = os.urandom(16), os.urandom(12)
cle = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sel, iterations=ITER).derive(mdp.encode())
chiffre = AESGCM(cle).encrypt(iv, contenu.encode(), None)
b64 = lambda b: base64.b64encode(b).decode()
modele = (ici / "espace-musiciens.modele.html").read_text(encoding="utf-8")
page = (modele.replace("{{SEL}}", b64(sel)).replace("{{IV}}", b64(iv))
        .replace("{{DONNEES}}", b64(chiffre)).replace("{{ITER}}", str(ITER)))
(racine / "espace-musiciens.html").write_text(page, encoding="utf-8")
print("espace-musiciens.html généré.")
