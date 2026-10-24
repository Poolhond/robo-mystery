# ROBO MYSTERY — Spelconcept

**Versie:** 0.9  
**Status:** Ontwerpfase — geen nieuwe gamecode  
**Laatste update:** 25 oktober 2026 — vrije laboratoriumverkenning met hervatbare deelvoortgang; uitdaging 4 gebruikt automatisch symbool, zelf getypt woord en zelf gekozen kleur

## 1. Kernidee

ROBO MYSTERY is een compact digitaal mysterie-avontuur voor **Wannes (12)**, bedoeld om op zijn verjaardag zelf te spelen. Wannes bestuurt een speelgoedrobot door een vreemde, speelse wereld. Hij krijgt een geheim bericht: er is iets vreemds aan de hand in het speelgoedlab, en de robot moet het onderzoeken.

Wannes verkent vrij een speelgoedlaboratorium en kiest zelf in welke volgorde hij de eerste drie uitdagingen speelt. Hij mag elke uitdaging halverwege verlaten en later precies verdergaan waar hij stopte. De grote deur kan hij vanaf het begin ontdekken, maar hij leert gaandeweg dat hij de drie uitdagingen nodig heeft om het slot op te lossen. Uitdaging 1 bestaat uit drie match-3-levels en levert de letters B, A en L op. Wanneer die opengaat, blijkt dat de speelgoedfiguren in het geheim een verjaardagsfeest voor Wannes hebben voorbereid. De robot is het instrument waarmee Wannes zijn eigen verrassing ontdekt.

Wannes sluit af met een laatste interactieve handeling waarmee het feest begint.

## 2. Vastgelegde spelbeslissingen

- De speler is **Wannes**; hij bestuurt de robot als zijn handen en ogen.
- Het feest aan het einde is **voor Wannes**, niet voor de robot.
- Wannes speelt het spel op zijn verjaardag zelf.
- Het mysterie blijft aan het begin onduidelijk.
- Het avontuur bevat vier hoofd uitdagingen: match-3, logica, een volg-minigame en het slot. De eerste drie zijn vrij te spelen in elke volgorde.
- Het overkoepelende thema is goochelen: Wannes houdt van goocheltrucs, puzzels en raadsels.
- De andere speelgoedfiguren bereiden de verrassing voor.
- De eerste drie uitdagingen leveren samen een symbool, een woord en een kleur op. Het symbool verschijnt automatisch op het slot zodra uitdaging 2 voltooid is; Wannes typt zelf het woord BAL en kiest zelf signaalrood.
- De aanwijzingen voor het grote slot zijn: het woord BAL uit uitdaging 1, de ster met een oog uit uitdaging 2 en signaalrood uit uitdaging 3. Het symbool verschijnt automatisch; Wannes voert alleen het woord en de kleur zelf in.
- Mobile-first, bediening met één duim, geen account, gratis op GitHub Pages.
- De oude prototypecode is verwijderd; de uiteindelijke game wordt later vanaf een schone basis gebouwd.
- Nieuwe gamecode wordt pas gemaakt wanneer het ontwerpdossier is uitgewerkt en goedgekeurd.

## 3. Verhaal

### Proloog — Een geheim bericht

Wannes opent het spel en ziet een kort geheim bericht dat de robot het speelgoedlab in stuurt. De robot wordt wakker. De omgeving lijkt vertrouwd, maar er zijn vreemde details: een spoor van gekleurde knopen, snippers die op confetti lijken en een deur die gesloten blijft. Het spel geeft nog niet prijs wat het doel is.

### Uitdaging 1 — De robotfabriek

Wannes speelt drie korte match-3-levels in een retro-futuristisch speelgoedlaboratorium. Hij verzamelt rode energiecellen, breekt houten kistjes open en laat een gouden energiesleutel naar een uitgang vallen. Elk level levert één letter op: B, A en L. Samen vormen ze het woord BAL, de woordaanwijzing voor het grote slot. Zie docs/CHALLENGES.md.

### Uitdaging 2 — De drie raadselmeesters

Deze uitdaging bestaat uit drie opeenvolgende puzzels die samen één avontuur vormen:

1. Wannes kraakt de cijfercode **042** en opent een klein geheim deurtje.
2. Achter het deurtje ontmoet hij de aap, panda en schildpad. Hun uitspraken volgen de regel dat precies één uitspraak waar is. Wannes redeneert dat de aap de messing sleutel heeft.
3. Met de sleutel onderzoekt Wannes drie kistjes. Ook daar is precies één uitspraak waar; het rode kistje is de juiste keuze. De kist onthult de **ster met een oog**, de symboolaanwijzing voor het grote slot in uitdaging 4.

De kist bevat geen gouden medaille. De ster met een oog is de opbrengst van deze uitdaging. De drie puzzels zijn onderdelen van uitdaging 2, geen drie extra hoofd uitdagingen.

### Uitdaging 3 — De onmogelijke bekers

Wannes volgt een rood balletje onder drie bewegende bekers in drie rondes met opbouwende moeilijkheid: twee, drie en vier wissels. De wissels worden steeds iets sneller maar blijven volledig zichtbaar. De beloning is signaalrood, de derde aanwijzing voor het grote slot.

### Uitdaging 4 — Het slot van het geheim

Wannes kan de deur op elk moment onderzoeken. Hij ontdekt dat er drie aanwijzingen nodig zijn, maar de deur opent pas wanneer alle drie de uitdagingen voltooid zijn. De ster met een oog verschijnt automatisch op het slot na uitdaging 2. Wannes typt zelf BAL en kiest zelf signaalrood. Verkeerde invoer geeft feedback zonder straf; hij kan onbeperkt proberen.

### Finale — De deur gaat open

De deur onthult een feestlocatie die de speelgoedfiguren voor Wannes hebben klaargemaakt. De aap, panda, schildpad en regenboogoctopus zijn erbij. Ze roepen “Gefeliciteerd, Wannes!” De robot stapt opzij voor het verjaardagskind. De eerdere aanwijzingen blijken onderdelen van het geheime plan.

## 4. De interactieve feestfinale

De onthulling is niet het einde van de interactie. Wannes krijgt nog één eenvoudige, betekenisvolle handeling waarmee het feest begint. Mogelijke opties (keuze volgt):
- aan een lint trekken waarna confetti en lichtjes aangaan;
- een feestknop indrukken;
- de taart aansnijden samen met de robot.

Daarna doet de robot een kaarttruc waarvan de uitkomst altijd “Gefeliciteerd, Wannes!” is, gevolgd door een korte feestelijke slotscène. De toon verschuift van mysterie naar warmte, humor en verrassing.

### Echte slotscène (nog open)

Het laatste scherm kan een echte opdracht bevatten voor na het spel (“Draai je om”, “Ga naar de woonkamer”, …). Dit hangt af van wat Wannes in het echt wacht. De tekst moet later op één centrale plek in de game-inhoud staan zodat die eenvoudig aanpasbaar is. Zie docs/DECISIONS.md.

## 5. Personages

De speelgoedfiguren vormen samen het geheime organisatieteam. Hun rollen zijn voorlopig.

- **De robot:** instrument van Wannes; hij is de rode draad door alle scènes.
- **Schildpad:** bewaakt een aanwijzing en vraagt Wannes goed op te letten.
- **Aap:** zorgt voor humor en bewaakt de sleutel in uitdaging 2.
- **Panda:** bewaakt een patroon of raadsel.
- **Regenboogoctopus:** helpt bij de kleurrijke feestversiering.

De herkenbare vormen en kleuren van de bestaande speelgoedfiguren blijven leidend. Nieuwe personages worden niet toegevoegd zonder reden.

## 6. Verhaalregels

1. Geef vooraf niet te veel uitleg; Wannes ontdekt het verhaal door te spelen.
2. Elke uitdaging heeft een duidelijke functie in het avontuur.
3. De robot blijft de rode draad door alle scènes.
4. De uitdagingen testen verschillende vaardigheden: observeren, logisch nadenken en volgen; het slot vraagt dat Wannes zijn ontdekkingen toepast.
5. Aanwijzingen zijn vóór de finale mysterieus en achteraf logisch.
6. De speelgoedfiguren mogen verdacht gedrag vertonen, maar mogen de verrassing niet te vroeg verklappen.
7. De deur is het centrale doel dat de vier uitdagingen verbindt. Wannes kiest zelf de volgorde waarin hij het laboratorium verkent.
8. De feestfinale is interactief, maar kort en toegankelijk.
9. Teksten spreken Wannes direct aan, in het Nederlands en passend bij een twaalfjarige: speels, geen babytaal.
10. Wannes kan niet vastlopen: elke uitdaging heeft hints en geen echte game-over.
14. Voortgang wordt per deelstap bewaard. Wisselen van uitdaging of het sluiten en heropenen van de browser mag geen opgeloste puzzels, verdiende aanwijzingen of lopende puzzelstand verliezen.
11. De drie puzzels van uitdaging 2 blijven een vaste ketting: code → sleutel → kistje met de ster-met-oog-aanwijzing.
12. Uitdaging 1 bestaat uit drie match-3-levels; de letters B, A en L vormen samen de woordaanwijzing BAL.
13. Het oude prototype wordt niet gebruikt als basis voor de nieuwe game.

## 7. Spelvorm

Een compact point-and-click-avontuur: Wannes tikt op plekken en voorwerpen om de robot ernaartoe te sturen, onderzoekt interactieve elementen en speelt minigames. Geschikt voor een telefoon; de technische randvoorwaarden staan in docs/TECH-SPEC.md. Streefduur: ongeveer 8 tot 12 minuten.

## 8. Nog te beslissen

- De exacte spelersteksten, feedback en hintniveaus van de uitdagingen.
- De exacte vormgeving van het slot en de kleurstalen; de werking ligt vast: symbool automatisch, woord zelf typen, kleur zelf kiezen.
- De definitieve rollen van de speelgoedfiguren buiten uitdaging 2.
- Welke interactieve handeling het feest start.
- Of er een echte opdracht aan het einde komt, en welke.
- De inhoud van de persoonlijke boodschap.
- Definitieve spelnaam, kleurenset en assets.

## 9. Volgende ontwerpfase

Werk het volledige dossier verder uit: spelersteksten, hints, schermenlijst, assets en finale. Controleer daarna alle documenten op tegenstrijdigheden. Pas als het dossier compleet en goedgekeurd is, wordt de master-prompt geschreven.

**Geen nieuwe gamecode bouwen zolang het dossier niet af is.**
