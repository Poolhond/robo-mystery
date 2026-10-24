# ROBO MYSTERY — Spelconcept

**Versie:** 0.5  
**Status:** Ontwerpfase — geen codeontwikkeling  
**Laatste update:** 24 oktober 2026 — Wannes is speler én verjaardagskind; goochelthema toegevoegd

## 1. Kernidee

ROBO MYSTERY is een compact digitaal mysterie-avontuur voor **Wannes (12)**, bedoeld om op zijn verjaardag zelf te spelen. Wannes bestuurt een speelgoedrobot door een vreemde, speelse wereld. Hij krijgt een geheim bericht: er is iets vreemds aan de hand in het speelgoedlab, en de robot moet het onderzoeken.

Wannes doorloopt vier uitdagingen met een goochelthema (observeren, raden, volgen, combineren). Elke uitdaging brengt de robot dichter bij een mysterieuze deur. Wanneer die opengaat, blijkt dat de speelgoedfiguren in het geheim een verjaardagsfeest voor **Wannes** hebben voorbereid. De robot was het instrument waarmee Wannes zijn eigen verrassing ontdekte.

Wannes sluit af met een laatste interactieve handeling waarmee het feest begint.

## 2. Vastgelegde spelbeslissingen

- De speler is **Wannes**; hij bestuurt de robot als zijn handen en ogen.
- Het feest aan het einde is **voor Wannes**, niet voor de robot.
- Wannes speelt het spel op zijn verjaardag zelf.
- Het mysterie blijft aan het begin onduidelijk.
- Het avontuur bevat vier uitdagingen: een mix van observatiepuzzel, raadsels, minigame en combinatiepuzzel.
- Het overkoepelende thema is **goochelen** (Wannes houdt van goocheltrucs, puzzels en raadsels).
- De andere speelgoedfiguren bereiden de verrassing voor.
- De vier uitdagingen leiden naar één gesloten deur.
- Het openen van de deur onthult het verjaardagsfeest.
- De speler voert na de onthulling nog een interactieve handeling uit (lint, feestknop of taart; keuze nog open).
- De wereld is geïnspireerd op het handgemaakte speelgoedlaboratorium en de bestaande karakterreferenties.
- Mobile-first, bediening met één duim, geen account, gratis op GitHub Pages.
- De gamecode wordt pas gemaakt wanneer het dossier af is.

## 3. Verhaal

### Proloog — Een geheim bericht
Wannes opent het spel en ziet een kort bericht (geschreven als een geheime opdracht) dat de robot het speelgoedlab in stuurt. De robot wordt wakker. De omgeving lijkt vertrouwd, maar er zijn vreemde details: een spoor van gekleurde knopen, snippers die op confetti lijken, een deur die gesloten blijft. Het spel geeft nog niet prijs wat het doel is.

### Uitdaging 1 — Het spoor ("Wat is er verdwenen?")
Een observatiepuzzel in goochelstijl. Zie `docs/CHALLENGES.md`.

### Uitdaging 2 — Het raadsel
De speelgoedfiguren geven raadsels waarvan de antwoorden letters of een woord opleveren.

### Uitdaging 3 — Het mechanisme ("De goochelbekers")
De actievere minigame: volg het bekertje. Het mechanisme opent de weg naar het laatste deel van het lab.

### Uitdaging 4 — De laatste sleutel
Wannes combineert de aanwijzingen uit de eerste drie uitdagingen om het slot op de deur te openen.

### Finale — De deur gaat open
De deur onthult een feestlocatie die de speelgoedfiguren zelf hebben klaargemaakt. De aap, panda, schildpad en regenboogoctopus zijn erbij. Ze roepen "Gefeliciteerd, Wannes!" De robot stapt opzij voor het verjaardagskind. Het spoor, de vreemde machine en de aanwijzingen blijken onderdelen van het geheime plan.

## 4. De interactieve feestfinale

De onthulling is niet het einde van de interactie. Wannes krijgt nog één eenvoudige, betekenisvolle handeling waarmee het feest begint. Mogelijke opties (keuze volgt):
- aan een lint trekken waarna confetti en lichtjes aangaan;
- een feestknop indrukken;
- de taart aansnijden samen met de robot.

Daarna doet de robot een **kaarttruc** waarvan de uitkomst altijd "Gefeliciteerd, Wannes!" is, gevolgd door een korte feestelijke slotscène. De toon verschuift van mysterie naar warmte, humor en verrassing.

### Echte slotscène (nog open)
Het laatste scherm kan een echte opdracht bevatten voor na het spel ("Draai je om", "Ga naar de woonkamer", …). Dit hangt af van wat Wannes in het echt wacht. De tekst staat later op één plek in het spel zodat die eenvoudig aanpasbaar is. Zie `docs/DECISIONS.md`.

## 5. Personages

De speelgoedfiguren vormen samen het geheime organisatieteam. Hun rollen zijn voorlopig.

- **De robot:** instrument van Wannes in het spel; hij is de rode draad door alle scènes.
- **Schildpad:** laat een spoor of stille aanwijzing achter.
- **Aap:** zorgt voor humor en afleiding.
- **Panda:** bewaakt een patroon of raadsel.
- **Regenboogoctopus:** helpt bij de kleurrijke feestversiering.

De herkenbare vormen en kleuren van de bestaande speelgoedfiguren blijven leidend. Nieuwe personages worden niet toegevoegd zonder reden.

## 6. Verhaalregels

1. Geef vooraf niet te veel uitleg; Wannes ontdekt het verhaal door te spelen.
2. Elke uitdaging heeft een functie in het avontuur en levert een aanwijzing op.
3. De robot blijft de rode draad door alle scènes.
4. Varieer de uitdagingen: observeren, logisch nadenken, handelen en eerdere informatie combineren.
5. Aanwijzingen zijn vóór de finale mysterieus en achteraf logisch.
6. De speelgoedfiguren mogen verdacht gedrag vertonen maar mogen de verrassing niet te vroeg verklappen. Verjaardagsdetails (snippers, slingers) blijven subtiel tot de deur opengaat.
7. De deur is het centrale doel dat de vier uitdagingen verbindt.
8. De feestfinale is interactief, maar kort en toegankelijk.
9. Teksten spreken Wannes direct aan, in het Nederlands, in een toon die past bij een 12-jarige: speels, geen babytaal.
10. Wannes kan niet vastlopen: elke uitdaging heeft hints en geen echte game over.

## 7. Spelvorm

Een compact point-and-click-avontuur: Wannes tikt op plekken en voorwerpen om de robot ernaartoe te sturen, onderzoekt interactieve elementen en speelt de minigames. Geschikt voor een telefoon; de exacte technische keuzes staan in `docs/TECH-SPEC.md`. Streefduur: ongeveer 8 tot 12 minuten.

## 8. Nog te beslissen

- De exacte raadsels, antwoorden en het sleutelwoord (zie `docs/CHALLENGES.md`).
- De definitieve rollen van de speelgoedfiguren.
- Welke interactieve handeling het feest start.
- Of er een echte opdracht aan het einde komt, en welke.
- De inhoud van de slotscène en de persoonlijke boodschap.
- Naam van het spel.

## 9. Volgende ontwerpfase

Werk `docs/CHALLENGES.md` uit tot alle raadsels, antwoorden, hints en teksten vastliggen. Daarna schermenlijst en teksten, dan de master-prompt.

**Geen code bouwen zolang het dossier niet af is.**
