# RP2040 HID – Rubber Ducky Concept with CircuitPython

## Definition / Context
Le **Rubber Ducky** est une clé USB qui agit comme un clavier (HID) et exécute automatiquement des frappes lorsqu’elle est branchée.  
Avec une carte **RP2040** (Raspberry Pi Pico ou dérivé), on peut reproduire ce comportement à faible coût en utilisant **CircuitPython** et les librairies HID d’Adafruit.  

Ce projet est un **side project éducatif** : comprendre le concept BadUSB, expérimenter avec la RP2040, et garder une marche à suivre claire pour pouvoir le refaire plus tard.

---

## Hardware Requirements
- RP2040 board (Raspberry Pi Pico ou clé USB RP2040)  
- Un PC cible (exemple ici : Windows)  

---

## Step 1 – Bootloader Mode
- Maintenir le bouton **BOOTSEL** en branchant la RP2040.  
- La carte apparaît comme un disque **RPI-RP2** → elle est en mode **bootloader**.  

---

## Step 2 – Install CircuitPython
- Télécharger le firmware CircuitPython adapté à la RP2040 :  
  👉 [CircuitPython for RP2040](https://circuitpython.org/board/adafruit_feather_rp2040/)  
- Drag and Drop le fichier `.uf2` dans **RPI-RP2**.  
- La carte redémarre automatiquement en **CIRCUITPY** (nouveau volume USB).  

*(Optionnel)* Pour repartir de zéro : copier `flash_nuke.uf2` dans **RPI-RP2** avant de flasher le firmware.  

---

## Step 3 – Install Libraries
- Télécharger le **CircuitPython Bundle** correspondant à ta version :  
  👉 [Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)  
- Depuis le bundle, copier dans `CIRCUITPY/lib/` :  
  - le dossier **adafruit_hid/**  
  - le fichier **adafruit_ducky.mpy**  
- Depuis le bundle des layouts clavier, ajouter :  
  - **keyboard_layout_win_fr.mpy** et **keycode_win_fr.mpy** (si l’OS cible est en FR/AZERTY)  

Arborescence attendue :
```
CIRCUITPY/
│
├── code.py
├── payload.txt
└── lib/
├── adafruit_hid/
├── adafruit_ducky.mpy
├── keyboard_layout_win_fr.mpy
└── keycode_win_fr.mpy
```
---

## Step 4 – Add Your Scripts
- **code.py** : script principal qui charge et exécute le payload.  
- **payload.txt** : script DuckyScript contenant les frappes clavier.  

Entraînez-vous avec les payloads que vous voulez (ouvrir Notepad, taper un texte, lancer une URL, etc.).  

---

## Step 5 – Execution
- Débrancher puis rebrancher la RP2040.  
- Le script **code.py** est exécuté automatiquement.  
- Le contenu de **payload.txt** est injecté sur la machine cible, exactement comme un Rubber Ducky.  

---

## Step 6 – Hide CIRCUITPY (Optional)
Par défaut, Windows ouvre l’explorateur de fichier sur le disque **CIRCUITPY** à chaque branchement (test).  
Si vous voulez que la clé se comporte comme un vrai Rubber Ducky (uniquement HID, pas de stockage visible) :  

1. Créez un fichier `boot.py` à la racine avec :  
   ```python
   import storage
   storage.disable_usb_drive()
   ```

### Après ça :

✅ Plus d’explorateur : la clé est invisible comme périphérique de stockage.
✅ Elle agit uniquement comme **clavier HID**.

⚠️ ATTENTION !!! Vous ne pourrez **plus modifier vos fichiers**.

---

## ❗ Problem ? Reset !

Si vous devez rééditer vos fichiers après avoir désactivé le stockage :

* Utilisez **flash\_nuke.uf2** pour réinitialiser complètement la carte.
* Réinstallez ensuite CircuitPython et recopiez vos fichiers.

---

## Advantages / Drawbacks

**Avantages :**

* Très faible coût (\~5 €)
* Fonctionne "comme" un Rubber Ducky (\~80 \$)
* Simple à personnaliser avec un fichier texte

**Inconvénients :**

* Mémoire limitée (\~256 KB)
* Un peu plus lent que la Rubber Ducky officielle (firmware C plus optimisé)
* Obligation de reflasher si vous désactivez le stockage et voulez reprogrammer

---

## Security Note

⚠️ **Utilisation responsable uniquement.**

* N’utilisez jamais ce type de périphérique sans autorisation explicite.
* Ce projet est destiné à l’apprentissage, aux démonstrations.



