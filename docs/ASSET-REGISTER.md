# De mysterieuze fabriek — Assetregister & referenties

**Versie:** 1.4  
**Status:** De elf beeldbestanden zijn geordend onder `assets/` en hebben de extensie `.png`. De beeldbytes zijn bij het verplaatsen niet gewijzigd. De mechanische vogel is uitgesloten van het spel en mag niet worden gebruikt.

## Bindende gebruiksregel: assets zijn inspiratiebronnen

De bestanden in `assets/` zijn **geen letterlijke inventaris van wat er in het spel moet verschijnen**. Ze geven de ontwikkelaar herkenbare visuele aanknopingspunten voor het genereren van een eigen, samenhangende spelwereld. Gebruik de assets niet automatisch als ongewijzigde plaatjes in de game.

- Hergebruik herkenbare eigenschappen van de speelgoedfiguren en goedgekeurde elementen, zoals silhouet, kleur, proporties en onderscheidende details.
- Genereer waar nodig nieuwe scènes, achtergronden, decorstukken, animaties en spelobjecten die passen bij het spelconcept en de art direction.
- De ontwikkelaar mag compositie, schaal, pose en context aanpassen; de referentie hoeft niet letterlijk te worden nagebouwd.
- Niet elk object uit een referentie hoeft in het spel te verschijnen. De plaats en functie van interactieve elementen worden bepaald door het goedgekeurde spelconcept.
- Een uitgesloten ontwerp, in het bijzonder de mechanische vogel, mag niet worden gebruikt. Voor de mechanische vogel is de uitsluiting definitief.
- Behoud de identiteit van belangrijke personages; maak geen generieke vervangingen die hun herkenbare kenmerken verliezen.

| ID | Beschrijving | Hoofdfunctie | Status |
|---|---|---|---|
| AST-TITLE-01 | Verticale vintage zeefdrukposter voor het beginscherm: snoepfabriek, gestreepte schoorstenen, rook, gloeiende ramen, titel en startknop; geen personages | Beginscherm / title screen voor iPhone 9:19,5 | Concept goedgekeurd; bestand `assets/title-screen/AST-TITLE-01-title-poster.png` aanwezig; PNG-formaat bevestigd door Michel |
| AST-DECOR-01 | Rood hart met opgeheven handen en stralen, minimalistische vintage zeefdruk | Decorstuk voor de controlekamer | Ontwerp uitgewerkt; bestand `assets/decor/AST-DECOR-01-red-heart.png` aanwezig; PNG-formaat bevestigd door Michel |
| AST-DECOR-02 | Houten vogelhuisje met rood-oranje, gefacetteerde vogel die uit de opening kijkt | Decorstuk voor de controlekamer | Ontwerp uitgewerkt; bestand `assets/decor/AST-DECOR-02-birdhouse.png` aanwezig; PNG-formaat bevestigd door Michel |
| AST-DECOR-03 | Mechanische bouwsteen-vogel met roestoranje lichaam, donkerblauwe uitgespreide vleugels en ronde blauwe displaybasis | Decorstuk voor de controlekamer | Ontwerp uitgewerkt; bestand `assets/decor/AST-DECOR-03-mechanical-bird.png` aanwezig; **definitief uitgesloten — niet gebruiken** |
| AST-DECOR-04 | Vleesetende bekerplant in witte en turquoise kweekkast met opengeklapt deksel | Decorstuk en interactieve easter egg in de controlekamer | Ontwerp uitgewerkt; bestand `assets/decor/AST-DECOR-04-pitcher-terrarium.png` aanwezig; PNG-formaat bevestigd door Michel |
| AST-ROOM-01 | De door Michel aangeleverde verticale afbeelding van de controlekamer: computer links, hoge groene cijfercode-locker in het midden, grote rode deur rechts en tafel met drie bekers vooraan. Bevat ook het hartkunstwerk en de vleesetende plant. | **Vaste visuele basis van de speelruimte** en referentie voor de posities van de vier hoofdobjecten en drie easter eggs | Door Michel bevestigd als dé ruimte; bestand `assets/rooms/control-room/AST-ROOM-01-control-room-reference.png` aanwezig en door Michel gecontroleerd |
| REF-01 | Kamer 3 — The Signal Room: signaalmonitor, satellietschotel, technische apparatuur, verhaalpaneel, inventaris en score | Primaire referentie voor omgevingsstijl en geïntegreerde game-interface | Kernreferentie |
| REF-02 | Karakter-/conceptblad: The Signal Bird, Winged Guardian, The Heart Mark en The Golden Clue | Karakterpresentatie, symbolen en objecten | Kernreferentie |
| REF-03 | Overzicht met signaalvogel, aap, panda, octopus, schildpad en aanvullende symbolen | Verhouding tussen personages, aanzichten en karakterbladen | Kernreferentie |
| REF-04 | Het speelgoedlaboratorium: kleine geometrische huisjes, gestreepte schoorstenen, kleurrijke daken en een knoppenroute op een groene basis | Specifieke omgevingsconceptreferentie | Kernreferentie voor deze wereld |
| REF-05 | Verticale poster met kinderen en geometrische achtergrondvlakken, geometrische achtergrondvlakken | Aanvullende compositiereferentie; robotfiguur niet overnemen | Aanvullend |
| AST-TURTLE-01 | Verweerde zeefdrukillustratie van de groene pluchen schildpad, gebaseerd op Michels foto | Karakterasset: de schildpad / geheime bewaker | Bestand aanwezig: `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png`; door Michel gecontroleerd |
| AST-BIRD-01 | Zeefdrukillustratie van de houten nestkast met rood-oranje zangvogel, gebaseerd op Michels foto | Karakter-/omgevingsasset voor de signaalvogel en haar nestkast | Een afzonderlijke definitieve export is niet teruggevonden in de huidige tree; niet verwarren met het aanwezige bestand AST-DECOR-02-birdhouse.png |
| AST-ENV-01 | Zeefdrukillustratie van het fysieke speelgoedlaboratorium | Primaire omgevingsasset voor het speelgoedlaboratorium | Bestand aanwezig: `assets/rooms/toy-laboratory/AST-ENV-01.png`; door Michel gecontroleerd |
| AST-ROBOT-01 | Eerder gegenereerde zeefdrukillustratie van de witte speelgoedrobot | Vervallen asset; robot is volledig uit het spelconcept geschrapt | Niet gebruiken; archiefreferentie, geen gameasset |
| REF-CHAR-02 | Groepsposter met Charlie, RidderUs en Schildje samen | Compositie- en stijlreferentie voor de drie hoofdrolfiguren van uitdaging 2 | Referentie uit chat; nog niet als repo-bestand opgeslagen |
| CHAR-CHARLIE-01 | Echte pluchen Charlie, bruine aap met lichtbruine snuit en oranje jas met twee knopen | Karakterreferentie voor het logische raadsel in uitdaging 2 | Referentie uit chat; losse goedgekeurde asset nog te maken |
| CHAR-RIDDERUS-01 | Oranje figuur met cyaan vizier, grijze helm met verticale openingen en gele pompon; geen armen | Karakterreferentie voor het logische raadsel in uitdaging 2 | Referentie uit chat; losse goedgekeurde asset nog te maken |
| CHAR-SCHILDJE-01 | Groene pluchen schildpad met breed schild, korte flippers en grote donkere ogen | Karakterreferentie voor het logische raadsel in uitdaging 2 | Referentie uit chat; losse goedgekeurde asset nog te maken |
| AST-CHARLIE-01 | Definitieve losse illustratie Charlie, minimalistische vectorvorm met sterke verweerde zeefdruk | Gameasset voor uitdaging 2 en eventuele finale | Aanwezig in de repository; gecontroleerd door Michel |
| AST-RIDDERUS-01 | Definitieve losse illustratie RidderUs, minimalistische vectorvorm met sterke verweerde zeefdruk | Gameasset voor uitdaging 2 en eventuele finale | Aanwezig in de repository; gecontroleerd door Michel |
| AST-SCHILDJE-01 | Definitieve losse illustratie Schildje, minimalistische vectorvorm met sterke verweerde zeefdruk | Gameasset voor uitdaging 2 en eventuele finale | Aanwezig in de repository; gecontroleerd door Michel |

## Vaste omgevingsreferentie — AST-ROOM-01

**Beslissing:** Michel heeft bevestigd dat de aangeleverde afbeelding met de controlekamer de speelruimte is. Ontwerp geen alternatieve kamer en verander de compositie niet opnieuw zonder expliciete toestemming. Gebruik deze afbeelding als de vaste visuele basis.

**Hoofdobjecten en locaties:** computer links (uitdaging 1), hoge groene locker met cijfercode in het midden (uitdaging 2), grote rode deur rechts (uitdaging 4) en tafel met drie bekers vooraan (uitdaging 3). De vleesetende plant en het hartkunstwerk zijn decorstukken met interactieve easter eggs. De schuif/lade voor de pandasurprise moet als interactieve zone worden toegewezen aan een bestaande kast of lade in deze ruimte; voeg daarvoor niet zomaar een nieuw meubel toe.

**Belangrijk:** de afbeelding is goedgekeurd als ruimte en compositie. De exacte klikzones, zoomtoestanden en mobiele bediening worden later in het dossier beschreven. Dit is nog geen toestemming om code te bouwen.

## Vervallen asset — AST-ROBOT-01 (niet gebruiken)

**Status:** VERVALLEN. De robot is volledig geschrapt uit het concept; de oude afbeelding mag niet in de game worden gebruikt.  



**Gebruik:** niet opnemen in de game of toekomstige assetbundels.

## Tweede uitgewerkte asset — AST-ENV-01

**Bron:** door Michel aangeleverde foto van de fysieke maquette van het speelgoedlaboratorium.  
**Assetrichting:** behoud de huisvormen, drie gestreepte schoorstenen, daken met veelkleurige korrels, groene basis en route van knopen naar de voordeur.  
**Stijlbehandeling:** sterke, verweerde zeefdruk op warm crème papier; signaalrood, mosterdgeel, donker petrol en diep groen; halftoon, inktspikkels en onregelmatige drukdekking.  
**Compositie:** de volledige maquette als centraal onderwerp, met grafische cirkels op de achtergrond en een posterachtige uitsnede.  
**Bestand:** aanwezig als `assets/rooms/toy-laboratory/AST-ENV-01.png`. Door Michel gecontroleerd; gebruik als omgevingsreferentie voor het speelgoedlaboratorium.

## Derde uitgewerkte asset — AST-BIRD-01

**Bron:** door Michel aangeleverde foto van de houten nestkast met de rood-oranje vogel.  
**Assetrichting:** behoud de herkenbare houten nestkast met schuin dak en de vogel die naar links kijkt; de rode kop/borst, donkere snavel en gestreepte vleugels blijven herkenningspunten.  
**Stijlbehandeling:** sterke, verweerde jarenzeventig-zeefdruk op warm crème papier, met signaalrood, mosterdgeel, donker petrol en groen; grove halftoon, inktspikkels, krassen en lichte kleurplaatverschuiving.  
**Compositie:** nestkast en vogel centraal, met eenvoudige geometrische kleurvlakken achter het onderwerp; geen extra tekst.  
**Bestand:** een afzonderlijke geïsoleerde export is niet teruggevonden in de huidige repositorytree. Het aanwezige vogelhuisje staat onder assets/decor/AST-DECOR-02-birdhouse.png; bevestig eerst of dit inhoudelijk de bedoelde asset is.

## Vierde uitgewerkte asset — AST-TURTLE-01

**Bron:** door Michel aangeleverde foto van de groene pluchen schildpad.  
**Assetrichting:** behoud het zachte, pluizige groene lijf, de brede schild, vier korte flippers, de lichte stik-/knopdetails en de grote donkere ogen.  
**Stijlbehandeling:** sterke verweerde zeefdruk op warm crème papier; diep mosgroen en geelgroen, met signaalrode en mosterdgele drukvlakken en donker petrol; grove halftoon, korrel, inktspikkels en lichte kleurplaatverschuiving.  
**Compositie:** schildpad centraal, als herkenbaar personage met eenvoudige geometrische achtergrondvlakken; geen extra tekst.  
**Bestand:** bestand `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` aanwezig; door Michel gecontroleerd.

## Nog te maken of te bevestigen game-assets

- **AST-PANDA-01:** panda-knuffel in vintage zeefdrukstijl — bestand aanwezig: `assets/characters/panda/AST-PANDA-01-panda-screenprint.png`; door Michel gecontroleerd.

De volgende lijst beschrijft assets die inhoudelijk nodig kunnen zijn voor de huidige uitdagingen. Ze zijn niet automatisch al als bestanden aanwezig in de repository. Definitieve selectie en prioriteit volgen na het uitwerken van de laboratoriumroute.

- Match-3-doelobjecten en obstakels: rode energiecellen als doel in level 1, houten kistjes als obstakels in level 2 en gouden energiesleutel als doelobject in level 3. De gewone verwisselbare tegels zijn uitsluitend effen kleurvlakken zonder symbolen, pictogrammen, letters of illustraties. De energiecellen, kistjes en sleutel zijn afzonderlijke visuele doelobjecten waar het levelontwerp ze vereist.
- Uitdaging 2: codepaneel, geheim deurtje, messing sleutel, aap, panda, schildpad, drie gekleurde kistjes en een klein, plat vintage gedrukt kaartje met de ster-met-oog-aanwijzing in het rode kistje. Het kaartje is een benodigde spelasset; ontwerp/generatie gebeurt tijdens de bouw.
- Uitdaging 3: goocheltafel, drie bekers, rood balletje en kleurstaal voor signaalrood.
- Uitdaging 4: grote deur, leeg symboolvenster, ster-met-oog-status, woordveld, gelabelde kleurstalen en OPEN DE DEUR-knop.
- Finale: feestomgeving, confetti/lichtaccenten en de personages die daadwerkelijk in de finale worden gebruikt.

**Beloningsconsistentie:** BAL wordt uitsluitend verdiend in uitdaging 1. Uitdaging 2 levert de ster met een oog op. Uitdaging 3 levert signaalrood op. Gebruik daarom geen assetomschrijving zoals “BAL-aanwijzingsobject” voor uitdaging 2.

## Gedeelde kenmerken
- Warme crème/papierkleur.
- Signaalrood en mosterdgeel als accenten.
- Donker petrol en groen als diepe kleuren.
- Sterk zichtbare papier- en inktverwering.
- Geometrische vlakken, stevige contouren en retro-futuristische details.
- Een combinatie van gedetailleerde illustratie en grafische compositie.

## Assetbeheer — regels
1. Behoud het originele bestand en de originele naam.
2. Geef iedere asset een stabiel ID.
3. Noteer bron, functie, status en eventuele varianten.
4. Bewaar bronmateriaal apart van bewerkte exports.
5. Markeer assets als concept, goedgekeurd of vervangen; overschrijf de bron niet stilzwijgend.
6. Laat tekst die essentieel is voor de gameplay waar mogelijk als echte interface-tekst bestaan, niet alleen als tekst in een afbeelding.

## Ontbrekende metadata
De elf beeldbestanden staan nu in de afgesproken mappen onder `assets/` en hebben de extensie `.png`. Michel heeft bevestigd dat de aangeleverde afbeeldingen PNG-bestanden zijn. De bestanden zijn niet geconverteerd of opnieuw opgeslagen; alleen de paden en namen zijn opgeschoond. De bestanden die al aanwezig zijn, zijn niet automatisch allemaal definitieve game-assets. Afmetingen, rol, herkomst en goedkeuringsstatus moeten per bestand worden bevestigd.

## Volgende stap
Controleer de originele bestanden één voor één, bevestig de rol van elke referentie en registreer eventuele aparte karakterbladen, kamers, voorwerpen, iconen en textuurvoorbeelden.


## Karakterset uitdaging 2 — hoofdrolfiguren (nieuw dossieronderdeel)

**Status:** de onderstaande richtlijnen bewaren de karakteridentiteit uit de referentiebeelden. De drie losse zeefdrukillustraties van Charlie, RidderUs en Schildje zijn inmiddels aanwezig in de repository en door Michel gecontroleerd; zie de actuele paden in de tabel hieronder. De bronbeschrijvingen blijven bruikbaar als identiteitseisen, maar de oude bestandsnaamvoorstellen en de historische planningstekst zijn niet leidend.

### REF-CHAR-02 — Groepsreferentie: Charlie, RidderUs en Schildje

**Bronbestand:** `CB12583C-C094-4781-B3F7-09805B768190.jpeg` (711 × 1536 px, JPEG).  
**Rol:** groepscompositie en stijlvoorbeeld voor de drie hoofdrolfiguren in het raadsel van uitdaging 2.  
**Wat deze afbeelding vastlegt:** de drie figuren staan samen in één warme, verticale jarenzeventig-popartposter, met crème papier, geometrische vlakken, plantvormen en verweerde zeefdruk. Dit is de beste referentie voor hoe de figuren samen in dezelfde beeldwereld kunnen staan. De compositie is géén verplichte pose voor toekomstige losse assets.

### CHAR-CHARLIE-01 — Charlie, de aap

**Bronbestand:** `IMG_0228.jpeg` (1152 × 1536 px, JPEG).  
**Referentie:** de echte pluchen Charlie met bruine kop en kruin, lichtbruine snuit en wangen, ronde uitstekende oren, grote donkere ogen en oranje jas met kraag en twee knopen.  
**Onveranderlijke herkenningspunten:**
- bruine pluchen kop met duidelijk lichtere snuit en gezichtsvlak;
- twee ronde oren die aan beide kanten zichtbaar uitsteken;
- twee grote, donkere, glanzende ogen;
- oranje jas met brede kraag en twee grote knopen;
- zachte, vriendelijke en een tikje ondeugende uitstraling.
**Vormregels:** behoud Charlie als aap en als zittende pluchen pop met armen en benen. Geen helm, geen astronautenvenster en geen robotachtige lichaamsvorm. De jas blijft oranje; verander die niet naar een andere kleur om het palet af te dwingen.  
**Gewenste eerste asset:** geïsoleerd volledig figuur, transparante achtergrond waar mogelijk; daarnaast hoofd-/schouderportret en drie bruikbare expressies (neutraal, nadenkend, geheimzinnig/ondeugend).  
**Bestandsnaamvoorstel:** `assets/characters/charlie/charlie-full.webp`, met bronfoto apart bewaard.

### CHAR-RIDDERUS-01 — RidderUs, het oranje figuur

**Bronbestand:** `FA536B09-396F-45D1-AA7D-50B1E54526DF.jpeg` (1024 × 1536 px, JPEG).  
**Referentie:** het eenvoudige oranje figuur met afgeronde, verticale romp, twee korte benen, een groot cyaan vizier met donker petrolkleurige rand en een donkergrijze metalen helm met verticale kijkopeningen en een gele pompon.
**Onveranderlijke herkenningspunten:**
- heldere oranje romp en twee korte benen; geen armen zichtbaar in het gevestigde ontwerp;
- groot afgerond cyaan vizier, omlijst met donker petrol;
- grijze, koepelvormige ridder-/ruimtehelm met donkere verticale openingen;
- gele, zachte pompon bovenop de helm;
- stevige donker-petrol contour.
**Vormregels:** behoud het herkenbare silhouet en de verhouding tussen helm, vizier en romp. Geen armen toevoegen, geen gezicht of menselijke ogen achter het vizier toevoegen, en de figuur niet als een generieke robot herontwerpen. De lichte achtergrond van de referentiefoto hoort niet bij de figuur zelf.  
**Gewenste eerste asset:** volledig figuur als vrijstaand beeld met transparante achtergrond waar mogelijk; plus frontaal, driekwart en een kleine reeks toestandvarianten (rust, alert, verbaasd).  
**Bestandsnaamvoorstel:** `assets/characters/ridderus/ridderus-full.webp`, met bronfoto apart bewaard.

### CHAR-SCHILDJE-01 — Schildje, de schildpad

**Bronbestand:** `IMG_0199.jpeg` (1152 × 1536 px, JPEG).  
**Referentie:** echte groene pluchen schildpad met brede, licht gemêleerde groene schildvorm, korte flippers, pluizige stof, kleine lichte stik-/knopdetails en grote donkere ogen. De kop steekt naar voren en iets naar links.
**Onveranderlijke herkenningspunten:**
- zacht mosgroen, pluizig lijf;
- breed, afgerond schild met zichtbare rand en subtiele naden/strepen;
- vier korte flippers, geen lange poten;
- vooruitstekende kop met grote donkere ogen;
- klein lichtkleurig detail op het schild behouden waar zichtbaar en passend.
**Vormregels:** het blijft een kleine pluchen schildpad; geen glad reptielenpantser, schubben of spitse snuit toevoegen. Het reliëf van de stof moet in zeefdrukvorm worden vertaald via gerichte halftoon en inkttextuur, niet weggepoetst tot vlak groen.  
**Gewenste eerste asset:** volledig figuur, vrijstaand met transparante achtergrond waar mogelijk; voor het raadsel ook een duidelijke front-/driekwartpose en een kleine pose waarin Schildje iets lijkt te bewaken.  
**Bestandsnaamvoorstel:** `assets/characters/schildje/schildje-full.webp`, met bronfoto apart bewaard.

### Gedeelde assetregels voor de drie hoofdrolfiguren

- **Bronidentiteit gaat voor stijl:** behoud proporties, gezicht, kleding en kenmerkende onderdelen van het speelgoed. Stijlconversie mag details vereenvoudigen, maar mag de figuur niet vervangen door een vergelijkbaar generiek ontwerp.
- **Beeldstijl:** dezelfde verweerde, handgedrukte jarenzeventig-zeefdruk als de goedgekeurde art direction; warme crème papierkleur, grove halftoon op stof en subtiele kleurplaatverschuiving.
- **Palet:** gebruik het vastgelegde palet als omgevings- en drukpalet: oud papier `#F3DDA8`, signaalrood `#D94330`, mosterdgeel `#E9B638`, donker petrol `#174B56`, bosgroen `#28513D` en inktzwart `#292A24`. Behoud de eigen oranje, bruine, groene en cyaan identiteitskleuren wanneer de herkenbaarheid die vereist; paletconsistentie betekent niet dat de personages opnieuw worden ingekleurd.
- **Achtergrond:** losse karakterassets moeten zonder posterachtergrond bruikbaar zijn. Lever een transparante export als dat technisch lukt; anders een nette effen oud-papieren achtergrond zonder decoratieve voorwerpen.
- **Geen tekst ingebakken:** namen, dialogen en puzzeltekst worden later als echte game-tekst toegevoegd.
- **Consistentie:** ogen, contouren, textuursterkte en belichting moeten tussen de drie losse assets overeenkomen.
- **Gebruik:** uitdaging 2 heeft de figuren nodig in een leesbare raadselopstelling. Maak hun gezichten en silhouettes op iPhone-formaat herkenbaar; druktextuur mag belangrijke trekken niet verbergen.
- **Status:** de drie losse basisillustraties zijn geïdentificeerd, aanwezig en door Michel gecontroleerd. Aanvullende posevarianten zijn niet vereist voor de dossierafronding; de ontwikkelaar kan tijdens de bouw bepalen of extra varianten technisch nodig zijn.


## Hoofdrolfiguren — uitdaging 2

De drie losse illustraties staan al in de repository. De onderstaande `.jpg`-paden uit de eerdere uploadplanning zijn vervallen; gebruik de actuele `.png`-paden uit de gecontroleerde GitHub-inventaris. Michel heeft de afbeeldingen gecontroleerd.

| Asset-ID | Personage | Repositorypad / bestandsnaam |
|---|---|---|
| AST-CHARLIE-01 | Charlie | `assets/characters/charlie/AST-CHARLIE-01-charlie-screenprint.png` |
| AST-RIDDERUS-01 | RidderUs | `assets/characters/ridderus/AST-RIDDERUS-01-ridderus-screenprint.png` |
| AST-SCHILDJE-01 | Schildje | `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` |

**Bestandsafspraken**
- Michel heeft de afbeeldingen en hun technische eigenschappen gecontroleerd. Gebruik de bestaande bestanden en paden; converteer of overschrijf ze niet stilzwijgend.
- ID's zijn stabiel en worden niet gewijzigd als later een export wordt vervangen.
- Bij een latere transparante of opgeschoonde export krijgt die een aparte variantnaam, bijvoorbeeld `-transparent.png`; overschrijf het origineel niet stilzwijgend.
- Deze versie is de gekozen karakterstijl: minimalistische vectorvormen met sterke, verweerde zeefdruktextuur.
- Status: de huidige basisillustraties zijn aanwezig op de PNG-paden hierboven en door Michel gecontroleerd. Behandel deze bestanden als de goedgekeurde basisassets; verander of overschrijf ze niet stilzwijgend.

## Gekozen afwerking — karakterconceptsheet

**Beslissing:** optie A — sterke, uitgesproken verweerde zeefdruk.

Een eerste gezamenlijke conceptsheet is gegenereerd om de samenhang van de drie personages en de gekozen druktextuur te verkennen. De sheet is een **conceptreferentie**, geen goedgekeurde in-game asset en geen vervanging voor de bronfoto's. De figuren moeten nog afzonderlijk worden uitgewerkt en gecontroleerd op identiteit, proporties en details.

**Beoordelingspunten voor de volgende ronde**
1. Charlie: gezicht, oren, lichte snuit en oranje jas met twee knopen moeten overeenkomen met de bron.
2. RidderUs: geen armen; cyaan vizier, grijze helm met verticale openingen en gele pompon blijven exact herkenbaar.
3. Schildje: brede groene pluchen schildvorm, korte flippers en grote donkere ogen blijven behouden.
4. Alle drie: duidelijke silhouette en gezichtsdetails ondanks de zware inkttextuur.
5. Export: één losse basisasset per figuur, bij voorkeur met transparante achtergrond; geen ingebakken labels of tekst.
6. Status: conceptsheet blijft een stijl- en samenhangsreferentie; de drie afzonderlijke basisassets zijn aanwezig en door Michel gecontroleerd. De conceptsheet vervangt die losse assets niet.


## AST-TITLE-01 — Beginschermposter

- **Asset-ID:** `AST-TITLE-01`
- **Actuele bestandsnaam:** `AST-TITLE-01-title-poster.png`
- **Repositorypad:** `assets/title-screen/AST-TITLE-01-title-poster.png`
- Eerdere `.jpg`-verwijzingen zijn verouderd en niet leidend.
- **Gebruik:** vaste posterillustratie voor het beginscherm; animaties worden later als aparte UI-/CSS-lagen toegevoegd.
- **Inhoud:** titel “DE MYSTERIEUZE FABRIEK”, teaser “ER IS IETS VREEMDS AAN DE HAND...”, de snoepfabriek, en de vormgeving van de startknop.
- **Compositie:** verticaal, bedoeld voor iPhone-verhouding 9:19,5.
- **Personages:** geen Charlie, RidderUs of Schildje zichtbaar; hun aanwezigheid blijft een verrassing.
- **Animatieplan:** de poster zelf blijft statisch; later kunnen rook, fabrieklichtjes en startknop afzonderlijk subtiel bewegen.
- **Status:** ontwerp goedgekeurd als richting; bestand `assets/title-screen/AST-TITLE-01-title-poster.png` aanwezig en door Michel gecontroleerd.
- **Belangrijk:** als de knop in de afbeelding behouden blijft, moet later worden beslist of de volledige poster als één klikbaar vlak werkt of dat de knop grafisch wordt afgedekt/vervangen door een echte toegankelijke HTML-knop. De animaties en bediening mogen niet in de afbeeldingspixels worden ingebakken.


## Decorassets voor de controlekamer — actuele paden

De vier onderstaande illustraties staan al in de repository. De mechanische vogel blijft uitgesloten van gebruik in het spel.

| Asset-ID | Bestandsnaam | Repositorypad |
|---|---|---|
| AST-DECOR-01 | `AST-DECOR-01-red-heart.png` | `assets/decor/AST-DECOR-01-red-heart.png` |
| AST-DECOR-02 | `AST-DECOR-02-birdhouse.png` | `assets/decor/AST-DECOR-02-birdhouse.png` |
| AST-DECOR-03 | `AST-DECOR-03-mechanical-bird.png` | `assets/decor/AST-DECOR-03-mechanical-bird.png` |
| AST-DECOR-04 | `AST-DECOR-04-pitcher-terrarium.png` | `assets/decor/AST-DECOR-04-pitcher-terrarium.png` |

### Uploadafspraken

- De vier bestanden zijn conceptillustraties in dezelfde vintage vector-/zeefdrukrichting als de game.
- Elk object blijft een zelfstandige asset die later afzonderlijk in de controlekamer kan worden geplaatst.
- Status: ontwerp uitgewerkt; de vier decorbestanden staan wel in de huidige repository. Controleer de visuele inhoud voordat ze als definitieve game-assets worden behandeld.
- Gebruik de bestaande paden zoals hierboven; upload de bestanden niet opnieuw onder alternatieve extensies.
- De gegenereerde illustraties hebben momenteel een crèmekleurige achtergrond; ze zijn niet transparant.


## Gecontroleerde GitHub-inventaris

De volgende elf bestanden zijn teruggevonden onder de huidige `assets/`-paden. De Git-blobs zijn behouden. Dit bevestigt hun aanwezigheid en huidige pad, maar **niet** het werkelijke afbeeldingsformaat, de beeldafmetingen of de definitieve goedkeuringsstatus.

| Huidige bestandsnaam in GitHub-root | Voorlopige koppeling | Status / actie |
|---|---|---|
| `assets/characters/charlie/AST-CHARLIE-01-charlie-screenprint.png` | Charlie | Aanwezig; door Michel gecontroleerd |
| `assets/characters/ridderus/AST-RIDDERUS-01-ridderus-screenprint.png` | RidderUs | Aanwezig; door Michel gecontroleerd |
| `assets/characters/schildje/AST-SCHILDJE-01-schildje-screenprint.png` | Schildje | Aanwezig; bestandstype en visuele overeenkomst controleren |
| `assets/title-screen/AST-TITLE-01-title-poster.png` | Titelposter | Aanwezig; door Michel gecontroleerd |
| `assets/rooms/control-room/AST-ROOM-01-control-room-reference.png` | Vaste controlekamerreferentie | Aanwezig; door Michel gecontroleerd |
| `assets/decor/AST-DECOR-01-red-heart.png` | Rood hart | Aanwezig; PNG-formaat bevestigd door Michel; afmetingen en definitieve export controleren |
| `assets/decor/AST-DECOR-02-birdhouse.png` | Vogelhuisje met vogel | Aanwezig; door Michel gecontroleerd |
| `assets/decor/AST-DECOR-03-mechanical-bird.png` | Mechanische vogel | Aanwezig, maar uitgesloten van het spel; niet gebruiken |
| `assets/decor/AST-DECOR-04-pitcher-terrarium.png` | Vleesetende bekerplant | Aanwezig; door Michel gecontroleerd |
| `assets/rooms/toy-laboratory/AST-ENV-01.png` | Speelgoedlaboratorium | Aanwezig; door Michel gecontroleerd |
| `assets/characters/panda/AST-PANDA-01-panda-screenprint.png` | Panda | Aanwezig; door Michel gecontroleerd |

### Voorzichtig omgaan met extensies

Alle elf huidige afbeeldingsbestanden hebben een `.png`-pad in GitHub. De extensie op zichzelf bevestigt niet het interne bestandsformaat. De namen en paden zijn opgeschoond; de oorspronkelijke beeldbytes zijn behouden. De mechanische vogel staat in de map met decorassets om hem veilig te bewaren, maar mag niet in de kamercompositie of game worden gebruikt. Dit is een vaste uitsluiting, geen open ontwerpkeuze.


## Assetorganisatie — synchronisatie 25 oktober 2026

De elf aanwezige afbeeldingsbestanden met `.png`-paden staan onder `assets/characters/`, `assets/title-screen/`, `assets/rooms/control-room/`, `assets/rooms/toy-laboratory/` en `assets/decor/`. Zie [de assetaudit](ASSET-AUDIT-2026-10-25.md) voor de actuele paden. Michel heeft de afbeeldingen zelf gecontroleerd.

De elf afbeeldingsbestanden zijn aanwezig in de repository en door Michel gecontroleerd. Nieuwe afbeeldingen worden alleen gemaakt als een concrete asset ontbreekt. De ontwikkelaar kan eenvoudige puzzelobjecten en interface-elementen zelf tekenen als dat de stijl en leesbaarheid ondersteunt.
