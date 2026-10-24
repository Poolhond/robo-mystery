# ROBO MYSTERY — Beslissingen en open punten

**Versie:** 0.1  
**Doel:** één plek waar staat wat vaststaat en wat nog open is, zodat niets opnieuw wordt uitgevonden tijdens de bouw.

## Vastgelegd (24 oktober 2026)

| Onderwerp | Beslissing |
|---|---|
| Speler | Wannes (12), speelt het spel op zijn verjaardag zelf |
| Rol van de robot | Wannes bestuurt de robot; de robot is zijn instrument |
| Feest | Het feest aan het einde is voor Wannes, niet voor de robot |
| Thema | Goochelen (trucjes, puzzels, raadsels) |
| Opbouw | Vier uitdagingen, één deur, onthulling, interactieve finale |
| Interesses Wannes | Goocheltrucs, leuke puzzels, raadsels |
| Platform | Mobile-first webspel, GitHub Pages, geen account |
| Taal | Nederlands |
| Bouwmethode | Eerst het hele dossier, daarna één uitgebreide master-prompt, daarna één ronde fixes na testen op iPhone |
| Bouwer | Beginner, geen laptop, iPhone/iPad, bouwt met Codex |

## Nog open — nodig vóór de bouw

1. **Raadsels en sleutelwoord** (hoogste prioriteit): schrijf alle raadsels met antwoorden; kies het woord dat de letters vormen.
2. **Aanwijzingen**: definitieve keuze voor symbool, woord en kleur uit uitdaging 1, 2 en 3.
3. **Slotscène**: wat gebeurt er in het echt na het spel? Welke tekst past hierbij? Staat in `content.js`.
4. **Feesthandeling**: lint, feestknop of taart.
5. **Persoonlijke boodschap**: wat staat er op de slotkaart, wie "spreekt" (de figuren, de robot, de bouwer)?
6. **Spelnaam**: nu "ROBO MYSTERY" als werktitel in het dossier; er is nog geen definitieve naam.
7. **Kleurenset**: er bestaan drie verschillende sets (art direction `#F3DDA8 / #174B56`, prototype `#f4e6c7 / #2d6870`, en de eerder genoemde wens `#F2E2BD / #17485A`). Kies er één als enige bron.
8. **Lettertype**: systeemlettertypen met een zwaar, grafisch voorkeursstijl (geen externe fonts).
9. **Puntentelling**: exacte regels.
10. **Prototype `index.html`**: weggooien of als basis gebruiken? Het volgt een ander verhaal (vier plekken, kleurencode, geen deur of feest). Advies: weggooien en in de nieuwe bouw opgaan.

## Nog open — assets

- Zet alle afbeeldingsbestanden daadwerkelijk in de repository (`assets/characters/`, `assets/rooms/`, `assets/ui/`). Nu staan ze alleen in de chat of nog nergens; zonder die bestanden kan Codex ze niet gebruiken.
- Geef elk bestand een naam gelijk aan het asset-ID (bijvoorbeeld `ast-robot-01.png`).
- Maak lijsten van wat nog ontbreekt: octopus, aap, panda als losse assets; achtergrond per uitdaging; deur; feestscène; knoppen, kaders en iconen; beker en bal; doek.
- Geef per asset aan voor welke uitdaging of welk scherm het dient.

## Volgende stappen (volgorde)
1. Raadsels, sleutelwoord en aanwijzingen vastleggen (`docs/CHALLENGES.md`).
2. Slotscène en persoonlijke boodschap bepalen.
3. Schermenlijst en alle teksten uitschrijven (`content.js`-inhoud).
4. Assets uploaden en benoemen.
5. Kleurenset kiezen.
6. Master-prompt schrijven, die naar alle bestanden verwijst.
7. Bouwen, testen op iPhone, één ronde fixes.
