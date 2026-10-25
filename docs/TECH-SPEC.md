# De mysterieuze fabriek — Technische specificatie

**Versie:** 1.4  
**Status:** Specificatie voor één zelfstandige bouwopdracht. Na goedkeuring van het dossier wordt deze specificatie samen met de master-prompt gebruikt om het volledige spel te laten bouwen, testen en opleveren. Er wordt geen aparte voorafgaande technische uitwerkronde vereist.  
**Samenhang:** `docs/GAME-CONCEPT.md`, `docs/CHALLENGES.md`, `docs/DECISIONS.md` en `docs/ART-DIRECTION.md` zijn leidend voor respectievelijk spelverloop, puzzels, goedgekeurde ontwerpkeuzes en visuele stijl. Bij tegenstrijdigheid moet de afwijking eerst in het dossier worden opgelost.

## 1. Platform en grenzen

- Statische webapp, gehost op GitHub Pages.
- Mobile-first; primair iPhone Safari in portret. Ook bruikbaar op iPad en desktop.
- Geen account, server, tracking, advertenties, aankopen of externe diensten.
- Geen frameworks, externe bibliotheken, externe scripts of externe lettertypen.
- Het spel is volledig stil: geen muziek, geluidseffecten, gesproken tekst of audiobestanden.
- Start pas met de implementatie wanneer de master-prompt en het dossier expliciet zijn goedgekeurd. Daarna voert de gameontwikkelaar de volledige bouw, technische uitwerking, tests, foutopsporing en correcties zelfstandig uit.

## 2. Bestands- en padregels

De precieze mappenstructuur wordt afgestemd op het assetregister vóór de bouw. De beoogde minimale structuur is:

```
index.html
style.css
game.js
content.js
assets/
  characters/
  rooms/
  title-screen/
  puzzles/
  decor/
  ui/
docs/
```

- Gebruik URL-paden relatief aan de app, zoals `assets/rooms/control-room/example.png`; gebruik geen absolute paden die met `/` beginnen. GitHub Pages publiceert de app onder een repository-subpad.
- Gebruik alleen bestanden die in `docs/ASSET-REGISTER.md` zijn opgenomen en waarvan de werkelijke bestandstypen gecontroleerd zijn.
- Geen verwijzing naar een audio-map of audiobestand.
- De uiteindelijke bestandsnamen en assetlocaties moeten overeenkomen met het assetregister. Geen namen of bestanden verzinnen.

## 3. Tekst, puzzelinhoud en presentatie

- Spelergerichte teksten, puzzelstellingen, hints, feedback en eindteksten worden op één beheersbare plek bijgehouden, bij voorkeur in `content.js`; presentatie en spelstatus blijven daarvan gescheiden.
- De naam Wannes en de goedgekeurde eindtekst worden centraal beheerd. De eindtekst is exact: **“Proficiat Wannes!”** gevolgd door **“Dat verdient een cadeau.”**
- Alle essentiële tekst blijft echte HTML-tekst en wordt niet uitsluitend in een afbeelding ingebakken.
- De technische implementatie mag de vastgelegde puzzelregels, volgorde, antwoorden, hints of eindscène niet zelfstandig aanpassen. De ontwikkelaar kiest zelfstandig de technische middelen om die goedgekeurde werking betrouwbaar te realiseren.

## 4. Schermen en stabiele toestands-ID's

Onderstaande ID's zijn technische namen, geen zichtbare spelertekst. De precieze visuele inhoud volgt het concept- en uitdagingen-dossier.

| ID | Betekenis | Belangrijk gedrag |
|---|---|---|
| `title` | Titelposter | Biedt START / VERDER SPELEN en een kleinere optie “Opnieuw beginnen” met bevestiging. |
| `workshop` | Volledige werkplaats | Alle vier hoofdobjecten blijven zichtbaar; vrije verkenning. |
| `match3` | Computer / uitdaging 1 | Drie match-3-niveaus; bewaart huidig bord en deelvoortgang. |
| `locker` | Groene locker / uitdaging 2 | Code 042 en de volledige logica-/kistketen; bewaart elke deelstap. |
| `cups` | Bekers / uitdaging 3 | Drie rondes; bewaart ronde, balpositie en voortgang. |
| `door` | Grote rode deur / slot | Deur is steeds onderzoekbaar; slot kan onvolledig zijn en toont feedback bij invoer. |
| `finale` | Feestfinale | Alleen bereikbaar na de juiste combinatie; voert de goedgekeurde feestsequentie uit. |

Een puzzel kan intern extra substaten hebben. De ontwikkelaar bepaalt de interne implementatie en documenteert die waar nuttig; elke zichtbare toestand en noodzakelijke overgang moet wel overeenkomen met `docs/SCREEN-SPEC.md`. Een modal of hintpaneel is geen zelfstandige wereldlocatie.

### Navigatie

- Na START komt de speler in de werkplaats; er is geen verplichte proloog.
- Elke uitdaging zoomt in op het betreffende object. De terugknop brengt de speler terug naar dezelfde werkplaatsweergave.
- Teruggaan of van scherm wisselen reset nooit de puzzel.
- De grote deur mag op elk moment worden onderzocht. De deur gaat pas open wanneer alle drie uitdagingen voltooid zijn en de juiste combinatie is ingevoerd.
- De optionele easter eggs veranderen de hoofdvoortgang niet.

### Uitgewerkte deeltoestanden

De bovenstaande hoofdschermen zijn verder opgesplitst in stabiele toestands-ID's in [`docs/SCREEN-SPEC.md`](SCREEN-SPEC.md). Dat document is leidend voor zichtbare deeltoestanden, spelersteksten, fout- en succesfeedback, hinttoestanden, finaleovergangen en herstel na herladen. De scherm-ID's moeten in de implementatie herkenbaar blijven, ook als de interne code andere namen gebruikt.

## 5. Spelstatus en voortgang

Bewaar één versieerbaar statusobject. De definitieve interne namen mogen verschillen, maar moeten minstens onderstaande informatie ondubbelzinnig afdekken:

- schema-/versienummer voor migratie en validatie;
- huidige scherm en terugkeerlocatie in de werkplaats;
- voltooiingsstatus van elk van de drie uitdagingen;
- exacte voortgang per uitdaging, inclusief relevante deelstappen;
- match-3-niveau, exacte bordstand, lopende animatie-/doelstatus en reeds behaalde letters; alle drie levels hebben geen zettenlimiet of timer;
- locker-/logicapuzzelstappen, gevonden sleutel en ster-met-oog-aanwijzing;
- bekerronde, aantal wissels en huidige positie van de rode bal;
- invoerstatus van BAL en signaalrood, inclusief of de deur geopend is;
- hints per puzzelscherm: huidig hintniveau en of de oplossing is aangevraagd/getoond;
- finale-status zodat herladen geen feestsequentie onbedoeld opnieuw start;
- optionele easter-eggstatus, indien die wordt onthouden.

### Opslaan en hervatten

- Sla na elke betekenisvolle voortgangsactie op, niet alleen wanneer een uitdaging volledig is afgerond.
- Bewaar alleen serialiseerbare gegevens; sla geen DOM-elementen, callbacks of tijdelijke animatieobjecten op.
- Bij terugkeer naar een puzzel wordt de laatst opgeslagen deelstap hersteld.
- Bij herladen, Safari afsluiten en opnieuw openen of tijdelijk verlies van focus mag geldige opgeslagen voortgang niet verloren gaan.
- De titel toont **VERDER SPELEN** als er geldige bewaarde voortgang bestaat. START wordt gebruikt wanneer er nog geen voortgang is.
- “Opnieuw beginnen” vereist een duidelijke bevestigingsvraag. Alleen na bevestiging wordt de opgeslagen spelvoortgang gewist en de beginsituatie geladen.

### Ontbrekende of beschadigde opslag

- Geen bestaande opslag: start met een schone beginsituatie.
- Onleesbare, ongeldige of niet-ondersteunde opslag: laat de app niet crashen. Toon op de titel een begrijpelijke melding dat de voortgang niet kon worden hersteld, en bied aan opnieuw te beginnen.
- Verwijder beschadigde data pas nadat de speler de herstel-/herstartkeuze heeft bevestigd; overschrijf niet stilzwijgend mogelijk herstelbare voortgang.
- Als `localStorage` niet beschikbaar is, mag het spel in een tijdelijke sessie speelbaar blijven, maar moet duidelijk zijn dat voortgang bij sluiten of herladen niet gegarandeerd bewaard blijft.
- Gebruik een opslagversie en valideer de verplichte velden voordat status wordt hersteld. Een migratie mag geen voortgang of puzzelregels verzinnen.

## 6. Hintpaneel: vaste interactieregels

Deze regels zijn al goedgekeurd en mogen tijdens implementatie niet opnieuw ontworpen worden.

- Elke puzzel heeft een eigen `?`-knop en eigen hintstatus. Hints verschijnen uitsluitend wanneer Wannes er zelf om vraagt; nooit automatisch na fouten of herhaalde pogingen.
- De hintstatus is gekoppeld aan de puzzel. Bij verlaten van die puzzel sluit het paneel uit beeld; bij terugkeer blijft de voortgang bewaard en wordt het laatst bekeken hintniveau hervat.
- Het paneel heeft drie stippen voor de drie hintniveaus en één knop **VOLGENDE HINT**.
- Na hint 3 verandert de knop in **TOON OPLOSSING**.
- Dit opent de bevestiging **“Wil je de oplossing zien?”** met **BEKIJKEN** en **TERUG**.
- Na bevestiging toont de oplossing de exacte volgende handeling. Het juiste element pulseert subtiel totdat de speler die handeling uitvoert.
- Na een geslaagde actie sluit het paneel automatisch. De `?` blijft beschikbaar; bij opnieuw openen wordt het laatst bekeken hintniveau getoond.
- De hints en oplossing mogen geen voortgang veranderen totdat de speler de aangegeven puzzelhandeling zelf uitvoert.

## 7. Puzzelbetrouwbaarheid en zelfstandige verificatie

- De inhoudelijke regels en correcte oplossingen staan in `docs/CHALLENGES.md`; deze technische specificatie verandert ze niet.
- De ontwikkelaar is verantwoordelijk voor het ontwerpen en genereren van concrete beginborden, testdata en interne puzzeltoestanden. Michel hoeft vooraf geen matrices, zetreeksen, solverresultaten of technisch bewijs aan te leveren.
- Match-3-borden moeten volgens de vastgelegde regels speelbaar zijn. Alle drie levels gebruiken een raster van 5 × 7, vier effen kleurvlakken zonder symbolen, willekeurige aanvulling en geen zettenlimiet, timer of straf. De ontwikkelaar genereert een geldige starttoestand zonder ongewenste automatische matches, controleert dat er minstens één geldige zet is en controleert dat het doel haalbaar blijft.
- Level 2 moet vijf kisten correct verwijderen wanneer een geldige match direct naast ze plaatsvindt, ook wanneer meerdere kisten door dezelfde match of cascade geraakt worden. De kistvoortgang mag nooit teruglopen.
- Level 3 moet de gouden sleutel logisch verticaal laten vallen wanneer de ruimte eronder vrijkomt, tot ze de uitgang onderaan bereikt.
- Na elke zet moet de logische bordtoestand worden berekend en gevalideerd; animaties tonen diezelfde uitkomst in begrijpelijke stappen. De spelstatus mag geen tegenstrijdige of dubbele verwerking van een tik bevatten.
- Als er geen geldige zet bestaat, schud de ontwikkelaar het bord gecontroleerd opnieuw. Behaalde doelvoortgang en verwijderde doelobjecten blijven behouden.
- Test cascades, randgevallen, herhaald tikken, snel opeenvolgende invoer, navigatie tijdens of na animaties, herladen en herstel. Los gevonden fouten zelfstandig op en herhaal de relevante tests.
- Bij bekers moet de actuele balpositie ondubbelzinnig worden bijgehouden; de animatie mag de logische positie niet wijzigen of verbergen.
- Foute invoer geeft duidelijke feedback en wist geen eerder verdiende aanwijzingen of voltooide uitdagingen.
- De ster-met-oog-aanwijzing verschijnt automatisch zodra de relevante kistuitdaging is voltooid. BAL en signaalrood voert Wannes zelf in/selecteert hij zelf bij de deur.
- De feestfinale kan maar één keer als nieuwe voortgangsovergang worden geactiveerd. Herladen tijdens de finale mag geen extra puzzel of extra verplichte tik introduceren.

## 8. Mobiel en toegankelijkheid

- Tikbediening; geen hover, rechtsklik of dubbelklik als noodzakelijke interactie.
- Richtmaat voor tikvlakken: minimaal 44 × 44 CSS-pixels.
- Gebruik `width=device-width, initial-scale=1, viewport-fit=cover`, veilige schermranden via `env(safe-area-inset-*)` en passende hoogte-eenheden zoals `100svh`.
- Geen horizontale pagina-scroll. Gewone lopende tekst is bij voorkeur minimaal 16 px en blijft binnen het scherm.
- Voorkom onbedoelde tekstselectie en dubbelklik-zoom waar dat de spelbediening hindert, zonder standaard browsergedrag onnodig uit te schakelen.
- Respecteer `prefers-reduced-motion`; belangrijke informatie mag niet uitsluitend door beweging worden overgebracht.
- Ontwerp en test in iPhone-portret eerst, en controleer daarna iPad en desktop.

## 9. Assets, prestaties en foutafhandeling

- Assetnamen, rol, bestandstype en status moeten overeenkomen met `docs/ASSET-REGISTER.md`.
- Laad alleen noodzakelijke assets en voorkom timers/animaties die blijven lopen wanneer de speler een scherm verlaat.
- Als een afbeelding ontbreekt, blijft de app bruikbaar en toont ze een eenvoudige, herkenbare fallback; ontbrekende assets mogen geen stille crash veroorzaken.
- Geen geluid of audiobediening.
- Gebruik kleurvariabelen en de visuele stijl uit `docs/ART-DIRECTION.md`; gebruik geen nieuwe stijl of beeldtaal zonder het dossier aan te passen.

## 10. Acceptatietests vóór oplevering

De gameontwikkelaar voert onderstaande tests zelfstandig uit, herstelt fouten die hij vindt en herhaalt de relevante tests. De implementatie is pas klaar wanneer alle onderstaande controles zijn geslaagd. Voeg waar nuttig geautomatiseerde tests toe; controleer interactieve animaties en mobiele bediening daarnaast ook handmatig:

1. **Start:** START opent de werkplaats; VERDER SPELEN verschijnt bij geldige opgeslagen voortgang; “Opnieuw beginnen” vraagt bevestiging.
2. **Vrije volgorde:** de drie uitdagingen kunnen in iedere volgorde worden gespeeld.
3. **Match-3:** Level 1 verzamelt 10 rode energiecellen en geeft B; Level 2 verwijdert 5 houten kistjes en geeft A; Level 3 laat de gouden sleutel naar de uitgang onderaan vallen en geeft L. Alle drie gebruiken 5 × 7 en hebben geen zettenlimiet of timer. De ontwikkelaar genereert en test zelf geldige beginborden en representatieve testtoestanden. Geldige/ongeldige zetten, animaties, aanvulling, cascades, vastlopende-bordherstel en hervatten werken correct; letters en exacte bordstatus blijven bewaard.
4. **Locker:** code 042, personagelogica, kistlogica, sleutel en ster-met-oog volgen exact het uitdagingen-dossier.
5. **Bekers:** de drie rondes volgen de vastgelegde wisselaantallen; de balpositie en ronde blijven correct na terugkeer en herladen.
6. **Deur:** kan vroeg worden bekeken maar opent niet vóór voltooiing van alle uitdagingen; correcte combinatie opent de deur, foutieve combinatie wist geen voortgang.
7. **Hints:** er verschijnt niets automatisch; elke puzzel behoudt eigen hintstatus; alle drie hints, oplossing bevestigen, teruggaan en subtiele pulsering werken volgens §6.
8. **Navigatie:** heen en terug tussen werkplaats en uitdaging behoudt de exacte deelstap.
9. **Opslag:** herladen en opnieuw openen van Safari herstellen geldige voortgang; lege, beschadigde en niet-ondersteunde opslag veroorzaken geen crash en leiden niet tot stilzwijgend dataverlies.
10. **Finale:** deur opent naar de feestscène; grote rode knop start de visuele feestreactie; tekst verschijnt in de juiste volgorde en exact zoals vastgelegd; geen extra actie, puzzel of geluid.
11. **Easter eggs:** de drie goedgekeurde easter eggs zijn optioneel en beïnvloeden de hoofdvoortgang niet.
12. **Hosting:** alle assetpaden werken op de GitHub Pages-repository-subpath; er zijn geen onbedoelde absolute paden, externe afhankelijkheden of consolefouten.
13. **iPhone Safari:** tekst, overlays, knoppen, veilige schermranden, terugknoppen en animaties werken in portret; er is geen horizontale scroll.
14. **Andere schermen:** iPad en desktop blijven bruikbaar.
15. **Stilte en beweging:** geen audio wordt geladen of afgespeeld; verminderde beweging wordt gerespecteerd.

## 11. Wat niet gebouwd wordt

- Accounts, ranglijsten, netwerkfuncties, tracking, advertenties of aankopen.
- Verplichte proloog of extra opdracht na de goedgekeurde eindtekst.
- Audio, gesproken tekst of geluidseffecten.
- Verborgen resetgebaar dat de goedgekeurde titelbediening vervangt.
- Extra puzzels, personages of regels die niet in het dossier zijn goedgekeurd.

## 12. Werkwijze met één master-prompt

Deze specificatie wordt samen met het goedgekeurde projectdossier en de repository-assets aan de gameontwikkelaar gegeven via één uitgebreide master-prompt. De opdracht moet de ontwikkelaar verplichten om zelfstandig:

1. de repository, documenten en aanwezige assets te inspecteren voordat hij wijzigingen aanbrengt;
2. te signaleren welke bestanden ontbreken of onduidelijk zijn en assets veilig te controleren en correct te organiseren zonder originele bestanden stilzwijgend te verliezen;
3. het complete spel vanaf een schone, passende structuur te implementeren, zonder een aparte tussenronde waarin Michel technische details moet uitwerken;
4. zelf de concrete beginborden, interne toestanden, animaties en testgevallen te genereren;
5. alle acceptatietests uit §10 uit te voeren, inclusief de drie match-3-levels, opslag/herstel, schermovergangen, hints, finale en GitHub Pages-subpad;
6. gevonden bugs en technische tekortkomingen zelfstandig te herstellen en de relevante tests opnieuw uit te voeren;
7. te controleren dat het resultaat zonder externe afhankelijkheden werkt op iPhone Safari in portret en bruikbaar blijft op iPad en desktop;
8. een beknopt opleverrapport te geven met wat gebouwd is, welke tests zijn uitgevoerd, eventuele resterende beperkingen en de gepubliceerde URL.

### Wat vooraf nodig is en wat niet

Vóór de master-prompt moeten echte ontwerptegenstrijdigheden, ontbrekende essentiële assets en onduidelijke spelersgerichte regels worden opgelost. De ontwikkelaar mag geen nieuwe goedgekeurde ontwerpkeuzes verzinnen.

Het is **niet** nodig om vooraf concrete match-3-matrices, zetreeksen, solverbewijs, interne datamodellen, animatiecode of elk technisch randgeval afzonderlijk uit te werken. Dat zijn uitvoerings- en kwaliteitsverantwoordelijkheden van de ontwikkelaar. De ontwikkelaar moet deze onderdelen tijdens het bouwen zelf realiseren, testen en corrigeren binnen de vastgelegde spelregels.

De specificatie beschrijft dus de gewenste uitkomst en de kwaliteitscriteria; zij schrijft niet elke interne technische stap voor.
