# De mysterieuze fabriek

Persoonlijk verjaardagsmysterie voor **Wannes (12)**: een avontuur in een mysterieuze speelgoedfabriek vol goocheltrucs, puzzels en raadsels. Wannes onderzoekt zelf het speelgoedlaboratorium en ontdekt uiteindelijk het verjaardagsfeest dat voor hem is voorbereid.

## Huidige fase

**Voorontwerp en dossieropschoning. Er wordt nog geen gamecode gebouwd.** Eerst maken we de documenten onderling consistent en werken we daarna samen de nog openstaande ontwerpkeuzes af. Pas na expliciete goedkeuring volgt de master-prompt en de bouw.

## Dossier — bron per onderwerp

- [Spelconcept](docs/GAME-CONCEPT.md) — verhaal, spelstructuur, personages en finale.
- [Uitdagingen](docs/CHALLENGES.md) — vier uitdagingen, interactie, oplossingen, hints en aanwijzingen.
- [Beslissingen en open punten](docs/DECISIONS.md) — leidend overzicht van vastgelegde keuzes en open beslissingen.
- [Techniekregels](docs/TECH-SPEC.md) — beoogde technische aanpak en kwaliteitsregels voor de latere bouw.
- [Art Direction & Style Guide](docs/ART-DIRECTION.md) — visuele identiteit, kleuren, zeefdruktextuur en interface.
- [Assetregister en referenties](docs/ASSET-REGISTER.md) — referenties, bestanden, status en ontbrekende assets.

## Welke informatie is leidend?

1. `docs/DECISIONS.md` is leidend voor expliciet goedgekeurde ontwerpkeuzes en voor wat nog openstaat.
2. `docs/CHALLENGES.md` beschrijft de uitgewerkte werking van de puzzels, maar mag goedgekeurde keuzes niet tegenspreken.
3. `docs/GAME-CONCEPT.md` beschrijft het verhaal en de overkoepelende spelstructuur.
4. `docs/TECH-SPEC.md` beschrijft technische randvoorwaarden; het is nog geen definitief implementatieplan.
5. `docs/ART-DIRECTION.md` beschrijft de visuele richting.
6. `docs/ASSET-REGISTER.md` beschrijft de rol en status van beeldbestanden en referenties.

Bij een tegenstrijdigheid wordt niet stilzwijgend gegokt: noteer die in `docs/DECISIONS.md` als open punt en los ze op vóór de master-prompt.

## Uitgangspunten

- Geen bestuurbaar hoofdpersonage en geen robotpersonage; Wannes onderzoekt zelf de wereld.
- De maquette is het beginscherm. Na Start verschijnt de speelse technische ruimte.
- De eerste drie uitdagingen zijn in vrije volgorde speelbaar; de grote deur kan vroeg worden onderzocht.
- De aanwijzingen voor de deur zijn **BAL** (uitdaging 1), **ster met oog** (uitdaging 2) en **signaalrood** (uitdaging 3).
- Beeldtaal: retrofuturistische speelgoedwereld, handgedrukte jarenzeventig-popart en sterk verweerde zeefdruk.
- Mobile-first, Nederlandstalig, statisch gehost op GitHub Pages; geen account, server of externe bibliotheken.
- Voortgang moet lokaal bewaard blijven en hervatbaar zijn.
- Nieuwe ontwerpen zijn voorstellen totdat ze expliciet zijn goedgekeurd.

## Bestanden en assets

De repository bevat momenteel negen afbeeldingsbestanden in de hoofdmap. Ze zijn daadwerkelijk geüpload, maar staan nog niet in de beoogde `assets/`-mappenstructuur en hebben namen met dubbele extensies. Het assetregister moet bij de volgende assetronde op de werkelijke bestandsnamen en het juiste bestandstype worden afgestemd. Verplaats of hernoem ze niet zonder de verwijzingen en het register tegelijk bij te werken.

## Geen prototype als basis

De oude prototypecode is geen basis voor de uiteindelijke game. De nieuwe game wordt vanaf een schone structuur gebouwd nadat het dossier is opgeschoond, de open keuzes zijn afgerond en de specificatie is goedgekeurd.
