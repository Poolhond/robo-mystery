# ROBO MYSTERY

Persoonlijk verjaardagsmysterie voor **Wannes (12)**: een goocheltrucs-avontuur in een handgemaakte speelgoedwereld. Wannes onderzoekt zelf het speelgoedlaboratorium en ontdekt uiteindelijk het verjaardagsfeest dat voor hem is voorbereid.

## Huidige fase

We werken eerst het volledige ontwerpdossier uit. **Er wordt nog geen nieuwe gamecode ontwikkeld.** Het oude prototype is verwijderd omdat het niet bij het goedgekeurde spelconcept paste. Zodra concept, uitdagingen, teksten, assets en technische regels voldoende vastliggen, maken we één uitgebreide bouwopdracht (master-prompt), gevolgd door een testronde op een iPhone.

## Dossier — één bron per onderwerp

- [Spelconcept](docs/GAME-CONCEPT.md) — verhaal, spelstructuur, personages en finale.
- [Uitdagingen](docs/CHALLENGES.md) — vier uitdagingen, interactie, oplossingen, hints en aanwijzingen.
- [Beslissingen en open punten](docs/DECISIONS.md) — wat vastligt, wat nog openstaat en wat vóór de bouw nodig is.
- [Techniekregels](docs/TECH-SPEC.md) — beoogde technische aanpak en kwaliteitsregels voor de latere bouw.
- [Art Direction & Style Guide](docs/ART-DIRECTION.md) — visuele identiteit, kleuren, zeefdruktextuur en interface.
- [Assetregister en referenties](docs/ASSET-REGISTER.md) — referenties, assets, status en ontbrekende bestanden.

## Mappenstructuur

```
README.md                 Overzicht en startpunt
docs/
  GAME-CONCEPT.md         Verhaal en spelstructuur
  CHALLENGES.md            Uitdagingen en puzzels
  DECISIONS.md             Besluiten en open punten
  TECH-SPEC.md             Technische randvoorwaarden
  ART-DIRECTION.md         Visuele stijl
  ASSET-REGISTER.md        Referenties en assetstatus
```

## Uitgangspunten

- De originele ROBO MYSTERY-referenties zijn leidend.
- Beeldtaal: retrofuturistische sciencefiction met handgedrukte jarenzeventig-popart en sterk verweerde zeefdruktextuur.
- De interface hoort bij dezelfde vintage speelgoedwereld.
- Mobile-first, speelbaar in de browser, zonder account en gratis te hosten op GitHub Pages.
- Alle spelertekst is Nederlands en blijft echte tekst, niet tekst die in illustraties is ingebakken.
- Nieuwe ontwerpen zijn voorstellen totdat ze expliciet zijn goedgekeurd; controleer daarvoor docs/DECISIONS.md.
- Afbeeldingen die alleen in de chat zijn gegenereerd, gelden niet als bestanden in de repository. Ze moeten daadwerkelijk worden toegevoegd voordat de latere bouw ze kan gebruiken.

## Geen prototype als basis

De oude index.html is verwijderd. Die prototypecode volgde een ander verhaal en is niet geschikt als basis voor de uiteindelijke game. De nieuwe game wordt pas gebouwd nadat het ontwerpdossier is uitgewerkt en gecontroleerd.
