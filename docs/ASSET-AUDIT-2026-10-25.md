# Assetaudit — 25 oktober 2026

## Samenvatting

De negen afbeeldingsbestanden zijn door de eigenaar in de repository geüpload, maar staan momenteel allemaal in de repository-root. Er zijn nog geen `assets/`-mappen aanwezig. De bestanden hebben een verwarrende dubbele extensie: bijvoorbeeld `.jpg.PNG` of `.png.PNG`. GitHub rapporteert de bestanden als blobs van ongeveer 2,7–3,6 MB, en de laatste extensie lijkt `.PNG`; de oorspronkelijke afbeeldingsbytes zijn via de huidige connector niet beschikbaar om veilig opnieuw in te schrijven/om te zetten.

**Geen afbeeldingen zijn in deze audit verplaatst, hernoemd of verwijderd.** De correcte paden hieronder zijn het doelplan. Verplaats/rename de bestaande bestanden in GitHub UI, GitHub Desktop, of lokaal met Git, en verifieer daarna de assetregisterlinks.

## Bestaande uploads en doelpaden

| Huidige root-bestandsnaam | Gewenst repositorypad | Opmerking |
|---|---|---|
| `AST-CHARLIE-01-charlie-screenprint.jpg.PNG` | `assets/characters/charlie/AST-CHARLIE-01-charlie-screenprint.png` | PNG-afbeelding volgens de huidige naam; behoud extensie na verificatie van het echte bestandstype |
| `AST-RIDDERUS-01-ridderus-screenprint.jpg.PNG` | `assets/characters/ridderus/AST-RIDDERUS-01-ridderus-screenprint.png` | PNG-afbeelding volgens de huidige naam; controleer echt bestandstype |
| `AST-SCHILDJE-01-schildje-screenprint.jpg.PNG` | `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` | PNG-afbeelding volgens de huidige naam; controleer echt bestandstype |
| `AST-TITLE-01-title-poster.jpg.PNG` | `assets/title-screen/AST-TITLE-01-title-poster.png` | Statische poster; animatie komt later in afzonderlijke web-lagen |
| `AST-ROOM-01-control-room-reference.png.PNG` | `assets/rooms/control-room/AST-ROOM-01-control-room-reference.png` | Goedgekeurde compositie-/sfeerreferentie, geen definitieve speelbare UI |
| `AST-DECOR-01-red-heart.png.PNG` | `assets/decor/AST-DECOR-01-red-heart.png` | Decorasset |
| `AST-DECOR-02-birdhouse.png.PNG` | `assets/decor/AST-DECOR-02-birdhouse.png` | Decorasset |
| `AST-DECOR-03-mechanical-bird.png.PNG` | `assets/decor/AST-DECOR-03-mechanical-bird.png` | Decorasset; Michel twijfelde aan gebruik van mechanische vogel in kamerconcept, dus niet automatisch plaatsen in uiteindelijke kamer |
| `AST-DECOR-04-pitcher-terrarium.png.PNG` | `assets/decor/AST-DECOR-04-pitcher-terrarium.png` | Decorasset |

## Status van de repository

- De repo bevat het ontwerpdossier en negen geüploade afbeeldingsbestanden.
- Er is nog geen `index.html`, `style.css` of spelcode in de root aangetroffen. Dat is consistent met de vastgelegde afspraak: eerst het dossier en de assets, daarna pas de bouw.
- `README.md` is verouderd qua mappenstructuur: de beschreven `assets/characters`, `assets/rooms`, `assets/ui` bestaan nog niet.
- `docs/ASSET-REGISTER.md` was verouderd en zei nog dat de bestanden niet waren geüpload; deze audit moet als aanvullende actuele status worden gelezen totdat het register wordt opgeschoond.
- Er zijn inhoudelijke inconsistenties tussen enkele documenten: de repo heet ROBO MYSTERY terwijl de werktitel nu De mysterieuze fabriek is; oudere referenties/asset-ID's staan nog in het register; sommige bestanden heten alsof ze JPEG zijn maar eindigen op PNG.
- De illustratie van de controlekamer is een rijk conceptbeeld. Voor een bruikbare mobiele game moet de latere implementatie de vier hoofdinteracties apart aanklikbaar maken: terminal, locker (code pas zichtbaar nadat de speler de code heeft ontcijferd), bekertafel en prominente rode deur. De volledige illustratie alleen is geen werkende interface.

## Aanbevolen opruimvolgorde

1. Maak de mapstructuur in de repo: `assets/characters/charlie`, `assets/characters/ridderus`, `assets/characters/schildje`, `assets/title-screen`, `assets/rooms/control-room`, `assets/decor`.
2. Verplaats de negen bestaande afbeeldingen naar de doelpaden en hernoem de extensies enkel na controle van het echte bestandstype. Gebruik GitHub web-interface via Move file of een lokale Git-client zodat de binaire bytes exact behouden blijven.
3. Werk daarna `docs/ASSET-REGISTER.md` bij met relatieve links naar de werkelijk aanwezige bestanden en verwijder verouderde statussen.
4. Werk `README.md` en `docs/TECH-SPEC.md` bij naar dezelfde mapstructuur en consistente terminologie.
5. Maak nog geen gamecode totdat de interacties, interface-overlays, beeldkaders voor iPhone 9:19,5 en assetgebruik zijn vastgelegd.

## Belangrijke inhoudelijke feedback

- **Goede basis:** de palette- en zeefdrukrichting is consistent in de recente assets, en namen/ID's geven al een begrijpelijke ordening.
- **Belangrijkste risico:** de bestanden zijn groot (2,7–3,6 MB elk). Negen beelden zitten samen rond 28 MB. Voor een snel ladende mobiele webapp loont het om later de bestanden te optimaliseren en afmetingen passend te maken; behoud wel de oorspronkelijke masterbestanden in een aparte map.
- **Statusovergangen duidelijk scheiden:** concept, goedgekeurd ontwerp, aanwezig in repo en daadwerkelijk gebruikt in game zijn vier verschillende statussen. Het register moet deze apart aangeven.
- **Geen automatische plaatsing van decor:** de mechanische vogel is als losse asset geüpload, maar na feedback is er twijfel over zijn gebruik in de controlekamer. Bewaar hem als asset, maar laat hem weg uit de kamercompositie totdat expliciet opnieuw goedgekeurd.
