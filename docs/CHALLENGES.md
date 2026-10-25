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

- Het speelbord bestaat uit een compact raster van gekleurde, duidelijk herkenbare fabriekssymbolen, bijvoorbeeld rode energiecellen, gele tandwielen, blauwe bouten en groene kristallen.
- Een geldige zet verwisselt twee horizontaal of verticaal aangrenzende symbolen.
- Een verwisseling telt alleen als er daardoor een match van minstens drie gelijke symbolen ontstaat. Als geen match ontstaat, bewegen de symbolen terug en wordt geen zet verbruikt.
- Een match verwijdert de passende symbolen; symbolen erboven vallen naar beneden en nieuwe symbolen vullen de lege plaatsen aan.
- Doelobjecten en obstakels moeten visueel anders zijn dan gewone match-symbolen.
- Het doel van het level en het aantal resterende zetten staan steeds duidelijk in beeld, zonder kleine tekst.
- Na een geldige match zijn animaties kort en leesbaar. De speler moet kunnen zien wat verdween en wat viel.
- Een level heeft een beperkt aantal zetten, maar mag niet onredelijk moeilijk zijn. Het ontwerp moet altijd minstens één oplosbare route hebben. Wannes kan zelf via de `?`-knop een hint vragen; hints verschijnen nooit automatisch na fouten of herhaald vastlopen.
- Er is geen game-over en geen tijdslimiet. Wannes mag rustig nadenken en opnieuw proberen.
- Een hint mag een mogelijke zet laten oplichten, maar voert die niet automatisch uit.
- Bij voltooiing krijgt Wannes een korte succesanimatie en de bijbehorende letter. De letter blijft zichtbaar in een vaste verzamelstrook boven of onder het bord.
- De game bewaart voortgang lokaal na elke geldige zet en bij elke belangrijke wijziging, zodat een onbedoelde herlaadactie geen reeds verdiende letters of de huidige puzzelstand wist.
- Als Wannes de speelgoedfabriek verlaat en terugkomt, gaat hij verder vanaf het huidige level, met dezelfde bordstand, resterende zetten en verzamelde voortgang. Een level wordt alleen opnieuw gestart als Wannes daar zelf voor kiest of expliciet om een reset vraagt.

### Level 1 — De energiecellen

**Verhaal:** de fabriek is donker. Een bericht op de laboratoriummonitor legt uit dat rode energiecellen nodig zijn om het eerste circuit te activeren.

**Doel:** verzamel **8 rode energiecellen** binnen **12 zetten**.

**Bord en regels:**
- Start met een raster van match-symbolen in vier soorten: rode energiecellen, gele tandwielen, blauwe bouten en groene kristallen.
- Alleen matches van rode energiecellen tellen mee voor het doel; matches van andere symbolen blijven nuttig om het bord te veranderen en nieuwe kansen te maken.
- De teller toont de voortgang van 0/8 tot 8/8.
- De beginsituatie moet zo worden ingericht dat er direct minstens één geldige match mogelijk is en dat het doel haalbaar is binnen het zetlimiet.
- Zodra de teller 8 bereikt, stopt het level direct en volgt de beloning; resterende zetten zijn een bonusgevoel, geen extra vereiste.

**Hintladder:**
1. Subtiel: één mogelijke match met rode energiecellen krijgt kort een zachte puls.
2. Duidelijker: de laboratoriummonitor toont: “Probeer rode energiecellen naast elkaar te krijgen.”
3. Expliciet: de game licht twee aangrenzende symbolen op die verwisseld kunnen worden om een geldige match te maken.

**Introductietekst op de laboratoriummonitor:**
> “De fabriek is uitgevallen. Verzamel acht rode energiecellen. Maak rijen van minstens drie dezelfde symbolen om ze op te laden!”

**Foutfeedback:**
- Ongeldige verwisseling: “Die combinatie vormt nog geen match. Probeer twee andere symbolen.”
- Geen rode energiecel geraakt: “Goed geprobeerd. Kijk of je ook rode energiecellen kunt laten verdwijnen.”

**Succesfeedback:**
> “Circuit één draait weer! Goed gedaan.”

**Beloning:** de letter **B** verschijnt op een metalen label. De letter wordt toegevoegd aan de verzamelstrook: **B _ _**.

### Level 2 — De geblokkeerde tandwielen

**Verhaal:** het tweede deel van de fabriek is geblokkeerd door houten transportkistjes. De tandwielen moeten weer kunnen draaien.

**Doel:** verwijder **4 houten kistjes** binnen **14 zetten**.

**Bord en regels:**
- Het bord bevat match-symbolen en vier houten kistjes als obstakels.
- De kistjes zijn geen verwisselbare match-symbolen en kunnen niet zelf worden verplaatst.
- Een match direct naast een kistje beschadigt of verwijdert dat kistje. Elk kistje verdwijnt na één geldige match ernaast.
- Een match die naast meerdere kistjes ligt, mag meer dan één kistje tegelijk verwijderen; de beginsituatie mag dit niet onbedoeld te makkelijk of onmogelijk maken.
- De kistjes blokkeren de vakjes die ze bezetten. De speler moet dus nadenken over matches rond de obstakels.
- De teller toont de voortgang van 0/4 tot 4/4; het level eindigt zodra alle vier weg zijn.
- Het bord moet vooraf gecontroleerd worden op bereikbaarheid: alle vier kistjes moeten binnen het zetlimiet verwijderbaar zijn.

**Hintladder:**
1. Subtiel: een mogelijke match naast een kistje pulseert.
2. Duidelijker: het spel zegt: “Maak een match naast een houten kistje om het open te breken.”
3. Expliciet: de game licht een concrete verwisseling op die naast een kistje een match vormt.

**Introductietekst van het spel:**
> “Deze kistjes blokkeren de tandwielen. Maak matches naast de kistjes om ze weg te breken. Ruim ze alle vier op!”

**Foutfeedback:**
- Ongeldige verwisseling: “Die zet maakt geen match. Kijk eens naar de symbolen naast een kistje.”
- Match zonder effect op kistjes: “De symbolen zijn weg, maar de kistjes staan er nog. Probeer vlak naast een kistje te spelen.”

**Succesfeedback:**
> “De tandwielen zijn vrij! De fabriek komt weer op gang.”

**Beloning:** de letter **A** verschijnt op een metalen label en wordt toegevoegd aan de verzamelstrook: **B A _**.

### Level 3 — De geheime uitgang

**Verhaal:** het laatste circuit zit achter een afgesloten luik. De sleutelvormige energiecapsule moet naar de uitgang onderaan het bord vallen.

**Doel:** laat de **gouden energiesleutel** naar de uitgang onderaan het bord vallen binnen **16 zetten**.

**Bord en regels:**
- De sleutel is een speciaal doelobject bovenaan het raster; ze is niet verwisselbaar met gewone symbolen.
- De sleutel zakt naar beneden wanneer de vakjes eronder door matches worden vrijgemaakt. Symbolen die verdwijnen maken ruimte; de sleutel valt mee met de zwaartekracht van het bord.
- Het level heeft een duidelijk gemarkeerde uitgang onderaan, zodat Wannes begrijpt waar de sleutel naartoe moet.
- Gewone matches zijn nodig om de route vrij te maken. Een match vlak onder de sleutel is vaak nuttig, maar het bord moet meerdere haalbare zetten bieden.
- De voortgang wordt visueel getoond met de sleutel en de uitgang; er hoeft geen ingewikkelde score te zijn.
- Het level eindigt zodra de sleutel de uitgang bereikt. Wannes kan zelf een hint vragen via de `?`-knop of bewust kiezen om het bord opnieuw te proberen.
- De sleutel moet tijdens vallen zichtbaar blijven en mag niet achter effecten of interface-elementen verdwijnen.

**Hintladder:**
1. Subtiel: de vakjes direct onder de sleutel lichten kort op.
2. Duidelijker: het spel zegt: “Maak ruimte onder de sleutel, dan kan ze naar beneden vallen.”
3. Expliciet: een geldige match die ruimte onder de sleutel maakt, wordt aangeduid.

**Introductietekst op het scherm:**
> “Daar is de energiesleutel! Maak de vakjes onder haar vrij en laat de sleutel naar de uitgang vallen.”

**Foutfeedback:**
- Ongeldige verwisseling: “Geen match deze keer. Zoek een combinatie die ruimte maakt.”
- Match elders: “Goed! Kijk nu of je ook ruimte onder de sleutel kunt vrijmaken.”

**Succesfeedback:**
> “De uitgang is open! De fabriek is weer helemaal wakker.”

**Beloning:** de letter **L** verschijnt en wordt toegevoegd aan de verzamelstrook: **B A L**.

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

- **Charlie (aap):** “De panda heeft de sleutel.”
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
1. “Wat gebeurt er als de aap de sleutel heeft?”
2. “Controleer hoeveel uitspraken waar zijn als RidderUs de sleutel heeft.”
3. “Test alle drie de mogelijkheden. Slechts één ervan voldoet aan de regel.”

### Deel 3 — De drie kistjes: vind de aanwijzing voor het grote slot

De aap wijst naar drie gesloten kistjes. De sleutel past op het slot van het gekozen kistje. Op elk kistje staat een uitspraak. De regel blijft: **precies één uitspraak is waar**.

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
