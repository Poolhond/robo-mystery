# ROBO MYSTERY — Beslissingen en open punten

**Versie:** 0.4  
**Doel:** één betrouwbare plek voor besluiten en open punten, zodat de inhoud niet telkens opnieuw wordt bedacht.

## Vastgelegd

| Onderwerp | Beslissing |
|---|---|
| Speler | Wannes (12), speelt het spel op zijn verjaardag zelf |
| Rol van de robot | Wannes bestuurt de robot; de robot is zijn instrument |
| Feest | De onthulling aan het einde is voor Wannes |
| Thema | Goochelen: trucjes, puzzels en raadsels |
| Opbouw | Vier hoofd uitdagingen, één grote deur, onthulling en interactieve finale |
| Platform | Mobile-first webspel, GitHub Pages, geen account |
| Taal | Nederlands |
| Bouwmethode | Eerst het volledige ontwerpdossier, daarna één master-prompt, daarna testen op iPhone en één gerichte fixronde |
| Uitdaging 1 — spelvorm | Drie eigen match-3-levels, geïnspireerd op het algemene spelprincipe van Royal Match; geen gekopieerde levels of vormgeving |\n| Uitdaging 1 — leveldoelen | Verzamel 8 rode energiecellen; verwijder 4 houten kistjes; laat de gouden energiesleutel naar de uitgang vallen |\n| Aanwijzing uit uitdaging 1 | De letters B, A en L, verdiend na elk level en samen gevormd tot het woord BAL |
| Uitdaging 2 — structuur | Drie opeenvolgende puzzels: code opent een geheim deurtje; logisch raadsel levert een sleutel; kistjesraadsel onthult de hoofdprijs |
| Uitdaging 2 — code | De voorgestelde cijfercode is 042 |
| Uitdaging 2 — sleutelraadsel | Precies één uitspraak is waar; de aap heeft de sleutel |
| Uitdaging 2 — kistjesraadsel | Precies één uitspraak is waar; het rode kistje is de juiste keuze |
| Aanwijzing uit uitdaging 2 | **Ster met een oog**, gevonden in het rode kistje; dit is de symboolaanwijzing voor uitdaging 4 |
| Gouden medaille | Niet gebruiken als inhoud van de kist; geschrapt |
| Aanwijzing uit uitdaging 3 | Signaalrood |
| Uitdaging 4 | Grote deur met symbool-, woord- en kleurschijf: ster met oog, BAL, signaalrood |
| Bouwstatus | Oude prototypecode is niet bruikbaar als basis; eerst ontwerpdossier afronden en goedkeuren |

## Nog open — ontwerp vóór de bouw

1. **Uitdaging 2 — spelersteksten:** definitieve introductie, personagedialogen, succes- en foutfeedback en afsluiting.
2. **Uitdaging 2 — hints:** exacte hintstappen voor de codepuzzel en het kistjesraadsel.
3. **Uitdaging 2 — onthulling van de ster-met-oog-aanwijzing:** kies hoe de aanwijzing in de kist verschijnt (bijvoorbeeld geheim kaartje of gegraveerd plaatje). De functie blijft hetzelfde: het symbool voor uitdaging 4.
4. **Uitdaging 1 en 3:** test de definitieve match-3-startborden en werk de bekerinteractie, teksten, oplossingen en assets verder uit.
5. **Slotscène:** bepaal wat er in het echt na het spel gebeurt en welke tekst daarbij hoort.
6. **Feesthandeling:** kies bijvoorbeeld een feestknop of lint.
7. **Persoonlijke boodschap:** bepaal de exacte verjaardagsboodschap en wie er spreekt.
8. **Spelnaam:** ROBO MYSTERY is de huidige werktitel.
9. **Kleurenset:** kies één definitieve set als enige bron. Er bestaan verschillende voorstellen in art direction en oudere prototypebestanden.
10. **Lettertype:** systeemlettertypen met een zwaar, grafisch karakter; geen externe fonts.
11. **Puntentelling:** beslis of score nodig is; voortgang mag nooit door score worden geblokkeerd.
12. **Assets:** bepaal welke referentiebeelden gebruikt worden en voeg definitieve afbeeldingsbestanden echt toe aan de repository.
13. **Dossiercontrole:** stem spelconcept, uitdagingen, techniek, art direction en assetregister op elkaar af vóór de master-prompt.

## Assets die nog moeten worden gecontroleerd of gemaakt

- Robot, aap, panda, schildpad en regenboogoctopus.
- Achtergronden per uitdaging.
- Klein metalen deurtje en groot slot/deur.
- Cijferwieltjes en OPEN-knop.
- Messing sleutel.
- Drie kistjes (rood, blauw, geel) en het BAL-aanwijzingsobject.
- Drie bekers en rood balletje.
- Doek, goochelvoorwerpen, knoppen, iconen en finale-/feestscène.

Geef assets consistente namen en leg per bestand vast voor welke scène het dient. Afbeeldingen die alleen in de chat zijn gegenereerd, staan nog niet automatisch in de repository.

## Werkvolgorde

1. Werk uitdaging 2 af in docs/CHALLENGES.md, inclusief teksten, hints en onthulling van BAL.
2. Werk de schermenlijst en spelersteksten uit, inclusief de drie match-3-levels van uitdaging 1.
3. Werk uitdaging 3, de resterende schermen en de echte finale uit.
4. Kies de definitieve art direction en controleer het assetregister.
5. Controleer het volledige dossier op tegenstrijdigheden.
6. Schrijf pas daarna de master-prompt.
7. Bouw de nieuwe game vanaf een schone basis, test op iPhone en voer één gerichte fixronde uit.

## Belangrijke afbakening

- De drie puzzels van uitdaging 2 zijn onderdelen van één hoofd uitdaging, niet drie aparte hoofd uitdagingen.
- Uitdaging 1 is een match-3-game met drie levels; de beloningen zijn achtereenvolgens B, A en L, samen BAL.
- De ster met het oog is de beloning van uitdaging 2; BAL is niet langer de beloning van uitdaging 2.
- De kist in uitdaging 2 bevat de **ster met een oog**, de symboolaanwijzing voor uitdaging 4 — geen gouden medaille. BAL komt uit uitdaging 1.
- De oude index.html-prototypecode wordt verwijderd en mag niet als basis voor de nieuwe game worden gebruikt.
- Er wordt geen nieuwe gamecode gebouwd zolang het volledige ontwerpdossier niet is goedgekeurd.
