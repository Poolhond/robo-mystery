# De mysterieuze fabriek — Beslissingen en open punten

**Versie:** 1.0  
**Doel:** één betrouwbare plek voor besluiten en open punten, zodat de inhoud niet telkens opnieuw wordt bedacht.

## Vastgelegd

| Onderwerp | Beslissing |
|---|---|
| Spelnaam | De mysterieuze fabriek (gekozen als nieuwe werktitel; robot is geschrapt) |
| Speler | Wannes (12), speelt het spel op zijn verjaardag zelf |
| Hoofdpersonage | Wannes onderzoekt de ruimte zelf; er is geen bestuurbaar hoofdpersonage |
| Feest | De onthulling aan het einde is voor Wannes |
| Thema | Een mysterieuze speelgoedfabriek met goocheltrucs, puzzels en raadsels |
| Opbouw | Vrije verkenning van het laboratorium; uitdagingen 1–3 in zelfgekozen volgorde; uitdaging 4 is de grote deur en het slot |
| Platform | Mobile-first webspel, GitHub Pages, geen account |
| Taal | Nederlands |
| Bouwmethode | Eerst het volledige ontwerpdossier afronden en goedkeuren, daarna één master-prompt, bouwen en testen op iPhone |
| Uitleg aan de speler | Minimale uitleg: korte mysterieuze introductie; Wannes ontdekt bediening en doelen grotendeels zelf. |
| Hintsysteem | Combinatie: een discrete hintknop én een automatische hint na meerdere mislukte pogingen. Hints verschijnen in drie stappen, van subtiele aanwijzing tot duidelijkere hulp. Geen game-over en onbeperkt opnieuw proberen. |
| Uitdaging 1 — spelvorm | Drie eigen match-3-levels, geïnspireerd op het algemene spelprincipe van match-3-games; geen gekopieerde levels of vormgeving |
| Uitdaging 1 — leveldoelen | Verzamel 8 rode energiecellen; verwijder 4 houten kistjes; laat de gouden energiesleutel naar de uitgang vallen |
| Aanwijzing uit uitdaging 1 | De letters B, A en L, verdiend na elk level en samen gevormd tot het woord BAL |
| Uitdaging 2 — structuur | Drie opeenvolgende deelpuzzels: code opent een geheim deurtje; logisch raadsel levert een messing sleutel; kistjesraadsel onthult de ster-met-oog-aanwijzing |
| Uitdaging 2 — code | De cijfercode is 042 |
| Uitdaging 2 — sleutelraadsel | Precies één uitspraak is waar; de aap heeft de sleutel |
| Uitdaging 2 — kistjesraadsel | Precies één uitspraak is waar; het rode kistje is de juiste keuze |
| Aanwijzing uit uitdaging 2 | Ster met een oog, gevonden in het rode kistje; het symbool verschijnt automatisch op het slot van uitdaging 4 |
| Gouden medaille | Geschrapt; niet gebruiken als beloning of inhoud van het kistje |
| Aanwijzing uit uitdaging 3 | Signaalrood |
| Uitdaging 3 — moeilijkheid | Drie rondes met respectievelijk twee, drie en vier wissels; snelheid neemt geleidelijk toe maar de beweging blijft eerlijk te volgen |
| Uitdaging 4 — bediening | De ster met oog verschijnt automatisch na uitdaging 2; Wannes typt zelf het woord en kiest zelf een kleur; grote knop OPEN DE DEUR |
| Uitdaging 4 — oplossing | Ster met oog (uitdaging 2), woord BAL (uitdaging 1), kleur signaalrood (uitdaging 3); onbeperkte pogingen |
| Startscherm en wereld | De maquette is uitsluitend het startscherm. Na Start onderzoekt Wannes zelf de technische ruimte. |
| Technische ruimte | Een compacte controlekamer, met de vier interactieve voorwerpen duidelijk gegroepeerd en weinig decoratie. Bedientableaus, meetinstrumenten en metalen lockers geven karakter; de volledige ruimte is tegelijk zichtbaar op het iPhone-scherm. De voorwerpen zijn geïntegreerd in de illustratie, zonder permanente extra pictogrammen of omlijningen. Bij aantikken zoomt het spel in op het gekozen voorwerp en opent een eigen, volledig scherm voor de uitdaging. Een duidelijke terugknop brengt Wannes terug naar dezelfde controlekamer. |
| Voorwerpen in de technische ruimte | Computerscherm = uitdaging 1; locker met cijfercode = uitdaging 2; tafel met bekers = uitdaging 3; grote deur = uitdaging 4. |
| Vrije verkenning | Wannes kiest zelf de volgorde van uitdagingen 1, 2 en 3. Hij kan uitdaging 4 vanaf het begin ontdekken, maar de deur opent pas als alle drie voltooid zijn en woord/kleur juist zijn |
| Tussentijdse voortgang | Elke uitdaging kan worden onderbroken en hervat vanaf de exacte deelstap; opgeloste puzzels, bordstanden, relevante rondevoortgang, beloningen en slotinvoer blijven bewaard. De terugknop brengt Wannes terug naar de controlekamer. |
| Opslaan | Lokale voortgang wordt na elke betekenisvolle actie opgeslagen; herladen of later terugkomen mag geen voortgang wissen |
| Bouwstatus | Oude prototypecode is niet bruikbaar als basis; er wordt geen gamecode gebouwd vóór goedkeuring van het volledige dossier |

## Nog open — ontwerp vóór de bouw

1. **Vrije laboratoriumverkenning:** de centrale ruimte en de vier voorwerpen liggen vast. Werk nog de exacte compositie, plaatsing en klikzones uit.
2. **Uitdaging 2 — spelersteksten:** definitieve introductie, personagedialogen, succes- en foutfeedback en afsluiting.
3. **Uitdaging 2 — hints:** exacte hintstappen voor de codepuzzel en het kistjesraadsel.
4. **Uitdaging 2 — onthulling van de ster-met-oog-aanwijzing:** kies hoe de aanwijzing in de kist verschijnt (bijvoorbeeld geheim kaartje of gegraveerd plaatje). De functie blijft hetzelfde: het symbool voor uitdaging 4.
5. **Uitdaging 1 en 3:** test de definitieve match-3-startborden en bekersnelheden op iPhone; werk teksten, oplossingen en assets verder uit.
6. **Slotscène:** bepaal wat er in het echt na het spel gebeurt en welke tekst daarbij hoort.
7. **Feesthandeling:** kies bijvoorbeeld een feestknop of lint.
8. **Persoonlijke boodschap:** bepaal de exacte verjaardagsboodschap en wie er spreekt.
9. **Spelnaam:** De mysterieuze fabriek is de gekozen werktitel. De definitieve titelvormgeving kan later nog worden uitgewerkt.
10. **Kleurenset:** definitief gekozen palet (zie Art Direction): oud papier `#F3DDA8`, signaalrood `#D94330`, mosterdgeel `#E9B638`, donker petrol `#174B56`, bosgroen `#28513D`, inktzwart `#292A24`.
11. **Lettertype:** systeemlettertypen met een zwaar, grafisch karakter; geen externe fonts.
12. **Puntentelling:** beslis of score nodig is; voortgang mag nooit door score worden geblokkeerd.
13. **Assets:** bepaal welke referentiebeelden gebruikt worden en voeg definitieve afbeeldingsbestanden echt toe aan de repository.
14. **Dossiercontrole:** stem spelconcept, uitdagingen, techniek, art direction en assetregister op elkaar af vóór de master-prompt.

## Assets die nog moeten worden gecontroleerd of gemaakt

- Aap, panda, schildpad en regenboogoctopus.
- Achtergronden per uitdaging.
- Klein metalen deurtje en groot slot/deur.
- Cijferwieltjes en OPEN-knop.
- Messing sleutel.
- Drie kistjes (rood, blauw, geel) en de ster-met-oog-aanwijzing in het rode kistje.
- Drie bekers en rood balletje.
- Doek, goochelvoorwerpen, knoppen, iconen en finale-/feestscène.

Geef assets consistente namen en leg per bestand vast voor welke scène het dient. Afbeeldingen die alleen in de chat zijn gegenereerd, staan nog niet automatisch in de repository.

## Werkvolgorde

1. Werk de technische ruimte verder uit: exacte compositie, plaatsing en klikzones van de vier voorwerpen.
2. Werk de resterende spelersteksten, hints, schermtoestanden en finale af.
3. Controleer en voeg de definitieve assets toe; stem het assetregister af op het spelconcept.
4. Controleer het volledige dossier op tegenstrijdigheden.
5. Schrijf pas daarna de master-prompt.
6. Bouw de nieuwe game vanaf een schone basis, test op iPhone en voer één gerichte fixronde uit.

## Belangrijke afbakening

- De drie puzzels van uitdaging 2 zijn onderdelen van één hoofd uitdaging, niet drie aparte hoofd uitdagingen.
- Wannes kiest zelf de volgorde van uitdagingen 1, 2 en 3; het laboratorium is vrij te verkennen.
- Wannes mag midden in een uitdaging stoppen en naar een andere gaan. Elke uitdaging hervat op de precieze plek waar hij gebleven was, ook na het sluiten en opnieuw openen van het spel.
- Uitdaging 4 is vanaf het begin te ontdekken maar pas op te lossen na voltooiing van alle drie de andere uitdagingen.
- Bij uitdaging 4 verschijnt de ster met het oog automatisch na uitdaging 2. Wannes typt zelf BAL en kiest zelf signaalrood.
- Uitdaging 1 is een match-3-game met drie levels; de beloningen zijn achtereenvolgens B, A en L, samen BAL.
- De ster met het oog is de beloning van uitdaging 2; BAL is niet langer de beloning van uitdaging 2.
- De kist in uitdaging 2 bevat de **ster met een oog**, de symboolaanwijzing voor uitdaging 4 — geen gouden medaille. BAL komt uit uitdaging 1.
- De oude index.html-prototypecode wordt verwijderd en mag niet als basis voor de nieuwe game worden gebruikt.
- Er is geen robotpersonage; de oude robotasset is vervallen en mag niet in de game worden gebruikt.
- Er wordt geen nieuwe gamecode gebouwd zolang het volledige ontwerpdossier niet is goedgekeurd.
