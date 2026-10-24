# ROBO MYSTERY — Uitdagingen

**Versie:** 0.5  
**Status:** Ontwerpdossier in ontwikkeling — nog geen nieuwe gamecode.  
**Focus van deze revisie:** uitdaging 1 herwerkt tot drie match-3-levels; beloningen afgestemd op het grote slot.

## Algemene spelregels

- Het spel bestaat uit vier hoofd uitdagingen: match-3-puzzels, logica/raadsels, volgen en combineren.
- Uitdagingen 1, 2 en 3 leveren elk één onderdeel op dat nodig is voor het slot in uitdaging 4.
- Fouten mogen de speler niet onherroepelijk blokkeren. Geef feedback, hints en nieuwe kansen.
- Het spel is Nederlandstalig, mobile-first en geschikt voor bediening op een iPhone.
- De verjaardagsverrassing blijft verborgen tot de deur in uitdaging 4 opengaat.

## Uitdaging 1 — De robotfabriek

**Status:** ontwerp vastgelegd op hoofdlijnen; nog geen gamecode.  
**Spelvorm:** drie korte match-3-levels, geïnspireerd op het algemene spelprincipe van Royal Match. Gebruik geen gekopieerde levels, artwork, personages, interface of merkspecifieke vormgeving. De eigen wereld is een retro-futuristisch speelgoedlaboratorium in handgedrukte popartstijl.

**Doel in het verhaal:** de robot heeft drie energiecellen nodig om een fabriekssysteem te activeren. Wannes helpt de robot door drie opeenvolgende puzzellevels. Elk level levert één letter op. Na level 3 vormt hij het woord **BAL**. Dit is de woordaanwijzing voor het grote slot in uitdaging 4.

**Beloning van uitdaging 1:** de letters **B**, **A** en **L**, in die volgorde, die samen **BAL** vormen.  
**Beloning die hier vervalt:** de ster met het oog hoort niet langer bij uitdaging 1. Die wordt voortaan verdiend in **uitdaging 2**.  
**Geschatte speelduur:** ongeveer 3 minuten, afhankelijk van het aantal pogingen.  
**Bediening:** tik op een symbool en vervolgens op een direct aangrenzend symbool om ze te verwisselen. Het bord en alle belangrijke bediening blijven zichtbaar op een iPhone in staande stand.

### Gemeenschappelijke spelregels voor de drie levels

- Het speelbord bestaat uit een compact raster van gekleurde, duidelijk herkenbare fabriekssymbolen, bijvoorbeeld rode energiecellen, gele tandwielen, blauwe bouten en groene kristallen.
- Een geldige zet verwisselt twee horizontaal of verticaal aangrenzende symbolen.
- Een verwisseling telt alleen als er daardoor een match van minstens drie gelijke symbolen ontstaat. Als geen match ontstaat, bewegen de symbolen terug en wordt geen zet verbruikt.
- Een match verwijdert de passende symbolen; symbolen erboven vallen naar beneden en nieuwe symbolen vullen de lege plaatsen aan.
- Doelobjecten en obstakels moeten visueel anders zijn dan gewone match-symbolen.
- Het doel van het level en het aantal resterende zetten staan steeds duidelijk in beeld, zonder kleine tekst.
- Na een geldige match zijn animaties kort en leesbaar. De speler moet kunnen zien wat verdween en wat viel.
- Een level heeft een beperkt aantal zetten, maar mag niet onredelijk moeilijk zijn. Het ontwerp moet altijd minstens één oplosbare route hebben; bij herhaald vastlopen kan een hint de aandacht op een mogelijke match richten.
- Er is geen game-over en geen tijdslimiet. Wannes mag rustig nadenken en opnieuw proberen.
- Een hint mag een mogelijke zet laten oplichten, maar voert die niet automatisch uit.
- Bij voltooiing krijgt Wannes een korte succesanimatie en de bijbehorende letter. De letter blijft zichtbaar in een vaste verzamelstrook boven of onder het bord.
- De game bewaart voortgang lokaal zodat een onbedoelde herlaadactie geen reeds verdiende letters hoeft te wissen.

### Level 1 — De energiecellen

**Verhaal:** de fabriek is donker. De robot legt uit dat hij rode energiecellen moet verzamelen om het eerste circuit te activeren.

**Doel:** verzamel **8 rode energiecellen** binnen **12 zetten**.

**Bord en regels:**
- Start met een raster van match-symbolen in vier soorten: rode energiecellen, gele tandwielen, blauwe bouten en groene kristallen.
- Alleen matches van rode energiecellen tellen mee voor het doel; matches van andere symbolen blijven nuttig om het bord te veranderen en nieuwe kansen te maken.
- De teller toont de voortgang van 0/8 tot 8/8.
- De beginsituatie moet zo worden ingericht dat er direct minstens één geldige match mogelijk is en dat het doel haalbaar is binnen het zetlimiet.
- Zodra de teller 8 bereikt, stopt het level direct en volgt de beloning; resterende zetten zijn een bonusgevoel, geen extra vereiste.

**Hintladder:**
1. Subtiel: één mogelijke match met rode energiecellen krijgt kort een zachte puls.
2. Duidelijker: de robot zegt: “Probeer rode energiecellen naast elkaar te krijgen.”
3. Expliciet: de game licht twee aangrenzende symbolen op die verwisseld kunnen worden om een geldige match te maken.

**Introductietekst van de robot:**
> “De fabriek is uitgevallen. Verzamel acht rode energiecellen. Maak rijen van minstens drie dezelfde symbolen om ze op te laden!”

**Foutfeedback:**
- Ongeldige verwisseling: “Die combinatie vormt nog geen match. Probeer twee andere symbolen.”
- Geen rode energiecel geraakt: “Goed geprobeerd. Kijk of je ook rode energiecellen kunt laten verdwijnen.”

**Succesfeedback:**
> “Circuit één draait weer! Goed gedaan.”

**Beloning:** de letter **B** verschijnt op een metalen label. De robot plaatst die in de verzamelstrook: **B _ _**.

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
2. Duidelijker: de robot zegt: “Maak een match naast een houten kistje om het open te breken.”
3. Expliciet: de game licht een concrete verwisseling op die naast een kistje een match vormt.

**Introductietekst van de robot:**
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
- Het level eindigt zodra de sleutel de uitgang bereikt. Bij herhaald mislukken kan het spel een hint geven of het bord opnieuw aanbieden.
- De sleutel moet tijdens vallen zichtbaar blijven en mag niet achter effecten of interface-elementen verdwijnen.

**Hintladder:**
1. Subtiel: de vakjes direct onder de sleutel lichten kort op.
2. Duidelijker: de robot zegt: “Maak ruimte onder de sleutel, dan kan ze naar beneden vallen.”
3. Expliciet: een geldige match die ruimte onder de sleutel maakt, wordt aangeduid.

**Introductietekst van de robot:**
> “Daar is de energiesleutel! Maak de vakjes onder haar vrij en laat de sleutel naar de uitgang vallen.”

**Foutfeedback:**
- Ongeldige verwisseling: “Geen match deze keer. Zoek een combinatie die ruimte maakt.”
- Match elders: “Goed! Kijk nu of je ook ruimte onder de sleutel kunt vrijmaken.”

**Succesfeedback:**
> “De uitgang is open! De fabriek is weer helemaal wakker.”

**Beloning:** de letter **L** verschijnt en wordt toegevoegd aan de verzamelstrook: **B A L**.

### De drie letters samen — onthulling van BAL

Na level 3 schuift de verzamelstrook naar het midden van het scherm. De letters **B**, **A** en **L** komen samen op één stevig metalen plaatje. De robot zegt:

> “B… A… L. Dat is je eerste geheime woord. Onthoud het goed — je hebt het later nodig!”

Het woord wordt niet gekoppeld aan een gouden medaille of een extra voorwerp uit uitdaging 2. Het is de expliciete woordaanwijzing van uitdaging 1 en wordt opgeslagen in de voortgang van het spel, zodat het later bij het grote slot gebruikt kan worden.

**Einde van uitdaging 1:** de robot toont een korte overgang naar het volgende mysterieuze onderdeel van het speelgoedlab. De ster met het oog wordt hier niet getoond en blijft gereserveerd als beloning van uitdaging 2.

### Ontwerp- en toegankelijkheidsregels

- Geen exacte nabootsing van Royal Match: gebruik alleen het algemene match-3-principe en maak eigen symbolen, doelen, animaties en teksten.
- Vermijd kleine tegels en minieme tikzones; alle vakjes moeten comfortabel met een duim te bedienen zijn.
- Gebruik naast kleur ook vorm of pictogram, zodat doelen niet alleen van kleurherkenning afhangen.
- Respecteer gereduceerde beweging waar mogelijk; animaties mogen nooit de enige manier zijn om spelstatus te begrijpen.
- Laat de speler na elke match genoeg tijd om het resultaat te zien; geen snelle automatische cascades die invoer verwarrend maken.
- Houd de instructie kort en toon het leveldoel altijd tijdens het spelen.
- De precieze rasterafmetingen, symbolenverdeling, zetlimieten en startborden moeten tijdens de technische uitwerking worden getest. Dit dossier legt de spelregels en doelen vast, niet de definitieve puzzelmatrices.

## Uitdaging 2 — De drie raadselmeesters

**Doel:** Wannes lost drie opeenvolgende puzzels op. De cijfercode opent een geheim deurtje, het logische raadsel levert een sleutel op en de laatste deductiepuzzel wijst het juiste kistje aan. In de kist zit **een aanwijzing die onderdeel is van de uitkomst van uitdaging 4**, niet een gouden medaille.

**Geschatte duur:** 3–5 minuten.  
**Bediening:** grote, duidelijke tikbare elementen; geschikt voor iPhone.  
**Fouten:** opnieuw proberen, zonder onherroepelijke blokkade.  
**Hints:** oplopend van subtiel naar expliciet.

### Deel 1 — Het geheime deurtje: kraak de cijfercode

De robot ontdekt een klein metalen deurtje met een mechanisch cijferslot van drie cijfers. Wannes krijgt vijf aanwijzingen:

- **682** — één cijfer is juist én staat op de juiste plaats.
- **614** — één cijfer is juist, maar staat op de verkeerde plaats.
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
- De robot geeft stapsgewijs hints als Wannes vastloopt.
- Bij 042 klikken de cijfers op hun plaats en springt het kleine deurtje open.

### Deel 2 — De drie speelgoedfiguren: wie heeft de sleutel?

Achter het deurtje zitten drie figuren verstopt: de aap, panda en schildpad. Ze bewaken een sleutel.

**Regel:** precies één van de drie uitspraken is waar; de andere twee zijn onwaar.

- **Aap:** “De panda heeft de sleutel.”
- **Panda:** “Ik heb de sleutel niet.”
- **Schildpad:** “De aap heeft de sleutel niet.”

**Vraag:** wie heeft de sleutel?

Wannes kiest de aap, panda of schildpad en bevestigt zijn antwoord.

#### Oplossing en logische controle

| Wie heeft de sleutel? | Uitspraak aap | Uitspraak panda | Uitspraak schildpad | Aantal ware uitspraken |
|---|---|---|---|---:|
| Aap | Onwaar | Waar | Onwaar | 1 |
| Panda | Waar | Onwaar | Waar | 2 |
| Schildpad | Onwaar | Waar | Waar | 2 |

**Juiste antwoord:** de aap heeft de sleutel.

#### Beloning en overgang
De aap haalt een kleine messing sleutel achter zijn rug vandaan en zegt:

> “Goed geredeneerd! Je hebt me door. Hier is de sleutel — maar je moet nog ontdekken welk kistje de moeite waard is.”

De sleutel wordt automatisch als gevonden voorwerp geregistreerd; Wannes hoeft geen code te onthouden.

#### Hints
1. “Wat gebeurt er als de aap de sleutel heeft?”
2. “Controleer hoeveel uitspraken waar zijn als de panda de sleutel heeft.”
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
- Bij de juiste keuze draait de sleutel, klikt het slot open en gaat het deksel langzaam omhoog.

**Inhoud van de kist:** een fysiek voorwerp of kaart met de aanwijzing die uitdaging 2 aan uitdaging 4 levert. De gouden medaille is geschrapt. De afgesproken aanwijzingen voor het grote slot zijn: **BAL** (uitdaging 1), ster met oog (uitdaging 2) en signaalrood (uitdaging 3). Daarom bevat de kist de ster-met-oog-aanwijzing — bijvoorbeeld op een geheim kaartje of een bijzonder gegraveerd plaatje. De onthulling mag het woord BAL niet eerder tonen dan op dit eindmoment van uitdaging 2.

**Reactie van de robot:**

> “Gevonden! Jij hebt de code gekraakt, de sleutel verdiend én het juiste kistje opgespoord!”

### Complete speelervaring van uitdaging 2

1. Wannes kraakt de code **042**.
2. Het geheime deurtje springt open en onthult de aap, panda en schildpad.
3. Wannes redeneert dat de aap de sleutel heeft.
4. De aap geeft hem de messing sleutel.
5. Wannes onderzoekt de uitspraken op drie kistjes en kiest het rode kistje.
6. De kist gaat open en onthult de **ster met een oog**, de symboolaanwijzing die nodig is voor uitdaging 4.

**Ontwerpregel:** de cijfercode, sleutel en kistjes zijn onderdelen van uitdaging 2. Het woord BAL is de opbrengst voor het grote slot. Voeg geen extra puzzel toe en vervang BAL niet door een gouden medaille.

## Uitdaging 3 — De onmogelijke bekers

**Status:** ontwerp uitgewerkt; moeilijkheid gekozen: **opbouwend**.  
**Spelvorm:** een klassieke bekers-truc in drie rondes. Wannes volgt één rood balletje terwijl drie bekers van plaats wisselen. De beweging wordt per ronde iets sneller, maar blijft volledig zichtbaar en eerlijk te volgen.

**Doel in het verhaal:** de robot toont een goocheltruc die de kleur van het laatste onderdeel van het grote slot onthult. Wannes moet het balletje volgen en de juiste beker kiezen in alle drie de rondes.

**Beloning van uitdaging 3:** de kleur **signaalrood**, de kleur-aanwijzing voor uitdaging 4.  
**Geschatte speelduur:** ongeveer 2 minuten.  
**Bediening:** Wannes tikt op één van drie grote bekers op het scherm; geschikt voor iPhone in staande stand.  
**Geen game-over:** na een fout mag Wannes opnieuw proberen. Bij herhaald vastlopen helpt de robot met een hint of toont hij de beginpositie opnieuw.

### De scène en de spelregels

De robot staat achter een kleine goocheltafel in het speelgoedlaboratorium. Drie stevige bekers staan naast elkaar op gemarkeerde plaatsen: links, midden en rechts. De bekers hebben elk een eigen herkenbare vorm en kleur, maar de juiste beker wordt niet aangeduid met een blijvend kenmerk. Het rode balletje is het enige doelobject.

Aan het begin van iedere ronde:
1. De robot toont het rode balletje duidelijk onder één beker.
2. De beker wordt opgetild of kort transparant getoond zodat Wannes de beginpositie goed ziet.
3. De beker wordt teruggezet en alle drie de bekers zijn even zichtbaar.
4. De wisselbewegingen beginnen pas wanneer Wannes klaar is; de speler hoeft niet op een startknop te drukken tijdens een animatie.
5. De bekers wisselen onderling van plaats. De hele beweging blijft zichtbaar; er zijn geen geheime teleportaties, verdwijntrucs of bewegingen buiten het scherm.
6. Na de laatste wissel stoppen de bekers volledig. Pas daarna kan Wannes een keuze maken.
7. Wannes tikt op de beker waaronder hij denkt dat het balletje ligt.
8. De gekozen beker gaat omhoog en toont of het balletje eronder ligt.
9. Een juist antwoord voltooit de ronde. Bij een fout antwoord geeft de robot korte feedback en volgt een nieuwe poging met een opnieuw getoonde beginpositie.

**Belangrijk:** de spelregels moeten visueel duidelijk maken dat de bekers zelf van plaats wisselen. De speler volgt de bekerpositie, niet een verwarrende reeks willekeurige animaties. Geen tijdslimiet voor het kiezen na afloop van de wissels.

### Ronde 1 — Leer de truc

**Doel:** de eerste juiste beker vinden na **2 wissels**.

- Het balletje wordt zichtbaar onder één beker geplaatst.
- De bekers wisselen twee keer van plaats.
- De wissels zijn langzaam, met een korte pauze tussen de bewegingen.
- De bekers volgen een duidelijk pad en overlappen elkaar niet.
- Deze ronde leert het principe en is bewust eenvoudig.

**Introductietekst van de robot:**
> “Let goed op het rode balletje. Ik wissel de bekers twee keer. Kijk waar het balletje eindigt!”

**Feedback bij een fout:**
> “Oei, die beker is leeg! Geen probleem — kijk opnieuw waar ik het balletje verstop.”

**Feedback bij succes:**
> “Juist! Je hebt de truc door.”

**Hints:**
1. Eerste hint: “Volg één beker tegelijk met je ogen.”
2. Tweede hint: de robot toont de beginpositie opnieuw en voert de twee wissels langzamer uit.
3. Extra hulp: de robot vertraagt de wissels en pauzeert kort nadat elke wissel voltooid is.

**Overgang:** het balletje springt kort op en neer en rolt daarna weer onder een beker voor ronde 2.

### Ronde 2 — De afleiding

**Doel:** de juiste beker vinden na **3 wissels**.

- De bekers wisselen drie keer van plaats.
- De animatie is iets sneller dan in ronde 1, maar elke wissel blijft afzonderlijk herkenbaar.
- Er is een korte pauze tussen de tweede en derde wissel, zodat de reeks niet als één onleesbare beweging aanvoelt.
- De robot probeert Wannes met een grapje af te leiden, maar de tekst verschijnt vóór of na de beweging, nooit over de bekers heen.
- De bekers blijven steeds volledig binnen het zichtbare speelgebied.

**Introductietekst van de robot:**
> “Goed opgelet! Nu drie wissels. Laat je niet afleiden door mijn geweldige goochelstem…”

**Grappige afleiding van de robot:**
> “Psst… wist je dat robots ook kunnen goochelen? Euh… blijf vooral naar de bekers kijken!”

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
- De robot blijft stil tijdens de daadwerkelijke wissels zodat hij niet visueel of tekstueel afleidt.
- Na de vierde wissel blijven de bekers stilstaan. Wannes krijgt alle tijd om zijn keuze te maken.

**Introductietekst van de robot:**
> “Klaar voor de meestertruc? Vier wissels. Blijf bij het rode balletje — jij kunt dit!”

**Feedback bij een fout:**
> “Bijna! Zelfs de beste goochelaars oefenen hun trucs. We proberen het nog een keer.”

**Feedback bij succes:**
> “Ongelooflijk! Je hebt alle drie de rondes gekraakt!”

**Hints:**
1. Eerste hint: “Probeer de beker te volgen in plaats van naar het balletje te zoeken.”
2. Tweede hint: de robot toont de beginpositie opnieuw en speelt de vier wissels op het tempo van ronde 2 af.
3. Extra hulp: de bekers wisselen opnieuw, één voor één, met een korte pauze na iedere wissel. Dit maakt de reeks eenvoudiger zonder de oplossing direct te tonen.

### Regels voor eerlijke moeilijkheid

- De gekozen opbouw is vast: **2 wissels → 3 wissels → 4 wissels**, met oplopende snelheid.
- De animaties moeten in echte tests op een iPhone goed te volgen zijn; als ronde 3 te moeilijk blijkt, verlaag dan de snelheid vóór je het aantal wissels verandert.
- De snelheid is geen reflex-test. Wannes hoeft niet tijdens een wissel te tikken en krijgt geen aftellende klok.
- Na een fout wordt de beginpositie opnieuw getoond. Er is geen strafscore, geen verloren leven en geen terugkeer naar een eerdere uitdaging.
- Bij herhaalde fouten wordt automatisch een hint aangeboden, maar de speler mag die negeren.
- De beker die het balletje verbergt mag niet steeds dezelfde kleur of vaste positie hebben. De startpositie varieert zodat Wannes de truc echt moet volgen.
- De wisselreeks moet gecontroleerd worden op geldige, visueel begrijpelijke bewegingen. Bekers mogen elkaar niet bedekken of buiten het scherm bewegen.
- Gebruik geen stroboscopische effecten of onnodige camerabewegingen. De feedback blijft ook begrijpelijk als beweging beperkt wordt.

### Beloning — signaalrood

Na het succes in ronde 3 tilt de robot de juiste beker op. Het rode balletje stijgt op, verandert in een gloeiende rode lichtbol en werpt een rode lichtcirkel op de tafel. De robot scant de lichtbol en projecteert een eenvoudige rode kleurstaal met het label **SIGNAALROOD**.

**Tekst van de robot:**
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
- Robotportret of klein robotfiguur voor dialoog.
- Rood lichtbol-effect en kleurstaal voor signaalrood.
- Eenvoudige markering voor de hintstand.
- Korte, optionele geluiden voor bekerwissel, beker optillen en succes; het spel moet volledig begrijpelijk blijven zonder geluid.

## Uitdaging 4 — Het slot van het geheim

Wannes combineert de drie aanwijzingen uit uitdagingen 1, 2 en 3 met drie bedieningselementen op de deur.

| Onderdeel van het slot | Aanwijzing | Herkomst |
|---|---|---|
| Symboolschijf | Ster met een oog | Uitdaging 1 |
| Woordschijf | BAL | Uitdaging 2 |
| Kleurschijf | Signaalrood | Uitdaging 3 |

Een verkeerde combinatie houdt de deur dicht, met een korte komische reactie. Wannes mag onbeperkt opnieuw proberen en kan hints krijgen. Bij de juiste combinatie gaat de deur open.

## Finale — de feestelijke onthulling

Achter de deur bevindt zich de verrassing die de speelgoedfiguren voor Wannes hebben voorbereid. Na de onthulling voert Wannes nog één eenvoudige feestelijke handeling uit, bijvoorbeeld op een grote feestknop drukken of aan een lint trekken. Daarna verschijnen confetti en een persoonlijke verjaardagsboodschap.

**Nog te beslissen:** de exacte echte slotscène, de persoonlijke boodschap en de laatste interactie.

## Volgende ontwerpstappen

1. Werk uitdaging 3 volledig uit, inclusief regels, hints, feedback en schermen.
2. Werk de schermenlijst en benodigde assets voor uitdaging 1 en 2 uit.
3. Werk de resterende uitdagingen, finale en persoonlijke boodschap verder uit.
4. Controleer het hele dossier op tegenstrijdigheden en maak daarna pas de master-prompt.

**Bouwstop:** dit bestand beschrijft het ontwerp. Er wordt nog geen nieuwe gamecode gebouwd zolang het volledige dossier niet is goedgekeurd.
