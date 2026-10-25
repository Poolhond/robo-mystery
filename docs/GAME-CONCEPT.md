# De mysterieuze fabriek — Spelconcept

**Versie:** 2.2  
**Status:** Voorontwerp; nog geen bouwklaar dossier en geen nieuwe gamecode  
**Laatste update:** 25 oktober 2026 — startbeleving vastgelegd als vrije ontdekking; werktitel gewijzigd naar De mysterieuze fabriek; robot geschrapt

## 1. Kernidee

De mysterieuze fabriek is een compact digitaal mysterie-avontuur voor **Wannes (12)**, bedoeld om op zijn verjaardag zelf te spelen. Wannes ontdekt zelf een vreemde, speelse speelgoedwereld. Na Start ziet hij meteen de volledige technische werkplaats en kiest hij zelf wat hij onderzoekt. Er is iets vreemds aan de hand en hij moet zelf ontdekken wat er achter de gesloten deur verborgen zit.

Wannes ziet eerst de volledige maquette als startscherm. Na Start onderzoekt Wannes zelf de technische ruimte. De volledige ruimte blijft tegelijk zichtbaar op het iPhone-scherm: het computerscherm voor uitdaging 1, de locker met cijfercode voor uitdaging 2, de tafel met bekers voor uitdaging 3 en de grote deur voor uitdaging 4. Wannes tikt op een voorwerp; het spel zoomt in en opent een apart volledig scherm voor de bijbehorende interactie. Hij kiest zelf in welke volgorde hij de eerste drie uitdagingen speelt. Hij mag elke uitdaging halverwege verlaten en later precies verdergaan waar hij stopte. De grote deur kan hij vanaf het begin ontdekken, maar hij leert gaandeweg dat hij de drie uitdagingen nodig heeft om het slot op te lossen. Uitdaging 1 bestaat uit drie match-3-levels en levert de letters B, A en L op. Wanneer die opengaat, blijkt dat de speelgoedfiguren in het geheim een verjaardagsfeest voor Wannes hebben voorbereid. Wannes ontdekt de verrassing zelf door de aanwijzingen te verzamelen en het slot te openen.

Na de deuropening drukt Wannes op de grote rode feestknop. Dat is de laatste interactieve handeling van het spel; daarna speelt de finale automatisch af.

## 2. Vastgelegde spelbeslissingen

- De werktitel is **De mysterieuze fabriek**; de definitieve grafische titeluitwerking volgt later.
- Visuele richting van de fabriek: een speelse technische ruimte/werkplaats met vier verspreid geplaatste, maar tegelijk zichtbare interactieve hoofdvoorwerpen. Bedieningspanelen, meetinstrumenten, kabels en metalen lockers geven karakter zonder de ruimte rommelig te maken. Alle vier de voorwerpen blijven tegelijk zichtbaar en herkenbaar op het iPhone-scherm; de sfeer is mysterieus maar niet griezelig.
- Interactie: aantikken zoomt in op het gekozen voorwerp en opent een apart volledig scherm voor de uitdaging. Een duidelijke terugknop brengt Wannes terug naar dezelfde technische ruimte.
- De speler is **Wannes**; hij onderzoekt de ruimte zelf en bedient de voorwerpen rechtstreeks.
- Startbeleving: vrije ontdekking. Na Start ziet Wannes de volledige werkplaats en kiest zelf welk voorwerp hij onderzoekt; er is geen verplichte introductiescène of vooraf opgelegde route. Uitleg blijft minimaal en verschijnt alleen waar die bij een voorwerp of uitdaging nodig is. Hints zijn beschikbaar wanneer hij vastloopt.
- Het feest aan het einde is voor Wannes.
- Wannes speelt het spel op zijn verjaardag zelf.
- Het mysterie blijft aan het begin onduidelijk; de speler ontdekt de ruimte zonder verplichte proloog.
- Het avontuur bevat vier hoofduitdagingen: match-3, logica, een volg-minigame en het slot. De eerste drie zijn vrij te spelen in elke volgorde.
- Het overkoepelende thema is goochelen: Wannes houdt van goocheltrucs, puzzels en raadsels.
- De andere speelgoedfiguren bereiden de verrassing voor.
- De eerste drie uitdagingen leveren samen een symbool, een woord en een kleur op. Het symbool verschijnt automatisch op het slot zodra uitdaging 2 voltooid is; Wannes typt zelf het woord BAL en kiest zelf signaalrood.
- De aanwijzingen voor het grote slot zijn: het woord BAL uit uitdaging 1, de ster met een oog uit uitdaging 2 en signaalrood uit uitdaging 3. Het symbool verschijnt automatisch; Wannes voert alleen het woord en de kleur zelf in.
- Mobile-first, bediening met één duim, geen account, gratis op GitHub Pages.
- De oude prototypecode is verwijderd; de uiteindelijke game wordt later vanaf een schone basis gebouwd.
- Nieuwe gamecode wordt pas gemaakt wanneer het ontwerpdossier is uitgewerkt en goedgekeurd.

## 3. Verhaal

### Start — De werkplaats ontdekken

Na het beginscherm komt Wannes rechtstreeks in de volledige technische werkplaats terecht. Er is geen verplichte proloog of geheim bericht dat hem eerst een route oplegt. De ruimte zelf wekt nieuwsgierigheid: vreemde details, aanwijzingen in de omgeving en een deur die gesloten blijft. Wannes kiest zelf welk voorwerp hij als eerste onderzoekt. Korte uitleg verschijnt pas wanneer die nodig is bij een gekozen voorwerp of uitdaging.

### Uitdaging 1 — De speelgoedfabriek

Wannes speelt drie korte match-3-levels in een retro-futuristisch speelgoedlaboratorium. Hij verzamelt rode energiecellen, breekt houten kistjes open en laat een gouden energiesleutel naar een uitgang vallen. Elk level levert één letter op: B, A en L. Samen vormen ze het woord BAL, de woordaanwijzing voor het grote slot. Zie docs/CHALLENGES.md.

### Uitdaging 2 — De drie raadselmeesters

Deze uitdaging bestaat uit drie opeenvolgende puzzels die samen één avontuur vormen:

1. Wannes kraakt de cijfercode **042** en opent een klein geheim deurtje.
2. Achter het deurtje ontmoet hij Charlie de aap, RidderUs en Schildje de schildpad. Hun uitspraken volgen de regel dat precies één uitspraak waar is. Wannes redeneert dat Charlie de messing sleutel heeft. De panda hoort niet bij dit raadsel; die piept alleen even uit een lade als optionele easter egg en verschijnt later op het verjaardagsfeest.
3. Met de sleutel onderzoekt Wannes drie kistjes. Ook daar is precies één uitspraak waar; het rode kistje is de juiste keuze. De kist onthult de **ster met een oog**, de symboolaanwijzing voor het grote slot in uitdaging 4.

De kist bevat geen gouden medaille. De ster met een oog is de opbrengst van deze uitdaging. De drie puzzels zijn onderdelen van uitdaging 2, geen drie extra hoofd uitdagingen.

### Uitdaging 3 — De onmogelijke bekers

Wannes volgt een rood balletje onder drie bewegende bekers in drie rondes met opbouwende moeilijkheid: twee, drie en vier wissels. De wissels worden steeds iets sneller maar blijven volledig zichtbaar. De beloning is signaalrood, de derde aanwijzing voor het grote slot.

### Uitdaging 4 — Het slot van het geheim

Wannes kan de deur op elk moment onderzoeken. Als hij erop tikt, schuift/zoomt het beeld naar de deur zodat die centraal staat. Vanaf de eerste keer toont het slot visueel drie benodigde onderdelen — symbool, woord en kleur — zodat duidelijk is dat er drie dingen nodig zijn om de deur te openen. De uitleg is zo veel mogelijk visueel en bevat zo weinig mogelijk tekst. De ster met een oog verschijnt automatisch op het slot na uitdaging 2. Wannes typt zelf BAL en kiest zelf signaalrood. Verkeerde invoer geeft korte, liefst visuele feedback zonder straf; hij kan onbeperkt proberen.

### Finale — De deur gaat open

De deur onthult een feestlocatie die de speelgoedfiguren voor Wannes hebben klaargemaakt. De aap, panda, schildpad en regenboogoctopus zijn erbij. De onthulling wordt volledig visueel verteld; er is geen gesproken tekst of geluid. De feestzaal blijft eerst donker tot Wannes op de grote rode feestknop drukt. De eerdere aanwijzingen blijken onderdelen van het geheime plan.

## 4. De interactieve feestfinale

De deur zwaait open en onthult een verborgen verjaardagsfeest met de speelgoedfiguren, slingers, confetti en warm licht. De feestzaal is bij het openen eerst donker en stil. Wannes drukt vervolgens op de grote rode feestknop; de lichtjes springen aan en confetti barst los. Daarna wordt de scène rustiger en verschijnt de boodschap geleidelijk in twee stappen: eerst **“Proficiat Wannes!”**, daarna **“Dat verdient een cadeau.”** De speelgoedfiguren en de feestscène blijven zichtbaar.

De feestknop is de laatste interactieve handeling. Er is geen extra tik nodig om de boodschap te tonen, geen kaarttruc als extra interactie, geen geluid en geen aanvullende opdracht of raadsel om naar het echte cadeau te leiden.

## 5. Personages

De speelgoedfiguren vormen samen het geheime organisatieteam. Hun rollen zijn voorlopig.

- **Schildpad:** bewaakt een aanwijzing en vraagt Wannes goed op te letten.
- **Aap:** zorgt voor humor en bewaakt de sleutel in uitdaging 2.
- **Panda:** hoort niet bij het sleutelraadsel; hij verschijnt alleen als optionele easter egg uit de lade en later op het verjaardagsfeest.
- **Regenboogoctopus:** helpt bij de kleurrijke feestversiering.

De herkenbare vormen en kleuren van de bestaande speelgoedfiguren blijven leidend. Nieuwe personages worden niet toegevoegd zonder reden.

### Drie optionele easter eggs in de werkplaats

Deze kleine interacties zijn verborgen details in de omgeving. Ze zijn niet nodig om de hoofd uitdagingen op te lossen.

1. **Pandaschuif:** als Wannes op een schuif/lade van het meubel tikt, gaat die open en verschijnt kort een vierde speelgoedfiguur: een panda. De schuif sluit daarna vanzelf. De panda-illustratie is toegevoegd als `assets/characters/panda/AST-PANDA-01-panda-screenprint.png`; controleer de visuele overeenkomst vóór gebruik.
2. **Vleesetende plant:** de eerste tik zoomt in op de plant en laat een vlieg rondvliegen. Bij de tweede tik vliegt de vlieg in de bloem en klapt het klepje dicht. Bij de derde tik zoomt het beeld terug uit naar de werkplaats.
3. **Hartkunstwerk:** bij aantikken zoomt het beeld in op het kunstwerk. Het hart begint te kloppen en de afgebeelde mensen dansen; daarna zoomt het beeld terug uit.

De interacties moeten kort, duidelijk en herhaalbaar zijn. Ze mogen de hoofdvoortgang niet wijzigen of blokkeren. Zie `docs/DECISIONS.md` voor de goedgekeurde beslissing.

## 6. Verhaalregels

1. Geef vooraf niet te veel uitleg; Wannes ontdekt het verhaal door te spelen. Instructies blijven kort en hints zijn beschikbaar wanneer hij vastloopt.
2. Elke uitdaging heeft een duidelijke functie in het avontuur.
3. De aanwijzingen en de gesloten deur vormen de rode draad door alle scènes.
4. De uitdagingen testen verschillende vaardigheden: matchen en plannen, logisch nadenken en goed observeren; het slot vraagt dat Wannes zijn ontdekkingen toepast.
5. Aanwijzingen zijn vóór de finale mysterieus en achteraf logisch.
6. De speelgoedfiguren mogen verdacht gedrag vertonen, maar mogen de verrassing niet te vroeg verklappen.
7. De deur is het centrale doel dat de vier uitdagingen verbindt. Wannes kiest zelf de volgorde waarin hij de eerste drie uitdagingen verkent.
8. De feestfinale is interactief, maar kort en toegankelijk.
9. Teksten spreken Wannes direct aan, in het Nederlands en passend bij een twaalfjarige: speels, geen babytaal.
10. Wannes kan niet vastlopen: elke uitdaging heeft hints en geen echte game-over.
11. De drie deelpuzzels van uitdaging 2 blijven een vaste ketting: code → sleutel → kistje met de ster-met-oog-aanwijzing.
12. Uitdaging 1 bestaat uit drie match-3-levels; de letters B, A en L vormen samen de woordaanwijzing BAL.
13. Voortgang wordt per deelstap bewaard. Wisselen van uitdaging of het sluiten en opnieuw openen van de browser mag geen opgeloste puzzels, verdiende aanwijzingen of lopende puzzelstand verliezen.
14. Het oude prototype wordt niet gebruikt als basis voor de nieuwe game.

## 7. Spelvorm

Een compact point-and-click-avontuur: de maquette is uitsluitend het startscherm. Na Start onderzoekt Wannes de technische ruimte van het speelgoedlaboratorium. De volledige ruimte en vier interactieve voorwerpen blijven tegelijk zichtbaar; Wannes tikt op een voorwerp om de bijbehorende interactie te openen. Geschikt voor een telefoon; de technische randvoorwaarden staan in docs/TECH-SPEC.md. Streefduur: ongeveer 10 tot 15 minuten, inclusief vrije verkenning, de drie uitdagingen en de finale. Dit is een richtwaarde en geen tijdslimiet.

## 8. Nog uit te werken vóór de bouw

- De spelersteksten, feedback en hints staan uitgewerkt in `docs/SCREEN-SPEC.md` en `docs/CHALLENGES.md`; controleer ze bij de eindcontrole op concrete tegenstrijdigheden. Hints verschijnen uitsluitend wanneer Wannes zelf op `?` drukt; de voortgang wordt per puzzelscherm onthouden.
- De exacte plaatsing en raakvlakken van de vier hoofdvoorwerpen en de drie reeds gekozen easter eggs.
- De exacte visuele vorm waarin de ster-met-oog-aanwijzing in het rode kistje verschijnt.
- De technische testbaarheid van de match-3-startborden en de bekersnelheden op iPhone.
- De aanvullende spelassets die tijdens de bouw nodig blijken; de aanwezige referentiebeelden en mappenstructuur zijn gecontroleerd.
- De resterende schermenlijst en de precieze rollen van de speelgoedfiguren buiten de vastgelegde puzzel- en finalehandelingen.

De slotwerking, feestknop, finalevolgorde, boodschap, speelduur, kleurpalet en typografische richting zijn al vastgelegd en mogen niet opnieuw als open ontwerpkeuzes worden behandeld.

## 9. Volgende ontwerpfase

Werk eerst de open punten uit deze lijst af. Controleer daarna `CHALLENGES.md`, `TECH-SPEC.md`, `ART-DIRECTION.md` en `ASSET-REGISTER.md` op tegenstrijdigheden met de goedgekeurde beslissingen. Pas als het volledige dossier consistent en goedgekeurd is, wordt de master-prompt geschreven.

**Geen nieuwe gamecode bouwen zolang het dossier niet af is.**
