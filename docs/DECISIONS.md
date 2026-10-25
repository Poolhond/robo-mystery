# De mysterieuze fabriek — Beslissingen en open punten

**Versie:** 2.7  
**Doel:** één betrouwbare plek voor goedgekeurde besluiten en open punten, zodat de inhoud niet telkens opnieuw wordt bedacht.

## Dossierstatus en bronvolgorde

Dit document is leidend voor de status van ontwerpkeuzes. Een keuze geldt alleen als vastgelegd wanneer die onder **Vastgelegd** staat. De overige documenten werken die keuzes inhoudelijk uit, maar mogen ze niet stilzwijgend wijzigen. Bij een tegenstrijdigheid wordt de bouw geblokkeerd totdat het punt hier is opgelost.

Bronvolgorde: (1) dit beslissingsdocument voor goedkeuring/open status, (2) `CHALLENGES.md` voor de puzzelwerking, (3) `GAME-CONCEPT.md` voor verhaal en structuur, (4) `TECH-SPEC.md` voor technische randvoorwaarden, (5) `ART-DIRECTION.md` voor stijl en (6) `ASSET-REGISTER.md` voor bestandsstatus.

**Huidige fase:** dossieropschoning. Dit is geen toestemming om gamecode te bouwen.

## Vastgelegd

| Onderwerp | Beslissing |
|---|---|
| Spelnaam | De mysterieuze fabriek (gekozen als nieuwe werktitel; robot is geschrapt) |
| Speler | Wannes (12), speelt het spel op zijn verjaardag zelf |
| Hoofdpersonage | Wannes onderzoekt de ruimte zelf; er is geen bestuurbaar hoofdpersonage |
| Feest | De onthulling aan het einde is voor Wannes |
| Finale-onthulling | De deur zwaait open en onthult een verborgen verjaardagsfeest met de speelgoedfiguren, slingers, confetti en warm licht. De sfeer verschuift van mysterie naar een warme, feestelijke verrassing. |
| Finalehandeling | Wannes drukt op een grote rode feestknop. Die activeert de lichtjes en confetti en vormt de laatste interactieve handeling van het spel. |
| Verjaardagsboodschap | Na de feestknop feliciteren de speelgoedfiguren Wannes samen met een warme, speelse boodschap. De exacte tekst wordt later uitgewerkt. |
| Echte verrassing na het spel | Na de digitale onthulling krijgt Wannes een korte opdracht die naar een echte verrassing leidt. De exacte formulering en eventuele bestemming worden later bepaald. |
| Puzzelmoeilijkheid | Leuk uitdagend: Wannes moet nadenken en goed observeren. De moeilijkheid bouwt eerlijk op; hints helpen wanneer hij vastloopt. Geen puzzel mag de voortgang blokkeren. |
| Speelduur — ontwerpbeslissing 15 | **Optie B — gebalanceerd.** Reken op ongeveer 2 minuten per hoofd uitdaging, met extra tijd voor de drie match-3-levels en de finale. De totale speelduur blijft een richtwaarde; puzzels mogen niet gehaast aanvoelen en hints moeten de voortgang toegankelijk houden. |
| Thema | Een mysterieuze speelgoedfabriek met goocheltrucs, puzzels en raadsels |
| Opbouw | Vrije verkenning van het laboratorium; uitdagingen 1–3 in zelfgekozen volgorde; uitdaging 4 is de grote deur en het slot |
| Platform | Mobile-first webspel, GitHub Pages, geen account |
| Beginscherm | Combineer een vintage filmposter met subtiele animaties: langzame schoorsteenrook, af en toe oplichtende fabrieklichtjes, een optionele tikbare easter egg en een zachte startknop-puls. Ontwerp voor iPhone-verhouding 9:19,5; titel en startknop blijven duidelijk en binnen de veilige zones. Zie `docs/ART-DIRECTION.md`. |
| Verrassing personages | Charlie, RidderUs en Schildje worden niet getoond of herkenbaar gehint op het beginscherm. De speler ontdekt hen pas tijdens het avontuur. |
| Taal | Nederlands |
| Bouwmethode | Eerst het volledige ontwerpdossier afronden en goedkeuren, daarna één master-prompt, bouwen en testen op iPhone |
| Startbeleving — vrije ontdekking | **Keuze A.** Na Start ziet Wannes de volledige technische werkplaats en kiest hij zelf welk voorwerp hij onderzoekt. Geen verplichte introductiescène of vooraf opgelegde route; de ruimte en voorwerpen wekken nieuwsgierigheid. Korte uitleg mag alleen verschijnen wanneer die bij een gekozen voorwerp of uitdaging hoort. |
| Hintsysteem | Combinatie: een discrete hintknop én een automatische hint na meerdere mislukte pogingen. Elke uitdaging heeft drie hintstappen: eerst een subtiele aanwijzing, daarna een gerichte aanwijzing en als derde stap zo nodig de oplossing of de exacte volgende handeling. Geen game-over en onbeperkt opnieuw proberen. |
| Uitdaging 1 — spelvorm | Drie eigen match-3-levels, geïnspireerd op het algemene spelprincipe van match-3-games; geen gekopieerde levels of vormgeving |
| Uitdaging 1 — schermpresentatie | Het match-3-spel speelt zich visueel af op het bestaande retro-computerscherm in de controlekamer. Na aantikken zoomt de computer in; het spelbord blijft geïntegreerd in het scherm en volgt de vastgelegde verweerde jarenzeventig-zeefdrukstijl. Geen los modern spelvenster of afwijkende stijl. |
| Uitdaging 1 — leveldoelen | Verzamel 8 rode energiecellen; verwijder 4 houten kistjes; laat de gouden energiesleutel naar de uitgang vallen |
| Aanwijzing uit uitdaging 1 | De letters B, A en L, verdiend na elk level en samen gevormd tot het woord BAL |
| Uitdaging 2 — structuur | Drie opeenvolgende deelpuzzels: code opent een geheim deurtje; logisch raadsel levert een messing sleutel; kistjesraadsel onthult de ster-met-oog-aanwijzing |
| Uitdaging 2 — schermpresentatie | Na aantikken zoomt het beeld in op de bestaande groene locker. De codepuzzel, het geheime deurtje, het personageraadsel en het kistjesraadsel spelen zich visueel af binnen/op deze locker, in dezelfde verweerde jarenzeventig-zeefdrukstijl. Geen los modern spelvenster of afwijkende grafische stijl. |
| Uitdaging 2 — code | De cijfercode is 042 |
| Uitdaging 2 — sleutelraadsel | Precies één uitspraak is waar; de aap heeft de sleutel |
| Uitdaging 2 — kistjesraadsel | Precies één uitspraak is waar; het rode kistje is de juiste keuze |
| Aanwijzing uit uitdaging 2 | Ster met een oog, gevonden in het rode kistje; het symbool verschijnt automatisch op het slot van uitdaging 4 |
| Gouden medaille | Geschrapt; niet gebruiken als beloning of inhoud van het kistje |
| Aanwijzing uit uitdaging 3 | Signaalrood |
| Uitdaging 3 — moeilijkheid | Drie rondes met respectievelijk twee, drie en vier wissels; snelheid neemt geleidelijk toe maar de beweging blijft eerlijk te volgen |
| Uitdaging 3 — schermpresentatie | Na aantikken zoomt het beeld in op de bestaande tafel met drie bekers. De bekers-truc en het rode balletje spelen zich af op deze tafel, in dezelfde verweerde jarenzeventig-zeefdrukstijl. Geen los modern spelvenster of afwijkende grafische stijl. Na afloop keert Wannes terug naar dezelfde controlekamer. |
| Uitdaging 4 — bediening | De ster met oog verschijnt automatisch na uitdaging 2; Wannes typt zelf het woord en kiest zelf een kleur; grote knop OPEN DE DEUR |
| Uitdaging 4 — oplossing | Ster met oog (uitdaging 2), woord BAL (uitdaging 1), kleur signaalrood (uitdaging 3); onbeperkte pogingen |
| Startscherm en wereld | De maquette is uitsluitend het startscherm. Na Start onderzoekt Wannes zelf de technische ruimte. |
| Technische ruimte | **Optie C — speelse werkplaats.** De vier hoofdvoorwerpen staan wat verspreider, alsof de fabriek echt gebruikt wordt, maar blijven allemaal zichtbaar op het iPhone-scherm. De ruimte mag karaktervolle details bevatten zonder rommelig te worden. De voorwerpen zijn geïntegreerd in de illustratie, zonder permanente extra pictogrammen of omlijningen. Bij aantikken zoomt het spel in op het gekozen voorwerp en opent een eigen, volledig scherm voor de uitdaging. Een duidelijke terugknop brengt Wannes terug naar dezelfde controlekamer. |
| Kleine interactieve details en easter eggs | **Drie geheimen vastgelegd.** (1) **Pandaschuif:** Wannes tikt op de lade/schuif van het meubel; één schuif gaat open, onthult kort een vierde speelgoedfiguur — een panda die nog als asset moet worden uitgewerkt — en schuift daarna vanzelf weer dicht. (2) **Vleesetende plant:** eerste tik zoomt in op de plant en start een vlieg die rondvliegt; tweede tik laat de vlieg in de bloem vliegen, waarna het klepje dichtklapt; derde tik zoomt terug uit naar het overzicht. (3) **Hartkunstwerk:** tikken zoomt in op het kunstwerk; het hart begint te kloppen en de afgebeelde mensen dansen; daarna zoomt het beeld terug uit. Alle drie zijn optioneel, geven geen puzzelvoordeel en blokkeren de hoofdvoortgang niet. |
| Voorwerpen in de technische ruimte | Computerscherm = uitdaging 1; locker met cijfercode = uitdaging 2; tafel met bekers = uitdaging 3; grote deur = uitdaging 4. |
| Vrije verkenning | Wannes kiest zelf de volgorde van uitdagingen 1, 2 en 3. Hij kan uitdaging 4 vanaf het begin ontdekken, maar de deur opent pas als alle drie voltooid zijn en woord/kleur juist zijn |
| Tussentijdse voortgang | Elke uitdaging kan worden onderbroken en hervat vanaf de exacte deelstap; opgeloste puzzels, bordstanden, relevante rondevoortgang, beloningen en slotinvoer blijven bewaard. De terugknop brengt Wannes terug naar de controlekamer. |
| Opslaan | Lokale voortgang wordt na elke betekenisvolle actie opgeslagen; herladen of later terugkomen mag geen voortgang wissen |
| Karakterset uitdaging 2 | **Charlie, RidderUs en Schildje** zijn de drie hoofdrolfiguren in het raadsel. Hun echte pluchen/figuuridentiteit en vaste herkenningspunten blijven leidend; de nieuwe verweerde zeefdrukstijl verandert die niet. Zie `docs/ASSET-REGISTER.md`. Definitieve losse assets moeten nog worden gemaakt en goedgekeurd. |
| Karakterafwerking — optie A | Gekozen: sterke, uitgesproken verweerde jarenzeventig-zeefdruk met zichtbare korrel, inktspikkels, slijtage en subtiele drukregistratie. Herkenbare gezichtsdetails en silhouetten blijven helder. De groepssheet is alleen een conceptreferentie; losse karakterassets moeten apart worden beoordeeld. |
| Bouwstatus | Oude prototypecode is niet bruikbaar als basis; er wordt geen gamecode gebouwd vóór goedkeuring van het volledige dossier |

## Nog open — ontwerp vóór de bouw

1. **Vrije laboratoriumverkenning:** de speelse werkplaats en de vier hoofdvoorwerpen liggen vast. Werk nog de exacte compositie, plaatsing en klikzones uit. De drie easter eggs zijn gekozen; werk hun timing, animaties en klikzones uit zonder dat ze de hoofdvoortgang blokkeren.
2. **Uitdaging 2 — spelersteksten:** definitieve introductie, personagedialogen, succes- en foutfeedback en afsluiting.
3. **Uitdaging 2 — hints:** schrijf de exacte drie hintstappen voor de codepuzzel en het kistjesraadsel.
4. **Uitdaging 2 — onthulling van de ster-met-oog-aanwijzing:** kies hoe de aanwijzing in de kist verschijnt (bijvoorbeeld geheim kaartje of gegraveerd plaatje). De functie blijft hetzelfde: het symbool voor uitdaging 4.
5. **Uitdaging 1 en 3:** test de definitieve match-3-startborden en bekersnelheden op iPhone; werk teksten, oplossingen en assets verder uit.
6. **Slotscène:** bepaal de exacte tekst van de opdracht die Wannes na het spel naar de echte verrassing leidt.
7. **Persoonlijke boodschap:** schrijf en keur de exacte verjaardagsboodschap van de speelgoedfiguren goed.
8. **Titelvormgeving:** de werktitel is vastgelegd als *De mysterieuze fabriek*. De definitieve grafische titeluitwerking kan later worden gemaakt; de naamkeuze zelf staat niet meer open.
9. **Puntentelling:** beslis of score nodig is; voortgang mag nooit door score worden geblokkeerd.
10. **Assets:** bepaal welke referentiebeelden definitief gebruikt worden en werk de bestanden uit in een consistente mappenstructuur.
11. **Dossiercontrole:** stem spelconcept, uitdagingen, techniek, art direction en assetregister op elkaar af vóór de master-prompt.

**Reeds vastgelegd, geen open keuze:** het kleurpalet staat vast zoals beschreven in `ART-DIRECTION.md`. De typografie gebruikt systeemlettertypen met een zwaar, grafisch karakter; er komen geen externe fonts.

## Assets die nog moeten worden gecontroleerd of gemaakt

- Aap, panda, schildpad en regenboogoctopus.
- Achtergronden per uitdaging.
- Klein metalen deurtje en groot slot/deur.
- Cijferwieltjes en OPEN-knop.
- Messing sleutel.
- Drie kistjes (rood, blauw, geel) en de ster-met-oog-aanwijzing in het rode kistje.
- Drie bekers en rood balletje.
- Doek, goochelvoorwerpen, knoppen, iconen en finale-/feestscène.
- Drie decoratieve interactieve details/easter eggs voor de technische ruimte; exacte lijst nog te bepalen.

Geef assets consistente namen en leg per bestand vast voor welke scène het dient. De negen huidige rootbestanden zijn geüpload, maar niet alle in het assetregister genoemde exports zijn daarmee aanwezig; onderscheid bestaande bestanden van concepten en nog te maken exports.

## Werkvolgorde

1. Werk de technische ruimte verder uit: exacte compositie, plaatsing en klikzones van de vier hoofdvoorwerpen; kies daarnaast precies drie optionele interactieve details/easter eggs.
2. Werk de resterende spelersteksten, hints, schermtoestanden en finale af.
3. Controleer en voeg de definitieve assets toe; stem het assetregister af op het spelconcept.
4. Controleer het volledige dossier op tegenstrijdigheden.
5. Schrijf pas daarna de master-prompt.
6. Bouw de nieuwe game vanaf een schone basis, test op iPhone en voer één gerichte fixronde uit.

## Belangrijke afbakening

- De drie puzzels van uitdaging 2 zijn onderdelen van één hoofd uitdaging, niet drie aparte hoofd uitdagingen.
- Wannes kiest zelf de volgorde van uitdagingen 1, 2 en 3; het laboratorium is vrij te verkennen.
- Wannes mag midden in een uitdaging stoppen en naar een andere gaan. Elke uitdaging hervat op de precieze plek waar hij gebleven was, ook na het sluiten en opnieuw openen van het spel.
- Uitdaging 4 is vanaf het begin te ontdekken maar pas op te lossen na voltooiing van alle drie de andere uitdagingen.
- Bij uitdaging 4 verschijnt de ster met het oog automatisch na uitdaging 2. Wannes typt zelf BAL en kiest zelf signaalrood.
- Uitdaging 1 is een match-3-game met drie levels; de beloningen zijn achtereenvolgens B, A en L, samen BAL.
- De ster met het oog is de beloning van uitdaging 2; BAL is niet langer de beloning van uitdaging 2.
- De kist in uitdaging 2 bevat de **ster met een oog**, de symboolaanwijzing voor uitdaging 4 — geen gouden medaille. BAL komt uit uitdaging 1.
- De oude index.html-prototypecode wordt verwijderd en mag niet als basis voor de nieuwe game worden gebruikt.
- Er is geen robotpersonage; de oude robotasset is vervallen en mag niet in de game worden gebruikt.
- Er wordt geen nieuwe gamecode gebouwd zolang het volledige ontwerpdossier niet is goedgekeurd.
