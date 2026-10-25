# Level 1 — De energiecellen

**Versie:** 1.1  
**Status:** ontwerp en simulatie gevalideerd voor de beschreven regels; geen gamecode.  
**Branch:** `design/level-1-random-refill`  
**Doel:** dit document vervangt voor level 1 de eerdere doelwaarde van 8 cellen en de limiet van 12 zetten. De algemene match-3-regels blijven gelden waar ze niet met dit document botsen.

## Speldoel

Verzamel **minstens 10 rode energiecellen** door matches van drie of meer gelijke symbolen te maken. Zodra de teller 10 of hoger bereikt, voltooit Wannes het level en verdient hij de letter **B**. Een match kan het totaal boven 10 brengen; exact 10 is niet vereist.

**Introductietekst**

> De fabriek is uitgevallen. Verzamel tien rode energiecellen. Maak rijen van minstens drie dezelfde symbolen om ze op te laden!

**Succesfeedback**

> Circuit één draait weer! Goed gedaan.

## Bord en bediening

- Raster: **5 kolommen × 7 rijen**.
- Vier gewone symbolen: rood (energiecel), blauw (bout), groen (kristal) en geel (tandwiel). In de definitieve illustraties krijgt elk symbool ook een eigen herkenbare vorm, niet alleen een kleur.
- Tik op één vakje en daarna op een direct aangrenzend vakje horizontaal of verticaal om de symbolen te wisselen.
- Een wissel telt alleen als die minstens één horizontale of verticale match van 3+ symbolen veroorzaakt.
- Een wissel zonder match wordt teruggedraaid en telt niet als zet.
- Matches van alle vier kleuren mogen het bord veranderen; alleen verwijderde rode symbolen tellen mee voor het doel.
- Na een match verdwijnen alle betrokken symbolen, de overblijvende symbolen vallen omlaag en lege vakjes worden gevuld.
- Alle gelijktijdige horizontale en verticale matches worden als één verwijderingsronde afgehandeld. Een symbool dat deel is van een kruis-match telt maar één keer. Daarna wordt zwaartekracht en aanvulling toegepast; eventuele nieuwe matches vormen een kettingreactie.
- De teller blijft altijd zichtbaar en toont `0/10` tot het doel bereikt is.

## Geen zettenlimiet

- Er is **geen zettenlimiet, timer, levenssysteem of game-over door fouten**.
- Wannes mag zo veel geldige zetten doen als hij nodig heeft.
- Ongeldige wissels worden teruggedraaid met vriendelijke feedback en zonder straf.
- De uitdaging komt uit het zoeken naar nuttige combinaties, niet uit een aftellende teller.

## Willekeurige aanvulling — geen vaste aanvulreeks

Nieuwe symbolen worden **willekeurig** gekozen uit de vier soorten met gelijke kans (25% per soort). Er wordt geen vooraf vastgelegde herhaalreeks gebruikt.

- Voor gewone spelruns gebruikt de game een normale willekeurige generator.
- Voor automatische tests mag een seed worden ingesteld zodat een test exact reproduceerbaar is. Een testseed is alleen een testhulpmiddel en wordt geen spelontwerpregel.
- De generator kiest elk nieuw symbool onafhankelijk; er wordt geen kunstmatige kleurverdeling of voorkeurskleur toegepast.
- Willekeur mag geen doodlopend bord opleveren: na elke cascade wordt gecontroleerd of er een geldige zet bestaat.

## Automatisch herstel bij vastlopen

Een bord kan geen geldige zetten meer hebben, ook al zijn er onbeperkt veel zetten toegestaan. Daarom:

1. Na het volledig afhandelen van een match en alle kettingreacties controleert de game of er een aangrenzende wissel bestaat die een match oplevert.
2. Als geen geldige zet bestaat, worden de bestaande symbolen geschud; de verzamelde rode energiecellen blijven behouden.
3. Het herschikte bord moet **geen automatische matches** bevatten en **minstens één geldige zet** hebben.
4. Als een shuffle niet aan beide voorwaarden voldoet, probeert de game opnieuw. De routine mag pas klaar zijn wanneer een geldig bord gevonden is.
5. De voortgangsteller, de verdiende beloning en de status van het level worden nooit gereset door herschikken.
6. Het bord wordt niet automatisch geschud als er nog een geldige zet is.

## Hints

- De hint verschijnt alleen wanneer Wannes zelf op `?` tikt.
- Een hint licht één geldige wissel op; de game voert de wissel niet zelf uit.
- Waar mogelijk kiest de hint een zet die rode energiecellen matcht. Als dat niet mogelijk is, toont de hint een andere geldige zet die het bord verder helpt.
- Geen automatische hints na fouten of na meerdere zetten zonder vooruitgang.

## Voltooiing en voortgang

- Het level eindigt zodra de teller **10 of hoger** is.
- Toon een korte, stille succesanimatie en de letter **B**.
- De verzamelstrook wordt `B _ _`.
- De letter en voltooide status worden opgeslagen volgens de algemene voortgangsregels.
- Terugkeren naar het level hervat de opgeslagen toestand; alleen een expliciete spelersactie mag een levelreset uitvoeren.

## Definitieve startmatrix

Rijen zijn van boven naar beneden genummerd; kolommen van links naar rechts. De letters zijn ontwikkelcodes, geen definitieve art:

```text
R Y Y R R
Y B Y Y R
Y Y B R B
B B R B R
B R R Y Y
G Y B Y G
Y B Y R Y
```

Deze matrix is geverifieerd als startbord: **geen automatische match** en **22 geldige aangrenzende wissels**. De matrix blijft vast; alleen de aanvulling is willekeurig.

## Simulatietest

De referentiesimulatie in `tests/level1_simulation.py` gebruikt dezelfde matrix en willekeurige aanvulling. Bij iedere stap kiest de test willekeurig één van de beschikbare geldige zetten. De test stopt zodra minstens 10 rode symbolen verzameld zijn. Als er geen geldige zetten meer zijn, wordt de shuffle-regel toegepast.

Resultaat van **1.000 onafhankelijke, seeded testpartijen**, opnieuw uitgevoerd tijdens de huidige implementatiestap:

| Controle | Resultaat |
|---|---:|
| Partijen die het doel bereikten | 1.000 / 1.000 |
| Partijen die automatisch moesten herschikken | 0 |
| Gemiddeld aantal geldige zetten | 5,05 |
| Mediaan aantal geldige zetten | 5 |
| 95e percentiel | 9 zetten |
| Langste geteste partij | 14 zetten |
| Startmatches | 0 |
| Geldige zetten bij de start | 22 |

De eerdere tabel met 10.000 partijen kon in deze werksessie niet volledig opnieuw worden uitgevoerd en geldt daarom niet als opnieuw geverifieerd resultaat. De 1.000 partijen hierboven zijn wel daadwerkelijk uitgevoerd met seeds 0 t/m 999. Ze testen de willekeurige-zetstrategie, niet elke mogelijke keuze die een speler kan maken. Een steekproef is geen wiskundig bewijs voor alle spelverlopen.
## Acceptatiecriteria vóór inbouw in de game

1. Bord is exact 5 × 7.
2. Startmatrix heeft geen automatische matches en minstens één geldige zet.
3. Alleen aangrenzende wissels zijn toegestaan.
4. Een wissel zonder match wordt teruggedraaid en verandert de voortgang niet.
5. Kruisende/overlappende matches tellen elk verwijderd vakje slechts één keer.
6. Zwaartekracht, willekeurige aanvulling en kettingreacties worden in die volgorde verwerkt.
7. Alleen rode verwijderde symbolen verhogen de doelsteller.
8. Doel wordt voltooid bij 10 of meer rode cellen.
9. Er is geen zettenlimiet of timer.
10. De aanvulling is willekeurig; een vaste aanvulreeks wordt niet in de productiegame gebruikt.
11. Een dood bord wordt herschikt zonder matches, met minstens één geldige zet en zonder voortgangsverlies.
12. De hints verschijnen alleen op verzoek en voeren geen zet uit.
13. Alle bediening past op iPhone-portret met ruime tikvlakken.
14. De testharness draait 10.000 seeded simulaties zonder vastlopen of mislukte voltooiing.

**Speelbare proef:** [prototype/level-1-energiecellen.html](../prototype/level-1-energiecellen.html) is een zelfstandig speelbare browserproef met deze basisregels. Het is nog niet geïntegreerd in de volledige fabriek, slaat nog geen voortgang op en is nog niet op een echte iPhone getest. De proef en de referentiesimulatie moeten vóór integratie nog doorlopen worden met de acceptatiecriteria hierboven.
