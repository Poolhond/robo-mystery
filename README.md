# De mysterieuze fabriek

Een persoonlijk verjaardagsmysterie voor **Wannes (12)**: een Nederlandstalig point-and-click-avontuur in een mysterieuze speelgoedfabriek. Wannes onderzoekt zelf de werkplaats, lost drie uitdagingen in zelfgekozen volgorde op en gebruikt de ontdekte aanwijzingen om de grote deur te openen. Achter de deur wacht de feestelijke verrassing.

## Projectstatus

**Fase: dossier afronden voor één zelfstandige bouwopdracht.**

Het doel is het complete spel te laten bouwen met één uitgebreide master-prompt. Na goedkeuring van het dossier krijgt de gameontwikkelaar de prompt, de volledige repository en de assets. De ontwikkelaar voert zelfstandig de technische uitwerking, implementatie, tests, foutopsporing en herstel uit. Er wordt nu nog geen gamecode geschreven.

## Start hier

Gebruik deze documenten als projectdossier:

- [Beslissingen en open punten](docs/DECISIONS.md) — leidende bron voor goedgekeurde keuzes, open punten en de werkvolgorde.
- [Spelconcept](docs/GAME-CONCEPT.md) — verhaal, wereld, personages en overkoepelende spelstructuur.
- [Uitdagingen](docs/CHALLENGES.md) — puzzelwerking, oplossingen, hints, feedback en finale.
- [Technische specificatie](docs/TECH-SPEC.md) — bindende technische randvoorwaarden, zelfstandige ontwikkelopdracht, opslag/herstel en acceptatietests voor de gameontwikkelaar.
- [Scherm- en toestandspecificatie](docs/SCREEN-SPEC.md) — gedetailleerde scherm-ID's, puzzel-deeltoestanden, teksten, hints, fout/succesfeedback en finaleovergangen.
- [Art Direction & Style Guide](docs/ART-DIRECTION.md) — visuele identiteit, kleuren, zeefdruktextuur en interface.
- [Assetregister en referenties](docs/ASSET-REGISTER.md) — beeldreferenties, asset-ID's, status en ontbrekende bestanden.
- [Assetaudit — 25 oktober 2026](docs/ASSET-AUDIT-2026-10-25.md) — momentopname van de negen geüploade afbeeldingen en het voorgestelde doelpad per bestand.

## Welke informatie is leidend?

1. `docs/DECISIONS.md` bepaalt welke ontwerpkeuzes goedgekeurd zijn en welke nog openstaan.
2. `docs/CHALLENGES.md` werkt de puzzels uit en mag goedgekeurde beslissingen niet tegenspreken.
3. `docs/GAME-CONCEPT.md` beschrijft het verhaal en de spelstructuur.
4. `docs/TECH-SPEC.md` beschrijft de technische randvoorwaarden en wat de gameontwikkelaar zelfstandig moet bouwen, testen en opleveren.
5. `docs/ART-DIRECTION.md` beschrijft de visuele stijl.
6. `docs/ASSET-REGISTER.md` beschrijft de bedoelde rol en status van assets. De assetaudit is een aanvullende momentopname van de huidige repositorybestanden.

Bij een tegenstrijdigheid tussen documenten mag de ontwikkelaar geen goedgekeurde ontwerpkeuze stilzwijgend wijzigen. Noteer het conflict in `docs/DECISIONS.md`. Alleen echte ontwerpkeuzes die invloed hebben op het verhaal, de spelregels, de visuele identiteit of de spelerservaring moeten vóór de master-prompt worden opgelost. Technische uitvoeringsdetails, testborden, algoritmes en herstelstrategieën zijn de verantwoordelijkheid van de ontwikkelaar.

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

De negen bestaande afbeeldingsbestanden zijn geordend onder de afgesproken `assets/`-mappen en hebben nu gewone `.png`-bestandsnamen. Michel heeft bevestigd dat het PNG-bestanden zijn. Alleen de paden en namen zijn gewijzigd; de bestaande beeldbytes zijn behouden. De mechanische vogel blijft buiten de goedgekeurde spelcompositie.

Volgende assetstap: controleer de afmetingen, transparantie en visuele inhoud en bepaal welke assets nog ontbreken. De bestaande afbeeldingen zijn niet geconverteerd of overschreven.

## Waarom er nog geen gamecode is

De oude prototypecode is geen basis voor de uiteindelijke game. De nieuwe game wordt vanaf een schone structuur gebouwd nadat het dossier en de benodigde assets zijn gecontroleerd en de master-prompt expliciet is goedgekeurd. De voorbereiding is niet bedoeld om elk technisch probleem vooraf op te lossen.

## Verdeling van verantwoordelijkheden

**Michel / dossier:** keurt ontwerpkeuzes goed en bewaakt het verhaal, de spelregels, de visuele stijl en de gewenste spelerservaring.

**Gameontwikkelaar / één master-prompt:** bouwt het volledige spel zelfstandig, kiest passende technische oplossingen, genereert geldige beginborden, test alle puzzels en overgangen, controleert opslag en herstel, test animaties en bediening, spoort bugs op en herstelt ze. De ontwikkelaar mag technische details invullen zolang die de goedgekeurde ontwerpkeuzes niet veranderen. De ontwikkelaar rapporteert eventuele echte ontwerpconflicten in plaats van zelf een nieuwe ontwerpregel te verzinnen.

## Eerstvolgende werkvolgorde

1. Houd de ontwerpdocumenten onderling consistent en rond alleen beslissingen af die de spelervaring daadwerkelijk bepalen.
2. Controleer de assets en hun bedoelde rol; technische bestandscontrole en veilige plaatsing mogen deel uitmaken van de zelfstandige bouwopdracht.
3. Controleer de resterende teksten, hints, schermovergangen en assetreferenties op duidelijke ontwerptegenstrijdigheden.
4. Maak één volledige master-prompt die de ontwikkelaar opdraagt de repository te inspecteren, het complete spel te bouwen, tests uit te voeren, fouten zelfstandig te herstellen en het resultaat op GitHub Pages te controleren.
5. Laat de ontwikkelaar de technische haalbaarheid van beginborden, cascades, kisten, sleutelbeweging, animaties en herstel tijdens de bouw verifiëren. Vooraf vaste matrices of apart solverbewijs uitwerken is geen vereiste.

Gebruik [GitHub-issue #1](https://github.com/Poolhond/robo-mystery/issues/1) als centrale checklist voor de voorbereiding van de master-prompt.
