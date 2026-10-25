# De mysterieuze fabriek — Scherm- en toestandspecificatie

**Versie:** 1.3  
**Status:** Werkdocument voor dossiercontrole; geen toestemming om gamecode te bouwen.  
**Doel:** elk zichtbaar scherm, elke betekenisvolle deeltoestand, overgang, tekst en herstelregel beschrijven voordat de master-prompt wordt geschreven.

## 1. Globale regels

- De speler ziet Nederlandse teksten; spreek Wannes direct aan, speels maar niet kinderachtig.
- De game is volledig stil. Geen audio, stem, trilfeedback of browsermelding als spelmechaniek. Een fout mag niet alleen via beweging of kleur worden aangegeven.
- Alle schermen zijn ontworpen voor iPhone-portret en tikbediening. Hoofdacties hebben grote tikvlakken.
- Elke uitdaging heeft een eigen hintstatus. Hints verschijnen alleen na tik op `?`. Het gedeelde hintpaneel volgt de regels in `TECH-SPEC.md`.
- Een schermwissel sluit overlays visueel, maar wist geen puzzelvoortgang. Teruggaan brengt Wannes naar dezelfde werkplaats.
- De drie hoofduitdagingen kunnen in elke volgorde worden gestart. De deur is vanaf het begin onderzoekbaar.
- Geen score, levens, timer, zettenlimiet, straf of automatische hint. Alle drie match-3-levels zijn onbeperkt en er is geen game-over.
- Alle teksten hieronder zijn de voorgestelde definitieve spelersteksten voor het dossier. Ze mogen pas als bouwtekst worden gebruikt nadat dit document als geheel is goedgekeurd.

## 2. Scherm-ID's en deeltoestanden

### T — Titelposter

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst |
|---|---|---|---|
| `T-01` | Vintage fabrieksposter, geen personages of herkenbare personagesilhouetten | START → `W-01`; bij opgeslagen voortgang VERDER SPELEN → herstelde toestand | Knop: **START** of **VERDER SPELEN** |
| `T-02` | Bevestigingsdialoog boven poster | Opnieuw beginnen → `T-03`; TERUG sluit dialoog | “Wil je opnieuw beginnen? Je huidige voortgang wordt gewist.” Knoppen: **OPNIEUW BEGINNEN**, **TERUG** |
| `T-03` | Verse starttoestand | Bevestiging voltooid → `W-01` | Geen extra tekst nodig |
| `T-04` | Herstelmelding bij ongeldige/beschadigde opslag | Kies opnieuw beginnen → schone `W-01`; TERUG laat herstelkeuze staan | “Je voortgang kon niet worden hersteld.” / “Je kunt opnieuw beginnen, maar je oude voortgang is mogelijk niet meer bruikbaar.” Knoppen: **OPNIEUW BEGINNEN**, **TERUG** |
| `T-05` | Tijdelijke sessie als opslag niet beschikbaar is | START opent werkplaats | “Voortgang kan op dit toestel niet betrouwbaar worden bewaard. Als je het spel sluit, kun je je voortgang verliezen.” |

### W — Volledige werkplaats

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst |
|---|---|---|---|
| `W-01` | Volledige werkplaats, vier hoofdobjecten tegelijk zichtbaar: computer links, groene locker centraal, bekertafel vooraan, rode deur rechts | Tik computer → `M-01`; locker → `L-01`; bekers → `C-01`; deur → `D-01` | Geen verplichte introductietekst |
| `W-02` | Werkplaats na terugkeer; objecten en voortgangsdetails onveranderd | Tik een object om verder te gaan | Geen tekst nodig |
| `W-E1` | Pandaschuif/lade open, panda piept even naar buiten | Korte animatie; lade sluit vanzelf naar `W-01` | Geen tekst |
| `W-E2` | Close-up vleesetende plant en vlieg | Tik 1: vlieg verschijnt; tik 2: vlieg vliegt naar binnen en klep klapt dicht; tik 3: terug naar `W-01` | Geen tekst |
| `W-E3` | Close-up hartkunstwerk | Hart pulseert en afgebeelde mensen dansen; daarna terug naar `W-01` | Geen tekst |

De drie easter eggs zijn optioneel, herhaalbaar en wijzigen geen hoofdvoortgang. Hun exacte klikzones en timing blijven onderdeel van de afzonderlijke compositie-/assetcontrole.

### M — Uitdaging 1: match-3

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst / feedback |
|---|---|---|---|
| `M-01` | Computer zoomt in; toont niveau, doel, voortgangsteller en letterstrook. Geen zettenaantal of timer: alle drie levels zijn onbeperkt. | Start bord → `M-02` | Intro per niveau staat in `CHALLENGES.md` |
| `M-02` | Actief bord, teller, zetten, `?` en terugknop | Selecteer tegel → `M-03` | Geen extra tekst |
| `M-03` | Eerste tegel geselecteerd | Tik aangrenzende tegel → controle zet; tik dezelfde/andere tegel → selectie bijwerken | Geen extra tekst |
| `M-04` | Ongeldige niet-matchende verwisseling keert terug | Bord keert terug naar `M-02`; geen zet afgetrokken. De feedback volgt de actieve levelbeschrijving. In Level 1 keren de vlakken zonder foutmeldingstekst terug. | Geen algemene fouttekst; gebruik alleen tekst die voor het actieve level expliciet is vastgelegd. |
| `M-05` | Geldige match wordt verwijderd; effen kleurvlakken vallen, het bord vult van boven aan en eventuele cascades spelen stap voor stap af. Doelobjecten reageren volgens het actieve level. | Na animatie → `M-02`, tenzij doel bereikt | Gebruik uitsluitend de level-specifieke feedback uit `CHALLENGES.md` |
| `M-06` | Leveldoel bereikt; korte succesreactie | Toon letter → `M-07` | Succesfeedback van het betreffende level |
| `M-07` | Letterbeloning en voortgangsstrook | Niveau 1 → niveau 2; niveau 2 → niveau 3; niveau 3 → `M-08` | “Circuit één draait weer! Goed gedaan.” / “De tandwielen zijn vrij! De fabriek komt weer op gang.” / “De uitgang is open! De fabriek is weer helemaal wakker.” |
| `M-08` | B, A en L samen op metalen plaatje | Terug naar werkplaats; uitdaging 1 gemarkeerd als voltooid | “B… A… L. Dat is je eerste geheime woord. Onthoud het goed — je hebt het later nodig!” |
| `M-09` | Hintpaneel open boven actief bord | Hints volgens gedeeld hintprotocol; puzzelstatus blijft bestaan | De drie inhoudelijke hints per level staan in `CHALLENGES.md` |
| `M-10` | Speler kiest level opnieuw proberen na zelfgekozen reset/geen game-over | Reset alleen het huidige level na expliciete actie; verdiende eerdere letters blijven | Bevestiging indien reset de huidige bordstand wist: “Dit level opnieuw starten? De huidige bordstand gaat verloren, maar je eerdere letters blijven bewaard.” |

**Belangrijke technische randvoorwaarde:** de vaste startborden, toegestane zetvolgorde, cascade-/vulregels en oplosbaarheid zijn nog niet gevalideerd. `M-01` tot `M-10` zijn schermtoestanden, geen bewijs dat de drie bordmatrices al bouwklaar zijn.

### L — Uitdaging 2: groene locker

#### Deel A — cijfercode 042

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst / feedback |
|---|---|---|---|
| `L-01` | Locker close-up met drie cijferwieltjes en OPEN | OPEN → juiste/foute controle | “Een geheim deurtje… Welke drie cijfers openen het slot?” |
| `L-02` | Cijfercode fout | Korte visuele terugslag; invoer blijft aanpasbaar; terug naar `L-01` | “Klik… nee, die code werkt niet. Probeer het opnieuw.” |
| `L-03` | Cijfercode 042 juist; klein deurtje opent | Onthul personages → `L-04` | “Het deurtje gaat open. Drie raadselmeesters bewaren hier een sleutel…” |
| `L-04` | Charlie, RidderUs en Schildje met hun uitspraken | Tik personage als antwoord → `L-05` | “Precies één van hen spreekt de waarheid. Wie heeft de sleutel?” |
| `L-05` | Antwoord geselecteerd, bevestiging | BEVESTIG → juist/fout; WIJZIGEN → `L-04` | Knoppen: **DIT IS MIJN ANTWOORD**, **WIJZIGEN** |
| `L-06` | Verkeerd antwoord | Antwoord blijft veranderbaar | “Niet helemaal. Test de drie mogelijkheden en tel telkens hoeveel uitspraken waar zijn.” |
| `L-07` | Charlie gekozen | Charlie haalt messing sleutel tevoorschijn | “Goed geredeneerd! Je hebt me door. Hier is de sleutel — maar je moet nog ontdekken welk kistje de moeite waard is.” |
| `L-08` | Drie kistjes met uitspraken; sleutel zichtbaar als verdiend | Kies kistje → `L-09` | “Precies één uitspraak is waar. Welk kistje moet je openen?” |
| `L-09` | Kistje geselecteerd, nog niet geopend | BEVESTIG → juiste/foute controle; WIJZIGEN → `L-08` | Knoppen: **OPEN DIT KISTJE**, **WIJZIGEN** |
| `L-10` | Verkeerd kistje | Kist blijft dicht; sleutel blijft beschikbaar | “Dat lijkt niet te kloppen. Controleer bij elk kistje welke uitspraken waar zijn.” |
| `L-11` | Rood kistje gaat open | Onthul ster-met-oog → `L-12` | “Gevonden! Jij hebt de code gekraakt, de sleutel verdiend én het juiste kistje opgespoord!” |
| `L-12` | Ster met oog duidelijk zichtbaar als beloning | Markeer uitdaging 2 voltooid; ster verschijnt automatisch bij deur | “Een ster met een oog… Dat moet een belangrijke aanwijzing zijn. Je hoeft dit symbool niet te onthouden: het wordt bij de grote deur bewaard.” |
| `L-13` | Hintpaneel bij code, logica of kistjes | Elke puzzelstap heeft een eigen hintniveau en hervatstatus | Exacte hints hieronder |

**Definitieve uitspraken van het sleutelraadsel**
- Charlie: “RidderUs heeft de sleutel.”
- RidderUs: “Ik heb de sleutel niet.”
- Schildje: “Charlie heeft de sleutel niet.”

**Hints — code 042**
1. “Begin met de aanwijzing 738. Welke cijfers kun je meteen uitsluiten?”
2. “De code bevat een 0, maar die staat niet op de derde plaats.”
3. “Combineer de aanwijzingen en controleer of elke cijferpositie aan alle regels voldoet.”

**Toon oplossing — na bevestiging:** toon **042** en markeer de drie cijferwieltjes in de juiste volgorde. Wannes stelt de wieltjes zelf in en drukt zelf op **OPEN**.

**Hints — wie heeft de sleutel?**
1. “Wat gebeurt er als Charlie de sleutel heeft?”
2. “Controleer hoeveel uitspraken waar zijn als RidderUs de sleutel heeft.”
3. “Maak voor Charlie, RidderUs en Schildje elk een rijtje en tel de ware uitspraken.”

**Toon oplossing — na bevestiging:** toon de volledige waar/onwaar-tabel en markeer de enige geldige rij. De uitleg eindigt met **“Charlie heeft de sleutel.”** Wannes kiest Charlie zelf.

**Hints — welk kistje?**
1. “Test eerst wat er gebeurt als de hoofdprijs in het rode kistje zit.”
2. “Tel bij elke mogelijke kistlocatie hoeveel uitspraken waar zijn.”
3. “Vergelijk de drie mogelijkheden en zoek de enige waarbij precies één uitspraak waar is.”

**Toon oplossing — na bevestiging:** toon per mogelijke kistlocatie welke uitspraken waar zijn. Markeer het rode kistje en leg uit dat alleen die keuze precies één ware uitspraak oplevert. Wannes kiest en bevestigt het kistje zelf.

De gewone hint 3 blijft een laatste denkstap en verklapt het antwoord niet. De exacte oplossing wordt uitsluitend getoond na **TOON OPLOSSING** → “Wil je de oplossing zien?” → **BEKIJKEN**.

### C — Uitdaging 3: de bekers

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst / feedback |
|---|---|---|---|
| `C-01` | Tafel, drie bekers, rode bal; introductie van huidige ronde | Beginpositie tonen → `C-02` | Introductietekst van de ronde in `CHALLENGES.md` |
| `C-02` | Bal is duidelijk onder startbeker; alle bekers stil | Automatisch start wissels → `C-03` | Geen tekst tijdens wissels |
| `C-03` | Actieve wisselanimatie; tikken geblokkeerd | Na 2/3/4 wissels → `C-04` | Geen tekst tijdens beweging |
| `C-04` | Bekers stil; keuze beschikbaar | Tik beker → `C-05` | Geen aftelklok |
| `C-05` | Gekozen beker gaat omhoog | Juist → `C-06`; fout → `C-07` | Geen dubbelzinnige feedback |
| `C-06` | Bal gevonden; ronde succes | Ronde 1/2 → volgende ronde `C-01`; ronde 3 → `C-08` | “Juist! Je hebt de truc door.” / “Netjes! Je laat je niet zomaar afleiden.” / “Ongelooflijk! Je hebt alle drie de rondes gekraakt!” |
| `C-07` | Lege beker, foutfeedback | Beginpositie opnieuw tonen; huidige ronde opnieuw proberen | Per ronde de fouttekst uit `CHALLENGES.md` |
| `C-08` | Rode lichtbol en kleurstaal | Markeer uitdaging 3 voltooid | “Aha! De truc is ontmaskerd. Onthoud deze kleur: signaalrood. Je hebt nu alle drie de aanwijzingen verzameld!” |
| `C-09` | Hintpaneel | Per ronde eigen hintniveau; terugkeer hervat niveau | De drie ronde-specifieke hints staan in `CHALLENGES.md` |

**Hintpaneel en rondehints:** de drie hints per ronde zijn gewone hints 1–3. Hint 3 is extra hulp, maar wijst de juiste beker nog niet aan. Na hint 3 verschijnt de aparte knop **TOON OPLOSSING**; dit is geen vierde hint. Na bevestiging toont de oplossing de beginpositie opnieuw en speelt de wissels vertraagd en één voor één af. Daarna krijgt de juiste beker een subtiele pulserende contour en verschijnt **“Tik op de beker met de contour.”** Wannes kiest de beker zelf.

### D — Uitdaging 4: de deur en het slot

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst / feedback |
|---|---|---|---|
| `D-01` | Gesloten deur; slot met drie onderdelen | Eerste bezoek → `D-02`; later bezoek → `D-03` | Eerste keer: “Een geheim slot! Het lijkt erop dat het drie aanwijzingen nodig heeft. Die moeten ergens in dit laboratorium verstopt zitten.” |
| `D-02` | Introductie gezien; symbool leeg indien uitdaging 2 niet af is | Vul woord/kleur zelf in of keer terug | Geen extra uitleg nodig |
| `D-03` | Slotstatus: ster-met-oog automatisch aanwezig indien uitdaging 2 af; woordveld en kleurstalen | Invoer bewaren; OPEN DE DEUR → `D-04` | Label: **GEHEIM WOORD**; knop: **OPEN DE DEUR** |
| `D-04` | Nog minstens één uitdaging onvoltooid | Meld ontbrekende aanwijzing; geen voortgang verloren | “Er ontbreekt nog een aanwijzing. Ga gerust verder op ontdekkingstocht — je kunt altijd terugkomen.” |
| `D-05` | Alle uitdagingen voltooid, woord en/of kleur onjuist | Foutfeedback; behoud invoer/keuze | “Klik… brom… nog niet juist. Kijk nog eens naar wat je ontdekt hebt.” |
| `D-06` | Combinatie juist | Vergrendeling klikt; deur opent naar donkere feestzaal | “Dat is hem! Jij hebt alle aanwijzingen gevonden én het geheim ontrafeld!” |
| `D-07` | Deur opent; warme lichtkier, geen extra interactie | Automatische overgang naar `F-01` | “Wacht eens… Ik denk dat ze daarbinnen op jou staan te wachten.” |
| `D-08` | Hintpaneel | Eigen hintstatus voor slot | Hint 1: “Je hebt al dingen ontdekt in het laboratorium. Kijk wat je al weet.” Hint 2: “Het symbool wordt voor je bewaard. Het woord moet je zelf typen en de kleur moet je zelf kiezen.” Hint 3: “Het woord komt uit de speelgoedfabriek, het symbool uit het kistjesraadsel en de kleur uit de bekers.” |

### F — Finale

| Toestand-ID | Wat zichtbaar is | Actie / overgang | Tekst / feedback |
|---|---|---|---|
| `F-01` | Deur staat open; feestzaal donker en stil; figuren zijn als silhouetten/figuren in de scène aanwezig zonder tekst | Wannes ziet de grote rode feestknop; tik → `F-02` | Geen extra dialoog |
| `F-02` | Rode feestknop wordt ingedrukt | Automatische visuele reactie start → `F-03` | Geen tekst vereist |
| `F-03` | Lichtjes springen aan, confetti barst los, figuren vieren feest | Animatie speelt vanzelf af → `F-04` | Geen audio of tweede tik |
| `F-04` | Feestbeeld wordt rustiger; eerste boodschap verschijnt | Automatisch na korte leesbare pauze → `F-05` | **“Proficiat Wannes!”** |
| `F-05` | Zelfde rustige feestbeeld; tweede boodschap verschijnt onder/na de eerste | Finale blijft zichtbaar; spel eindigt zonder extra actie | **“Dat verdient een cadeau.”** |
| `F-06` | Finale hersteld na herladen | Herstel naar rustig eindbeeld met beide teksten; feestanimatie niet opnieuw afspelen | Beide eindteksten zichtbaar |

**Finaleregels:** de tik op de rode feestknop is de laatste interactieve handeling. De twee boodschappen verschijnen vanzelf en in deze volgorde. Geen extra knop, kaarttruc, opdracht, raadsel, geluids- of trilfeedback.

## 3. Gedeelde overlay- en feedbacktoestanden

- `H-01`: hintpaneel dicht; alleen de `?`-knop zichtbaar.
- `H-02`: hintpaneel open op huidig niveau; drie stippen; knop **VOLGENDE HINT**.
- `H-03`: na hint 3 is de knop **TOON OPLOSSING**.
- `H-04`: bevestiging “Wil je de oplossing zien?” met **BEKIJKEN** en **TERUG**. TERUG brengt terug naar dezelfde hint 3.
- `H-05`: oplossingstekst met exact volgende handeling; het relevante element pulseert subtiel totdat Wannes die handeling uitvoert.
- `H-06`: na geslaagde puzzelactie sluit het paneel vanzelf. Bij opnieuw openen verschijnt het laatst bekeken niveau.
- `N-01`: korte neutrale foutfeedback bij ongeldige actie; verdwijnt zonder een andere puzzelstatus te resetten.
- `N-02`: korte succesfeedback; beloning wordt opgeslagen vóór een volgende overgang.

## 4. Persistentieregels per deeltoestand

| Gegevens | Moet bewaard blijven |
|---|---|
| Titel/werkplaats | Of er geldige voortgang is; herstart alleen na bevestiging |
| Match-3 | Niveau, exact bord, geselecteerde tegel indien relevant, zetten, doelen, cascade/herstelstatus, reeds verdiende letters |
| Locker | Cijferwieltjes, code correct/foutstatus waar nodig, sleutelraadselstatus/keuze, verdiende sleutel, kistkeuze, kist geopend, ster-met-oog verdiend |
| Bekers | Ronde, beginpositie, permutatie na iedere afgeronde wissel, aantal wissels, keuze en resultaat; animatie na herladen veilig hervatten vanuit een stabiele logische toestand |
| Deur | Eerste bezoek al gezien, automatisch symbool, woordveld, kleurkeuze, geopende status |
| Hints | Per afzonderlijk puzzelscherm huidig niveau en of oplossing is bevestigd/getoond; paneel zelf is na verlaten van het scherm dicht |
| Finale | Knop nog niet ingedrukt / feestanimatie bezig / eindbeeld bereikt; herladen tijdens finale gaat naar een veilige, niet-interactieve eindtoestand zonder feest opnieuw te starten |
| Easter eggs | Optioneel of ze onthouden worden; nooit invloed op hoofdvoortgang |

## 5. Open verificaties — niet stilzwijgend als afgerond markeren

1. **Match-3:** de exacte drie startmatrices moeten worden vastgelegd en met een solver/testprocedure op oplosbaarheid worden gecontroleerd volgens de gekozen spelregels. De huidige doelen zijn nog geen bewijs van oplosbaarheid; er zijn geen zetlimieten.
2. **Bekers:** concrete wisselroutes en snelheden moeten op iPhone-portret worden getest; elke animatie moet dezelfde permutatie opleveren als de interne logica.
3. **Visuele compositie:** exacte klikzones en plaatsing van de vier hoofdobjecten en drie easter eggs moeten nog worden vastgelegd.
4. **Assets:** werkelijke bestandstypen en definitieve locaties moeten worden gecontroleerd voordat de schermen aan specifieke afbeeldingen worden gekoppeld.
5. **Hintconsistentie:** de algemene regel is drie hints en daarna een aparte oplossing. De hintladder in dit document is aangepast om hint 3 niet als volledige oplossing te formuleren; controleer deze scheiding ook in alle puzzelbeschrijvingen in `CHALLENGES.md`.

## 6. Bouwstop

Dit document is een gedetailleerde specificatie, geen opdracht om te programmeren. Geen gamecode bouwen totdat de open verificaties zijn afgerond, de documenten onderling consistent zijn en het volledige dossier expliciet is goedgekeurd.
