# Assetaudit — 25 oktober 2026

## Samenvatting

De actuele GitHub-bestandsstructuur bevat **elf afbeeldingsbestanden** onder `assets/`. De eerdere verwijzing naar negen bestanden was verouderd. Deze audit bevestigt de paden en GitHub-bestandsgrootten, maar niet de werkelijke afbeeldingsafmetingen, transparantie of visuele inhoud. Die moeten worden gecontroleerd door de ontwikkelaar of met een afzonderlijke beeldinspectie.

De extensie `.png` is de naam in de repository; alleen op basis van een padnaam kan het werkelijke bestandsformaat niet worden bewezen. Er zijn in deze audit geen afbeeldingen geconverteerd, hernoemd, verplaatst of verwijderd.

## Huidige bestanden en paden

| Huidig repositorypad | Asset | Status / volgende actie |
|---|---|---|
| `assets/characters/charlie/AST-CHARLIE-01-charlie-screenprint.png` | Charlie | Aanwezig; visuele overeenkomst, werkelijke afmetingen en formaat controleren |
| `assets/characters/ridderus/AST-RIDDERUS-01-ridderus-screenprint.png` | RidderUs | Aanwezig; visuele overeenkomst, werkelijke afmetingen en formaat controleren |
| `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` | Schildje | Aanwezig; visuele overeenkomst, werkelijke afmetingen en formaat controleren |
| `assets/characters/panda/AST-PANDA-01-panda-screenprint.png` | Panda | Aanwezig; visuele inhoud en rol als optioneel personage controleren |
| `assets/title-screen/AST-TITLE-01-title-poster.png` | Titelposter | Aanwezig; compositie, afmetingen en werkelijke bestandstype controleren |
| `assets/rooms/control-room/AST-ROOM-01-control-room-reference.png` | Vaste controlekamerreferentie | Aanwezig; vaste ruimtecompositie, afmetingen en werkelijke bestandstype controleren |
| `assets/rooms/toy-laboratory/AST-ENV-01.png` | Speelgoedlaboratorium / maquette | Aanwezig; inhoud en rol als referentie verifiëren |
| `assets/decor/AST-DECOR-01-red-heart.png` | Rood hart | Aanwezig; visuele inhoud en formaat controleren |
| `assets/decor/AST-DECOR-02-birdhouse.png` | Vogelhuisje met vogel | Aanwezig; dit is het aanwezige vogelhuisje; niet automatisch gelijkstellen aan de aparte asset-ID AST-BIRD-01 |
| `assets/decor/AST-DECOR-03-mechanical-bird.png` | Mechanische vogel | Aanwezig, maar uitgesloten van het spel; niet gebruiken |
| `assets/decor/AST-DECOR-04-pitcher-terrarium.png` | Vleesetende bekerplant | Aanwezig; visuele inhoud en formaat controleren |

## Belangrijke bevindingen en documentatiecorrecties

1. **Bestandenaantal:** de huidige tree bevat elf afbeeldingsbestanden. Verwijzingen naar negen bestanden zijn verouderd en moeten niet meer worden gebruikt.
2. **Nestkast/vogel:** `AST-DECOR-02-birdhouse.png` bestaat. Een afzonderlijk bestand dat aantoonbaar overeenkomt met `AST-BIRD-01` is niet in de huidige tree teruggevonden. De registertekst die zegt dat de herziene geïsoleerde versie in de repository-root staat, is daarom niet bevestigd en mag niet als feit worden behandeld.
3. **Speelgoedlaboratorium:** `assets/rooms/toy-laboratory/AST-ENV-01.png` bestaat; de visuele inhoud en precieze status moeten nog worden bekeken.
4. **Personagebestanden:** de huidige drie basisillustraties staan op PNG-paden. Oudere tekst met voorgestelde JPEG- of WebP-paden beschrijft geen huidige bestanden en mag niet worden opgevat als bewijs dat die varianten aanwezig zijn.
5. **Mechanische vogel:** het bestand wordt veilig bewaard, maar hoort niet in de game zonder expliciete goedkeuring.
6. **Inspiratie versus game-assets:** aanwezigheid in de repository betekent niet automatisch dat een afbeelding letterlijk in het spel moet worden gebruikt of dat de asset definitief is goedgekeurd.

## Bindende gebruiksregel

De afbeeldingen zijn inspiratiebronnen voor een eigen, samenhangende spelwereld. De ontwikkelaar moet herkenbare kenmerken behouden waar die belangrijk zijn, maar mag compositie, schaal, uitsnede en context aanpassen. Nieuwe achtergronden, animaties en spelobjecten mogen worden gegenereerd waar nodig. Alles moet visueel op elkaar aansluiten en goed schalen op een mobiel scherm. Geen uitgesloten ontwerp gebruiken.

## Nog te controleren tijdens de technische bouw

- Werkelijke beeldformaten, pixelafmetingen, transparantie en bestandsgrootte in bytes.
- Visuele overeenkomst van personages met de goedgekeurde referenties.
- Gebruik van de controlekamerafbeelding als vaste compositiereferentie, met afzonderlijke interactieve zones.
- Welke ontbrekende puzzelobjecten beter als schaalbare interface/CSS-vormen kunnen worden gemaakt en welke een illustratie nodig hebben.
- Of een afzonderlijke `AST-BIRD-01`-export nog moet worden aangeleverd of bewust niet nodig is.

## Wijzigingsgrens

Deze audit corrigeert alleen de documentatie. Er zijn geen beeldbestanden verwijderd, overschreven, geconverteerd of verplaatst. De mechanische vogel blijft behouden als uitgesloten bestand.
