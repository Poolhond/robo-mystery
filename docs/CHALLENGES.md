# De mysterieuze fabriek — Uitdagingen

**Versie:** 1.3  
**Status:** Uitgewerkt voorontwerp; nog niet bouwklaar. Er wordt nog geen gamecode gebouwd.  
**Focus van deze revisie:** vrije verkenning van het laboratorium; uitdaging 4 vereenvoudigd tot woord en kleur, met automatische symboolherkenning.

## Algemene spelregels

- Het laboratorium is één verkenbare omgeving. Wannes kiest zelf in welke volgorde hij uitdaging 1, 2 en 3 speelt.
- Wannes mag een uitdaging op elk moment verlaten en later hervatten. De game bewaart de exacte voortgang binnen elke uitdaging, niet alleen de status voltooid/niet voltooid.
- Alle opgeloste deelpuzzels, verdiende letters en aanwijzingen blijven bewaard bij het wisselen van uitdaging, het herladen van de pagina en het opnieuw openen van het spel.
- De grote deur en uitdaging 4 zijn vanaf het begin te ontdekken, maar kunnen pas volledig worden opgelost wanneer uitdagingen 1, 2 en 3 voltooid zijn.
- Uitdagingen 1, 2 en 3 leveren samen een woord, een symbool en een kleur op. Het symbool verschijnt automatisch op het slot zodra uitdaging 2 voltooid is.
- Fouten mogen de speler niet onherroepelijk blokkeren. Geef feedback, hints en nieuwe kansen.
- Het spel is Nederlandstalig, mobile-first en geschikt voor bediening op een iPhone.
- De verjaardagsverrassing blijft verborgen tot de deur in uitdaging 4 opengaat.

## Uitdaging 1 — De speelgoedfabriek

**Status:** ontwerp vastgelegd op hoofdlijnen; nog geen gamecode.  
**Spelvorm:** drie korte match-3-levels, geïnspireerd op het algemene spelprincipe van Royal Match. Gebruik geen gekopieerde levels, artwork, personages, interface of merkspecifieke vormgeving. De eigen wereld is een retro-futuristisch speelgoedlaboratorium in handgedrukte popartstijl.

**Doel in het verhaal:** het fabriekssysteem is uitgevallen. Wannes herstelt het zelf door drie opeenvolgende puzzellevels. Elk level levert één letter op. Na level 3 vormt hij het woord **BAL**. Dit is de woordaanwijzing voor het grote slot in uitdaging 4.

**Beloning van uitdaging 1:** de letters **B**, **A** en **L**, in die volgorde, die samen **BAL** vormen.  
**Beloning die hier vervalt:** de ster met het oog hoort niet langer bij uitdaging 1. Die wordt voortaan verdiend in **uitdaging 2**.  
**Geschatte speelduur:** ongeveer 3 minuten, afhankelijk van het aantal pogingen.  
**Bediening:** tik op een symbool en vervolgens op een direct aangrenzend symbool om ze te verwisselen. Het bord en alle belangrijke bediening blijven zichtbaar op een iPhone in staande stand.

**Visuele presentatie:** het match-3-spel verschijnt alsof het op de bestaande retro-computermonitor in de controlekamer draait. Wanneer Wannes de computer aantikt, zoomt de camera in op de monitor en wordt het spelbord daarop zichtbaar, met de bestaande verweerde jarenzeventig-zeefdrukstijl, korrel, inktspikkels en het vastgelegde kleurpalet. Het wordt geen los modern gamevenster en krijgt geen afwijkende grafische stijl. De spelbediening moet wel groot en duidelijk genoeg blijven voor iPhone in staande stand.

### Gemeenschappelijke spelregels voor de drie levels

- Het speelbord gebruikt per level de speelstukken die in de levelbeschrijving zijn vastgelegd. In Level 1 zijn dit effen kleurvlakken zonder symbolen of pictogrammen; andere levels kunnen alleen eigen vormen of obstakels gebruiken als die expliciet in hun beschrijving staan.
- Een geldige zet verwisselt twee horizontaal of verticaal aangrenzende symbolen.
- Een verwisseling telt alleen als er daardoor een match van minstens drie gelijke symbolen ontstaat. Als geen match ontstaat, bewegen de symbolen terug en wordt geen zet verbruikt.
- Een match verwijdert de passende symbolen; symbolen erboven vallen naar beneden en nieuwe symbolen vullen de lege plaatsen aan.
- Doelobjecten en obstakels moeten visueel anders zijn dan gewone match-symbolen.
- Het doel en de relevante voortgang staan steeds duidelijk in beeld, zonder kleine tekst. Een zettenlimiet wordt alleen getoond bij levels waarvoor die expliciet is vastgelegd; Level 1 heeft geen zettenlimiet.
- Animaties zijn kort maar leesbaar. In Level 1 worden verwisseling, match, verdwijnen, vallen, aanvullen en cascades afzonderlijk en in begrijpelijke volgorde geanimeerd.
- De zetlimiet is levelspecifiek en geldt alleen waar die expliciet is vastgelegd. Level 1 heeft onbeperkt zetten. Voor elk level moet het bord volgens de eigen regels speelbaar zijn. Wannes kan via de `?`-knop een hint vragen; hints verschijnen nooit automatisch.
- Er is geen game-over en geen tijdslimiet. Wannes mag rustig nadenken en opnieuw proberen.
- Een hint mag een mogelijke zet laten oplichten, maar voert die niet automatisch uit.
- Bij voltooiing krijgt Wannes een korte succesanimatie en de bijbehorende letter. De letter blijft zichtbaar in een vaste verzamelstrook boven of onder het bord.
- De game bewaart voortgang lokaal na elke geldige zet en bij elke belangrijke wijziging, zodat een onbedoelde herlaadactie geen reeds verdiende letters of de huidige puzzelstand wist.
- Als Wannes de speelgoedfabriek verlaat en terugkomt, gaat hij verder vanaf het huidige level, met dezelfde bordstand, eventuele resterende zetten en verzamelde voortgang. Een level wordt alleen opnieuw gestart als Wannes daar zelf voor kiest of expliciet om een reset vraagt.

### Level 1 — De energiecellen

**Status:** inhoudelijke levelbeschrijving voor het dossier; nog geen gamecode. Dit werkt de bestaande doelstelling uit en wijzigt de vastgelegde hoofdstructuur niet.

#### 1. Verhaal en bedoeling

De computer in de controlekamer toont een beeld van het stilgevallen energiesysteem. De fabriek is donker en een deel van de installatie is uitgevallen. Op de monitor is een klein circuit zichtbaar waarvan de rode energie-indicatoren uit zijn. Wannes moet het circuit opnieuw opstarten door **10 rode energiecellen** te verzamelen.

Dit is het eerste van de drie match-3-levels. Het leert Wannes het basisprincipe zonder extra obstakels: effen kleurvlakken verwisselen, drie of meer kleurvlakken van dezelfde kleur combineren en de animatie van verdwijnen, vallen en aanvullen volgen. Het level mag uitdagend aanvoelen, maar moet onmiddellijk begrijpelijk zijn en vlot reageren.

Wanneer het level is opgelost, verdient Wannes de letter **B**. Die blijft bewaard voor het geheime woord **BAL**, dat pas compleet wordt na level 3.

#### 2. Wat Wannes op het iPhone-scherm ziet

De computer wordt de speelruimte; het spel verschijnt niet als een modern venster boven op de illustratie. De camera zoomt vanaf de werkplaats in op de bestaande computermonitor. De monitor, de metalen behuizing, knoppen, schroeven en een paar kabels blijven rond de speelruimte zichtbaar, zodat het duidelijk dezelfde fabriek blijft.

De monitor zelf toont één samenhangende, verticale spelcompositie:

1. **Kop van het scherm:** een klein technisch label met de naam **ENERGIECIRCUIT 01**. De voortgang **0/10** staat in grote, duidelijk leesbare cijfers. Er is geen zettenlimiet en geen tijdslimiet. De voortgang is informatie, geen decoratie.
2. **Centrale speelruimte:** één compact raster van effen kleurvlakken, zonder symbolen of pictogrammen op de vlakken. Dit is het grootste en belangrijkste onderdeel van het scherm. Het bord moet op een iPhone in staande stand zichtbaar en bedienbaar blijven; belangrijke informatie mag niet buiten het scherm vallen.
3. **Korte opdracht:** een kleine strook op de monitor toont: **VERZAMEL 10 RODE ENERGIECELLEN**. De opdracht blijft beschikbaar tijdens het spelen, maar mag het bord niet verdringen.
4. **Bediening:** een duidelijke `?`-knop voor hints. Een knop om het level opnieuw te starten mag bestaan, maar mag niet even dominant zijn als het bord of de opdracht. Opnieuw starten wist alleen de huidige levelpoging na een bewuste keuze.
5. **Beloning:** de letter B wordt pas bij succes prominent getoond. Vóór succes kan er een kleine vaste verzamelstrook met de positie van de drie letters zichtbaar zijn: **_ _ _**. De strook maakt duidelijk dat de levelbeloningen samen één woord vormen, maar verklapt BAL niet vooraf.

De volledige spelcompositie moet aanvoelen als één handgedrukte jarenzeventig-popartposter die op de computermonitor zichtbaar is. Het bord is geen los modern spelvenster. De speelstukken zijn effen, duidelijk van elkaar gescheiden kleurvlakken zonder pictogrammen of symbolen; de posterstijl komt uit de compositie, omliggende machine-illustratie, krachtige contouren, drukregistratie, halftoon en verweerde inkt, niet uit decoratie op elk speelvlak. De compositie is grafisch en geïllustreerd, niet opgebouwd uit standaard witte afgeronde tegels. Het geheel volgt de goedgekeurde jarenzeventig-zeefdrukstijl: oud papier `#F3DDA8`, signaalrood `#D94330`, mosterdgeel `#E9B638`, donker petrol `#174B56`, bosgroen `#28513D` en inktzwart `#292A24`. Gebruik sterke getekende contouren, ingedrukte inktvlakken, halftoon en plaatselijk versleten drukwerk. De textuur mag de illustratie karakter geven, maar mag cijfers, doelen of symbolen nooit onleesbaar maken. Geen gradients als standaard en geen emoji als eindasset.

#### 3. De vier kleurvlakken

De speelstukken zijn uitsluitend effen kleurvlakken. Er staan geen symbolen, pictogrammen, letters of illustraties op de vlakken. Omdat kleur het spelmechanisme is, moeten de kleuren voldoende contrast met elkaar hebben en consistent blijven.

- **Signaalrood:** de doelkleur. Rode vlakken tellen mee wanneer ze in een match verdwijnen.
- **Mosterdgeel, donker petrol/blauw en bosgroen:** de andere speelkleuren. Ze dienen om combinaties te maken en het bord te veranderen; ze tellen niet mee voor het doel.

Elk vlak heeft een effen kleurvlak als binnenkant en een sobere, duidelijke rand zodat de grenzen ook tijdens animaties leesbaar blijven. De zeefdruktextuur hoort vooral in de omliggende posterillustratie en de paneelranden. Op de kleine speelvlakken mag hoogstens een lichte, gelijkmatige inktkorrel zichtbaar zijn; geen patronen die als symbolen kunnen worden gelezen. Alle kleuren zijn gewone verwisselbare speelstukken; er zijn in dit eerste level geen obstakels of speciale stukken.

#### 4. Bord en beginsituatie

Het speelbord is een vast raster van **5 kolommen bij 7 rijen** (5 × 7), dus 35 vakken in totaal. Deze rasterafmeting ligt vast en mag tijdens de bouw niet worden gewijzigd. Het bord bevat uitsluitend effen kleurvlakken, zonder symbolen of pictogrammen. De exacte beginmatrix wordt als onderdeel van de technische uitwerking gecontroleerd. De gekozen beginsituatie moet aan alle voorwaarden voldoen:

- Er is onmiddellijk minstens één geldige zet.
- Een geldige zet betekent dat de verwisseling twee horizontaal of verticaal direct aangrenzende kleurvlakken betreft en een match van minstens drie vlakken van dezelfde kleur oplevert.
- Het startbord bevat geen automatische match die al verdwijnt voordat Wannes een actie uitvoert.
- Het doel van 10 rode energiecellen is haalbaar zonder zettenlimiet.
- De eerste kans is begrijpelijk zonder dat het spel automatisch een zet uitvoert.
- Als het bord geen geldige zet meer heeft, wordt het op een gecontroleerde manier opnieuw geschud. Dit mag de verzamelde voortgang niet veranderen.

Het speelbord start met een gecontroleerde beginopstelling, maar daarna worden nieuwe symbolen willekeurig aangevuld — niet volgens een vooraf vastgelegde of herhalende aanvulvolgorde. De willekeur moet echt zijn binnen de gekozen verdeling van de vier symbolen. De game controleert na het aanvullen of er geldige zetten mogelijk blijven; als er geen geldige zet meer is, wordt het bord opnieuw geschud zonder verzamelde energiecellen te verliezen. Omdat er geen zettenlimiet is, hoeft het spel geen vooraf bepaalde reeks zetten af te dwingen om het doel haalbaar te maken.

#### 5. Spelregels tijdens het spelen

1. Wannes tikt één kleurvlak aan; het krijgt een sobere, duidelijke selectie-indicatie.
2. Wannes tikt daarna op een horizontaal of verticaal aangrenzend kleurvlak. Er hoeft geen aparte bevestigingsknop te worden gebruikt.
3. Als de verwisseling geen match van minstens drie oplevert, schuiven de stukken direct en soepel terug. Er wordt geen zet afgetrokken en er volgt geen straf.
4. Als de verwisseling wel een match oplevert, verdwijnen de aaneengesloten drie of meer kleurvlakken van dezelfde kleur.
5. Alleen rode kleurvlakken die door een match verdwijnen verhogen de teller. Matches van andere kleuren tellen niet voor het doel, maar veranderen het bord en kunnen nieuwe kansen creëren.
6. De kleurvlakken boven lege vakken vallen naar beneden om de open plaatsen te vullen; nieuwe kleurvlakken komen van boven het bord binnen.
7. Als de vallende vlakken nog een match veroorzaken, wordt die cascade verwerkt. Elke stap wordt duidelijk geanimeerd en in een begrijpelijke volgorde getoond: eerst de verwisseling, dan de match, vervolgens het verdwijnen, daarna het vallen en aanvullen, en pas daarna een eventuele nieuwe cascade. Er is geen snelle opeenstapeling van effecten die Wannes het overzicht ontneemt.
8. De teller telt het aantal verzamelde rode energiecellen op en blijft altijd zichtbaar, van 0/10 tot 10/10. Hij gaat niet terug wanneer later opnieuw rode cellen verschijnen.
9. Het level eindigt onmiddellijk zodra de teller **10/10** bereikt. Er hoeft geen extra actie te worden gedaan.
10. Er is geen timer, geen zettenlimiet, geen levenssysteem, geen straf en geen game-over. Wannes mag rustig blijven spelen tot hij 10 rode energiecellen heeft verzameld. Hij hoeft het level niet opnieuw te starten omdat er te veel zetten zijn gebruikt.

#### 6. Bewegings- en feedbackstijl

Alle reacties zijn kort en hebben een duidelijk doel. De animaties ondersteunen het begrijpen van de spelregels en zijn geen permanente versiering.

- **Kleurvlak aangetikt:** het vlak krijgt een korte, duidelijke selectie-indicatie.
- **Ongeldige verwisseling:** beide vlakken bewegen terug naar hun oorspronkelijke positie. Geen straf en geen lange shake.
- **Geldige verwisseling:** de twee vlakken schuiven zichtbaar van plaats en stoppen duidelijk op hun nieuwe positie.
- **Match:** de drie of meer gelijke vlakken krijgen eerst een korte gezamenlijke nadruk, zodat Wannes kan zien welke combinatie telt.
- **Rode vlakken verdwijnen:** ze lossen zichtbaar op of worden met een korte drukinkt-/energieflits uit het bord gehaald; de teller loopt mee met de verdwenen rode vlakken.
- **Andere kleuren verdwijnen:** ze verdwijnen op dezelfde begrijpelijke manier, maar verhogen de rode teller niet.
- **Vallen en aanvullen:** vlakken erboven zakken zichtbaar in de lege plaatsen; nieuwe vlakken komen van boven het raster binnen. De beweging moet hun bestemming duidelijk maken, niet teleporteren.
- **Cascade:** pas nadat de nieuwe bordstand leesbaar is, wordt een volgende match geaccentueerd en verwerkt.
- **Doel bereikt:** de teller loopt naar 10/10 en het circuit op de monitor licht op. Daarna sluit de hintweergave automatisch en speelt een korte succesanimatie af.

#### 7. Hints voor dit level

Hints worden alleen getoond als Wannes zelf op de `?`-knop drukt. Ze zijn gebonden aan dit scherm en verschijnen niet op de werkplaats of bij een andere uitdaging. De voortgang van de hints wordt bewaard wanneer Wannes het hintpaneel sluit of het level verlaat; bij terugkeer ziet hij de laatst bekeken hint. Het hintpaneel blijft open totdat Wannes opnieuw op `?` drukt, behalve wanneer het level wordt opgelost: dan sluit het automatisch zodat de succesanimatie zichtbaar blijft. Ook na succes kan hij de laatst bekeken hint opnieuw openen.

Het paneel verschijnt direct onder de `?`-knop, is smal en gebruikt dezelfde geïntegreerde zeefdrukvormtaal. Drie kleine stippen tonen welke hint aan de beurt is. Eén knop **VOLGENDE HINT** doorloopt de drie stappen. Na hint 3 verandert die knop in **TOON OPLOSSING**; eerst verschijnt een compact bevestigingspaneel met **BEKIJKEN** en **TERUG**. De oplossing voert nooit automatisch een zet uit.

- **Hint 1 — subtiel:** laat één mogelijke zet met rode energiecellen kort pulseren. Tekst: **“Kijk eens welke rode energiecellen je samen kunt brengen.”**
- **Hint 2 — duidelijker:** tekst: **“Twee aangrenzende stukken wisselen kan een rij van drie of meer dezelfde stukken maken. Rode energiecellen vullen je teller.”** Er mag een passende kandidaatcombinatie kort oplichten, zonder de zet uit te voeren.
- **Hint 3 — oplossing:** na bevestiging tekst: **“Tik eerst op het rode stuk dat ik heb omlijnd en daarna op het aangrenzende stuk dat ook oplicht. Zo maak je een geldige match.”** De twee relevante stukken krijgen een dunne pulserende contour. De contour blijft staan totdat Wannes die actie uitvoert. Een verkeerde aanraking geeft geen extra waarschuwing of straf; de puzzel reageert zoals gewoonlijk en de contour blijft staan.

#### 8. Introductie- en feedbackteksten

**Introductie op de monitor:**

> **ENERGIECIRCUIT 01**  
> De fabriek is uitgevallen. Verzamel 10 rode energiecellen om het eerste circuit opnieuw te starten. Verwissel aangrenzende stukken en maak rijen van minstens drie dezelfde symbolen.

De tekst staat in een duidelijk paneel op de monitor en verdringt het bord niet. Zodra Wannes begint te spelen, blijft alleen de korte opdracht **VERZAMEL 10 RODE ENERGIECELLEN** als vaste herinnering zichtbaar.

**Feedback bij een verwisseling die geen match maakt:** geen foutmeldingstekst; de stukken keren gewoon terug. Dit voorkomt overbodige meldingen en sluit aan bij de afgesproken visuele feedback bij fouten.

**Feedback wanneer een match van andere symbolen wordt gemaakt:**

> “Goed! Zoek nu een kans om rode energiecellen te verzamelen.”

Deze tekst mag kort op het monitorpaneel verschijnen en verdwijnt weer zonder de bediening te blokkeren. Hij verschijnt niet na elke match opnieuw als dat storend zou worden.

**Succesfeedback:**

> **CIRCUIT ÉÉN DRAAIT WEER!**

Een verlichte lijn loopt door het circuit op de monitor. De letter **B** wordt daarna op een metalen label gedrukt of zichtbaar gemaakt; het is een onderdeel van de scène, geen standaard melding boven de game.

#### 9. Wat er bij succes verandert

- Het bord stopt en er worden geen nieuwe stukken meer toegevoegd.
- De teller blijft op **10/10** staan.
- Het circuit licht op met een korte, duidelijke animatie.
- De letter **B** verschijnt als een stevig, grafisch metalen label dat past bij de computerillustratie.
- De verzamelstrook verandert van **_ _ _** naar **B _ _**.
- De beloning wordt lokaal opgeslagen.
- Wannes krijgt een duidelijke manier om verder te gaan naar level 2. Hij wordt niet automatisch in een nieuwe puzzel gegooid.
- Als hij de uitdaging later verlaat en terugkomt, blijft level 1 voltooid en blijft de B zichtbaar. Het spel verliest geen voortgang door herladen of opnieuw openen.

#### 10. Wat niet in level 1 thuishoort

- Geen houten kistjes of andere obstakels; die horen bij level 2.
- Geen gouden energiesleutel of uitgang; die horen bij level 3.
- Geen ster met een oog of medaille; die aanwijzing hoort bij uitdaging 2.
- Geen tijdslimiet, levens, straf voor ongeldige zetten, automatische hints of verplichte tutorial die het spelen onderbreekt.
- Geen symbolen of pictogrammen op de speelvlakken, geen modern wit spelvenster, geen standaard emoji en geen afgeronde witte knoppen als uiteindelijke vormgeving.
- Geen automatische oplossingszet. Hints tonen of markeren alleen een mogelijke actie; Wannes voert die zelf uit.

**Te testen vóór de latere bouw:** de exacte startmatrix en kansverdeling van de vier kleuren; het raster blijft vast op 5 kolommen × 7 rijen en werking van willekeurige aanvulling zonder zettenlimiet. Dit zijn technische validatiepunten; ze mogen de hierboven beschreven spelregels en visuele richting niet stilzwijgend veranderen.

### Level 2 — De geblokkeerde tandwielen

**Status:** inhoudelijke levelbeschrijving; nog geen gamecode. Dit level bouwt bewust voort op Level 1. De speelervaring, vormgeving, bediening, raster, kleuren, animaties, hints, opslag en algemene match-3-regels blijven hetzelfde. Het verschil is het doel: in plaats van 10 rode kleurvlakken te verzamelen, moet Wannes **5 houten kistjes verwijderen**.

#### 1. Verhaal en bedoeling

Het eerste circuit draait weer, maar de tandwielen van de fabriek zitten nog geblokkeerd door houten transportkistjes. Wannes moet de kistjes wegwerken zodat de machine verder kan draaien.

Het level gebruikt dezelfde eenvoudige match-3-basis als Level 1. Wannes verwisselt aangrenzende effen kleurvlakken en maakt matches van minstens drie gelijke kleuren. Hij moet nu niet op een bepaalde kleur letten om die te verzamelen, maar matches maken die de houten kistjes raken. Elke kist die wordt verwijderd telt mee voor het doel.

Wanneer alle vijf kistjes verwijderd zijn, verdient Wannes de letter **A**. Die wordt toegevoegd aan de letterstrook: **B A _**.

#### 2. Wat Wannes op het iPhone-scherm ziet

De computer blijft de speelruimte. De camera zoomt in op dezelfde retro-computermonitor als in Level 1. De omliggende metalen behuizing, knoppen, schroeven en kabels blijven zichtbaar. Het spel is geïntegreerd in de verweerde jarenzeventig-zeefdrukwereld en verschijnt niet als een los modern gamevenster.

De verticale spelcompositie blijft gelijk aan Level 1:

1. **Kop van het scherm:** het label **TANDWIELEN 02** en een grote voortgangsteller **0/5**.
2. **Centrale speelruimte:** hetzelfde vaste raster van **5 kolommen × 7 rijen** (35 vakken).
3. **Korte opdracht:** **VERWIJDER 5 HOUTEN KISTJES** blijft tijdens het spelen zichtbaar.
4. **Bediening:** dezelfde `?`-knop voor hints en dezelfde terugknop. Er is geen zettenlimiet en geen tijdslimiet. Als opnieuw starten beschikbaar is, vraagt het spel eerst om bevestiging en wordt alleen de huidige levelpoging gereset.
5. **Beloning:** de letter A verschijnt pas bij succes. De letterstrook toont vóór succes **B _ _** en na succes **B A _**.

De stijl, schaal, contrasten en plaatsing van de elementen volgen Level 1. Gebruik het goedgekeurde kleurpalet: oud papier `#F3DDA8`, signaalrood `#D94330`, mosterdgeel `#E9B638`, donker petrol `#174B56`, bosgroen `#28513D` en inktzwart `#292A24`. De textuur mag cijfers, de voortgangsteller en de kistjes niet onleesbaar maken.

#### 3. Speelstukken en houten kistjes

De gewone speelstukken blijven exact dezelfde **effen kleurvlakken zonder symbolen of pictogrammen** als in Level 1:

- Signaalrood.
- Mosterdgeel.
- Donker petrol/blauw.
- Bosgroen.

Alle gewone kleurvlakken zijn verwisselbaar. Ze hebben een sobere duidelijke rand en geen letters, pictogrammen of illustraties op het vlak.

De vijf houten kistjes zijn de enige nieuwe spelcomponent ten opzichte van Level 1. Ze zijn visueel duidelijk te onderscheiden van de kleurvlakken: een eenvoudige, grafisch getekende houten transportkist met een krachtige contour en verweerde zeefdruktextuur. De kistjes bevatten geen tekst of decoratieve pictogrammen. Ze zijn **obstakels, geen verwisselbare speelstukken**. Een kistje bezet één vak van het raster en kan niet worden geselecteerd of verplaatst.

#### 4. Bord en beginsituatie

Het bord gebruikt hetzelfde vaste raster als Level 1: **5 kolommen × 7 rijen**, in totaal 35 vakken. De rasterafmeting verandert niet.

De beginopstelling bevat vijf houten kistjes en gewone effen kleurvlakken in de overige vakken. De exacte beginmatrix wordt later technisch vastgelegd en getest. De beginsituatie moet voldoen aan de volgende voorwaarden:

- Er is vanaf de start minstens één geldige zet.
- Er zijn geen automatische matches voordat Wannes zelf een zet uitvoert.
- De kistjes zijn zo geplaatst dat elk kistje met een geldige match bereikbaar is.
- Het doel om alle vijf kistjes te verwijderen is haalbaar volgens de vastgelegde regels.
- De startopstelling is begrijpelijk en niet onbedoeld triviaal; de kistjes mogen niet allemaal met één toevallige match verdwijnen.
- Als het bord geen geldige zet meer heeft, wordt het gecontroleerd opnieuw geschud zonder dat verwijderde kistjes terugkomen of voortgang verloren gaat.

Na de gecontroleerde beginopstelling worden nieuwe kleurvlakken willekeurig aangevuld, niet volgens een vooraf vastgelegde of herhalende aanvulvolgorde. Na aanvullen controleert het spel of er nog geldige zetten mogelijk zijn. Als die ontbreken, wordt het bord opnieuw geschud; de huidige kistjesvoortgang blijft behouden.

#### 5. Spelregels tijdens het spelen

1. Wannes tikt een kleurvlak aan en daarna een direct aangrenzend kleurvlak, horizontaal of verticaal.
2. Alleen een verwisseling die een match van minstens drie gelijke kleurvlakken oplevert, is geldig.
3. Als er geen match ontstaat, keren de twee vlakken terug naar hun oorspronkelijke plaats. Er wordt geen zet afgetrokken en er volgt geen straf of foutmeldingstekst.
4. Bij een geldige match worden de drie of meer gelijke kleurvlakken verwijderd.
5. **Een houten kistje wordt verwijderd wanneer een geldige match direct naast dat kistje verdwijnt.** Het kistje hoeft zelf geen deel van de match uit te maken en kan niet worden verwisseld.
6. Eén match kan meerdere kistjes verwijderen als de match direct naast meer dan één kistje ligt.
7. Elke verwijderde kist verhoogt de teller met één. De teller loopt op van **0/5** tot **5/5** en gaat nooit terug.
8. De gewone kleurvlakken boven lege vakken vallen naar beneden en nieuwe vlakken komen van boven het raster binnen. De kistjes die nog niet verwijderd zijn, blijven op hun vaste plaats en blokkeren hun vak.
9. Als het aanvullen een nieuwe match oplevert, wordt die als cascade verwerkt. Ook een cascade kan kistjes verwijderen als de match direct naast die kistjes ligt.
10. Er is geen zettenlimiet, timer, levenssysteem, straf of game-over. Wannes kan rustig verder spelen tot alle vijf kistjes weg zijn.
11. Het level eindigt zodra de teller **5/5** bereikt. Er is geen extra actie nodig.

#### 6. Bewegings- en feedbackstijl

De animaties volgen dezelfde duidelijke, stapsgewijze aanpak als Level 1:

- **Kleurvlak aangetikt:** een korte, duidelijke selectie-indicatie.
- **Ongeldige verwisseling:** de vlakken schuiven soepel terug; geen straf en geen foutmeldingstekst.
- **Geldige verwisseling:** de vlakken wisselen zichtbaar van plaats.
- **Match:** de betrokken kleurvlakken krijgen eerst een korte gezamenlijke nadruk, zodat Wannes ziet welke combinatie telt.
- **Kleurvlakken verdwijnen:** de vlakken lossen zichtbaar op of worden met een korte drukinkt-/energieflits uit het bord gehaald.
- **Kistje geraakt:** wanneer een match naast een kistje verdwijnt, krijgt het kistje een korte duidelijke reactie en breekt het zichtbaar open of valt het in stukken uiteen. Daarna verdwijnt het uit het raster en verhoogt de teller.
- **Vallen en aanvullen:** de resterende vlakken zakken zichtbaar in lege vakken; nieuwe vlakken komen van boven binnen. Ze teleporteren niet.
- **Cascade:** de huidige beweging wordt eerst afgerond en de nieuwe bordstand blijft even leesbaar voordat de volgende match wordt geaccentueerd.
- **Doel bereikt:** de teller loopt naar **5/5**, de geblokkeerde tandwielen komen zichtbaar in beweging en daarna speelt de succesanimatie af.

De animaties moeten begrijpelijk blijven op iPhone in staande stand. Geen snelle opeenstapeling van effecten die verbergt waarom een kistje verdwijnt.

#### 7. Hints voor dit level

De hintbediening en het gedrag van het paneel zijn hetzelfde als in Level 1. Hints verschijnen alleen als Wannes zelf op `?` tikt. De hintvoortgang wordt voor dit scherm bewaard; bij terugkeer ziet hij de laatst bekeken hint. Het paneel blijft open tot Wannes opnieuw op `?` tikt en sluit automatisch bij succes. De oplossingshint voert nooit zelf een zet uit.

- **Hint 1 — subtiel:** laat een mogelijke match naast een kistje kort pulseren. Tekst: **“Kijk eens wat er vlak naast de houten kistjes gebeurt.”**
- **Hint 2 — duidelijker:** tekst: **“Maak een match naast een houten kistje om het weg te breken.”** Een mogelijke match naast een kistje mag kort oplichten.
- **Hint 3 — oplossing:** na bevestiging tekst: **“Tik eerst op het kleurvlak dat ik heb omlijnd en daarna op het aangrenzende kleurvlak dat ook oplicht. Zo maak je een match naast een kistje.”** De twee betrokken vlakken krijgen een dunne pulserende contour die blijft staan tot Wannes de aangegeven actie uitvoert.

Na hint 3 verandert **VOLGENDE HINT** in **TOON OPLOSSING**. Eerst verschijnt de bevestiging **“Wil je de oplossing zien?”** met **BEKIJKEN** en **TERUG**. TERUG brengt hem terug naar hint 3. Een verkeerde aanraking geeft geen extra straf of waarschuwing; de contour blijft bij de juiste onderdelen.

#### 8. Introductie- en feedbackteksten

**Introductie op de monitor:**

> **TANDWIELEN 02**  
> De tandwielen zitten vast achter houten kistjes. Maak matches naast de kistjes om ze weg te breken. Verwijder alle 5 kistjes om de machine weer vrij te maken.

Zodra Wannes begint te spelen, blijft de korte opdracht **VERWIJDER 5 HOUTEN KISTJES** als vaste herinnering zichtbaar.

**Ongeldige verwisseling:** geen foutmeldingstekst; de vlakken keren terug.

**Geldige match die geen kistje raakt:** geen extra melding na elke match. De teller verandert alleen wanneer een of meer kistjes daadwerkelijk verdwijnen.

**Succesfeedback:**

> **DE TANDWIELEN DRAAIEN WEER!**

De tandwielen op het monitorpaneel komen met een korte illustratieve beweging op gang. Daarna verschijnt de letter **A** als een metalen label dat past bij de bestaande computerillustratie.

#### 9. Wat er bij succes verandert

- Het bord stopt; er worden geen nieuwe kleurvlakken meer toegevoegd.
- De teller blijft op **5/5** staan.
- De tandwielen komen zichtbaar in beweging.
- De letter **A** verschijnt op een metalen label.
- De verzamelstrook verandert van **B _ _** naar **B A _**.
- De beloning en de voltooide status worden lokaal opgeslagen.
- Wannes krijgt zelf de keuze om verder te gaan naar Level 3; hij wordt niet automatisch in een nieuwe puzzel gegooid.
- Als hij de uitdaging verlaat of het spel opnieuw opent, blijft Level 2 voltooid en blijft de letter A zichtbaar.

#### 10. Wat niet in Level 2 thuishoort

- Geen doel om 10 rode kleurvlakken te verzamelen; het doel is uitsluitend **5 houten kistjes verwijderen**.
- Geen zettenlimiet, timer, levens, straf of game-over.
- Geen symbolen of pictogrammen op de gewone kleurvlakken.
- Geen kistjes die kunnen worden geselecteerd of verwisseld.
- Geen automatische zet of automatische hint.
- Geen gouden energiesleutel of uitgang; die horen bij Level 3.
- Geen ster met een oog of medaille; die aanwijzing hoort bij uitdaging 2.
- Geen afwijkende interface of nieuwe beeldtaal ten opzichte van Level 1.

**Te testen vóór de latere bouw:** de exacte beginmatrix, de plaatsing van de vijf kistjes, geldige zetmogelijkheden, bereikbaarheid van ieder kistje en het correct behouden van kistjesvoortgang tijdens willekeurige aanvulling, cascades en herschudden.

### Level 3 — De geheime uitgang

**Status:** inhoudelijke levelbeschrijving; nog geen gamecode. Dit level bouwt verder op dezelfde match-3-basis als Level 1 en Level 2. De spelpresentatie, bediening, raster, kleuren, animaties, hints, opslag en algemene regels blijven gelijk. Het nieuwe doel is om de **gouden energiesleutel naar de uitgang onderaan het bord te laten vallen**.

#### 1. Verhaal en bedoeling

De eerste twee delen van de fabriek zijn hersteld. Het laatste circuit is echter nog afgesloten. Een gouden energiesleutel zit vast bovenaan het circuit. Wannes moet de kleurvlakken eronder met matches verwijderen zodat de sleutel door het bord naar de uitgang onderaan kan zakken.

Dit level draait niet om een kleur verzamelen of kistjes opruimen. Wannes maakt matches van minstens drie gelijke effen kleurvlakken om ruimte te maken in de kolom onder de sleutel. De sleutel is een doelobject en geen gewoon speelstuk.

Wanneer de sleutel de uitgang bereikt, verdient Wannes de letter **L**. De letterstrook wordt **B A L** en vormt het woord dat hij later nodig heeft bij de grote deur.

#### 2. Wat Wannes op het iPhone-scherm ziet

De computer blijft de speelruimte. De camera zoomt in op dezelfde retro-computermonitor als in Level 1 en Level 2. De metalen behuizing, knoppen, schroeven en kabels blijven zichtbaar. Het spel blijft geïntegreerd in de verweerde jarenzeventig-zeefdrukstijl en verschijnt niet als een los modern gamevenster.

De verticale spelcompositie blijft dezelfde als bij de vorige twee levels:

1. **Kop van het scherm:** het label **GEHEIME UITGANG 03** en een duidelijke illustratie van de gouden energiesleutel.
2. **Centrale speelruimte:** hetzelfde vaste raster van **5 kolommen × 7 rijen** (35 vakken).
3. **Doel en uitgang:** de sleutel begint bovenaan het raster. Onderaan is een duidelijk herkenbare uitgang gemarkeerd. De kolom waarin de sleutel zich bevindt en de route naar beneden moeten in één oogopslag te begrijpen zijn.
4. **Korte opdracht:** **LAAT DE GOUDEN SLEUTEL NAAR DE UITGANG VALLEN** blijft zichtbaar tijdens het spelen.
5. **Bediening:** dezelfde hintknop met vraagteken en dezelfde terugknop. Er is geen zettenlimiet en geen tijdslimiet. Als opnieuw starten beschikbaar is, vraagt het spel eerst om bevestiging en wordt alleen de huidige levelpoging gereset.
6. **Beloning:** de letter L verschijnt pas wanneer de sleutel de uitgang bereikt. De letterstrook toont vooraf **B A _** en na succes **B A L**.

Gebruik hetzelfde goedgekeurde kleurpalet: oud papier `#F3DDA8`, signaalrood `#D94330`, mosterdgeel `#E9B638`, donker petrol `#174B56`, bosgroen `#28513D` en inktzwart `#292A24`. De gouden sleutel mag een gedrukte mosterdgele/goudkleurige vorm krijgen met een donkere contour; geen glanzende 3D-metaalrender of gradient. Alle tekst en het doel blijven goed leesbaar.

#### 3. Speelstukken, sleutel en uitgang

De gewone speelstukken blijven dezelfde **effen kleurvlakken zonder symbolen of pictogrammen** als in Level 1 en Level 2:

- Signaalrood.
- Mosterdgeel.
- Donker petrol/blauw.
- Bosgroen.

Gewone kleurvlakken zijn verwisselbaar en hebben een sobere, duidelijke rand. Ze bevatten geen letters, symbolen, pictogrammen of illustraties.

De **gouden energiesleutel** is het enige speciale doelobject. Ze is visueel duidelijk te onderscheiden van de kleurvlakken, blijft tijdens het vallen zichtbaar en kan niet worden geselecteerd of verwisseld. De sleutel neemt één rasterpositie in en valt uitsluitend verticaal naar beneden wanneer de route onder haar vrij is. De **uitgang** is duidelijk onderaan het raster aangeduid en is geen gewoon speelvak of verwisselbaar object.

#### 4. Bord en beginsituatie

Het bord gebruikt hetzelfde vaste raster als de vorige levels: **5 kolommen × 7 rijen**, in totaal 35 vakken. De rasterafmeting verandert niet.

De beginsituatie bevat gewone kleurvlakken en één gouden energiesleutel bovenaan het bord. De uitgang bevindt zich onderaan in dezelfde kolom als de sleutel. De exacte beginmatrix wordt later technisch vastgelegd en getest. De beginsituatie moet aan de volgende voorwaarden voldoen:

- Er is vanaf de start minstens één geldige zet.
- Er zijn geen automatische matches voordat Wannes zelf een zet uitvoert.
- De sleutel begint bovenaan en de uitgang bevindt zich onderaan dezelfde kolom.
- De sleutel kan de uitgang bereiken door geldige matches en zwaartekracht; er is geen verborgen handeling of speciale knop nodig.
- Het bord biedt meer dan één haalbare zet, zodat Wannes niet afhankelijk is van één onduidelijke verplichte zet.
- De startopstelling is uitdagend genoeg om het doel te begrijpen en te plannen, maar niet onnodig moeilijk.
- Als het bord geen geldige zet meer heeft, wordt het gecontroleerd opnieuw geschud zonder de sleutelpositie, de uitgang of de voortgang onbedoeld te veranderen.

Na de gecontroleerde beginopstelling worden nieuwe kleurvlakken willekeurig aangevuld, niet volgens een vooraf vastgelegde of herhalende aanvulvolgorde. Na aanvullen controleert het spel of er geldige zetten mogelijk zijn. Als die ontbreken, wordt het bord opnieuw geschud. De sleutel blijft een afzonderlijk doelobject en wordt niet willekeurig opnieuw geplaatst.

#### 5. Spelregels tijdens het spelen

1. Wannes tikt een kleurvlak aan en daarna een direct aangrenzend kleurvlak, horizontaal of verticaal.
2. Alleen een verwisseling die een match van minstens drie gelijke kleurvlakken oplevert, is geldig.
3. Als de verwisseling geen match oplevert, keren de twee vlakken terug naar hun oorspronkelijke plaats. Er wordt geen straf of foutmeldingstekst getoond.
4. Bij een geldige match verdwijnen de drie of meer gelijke kleurvlakken.
5. Wanneer een match vakjes onder de sleutel vrijmaakt, valt de sleutel zichtbaar naar beneden door de vrijgekomen ruimte. Ze valt zo ver als de ononderbroken route onder haar toelaat.
6. De sleutel valt niet door kleurvlakken die nog op het bord liggen en wordt niet zijwaarts verplaatst door gewone zwaartekracht.
7. De kleurvlakken boven lege vakken vallen naar beneden en nieuwe kleurvlakken komen van boven het raster binnen. De sleutel blijft op haar actuele positie tenzij er ruimte onder haar vrijkomt.
8. Als het aanvullen een nieuwe match oplevert, wordt die als cascade verwerkt. Nadat de cascade is afgehandeld, wordt opnieuw gecontroleerd of de sleutel verder naar beneden kan vallen.
9. De sleutel mag niet verdwijnen achter een vallend kleurvlak, een animatie of een interface-element. De speler moet haar actuele positie tijdens elke stap kunnen volgen.
10. Er is geen zettenlimiet, timer, levenssysteem, straf of game-over. Wannes mag rustig proberen tot de sleutel de uitgang bereikt.
11. Het level eindigt zodra de sleutel de uitgang onderaan bereikt. Er is geen extra actie nodig.

#### 6. Bewegings- en feedbackstijl

De animaties volgen dezelfde duidelijke, stapsgewijze aanpak als Level 1 en Level 2:

- **Kleurvlak aangetikt:** een korte, duidelijke selectie-indicatie.
- **Ongeldige verwisseling:** de vlakken schuiven soepel terug; geen straf en geen foutmeldingstekst.
- **Geldige verwisseling:** de vlakken wisselen zichtbaar van plaats.
- **Match:** de betrokken kleurvlakken krijgen eerst een korte gezamenlijke nadruk, zodat Wannes ziet welke combinatie telt.
- **Kleurvlakken verdwijnen:** de vlakken lossen zichtbaar op of worden met een korte drukinkt-/energieflits uit het bord gehaald.
- **Sleutel valt:** de sleutel beweegt zichtbaar en vloeiend naar beneden, blijft tijdens de hele beweging in beeld en stopt duidelijk wanneer ze door een gevuld vak wordt tegengehouden of de uitgang bereikt.
- **Vallen en aanvullen:** gewone kleurvlakken zakken zichtbaar in lege vakken; nieuwe vlakken komen van boven binnen. Ze teleporteren niet.
- **Cascade:** de huidige beweging wordt eerst afgerond en de nieuwe bordstand blijft even leesbaar voordat een volgende match wordt geaccentueerd. Daarna wordt de positie van de sleutel opnieuw gecontroleerd.
- **Doel bereikt:** de sleutel valt in de uitgang, de uitgang licht op en het circuit komt tot leven. Daarna speelt de succesanimatie af.

Animaties moeten begrijpelijk blijven op iPhone in staande stand. De sleutelbeweging is een belangrijk onderdeel van het spelmechanisme en mag niet te snel verlopen of door andere effecten worden verborgen.

#### 7. Hints voor dit level

De hintbediening en het gedrag van het paneel zijn hetzelfde als in Level 1 en Level 2. Hints verschijnen alleen als Wannes zelf op de hintknop tikt. De hintvoortgang wordt voor dit scherm bewaard; bij terugkeer ziet hij de laatst bekeken hint. Het paneel blijft open tot Wannes opnieuw op de hintknop tikt en sluit automatisch bij succes. De oplossingshint voert nooit zelf een zet uit.

- **Hint 1 — subtiel:** laat de vakjes direct onder de sleutel kort pulseren. Tekst: **“Kijk eens wat er onder de gouden sleutel zit.”**
- **Hint 2 — duidelijker:** tekst: **“Maak ruimte onder de sleutel, dan kan ze naar beneden vallen.”** De relevante vakjes of een mogelijke match eronder mogen kort oplichten.
- **Hint 3 — oplossing:** na bevestiging tekst: **“Tik eerst op het kleurvlak dat ik heb omlijnd en daarna op het aangrenzende kleurvlak dat ook oplicht. Zo maak je ruimte onder de sleutel.”** De twee betrokken vlakken krijgen een dunne pulserende contour die blijft staan tot Wannes de aangegeven actie uitvoert.

Na hint 3 verandert **VOLGENDE HINT** in **TOON OPLOSSING**. Eerst verschijnt de bevestiging **“Wil je de oplossing zien?”** met **BEKIJKEN** en **TERUG**. TERUG brengt hem terug naar hint 3. Een verkeerde aanraking geeft geen extra straf of waarschuwing; de contour blijft bij de juiste onderdelen.

#### 8. Introductie- en feedbackteksten

**Introductie op de monitor:**

> **GEHEIME UITGANG 03**  
> Daar is de gouden energiesleutel! Maak de vakjes onder haar vrij en laat de sleutel naar de uitgang onderaan vallen.

Zodra Wannes begint te spelen, blijft de korte opdracht **LAAT DE GOUDEN SLEUTEL NAAR DE UITGANG VALLEN** als vaste herinnering zichtbaar.

**Ongeldige verwisseling:** geen foutmeldingstekst; de vlakken keren terug.

**Geldige match die de sleutel niet verder laat vallen:** geen extra melding na elke match. De sleutel blijft op haar huidige plek en de speler kan een nieuwe kans zoeken.

**Succesfeedback:**

> **DE UITGANG IS OPEN!**

De sleutel valt zichtbaar in de uitgang. Het circuit licht op en de fabriek wordt grafisch wakker. Daarna verschijnt de letter **L** als een metalen label dat past bij de bestaande computerillustratie.

#### 9. Wat er bij succes verandert

- Het bord stopt; er worden geen nieuwe kleurvlakken meer toegevoegd.
- De sleutel blijft zichtbaar in de uitgang.
- Het circuit licht op en de fabriek komt visueel tot leven.
- De letter **L** verschijnt op een metalen label.
- De verzamelstrook verandert van **B A _** naar **B A L**.
- De beloning en de voltooide status worden lokaal opgeslagen.
- Wannes krijgt zelf de keuze om terug te gaan naar de werkplaats; hij wordt niet automatisch naar het grote slot gestuurd.
- Als hij de uitdaging verlaat of het spel opnieuw opent, blijft Level 3 voltooid en blijft de letter L zichtbaar.
- Nadat de drie match-3-levels voltooid zijn, wordt uitdaging 1 als geheel voltooid en kan Wannes het woord **BAL** gebruiken bij de grote deur.

#### 10. Wat niet in Level 3 thuishoort

- Geen doel om rode kleurvlakken te verzamelen; dat hoort bij Level 1.
- Geen houten kistjes om te verwijderen; die horen bij Level 2.
- Geen zettenlimiet, timer, levens, straf of game-over.
- Geen symbolen of pictogrammen op de gewone kleurvlakken.
- Geen handmatige bediening van de sleutel en geen knop om haar naar beneden te duwen.
- Geen ster met een oog of medaille; die aanwijzing hoort bij uitdaging 2.
- Geen afwijkende interface of nieuwe beeldtaal ten opzichte van Level 1 en Level 2.

**Te testen vóór de latere bouw:** de exacte beginmatrix, de geldige zetmogelijkheden, het pad van de sleutel naar de uitgang, de volgorde van vallen/aanvullen/cascades en de garantie dat de sleutel nooit vast komt te zitten door een onoplosbare bordtoestand.


### De drie letters samen — onthulling van BAL

Na level 3 schuift de verzamelstrook naar het midden van het scherm. De letters **B**, **A** en **L** komen samen op één stevig metalen plaatje. De laboratoriummonitor toont:

> “B… A… L. Dat is je eerste geheime woord. Onthoud het goed — je hebt het later nodig!”

Het woord wordt niet gekoppeld aan een gouden medaille of een extra voorwerp uit uitdaging 2. Het is de expliciete woordaanwijzing van uitdaging 1 en wordt opgeslagen in de voortgang van het spel, zodat het later bij het grote slot gebruikt kan worden.

**Einde van uitdaging 1:** het spel toont een korte overgang naar het volgende mysterieuze onderdeel van het speelgoedlab. De ster met het oog wordt hier niet getoond en blijft gereserveerd als beloning van uitdaging 2.

### Ontwerp- en toegankelijkheidsregels

- Geen exacte nabootsing van Royal Match: gebruik alleen het algemene match-3-principe en maak eigen symbolen, doelen, animaties en teksten.
- Vermijd kleine tegels en minieme tikzones; alle vakjes moeten comfortabel met een duim te bedienen zijn.
- Gebruik naast kleur ook vorm of pictogram, zodat doelen niet alleen van kleurherkenning afhangen.
- Respecteer gereduceerde beweging waar mogelijk; animaties mogen nooit de enige manier zijn om spelstatus te begrijpen.
- Laat de speler na elke match genoeg tijd om het resultaat te zien; geen snelle automatische cascades die invoer verwarrend maken.
- Houd de instructie kort en toon het leveldoel altijd tijdens het spelen.
- De precieze rasterafmetingen, symbolenverdeling, zetlimieten en startborden moeten tijdens de technische uitwerking worden getest. Dit dossier legt de spelregels en doelen vast, niet de definitieve puzzelmatrices.

## Uitdaging 2 — De drie raadselmeesters

**Visuele presentatie:** de volledige uitdaging blijft verbonden aan de bestaande hoge groene locker in de controlekamer. Na aantikken zoomt het beeld in op de locker. De code wordt ingevoerd op/aan de locker; na het openen van het kleine geheime deurtje verschijnen de personages in de opening. Het sleutel- en kistjesraadsel worden vervolgens binnen dezelfde ingezoomde scène getoond, in de vastgelegde verweerde jarenzeventig-zeefdrukstijl. Geen los modern spelvenster. Een duidelijke terugknop brengt Wannes terug naar dezelfde controlekamer.

**Doel:** Wannes lost drie opeenvolgende puzzels op. De cijfercode opent een geheim deurtje, het logische raadsel levert een sleutel op en de laatste deductiepuzzel wijst het juiste kistje aan. In de kist zit **een aanwijzing die onderdeel is van de uitkomst van uitdaging 4**, niet een gouden medaille.

**Geschatte duur:** 3–5 minuten.  
**Bediening:** grote, duidelijke tikbare elementen; geschikt voor iPhone.  
**Fouten:** opnieuw proberen, zonder onherroepelijke blokkade.  
**Hints:** oplopend van subtiel naar expliciet.

### Deel 1 — Het geheime deurtje: kraak de cijfercode

Wannes ontdekt een klein metalen deurtje met een mechanisch cijferslot van drie cijfers. Wannes krijgt vijf aanwijzingen:

- **682** — één cijfer is juist én staat op de juiste plaats.
- **416** — één cijfer is juist, maar staat op de verkeerde plaats.
- **206** — twee cijfers zijn juist, maar staan allebei op de verkeerde plaats.
- **738** — geen enkel cijfer komt in de code voor.
- **780** — één cijfer is juist, maar staat op de verkeerde plaats.

**Oplossing:** **042**.

#### Controle van de logica
- Uit 738 volgt dat 7, 3 en 8 niet in de code zitten.
- Uit 780 volgt dat 0 in de code zit, maar niet op positie drie.
- Uit 206 volgen de cijfers 0 en 2, beide op andere posities dan getoond.
- Uit 682 volgt dat 2 op positie drie staat.
- Daardoor moet 0 op positie één staan.
- De resterende aanwijzingen leggen 4 vast op positie twee.

#### Interactie en feedback
- Wannes stelt drie cijferwieltjes in.
- Hij drukt op **OPEN**.
- Bij een verkeerde code trilt het slot kort; hij mag opnieuw proberen.
- Wannes kan zelf stapsgewijs hints aanvragen via de vaste `?`-knop.
- Bij 042 klikken de cijfers op hun plaats en springt het kleine deurtje open.

### Deel 2 — De drie speelgoedfiguren: wie heeft de sleutel?

Achter het deurtje zitten drie figuren verstopt: **Charlie de aap, RidderUs en Schildje de schildpad**. Zij bewaken samen een sleutel. De panda hoort niet bij dit raadsel: die piept alleen even uit een lade als optionele easter egg en is later aanwezig op het verjaardagsfeest.

**Regel:** precies één van de drie uitspraken is waar; de andere twee zijn onwaar.

- **Charlie (aap):** “RidderUs heeft de sleutel.”
- **RidderUs:** “Ik heb de sleutel niet.”
- **Schildje (schildpad):** “Charlie heeft de sleutel niet.”

**Vraag:** wie heeft de sleutel?

Wannes kiest Charlie, RidderUs of Schildje en bevestigt zijn antwoord.

#### Oplossing en logische controle

| Wie heeft de sleutel? | Uitspraak Charlie | Uitspraak RidderUs | Uitspraak Schildje | Aantal ware uitspraken |
|---|---|---|---|---:|
| Charlie | Onwaar | Waar | Onwaar | 1 |
| RidderUs | Waar | Onwaar | Waar | 2 |
| Schildje | Onwaar | Waar | Waar | 2 |

**Juiste antwoord:** Charlie de aap heeft de sleutel.

#### Beloning en overgang
Charlie haalt een kleine messing sleutel achter zijn rug vandaan en zegt:

> “Goed geredeneerd! Je hebt me door. Hier is de sleutel — maar je moet nog ontdekken welk kistje de moeite waard is.”

De sleutel wordt automatisch als gevonden voorwerp geregistreerd; Wannes hoeft geen code te onthouden.

#### Hints
1. “Wat gebeurt er als Charlie de sleutel heeft?”
2. “Controleer hoeveel uitspraken waar zijn als RidderUs de sleutel heeft.”
3. “Test alle drie de mogelijkheden. Slechts één ervan voldoet aan de regel.”

### Deel 3 — De drie kistjes: vind de aanwijzing voor het grote slot

Charlie wijst naar drie gesloten kistjes. De sleutel past op het slot van het gekozen kistje. Op elk kistje staat een uitspraak. De regel blijft: **precies één uitspraak is waar**.

- **Rood kistje:** “De hoofdprijs zit in het blauwe kistje.”
- **Blauw kistje:** “De hoofdprijs zit niet in het blauwe kistje.”
- **Geel kistje:** “De hoofdprijs zit niet in het rode kistje.”

**Vraag:** welk kistje moet Wannes openen?

#### Oplossing en logische controle
- Als de hoofdprijs in het **rode** kistje zit: rood is onwaar, blauw is waar, geel is onwaar — precies één uitspraak is waar.
- Als de hoofdprijs in het **blauwe** kistje zit: rood en geel zijn waar — twee uitspraken.
- Als de hoofdprijs in het **gele** kistje zit: blauw en geel zijn waar — twee uitspraken.

**Juiste antwoord:** het rode kistje.

#### Interactie en beloning
- Wannes kiest eerst een kistje en kan zijn redenering controleren.
- De sleutel wordt pas gebruikt als hij zijn keuze bevestigt.
- Een verkeerde keuze verbruikt de sleutel niet; Wannes kan opnieuw nadenken en een ander kistje kiezen.
- Als Wannes de uitdaging verlaat nadat hij de sleutel heeft verdiend, blijft de sleutel beschikbaar en blijft het kistjesraadsel onopgelost klaarstaan. Na terugkeer hoeft hij de eerdere puzzels niet opnieuw te doen.
- Bij de juiste keuze draait de sleutel, klikt het slot open en gaat het deksel langzaam omhoog.

**Inhoud van de kist:** een fysiek voorwerp of kaart met de aanwijzing die uitdaging 2 aan uitdaging 4 levert. De gouden medaille is geschrapt. De afgesproken aanwijzingen voor het grote slot zijn: **BAL** (uitdaging 1), ster met oog (uitdaging 2) en signaalrood (uitdaging 3). Daarom bevat de kist de ster-met-oog-aanwijzing — bijvoorbeeld op een geheim kaartje of een bijzonder gegraveerd plaatje. De onthulling van de ster met het oog hoort bij uitdaging 2. Het woord BAL wordt uitsluitend in uitdaging 1 verdiend.

**Reactie van het spel:**

> “Gevonden! Jij hebt de code gekraakt, de sleutel verdiend én het juiste kistje opgespoord!”

### Complete speelervaring van uitdaging 2

1. Wannes kraakt de code **042**.
2. Het geheime deurtje springt open en onthult Charlie, RidderUs en Schildje.
3. Wannes redeneert dat Charlie de sleutel heeft.
4. Charlie geeft hem de messing sleutel.
5. Wannes onderzoekt de uitspraken op drie kistjes en kiest het rode kistje.
6. De kist gaat open en onthult de **ster met een oog**, de symboolaanwijzing die nodig is voor uitdaging 4.

**Ontwerpregel:** de cijfercode, sleutel en kistjes zijn onderdelen van uitdaging 2. De ster met het oog is de symboolaanwijzing voor het grote slot. Het woord BAL komt uitsluitend uit uitdaging 1. Voeg geen extra puzzel toe en vervang de ster niet door een gouden medaille.

## Uitdaging 3 — De onmogelijke bekers

**Visuele presentatie:** na aantikken zoomt het beeld in op de bestaande tafel met drie bekers in de controlekamer. De bekers en het rode balletje bewegen op deze tafel; de goocheltruc blijft visueel geïntegreerd in de ruimte en gebruikt de vastgelegde verweerde jarenzeventig-zeefdrukstijl. Geen los modern spelvenster. Na voltooiing of verlaten van de uitdaging brengt een duidelijke terugknop Wannes terug naar dezelfde controlekamer.

**Status:** ontwerp uitgewerkt; moeilijkheid gekozen: **opbouwend**.  
**Spelvorm:** een klassieke bekers-truc in drie rondes. Wannes volgt één rood balletje terwijl drie bekers van plaats wisselen. De beweging wordt per ronde iets sneller, maar blijft volledig zichtbaar en eerlijk te volgen.

**Doel in het verhaal:** het laboratoriumsysteem toont een goocheltruc die de kleur van het laatste onderdeel van het grote slot onthult. Wannes moet het balletje volgen en de juiste beker kiezen in alle drie de rondes.

**Beloning van uitdaging 3:** de kleur **signaalrood**, de kleur-aanwijzing voor uitdaging 4.  
**Geschatte speelduur:** ongeveer 2 minuten.  
**Bediening:** Wannes tikt op één van drie grote bekers op het scherm; geschikt voor iPhone in staande stand.  
**Geen game-over:** na een fout mag Wannes opnieuw proberen. Wannes kan zelf een hint vragen via de vaste `?`-knop; het spel toont nooit automatisch een hint na herhaald vastlopen. Na een fout mag de beginpositie opnieuw worden getoond als onderdeel van de spel-feedback.

### De scène en de spelregels

Een kleine goocheltafel staat in het speelgoedlaboratorium. Drie stevige bekers staan naast elkaar op gemarkeerde plaatsen: links, midden en rechts. De bekers hebben elk een eigen herkenbare vorm en kleur, maar de juiste beker wordt niet aangeduid met een blijvend kenmerk. Het rode balletje is het enige doelobject.

Aan het begin van iedere ronde:
1. Het spel toont het rode balletje duidelijk onder één beker.
2. De beker wordt opgetild of kort transparant getoond zodat Wannes de beginpositie goed ziet.
3. De beker wordt teruggezet en alle drie de bekers zijn even zichtbaar.
4. De wisselbewegingen beginnen pas wanneer Wannes klaar is; de speler hoeft niet op een startknop te drukken tijdens een animatie.
5. De bekers wisselen onderling van plaats. De hele beweging blijft zichtbaar; er zijn geen geheime teleportaties, verdwijntrucs of bewegingen buiten het scherm.
6. Na de laatste wissel stoppen de bekers volledig. Pas daarna kan Wannes een keuze maken.
7. Wannes tikt op de beker waaronder hij denkt dat het balletje ligt.
8. De gekozen beker gaat omhoog en toont of het balletje eronder ligt.
9. Een juist antwoord voltooit de ronde. Bij een fout antwoord geeft het spel korte feedback en volgt een nieuwe poging met een opnieuw getoonde beginpositie.

**Belangrijk:** de spelregels moeten visueel duidelijk maken dat de bekers zelf van plaats wisselen. De speler volgt de bekerpositie, niet een verwarrende reeks willekeurige animaties. Geen tijdslimiet voor het kiezen na afloop van de wissels.

### Ronde 1 — Leer de truc

**Doel:** de eerste juiste beker vinden na **2 wissels**.

- Het balletje wordt zichtbaar onder één beker geplaatst.
- De bekers wisselen twee keer van plaats.
- De wissels zijn langzaam, met een korte pauze tussen de bewegingen.
- De bekers volgen een duidelijk pad en overlappen elkaar niet.
- Deze ronde leert het principe en is bewust eenvoudig.

**Introductietekst op het scherm:**
> “Let goed op het rode balletje. Ik wissel de bekers twee keer. Kijk waar het balletje eindigt!”

**Feedback bij een fout:**
> “Oei, die beker is leeg! Geen probleem — kijk opnieuw waar ik het balletje verstop.”

**Feedback bij succes:**
> “Juist! Je hebt de truc door.”

**Hints:**
1. Eerste hint: “Volg één beker tegelijk met je ogen.”
2. Tweede hint: het spel toont de beginpositie opnieuw en voert de twee wissels langzamer uit.
3. Extra hulp: het spel vertraagt de wissels en pauzeert kort nadat elke wissel voltooid is.

**Overgang:** het balletje springt kort op en neer en rolt daarna weer onder een beker voor ronde 2.

### Ronde 2 — De afleiding

**Doel:** de juiste beker vinden na **3 wissels**.

- De bekers wisselen drie keer van plaats.
- De animatie is iets sneller dan in ronde 1, maar elke wissel blijft afzonderlijk herkenbaar.
- Er is een korte pauze tussen de tweede en derde wissel, zodat de reeks niet als één onleesbare beweging aanvoelt.
- Het spel probeert Wannes met een grapje af te leiden, maar de tekst verschijnt vóór of na de beweging, nooit over de bekers heen.
- De bekers blijven steeds volledig binnen het zichtbare speelgebied.

**Introductietekst op het scherm:**
> “Goed opgelet! Nu drie wissels. Laat je niet afleiden door mijn geweldige goochelstem…”

**Grappige afleiding in het spel:**
> “Psst… let goed op de bekers. Het balletje blijft ergens onder verstopt!”

**Feedback bij een fout:**
> “Ha! Ik had je bijna te pakken. We doen het nog eens.”

**Feedback bij succes:**
> “Netjes! Je laat je niet zomaar afleiden.”

**Hints:**
1. Eerste hint: “Kies één beker en volg hoe die van plaats verandert.”
2. Tweede hint: de beginpositie wordt opnieuw getoond en de drie wissels worden trager afgespeeld.
3. Extra hulp: na elke wissel verschijnt heel kort een kleine neutrale markering op de nieuwe positie van de gevolgde beker; die verdwijnt vóór de keuze.

### Ronde 3 — De meestertruc

**Doel:** de juiste beker vinden na **4 wissels**. Dit is de moeilijkste ronde.

- De bekers wisselen vier keer van plaats.
- De wissels verlopen sneller dan in ronde 2, maar er blijft een korte, zichtbare overgang tussen elke wissel.
- De laatste wissel is niet extra versneld ten opzichte van de rest; de moeilijkheid komt uit het volgen van de volledige reeks, niet uit een oneerlijke plotselinge versnelling.
- er verschijnt geen tekst tijdens de daadwerkelijke wissels zodat hij niet visueel of tekstueel afleidt.
- Na de vierde wissel blijven de bekers stilstaan. Wannes krijgt alle tijd om zijn keuze te maken.

**Introductietekst op het scherm:**
> “Klaar voor de meestertruc? Vier wissels. Blijf bij het rode balletje — jij kunt dit!”

**Feedback bij een fout:**
> “Bijna! Zelfs de beste goochelaars oefenen hun trucs. We proberen het nog een keer.”

**Feedback bij succes:**
> “Ongelooflijk! Je hebt alle drie de rondes gekraakt!”

**Hints:**
1. Eerste hint: “Probeer de beker te volgen in plaats van naar het balletje te zoeken.”
2. Tweede hint: het spel toont de beginpositie opnieuw en speelt de vier wissels op het tempo van ronde 2 af.
3. Extra hulp: de bekers wisselen opnieuw, één voor één, met een korte pauze na iedere wissel. Dit maakt de reeks eenvoudiger zonder de oplossing direct te tonen.

### Regels voor eerlijke moeilijkheid

- De gekozen opbouw is vast: **2 wissels → 3 wissels → 4 wissels**, met oplopende snelheid.
- De animaties moeten in echte tests op een iPhone goed te volgen zijn; als ronde 3 te moeilijk blijkt, verlaag dan de snelheid vóór je het aantal wissels verandert.
- De snelheid is geen reflex-test. Wannes hoeft niet tijdens een wissel te tikken en krijgt geen aftellende klok.
- Na een fout wordt de beginpositie opnieuw getoond. Er is geen strafscore, geen verloren leven en geen terugkeer naar een eerdere uitdaging.
- Ook na herhaalde fouten verschijnt geen automatische hint. Wannes kiest zelf of hij de `?`-knop gebruikt.
- De beker die het balletje verbergt mag niet steeds dezelfde kleur of vaste positie hebben. De startpositie varieert zodat Wannes de truc echt moet volgen.
- De wisselreeks moet gecontroleerd worden op geldige, visueel begrijpelijke bewegingen. Bekers mogen elkaar niet bedekken of buiten het scherm bewegen.
- Gebruik geen stroboscopische effecten of onnodige camerabewegingen. De feedback blijft ook begrijpelijk als beweging beperkt wordt.

### Beloning — signaalrood

Na het succes in ronde 3 wordt de juiste beker opgetild. Het rode balletje stijgt op, verandert in een gloeiende rode lichtbol en werpt een rode lichtcirkel op de tafel. het laboratoriumsysteem analyseert de lichtbol en projecteert een eenvoudige rode kleurstaal met het label **SIGNAALROOD**.

**Tekst op het scherm:**
> “Aha! De truc is ontmaskerd. Onthoud deze kleur: signaalrood. Je hebt nu alle drie de aanwijzingen verzameld!”

De kleurstaal wordt toegevoegd aan de verzamelde aanwijzingen en blijft beschikbaar voor uitdaging 4. De ster met het oog en het woord BAL worden hier niet opnieuw uitgereikt.

### Schermen en benodigde onderdelen

1. **Introductiescherm:** goocheltafel, drie bekers, rode bal en korte instructie.
2. **Speelscherm:** drie bekers, bewegingsgebied, ronde-indicator en hintknop.
3. **Feedbackmoment:** beker gaat omhoog; bal zichtbaar of beker leeg.
4. **Succesmoment per ronde:** korte animatie en voortgang van ronde 1/3 naar 2/3 en 3/3.
5. **Beloningsscherm:** rode lichtbol en kleurstaal met het label SIGNAALROOD.

Benodigde assets:
- Drie eigen bekerillustraties in dezelfde retro-zeefdrukstijl.
- Rood balletje en eventueel een subtiele schaduw.
- Goocheltafel of afgebakend speelvlak.
- het spelportret of klein het spelfiguur voor dialoog.
- Rood lichtbol-effect en kleurstaal voor signaalrood.
- Eenvoudige markering voor de hintstand.
- Geen audio-assets nodig: het spel gebruikt geen geluidseffecten of achtergrondmuziek, ook niet bij bekerwissels, succes of de finale.

## Uitdaging 4 — Het slot van het geheim

**Status:** herwerkt volgens het principe van vrije verkenning.  
**Doel:** Wannes ontdekt de grote deur wanneer hij daar zelf naartoe wandelt. Hij ziet dat het slot aanwijzingen uit het laboratorium nodig heeft. Het symbool wordt automatisch ingevuld zodra uitdaging 2 voltooid is; aan het slot moet Wannes alleen nog het woord typen en een kleur kiezen.

### Vrije verkenning en ontdekking

Het laboratorium is één centrale omgeving waarin Wannes het spel zelf rondstuurt. De drie uitdagingen bevinden zich op verschillende plekken. Er is geen vaste volgorde en het spel verplicht hem niet eerst een bepaalde uitdaging af te werken.

De grote deur is ook vanaf het begin zichtbaar of vindbaar. Wannes mag ze meteen onderzoeken. Zo ontdekt hij zelf dat dit het centrale mysterie is. Het slot toont drie onderdelen:
- een symboolvenster;
- een invoerveld voor een woord;
- een kleurkeuze.

Bij de eerste ontdekking verschijnt een korte reactie:

> “Een geheim slot! Het lijkt erop dat het drie aanwijzingen nodig heeft. Die moeten ergens in dit laboratorium verstopt zitten.”

Het slot legt niet uit waar de aanwijzingen te vinden zijn. Wannes ontdekt dat door de rest van het laboratorium te verkennen en de uitdagingen in een zelfgekozen volgorde op te lossen.

### Hoe het slot reageert op voortgang

- **Voor uitdaging 2 is opgelost:** het symboolvenster toont een neutrale lege vorm of een oningevuld silhouet. Zodra Wannes uitdaging 2 voltooit en de ster met het oog vindt, verschijnt dit symbool automatisch op het slot. Wannes hoeft het niet zelf te kiezen.
- **Voor uitdaging 1 is opgelost:** het woordveld blijft beschikbaar, maar Wannes moet zelf het woord **BAL** intypen. Het spel geeft geen automatische invulling. Een hint kan hem herinneren aan de letters die hij verzameld heeft.
- **Voor uitdaging 3 is opgelost:** Wannes kan een kleur kiezen, maar de juiste kleur **signaalrood** moet hij zelf selecteren.
- De deur kan pas openen als alle drie de uitdagingen voltooid zijn én het juiste woord en de juiste kleur zijn ingevoerd of gekozen.
- Het woord dat Wannes al heeft getypt en de kleur die hij al heeft geselecteerd, blijven bewaard als hij het slot verlaat. Hij kan later terugkeren zonder zijn invoer kwijt te zijn. Het symbool is automatisch aanwezig als gevolg van uitdaging 2.
- Wannes kan uitdaging 4 op elk moment bezoeken en opnieuw bezoeken. De deur blijft zichtbaar als doel, zodat hij zelf kan beslissen wanneer hij terugkeert.

### De drie onderdelen van het slot

#### 1. Automatisch symbool — ster met een oog

- Het symboolvenster maakt zichtbaar dat het slot een symbool verwacht.
- Zodra uitdaging 2 is voltooid, verschijnt de **ster met een oog** automatisch in het venster met een korte mechanische klik.
- Er is geen symboolschijf en geen extra keuze nodig.
- Als uitdaging 2 nog niet voltooid is, toont het venster een lege omtrek en eventueel een subtiele indicatie dat er nog iets ontbreekt.
- De ster met een oog is dus een voortgangsbeloning, geen handeling die Wannes aan de deur moet uitvoeren.

#### 2. Zelf het woord typen

- Wannes krijgt één duidelijk invoerveld met het label **GEHEIM WOORD**.
- Hij typt zelf het woord dat hij in uitdaging 1 heeft ontdekt: **BAL**.
- Gebruik een groot invoerveld en een duidelijk toetsenbord op de telefoon. Hoofdletters en kleine letters worden gelijk behandeld; spaties voor of na het woord worden genegeerd.
- Het spel vult het woord niet automatisch in, ook niet nadat uitdaging 1 is voltooid.
- Bij een fout antwoord blijft zijn invoer staan zodat hij ze eenvoudig kan aanpassen.

**Hint bij vastlopen:** “Welke drie letters kreeg je in de speelgoedfabriek?”

#### 3. Zelf een kleur kiezen

- Wannes krijgt een kleine selectie grote, duidelijk gelabelde kleurstalen.
- Hij kiest zelf één kleur. De juiste kleur is **signaalrood**, de aanwijzing uit uitdaging 3.
- Iedere kleur heeft naast de kleur zelf ook een tekstlabel, zodat kleurherkenning niet de enige manier is om de keuze te begrijpen.
- De kleur wordt niet automatisch gekozen na uitdaging 3.
- Zijn keuze blijft geselecteerd tot hij een andere kleur kiest.

**Hint bij vastlopen:** “Denk aan het balletje dat je onder de bekers moest volgen.”

### Knop OPEN DE DEUR en controle

Onder het woordveld en de kleurkeuze staat één grote knop **OPEN DE DEUR**.

- De knop is zichtbaar en gemakkelijk met één duim te bedienen.
- Als nog niet alle drie de uitdagingen voltooid zijn, legt het spel vriendelijk uit dat het slot nog aanwijzingen mist. De deur geeft geen straf en Wannes kan meteen terug op ontdekking gaan.
- Als de uitdagingen voltooid zijn maar het woord of de kleur fout is, volgt korte mechanische feedback. Het symbool blijft staan en het woord en de kleur blijven geselecteerd.
- Er zijn onbeperkte pogingen en geen timer, verloren levens of game-over.
- Bij de juiste combinatie — automatisch verschenen ster met oog, woord **BAL** en kleur **signaalrood** — klikken de onderdelen vast en opent de deur.

### Juiste oplossing en herkomst

| Onderdeel | Hoe het wordt ingevuld | Herkomst |
|---|---|---|
| Symbool | Verschijnt automatisch | Uitdaging 2 |
| Woord | Wannes typt **BAL** | Uitdaging 1 |
| Kleur | Wannes kiest **signaalrood** | Uitdaging 3 |

De drie uitdagingen mogen in elke volgorde worden gespeeld. De volgorde van oplossen verandert niets aan de oplossing van het slot.

### Hints en feedback

Hints verschijnen uitsluitend wanneer Wannes zelf op de `?`-knop drukt. Ze verschijnen niet automatisch na fouten of na meerdere mislukte pogingen.

1. **Subtiele hint:** “Je hebt al dingen ontdekt in het laboratorium. Kijk wat je al weet.”
2. **Gerichte hint:** “Het symbool wordt voor je bewaard. Het woord moet je zelf typen en de kleur moet je zelf kiezen.”
3. **Expliciete hint:** de game herinnert Wannes aan de drie bronnen: de speelgoedfabriek, het kistjesraadsel en de bekers.

**Bij een onvolledige verzameling:**

> “Er ontbreekt nog een aanwijzing. Ga gerust verder op ontdekkingstocht — je kunt altijd terugkomen.”

**Bij een fout woord of verkeerde kleur:**

> “Klik… brom… nog niet juist. Kijk nog eens naar wat je ontdekt hebt.”

**Bij de juiste oplossing:**

> “Dat is hem! Jij hebt alle aanwijzingen gevonden én het geheim ontrafeld!”

Daarna licht het slot op en schuift de deur langzaam open. Eerst valt warm licht door de kier. Het spel zegt:

> “Wacht eens… Ik denk dat ze daarbinnen op jou staan te wachten.”

Daarna gaat de deur helemaal open en begint de verjaardagsfinale.

### Mobiele bediening en benodigde schermen

- Ontwerp voor iPhone in staande stand en bediening met één duim.
- Gebruik een groot tekstveld, duidelijke kleurstalen en hoog contrast.
- Toon het symbool als voortgangsstatus, niet als interactieve keuze.
- De deur blijft toegankelijk vanuit het laboratorium, ook als nog niet alle uitdagingen zijn opgelost.
- Animaties zijn kort en mogen geen noodzakelijke informatie verbergen.

Schermen en toestanden:
1. **Eerste ontdekking:** gesloten deur en slot met lege aanwijzingsstatussen.
2. **Slot in voortgang:** symbool verschijnt automatisch wanneer uitdaging 2 voltooid wordt.
3. **Woord en kleur invoeren:** groot invoerveld, kleurstalen en OPEN DE DEUR-knop.
4. **Nog aanwijzingen nodig:** vriendelijke melding en terugkeer naar vrije verkenning.
5. **Fout antwoord:** korte feedback zonder invoer of keuze te wissen.
6. **Deur opent:** mechanische beweging, warm licht en overgang naar de finale.

Benodigde assets:
- Grote deur in gesloten, gedeeltelijk geopende en open toestand.
- Symboolvenster met lege status en ster-met-oog-status.
- Groot woordveld en toetsenbordvriendelijke invoer.
- Gelabelde kleurstalen, inclusief signaalrood.
- Grote OPEN DE DEUR-knop, lampje en korte succes-/foutindicatoren.
- het spelillustratie voor reacties en warme lichtstraal voor de finale.

## Finale — de feestelijke onthulling

Achter de deur bevindt zich de verrassing die de speelgoedfiguren voor Wannes hebben voorbereid. Na de onthulling drukt Wannes op de grote rode feestknop. Die activeert visueel de lichtjes en confetti. Daarna wordt het beeld rustiger en verschijnt de boodschap in twee stappen: eerst **“Proficiat Wannes!”**, daarna **“Dat verdient een cadeau.”** De speelgoedfiguren en de feestscène blijven zichtbaar. Er is geen geluid, geen extra tik nodig en geen aanvullende opdracht of raadsel om naar het echte cadeau te leiden.

## Volgende ontwerpstappen

1. Ontwerp de vrije laboratoriumverkenning en de plekken waar Wannes de drie uitdagingen ontdekt.
2. Werk de schermenlijst en benodigde assets voor uitdaging 1, 2 en 3 uit.
3. Stem de finalebeschrijving af op de goedgekeurde boodschap en controleer dat er geen geluid, extra opdracht of extra interactie wordt toegevoegd.
4. Controleer het hele dossier op tegenstrijdigheden en maak daarna pas de master-prompt.

**Bouwstop:** dit bestand beschrijft het ontwerp. Er wordt nog geen nieuwe gamecode gebouwd zolang het volledige dossier niet is goedgekeurd.
