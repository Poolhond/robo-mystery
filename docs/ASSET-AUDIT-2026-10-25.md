# Assetaudit — 25 oktober 2026

## Samenvatting

De elf bestaande afbeeldingsbestanden zijn geordend in de afgesproken `assets/`-mappen. Volgens Michel zijn alle elf bestanden PNG-afbeeldingen. De bestandsnamen zijn opgeschoond zodat ze eindigen op `.png`. De bestaande Git-blobs zijn behouden: de beeldbytes zijn niet opnieuw opgeslagen, geconverteerd of overschreven. Alleen paden, bestandsnamen en documentatie zijn gewijzigd.

Controleer nog de afmetingen, transparantie en visuele overeenkomst tijdens de technische assetcontrole.

## Huidige bestanden en paden

| Huidig repositorypad | Asset | Status / volgende actie |
|---|---|---|
| `assets/characters/charlie/AST-CHARLIE-01-charlie-screenprint.png` | Charlie | Verplaatst zonder bestandsinhoud te wijzigen; afmetingen en visuele overeenkomst controleren |
| `assets/characters/ridderus/AST-RIDDERUS-01-ridderus-screenprint.png` | RidderUs | Verplaatst zonder bestandsinhoud te wijzigen; werkelijk formaat en visuele overeenkomst controleren |
| `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` | Schildje | Verplaatst zonder bestandsinhoud te wijzigen; werkelijk formaat en visuele overeenkomst controleren |
| `assets/title-screen/AST-TITLE-01-title-poster.png` | Titelposter | Verplaatst; afmetingen en definitieve export controleren |
| `assets/rooms/control-room/AST-ROOM-01-control-room-reference.png` | Goedgekeurde controlekamerreferentie | Verplaatst; afmetingen controleren. Gebruik als vaste kamercompositie |
| `assets/decor/AST-DECOR-01-red-heart.png` | Rood hart | Verplaatst; afmetingen en definitieve export controleren |
| `assets/decor/AST-DECOR-02-birdhouse.png` | Vogelhuisje met vogel | Verplaatst; afmetingen en visuele overeenkomst controleren |
| `assets/decor/AST-DECOR-03-mechanical-bird.png` | Mechanische vogel | Veilig bewaard als asset, maar niet in de spelcompositie gebruiken zonder expliciete goedkeuring |
| `assets/decor/AST-DECOR-04-pitcher-terrarium.png` | Vleesetende bekerplant | Verplaatst; bestandstype en definitieve export controleren |

| `assets/rooms/toy-laboratory/AST-ENV-01.png` | Speelgoedlaboratorium (AST-ENV-01) | Nieuw toegevoegd; afmetingen en visuele overeenkomst controleren |
| `assets/characters/panda/AST-PANDA-01-panda-screenprint.png` | Panda-knuffel | Nieuw toegevoegd; afmetingen en visuele overeenkomst controleren |

## Wat is uitgevoerd

- De elf bestaande afbeeldingen zijn naar hun doelmappen verplaatst door de oorspronkelijke Git-blobs te hergebruiken.
- De oorspronkelijke bytes zijn behouden; de bestandsnamen zijn opgeschoond en er is geen beeldconversie uitgevoerd.
- De mappenstructuur sluit nu aan bij het assetregister en de technische specificatie.
- De mechanische vogel blijft buiten de goedgekeurde gamecompositie.
- De assetregister- en README-verwijzingen zijn bijgewerkt naar de huidige paden.

## Wat nog gecontroleerd moet worden

1. Open elk bestand en controleer het werkelijke formaat, de afmetingen en de visuele inhoud.
2. Controleer dat de drie karakterillustraties overeenkomen met de goedgekeurde versies.
3. Controleer de titelposter en controlekamerreferentie als beeld, niet alleen op bestandsnaam.
4. Optimaliseer later de bestanden voor mobiel gebruik als dat nodig is. Bewaar de originele masters; converteer of verklein niet destructief.
5. Werk het assetregister bij als een bestand een afwijkende inhoud heeft of als er een definitieve variant wordt aangeleverd.

## Belangrijke ontwerpafspraken

- De afbeelding van de controlekamer is de vaste basis van de speelruimte. De computer, groene locker, bekertafel en rode deur moeten als afzonderlijke interactieve zones werken.
- De mechanische vogel is niet goedgekeurd voor plaatsing in de kamer en mag niet automatisch worden ingezet.
- De robot is geschrapt uit het spelconcept en mag niet worden toegevoegd.
- Conceptreferentie, goedgekeurd ontwerp, aanwezig bestand en daadwerkelijk gebruikte game-asset zijn verschillende statussen. Houd die uit elkaar.

## Nog niet als definitief bestand aangetroffen


- Eventuele ontbrekende losse karaktervarianten of aanvullende illustraties die echt nodig blijken voor het verhaal.

De gameontwikkelaar mag eenvoudige interface-elementen en puzzelobjecten zelf tekenen met CSS of andere ingebouwde technieken als dat visueel voldoende is. Maak geen extra afbeeldingsbestanden aan wanneer een eenvoudige, schaalbare interfacevorm beter werkt.
