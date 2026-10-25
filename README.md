# De mysterieuze fabriek

Een persoonlijk verjaardagsmysterie voor **Wannes (12)**: een Nederlandstalig point-and-click-avontuur in een mysterieuze speelgoedfabriek. Wannes onderzoekt zelf de werkplaats, lost drie uitdagingen in zelfgekozen volgorde op en gebruikt de ontdekte aanwijzingen om de grote deur te openen. Achter de deur wacht de feestelijke verrassing.

## Projectstatus

**Fase: dossieropschoning en ontwerp afronden.**

Er wordt nog geen gamecode gebouwd. Eerst worden de bestaande documenten en assets op elkaar afgestemd, worden de resterende ontwerpvragen afgehandeld en wordt de technische bouwspecificatie volledig gemaakt. De bouw start pas na expliciete goedkeuring van het dossier.

## Start hier

Gebruik deze documenten als projectdossier:

- [Beslissingen en open punten](docs/DECISIONS.md) — leidende bron voor goedgekeurde keuzes, open punten en de werkvolgorde.
- [Spelconcept](docs/GAME-CONCEPT.md) — verhaal, wereld, personages en overkoepelende spelstructuur.
- [Uitdagingen](docs/CHALLENGES.md) — puzzelwerking, oplossingen, hints, feedback en finale.
- [Technische specificatie](docs/TECH-SPEC.md) — technische randvoorwaarden, opslag/herstel en acceptatietests; nog afhankelijk van afronding en goedkeuring van het volledige dossier.
- [Scherm- en toestandspecificatie](docs/SCREEN-SPEC.md) — gedetailleerde scherm-ID's, puzzel-deeltoestanden, teksten, hints, fout/succesfeedback en finaleovergangen.
- [Art Direction & Style Guide](docs/ART-DIRECTION.md) — visuele identiteit, kleuren, zeefdruktextuur en interface.
- [Assetregister en referenties](docs/ASSET-REGISTER.md) — beeldreferenties, asset-ID's, status en ontbrekende bestanden.
- [Assetaudit — 25 oktober 2026](docs/ASSET-AUDIT-2026-10-25.md) — momentopname van de negen geüploade afbeeldingen en het voorgestelde doelpad per bestand.

## Welke informatie is leidend?

1. `docs/DECISIONS.md` bepaalt welke ontwerpkeuzes goedgekeurd zijn en welke nog openstaan.
2. `docs/CHALLENGES.md` werkt de puzzels uit en mag goedgekeurde beslissingen niet tegenspreken.
3. `docs/GAME-CONCEPT.md` beschrijft het verhaal en de spelstructuur.
4. `docs/TECH-SPEC.md` beschrijft de technische randvoorwaarden; het document moet vóór de bouw nog worden aangevuld.
5. `docs/ART-DIRECTION.md` beschrijft de visuele stijl.
6. `docs/ASSET-REGISTER.md` beschrijft de bedoelde rol en status van assets. De assetaudit is een aanvullende momentopname van de huidige repositorybestanden.

Bij een tegenstrijdigheid wordt niet stilzwijgend gegokt. Noteer het conflict als open punt in `docs/DECISIONS.md` en los het op vóór de master-prompt. Een latere ontwerpkeuze mag alleen worden gewijzigd na expliciete goedkeuring.

## Vaststaande uitgangspunten

- De speler is Wannes; er is geen bestuurbaar hoofdpersonage en geen robotpersonage.
- De maquette is het beginscherm. Na Start verschijnt de verkenbare werkplaats.
- De eerste drie uitdagingen zijn in zelfgekozen volgorde speelbaar; de grote deur kan vroeg worden onderzocht.
- De deur vraagt drie aanwijzingen: **BAL** (uitdaging 1), **ster met oog** (uitdaging 2) en **signaalrood** (uitdaging 3).
- De finalehandeling is het indrukken van een grote rode feestknop.
- Visuele stijl: retrofuturistische speelgoedwereld met handgedrukte jarenzeventig-popart en verweerde zeefdruk.
- Mobile-first, Nederlandstalig, bedoeld voor iPhone Safari en gehost als statische site op GitHub Pages.
- Geen account, server, externe bibliotheken, advertenties of tracking.
- Voortgang moet lokaal worden bewaard en exact hervatbaar zijn; een puzzel mag de speler niet blokkeren.
- Nieuwe ontwerpen zijn voorstellen totdat ze expliciet zijn goedgekeurd.

## Assets: huidige stand

De repository bevat negen geüploade afbeeldingsbestanden in de hoofdmap. Ze staan nog niet in de beoogde `assets/`-mappenstructuur en hebben dubbele extensies. De assetaudit stelt doelpaden voor, maar de bestanden zijn tijdens die audit **niet** verplaatst, hernoemd of verwijderd.

Volgende assetstap: controleer de werkelijke bestandstypen, verplaats de bestanden veilig naar de afgesproken doelmappen en werk daarna het assetregister bij. Verwijder of overschrijf geen originele afbeelding zonder controle.

## Waarom er nog geen gamecode is

De oude prototypecode is geen basis voor de uiteindelijke game. De nieuwe game wordt vanaf een schone structuur gebouwd nadat het dossier is opgeschoond, de open keuzes zijn afgehandeld en de technische specificatie met schermtoestanden, opslag/herstel en acceptatietests is goedgekeurd.

## Eerstvolgende werkvolgorde

1. README, beslissingen, uitdagingen, spelconcept en technische specificatie bijwerken — **eerste synchronisatieronde uitgevoerd**.
2. Assetregister afstemmen op de negen bestanden die aantoonbaar in de repository staan — **inventaris bijgewerkt; werkelijke bestandstypen en visuele overeenkomst nog te controleren**.
3. Scherm- en toestandspecificatie toegevoegd; controleer teksten en hints op onderlinge consistentie.
4. Controleer en structureer de definitieve assets en werk de klikzones/easter eggs uit.
5. Valideer de drie vaste match-3-startborden met een oplosbaarheidstest; schermtoestanden en een eerste tekst-/hintinventaris staan nu in SCREEN-SPEC.md, maar moeten nog inhoudelijk worden nagekeken.
6. Voer een laatste dossiercontrole uit en maak pas daarna de master-prompt.

Gebruik [GitHub-issue #1](https://github.com/Poolhond/robo-mystery/issues/1) als centrale checklist voor de voorbereiding van de master-prompt.
