# ROBO MYSTERY — Beslissingen en open punten

**Versie:** 0.2  
**Doel:** één plek waar staat wat vastligt en wat nog open is, zodat er tijdens het ontwerp en de latere bouw niets opnieuw wordt uitgevonden.

## Vastgelegd (24 oktober 2026)

| Onderwerp | Beslissing |
|---|---|
| Speler | Wannes (12), speelt het spel op zijn verjaardag zelf |
| Rol van de robot | Wannes bestuurt de robot; de robot is zijn instrument |
| Feest | Het feest aan het einde is voor Wannes, niet voor de robot |
| Thema | Goochelen: trucjes, puzzels en raadsels |
| Opbouw | Vier hoofd uitdagingen, één deur, onthulling en interactieve finale |
| Interesses Wannes | Goocheltrucs, leuke puzzels en raadsels |
| Platform | Mobile-first webspel, GitHub Pages, geen account |
| Taal | Nederlands |
| Bouwmethode | Eerst het hele dossier, daarna één uitgebreide master-prompt, daarna één testronde en fixes op iPhone |
| Bouwer | Beginner, geen laptop, iPhone/iPad, bouwt met Codex |
| Aanwijzing uit uitdaging 1 | Voorlopig: ster met een oog |
| Aanwijzing uit uitdaging 2 | Het geheime woord **BAL** |
| Aanwijzing uit uitdaging 3 | De kleur **signaalrood** |
| Uitdaging 2 — structuur | Drie opeenvolgende onderdelen: cijfercode opent een klein deurtje; drie raadselmeesters geven elk een letter; de letters vormen BAL |
| Code voor het kleine deurtje | 042 is een werkvoorstel en moet nog worden gevalideerd; het is niet de code voor de grote deur |
| Grote deur | Combineert symbool, woord en kleur uit uitdagingen 1–3 |
| Bouwstatus | Geen gamecode bouwen of aanpassen tot het volledige ontwerpdossier is uitgewerkt en goedgekeurd |

## Nog open — inhoud vóór de bouw

1. **Uitdaging 2 — definitieve raadsels:** schrijf drie ondubbelzinnige raadsels die in volgorde de letters B, A en L opleveren. Elk raadsel moet één eerlijk en duidelijk antwoord hebben.
2. **Uitdaging 2 — cijfercode:** controleer of de volledige cijferpuzzel voor code 042 logisch sluitend is. Als de aanwijzingen niet één unieke oplossing opleveren, herontwerp de puzzel of kies een andere code.
3. **Uitdaging 2 — teksten en hints:** schrijf de introductie, figuurdialogen, foutfeedback, hintniveaus en afsluiting.
4. **Slotscène:** bepaal wat er in het echt na het spel gebeurt en welke tekst daarbij hoort. Bewaar de tekst later op één centrale plek in de game-inhoud.
5. **Feesthandeling:** kies bijvoorbeeld een feestknop of lint.
6. **Persoonlijke boodschap:** bepaal de exacte verjaardagsboodschap en wie er spreekt.
7. **Spelnaam:** ROBO MYSTERY is voorlopig de werktitel.
8. **Kleurenset:** kies één definitieve set als enige bron. Er zijn verschillende voorstellen in omloop: art direction `#F3DDA8 / #174B56`, prototype `#f4e6c7 / #2d6870`, en eerder genoemd `#F2E2BD / #17485A`.
9. **Lettertype:** systeemlettertypen met een zwaar, grafisch karakter; geen externe fonts.
10. **Puntentelling:** beslis of score überhaupt nodig is en leg anders de regels vast. De score mag de voortgang nooit blokkeren.
11. **Prototype `index.html`:** nog beslissen wat ermee gebeurt. Het is oud, volgt een ander verhaal (vier plekken, kleurencode, geen centrale deur of verjaardagsfeest) en is niet de goedgekeurde basis voor de uiteindelijke game.

## Nog open — assets

- Zet afbeeldingsbestanden daadwerkelijk in de repository onder bijvoorbeeld `assets/characters/`, `assets/rooms/` en `assets/ui/`. Afbeeldingen die alleen in de chat zijn gegenereerd, zijn nog geen repositorybestanden.
- Geef elk bestand een naam die overeenkomt met het asset-ID, bijvoorbeeld `ast-robot-01.png`.
- Maak een complete lijst van ontbrekende assets: robot, aap, panda, schildpad, regenboogoctopus, achtergronden per uitdaging, kleine deur, grote deur, feestscène, knoppen, bekers, bal, doek en iconen.
- Noteer per asset voor welke uitdaging of welk scherm het dient.

## Volgende stappen — werkvolgorde

1. Maak uitdaging 2 inhoudelijk definitief in `docs/CHALLENGES.md): eerst de drie raadsels voor B-A-L, daarna de cijfercodepuzzel en alle teksten/hints.
2. Werk de schermenlijst en alle spelersteksten uit.
3. Bepaal de finale en de echte slotscène.
4. Controleer de art direction en kies één definitief kleurenpalet.
5. Werk het assetregister bij en voeg de gekozen bestanden daadwerkelijk toe.
6. Controleer het hele dossier op tegenstrijdigheden.
7. Schrijf pas daarna de master-prompt voor de bouw.
8. Bouw, test op iPhone en voer één gerichte fixronde uit.

## Belangrijke afbakening

- De drie raadsels binnen uitdaging 2 zijn **geen drie extra hoofd uitdagingen**.
- Het woord **BAL** is de aanwijzing die uitdaging 2 oplevert voor het grote slot in uitdaging 4.
- Voeg geen sleutel-en-kistjespuzzel of andere extra beloning toe die het afgesproken ontwerp verandert, tenzij Michel dat expliciet opnieuw kiest.
- De bestaande `index.html` blijft voorlopig alleen referentie; niet gebruiken als goedgekeurde basis.
- Geen gamecode bouwen zolang het ontwerpdossier niet volledig is uitgewerkt en goedgekeurd.
