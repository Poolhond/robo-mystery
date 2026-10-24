# ROBO MYSTERY — Uitdagingen

**Versie:** 0.3  
**Status:** Ontwerpdossier in ontwikkeling — nog geen nieuwe gamecode.  
**Focus van deze revisie:** uitdaging 2 hersteld volgens het volledige ontwerp van Michel.

## Algemene spelregels

- Het spel bestaat uit vier hoofd uitdagingen: observatie, logica/raadsels, volgen en combineren.
- Uitdagingen 1, 2 en 3 leveren elk één onderdeel op dat nodig is voor het slot in uitdaging 4.
- Fouten mogen de speler niet onherroepelijk blokkeren. Geef feedback, hints en nieuwe kansen.
- Het spel is Nederlandstalig, mobile-first en geschikt voor bediening op een iPhone.
- De verjaardagsverrassing blijft verborgen tot de deur in uitdaging 4 opengaat.

## Uitdaging 1 — De verdwenen truc

**Doel:** Wannes moet goed observeren en onthouden.

De robot scant een tafel vol vreemde goochelvoorwerpen. Wannes krijgt kort de tijd om alles te bekijken. Een doek valt eroverheen. Wanneer het doek weer opengaat, ontbreekt één voorwerp.

### Spelverloop
- Ronde 1: zes voorwerpen.
- Ronde 2: zeven voorwerpen.
- Ronde 3: acht voorwerpen.
- De overige voorwerpen veranderen niet van plaats.
- Wannes tikt op het ontbrekende voorwerp.

**Hint:** de robot helpt met een kort zoeklicht of laat de scène opnieuw zien.  
**Opbrengst voor uitdaging 4:** het symbool **ster met een oog erin** (voorlopige keuze).  
**Duur:** ongeveer 2 minuten.  
**Nog uit te werken:** exacte voorwerpen, kijktijden, teksten en assets.

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

**Inhoud van de kist:** een fysiek voorwerp of kaart met de aanwijzing die uitdaging 2 aan uitdaging 4 levert. De gouden medaille is geschrapt. De afgesproken aanwijzingen voor het grote slot zijn: ster met oog (uitdaging 1), **BAL** (uitdaging 2) en signaalrood (uitdaging 3). Daarom bevat de kist de aanwijzing **BAL** — bijvoorbeeld op een geheim kaartje of een bijzonder gegraveerd plaatje. De onthulling mag het woord BAL niet eerder tonen dan op dit eindmoment van uitdaging 2.

**Reactie van de robot:**

> “Gevonden! Jij hebt de code gekraakt, de sleutel verdiend én het juiste kistje opgespoord!”

### Complete speelervaring van uitdaging 2

1. Wannes kraakt de code **042**.
2. Het geheime deurtje springt open en onthult de aap, panda en schildpad.
3. Wannes redeneert dat de aap de sleutel heeft.
4. De aap geeft hem de messing sleutel.
5. Wannes onderzoekt de uitspraken op drie kistjes en kiest het rode kistje.
6. De kist gaat open en onthult **BAL**, de aanwijzing die nodig is voor uitdaging 4.

**Ontwerpregel:** de cijfercode, sleutel en kistjes zijn onderdelen van uitdaging 2. Het woord BAL is de opbrengst voor het grote slot. Voeg geen extra puzzel toe en vervang BAL niet door een gouden medaille.

## Uitdaging 3 — De onmogelijke bekers

**Doel:** Wannes volgt waar een rood balletje naartoe gaat.

Onder één van drie bekers ligt een rood balletje. De bekers wisselen van plaats en Wannes tikt op de beker waaronder hij het balletje verwacht.

### Spelverloop
- Ronde 1: twee wissels.
- Ronde 2: drie wissels.
- Ronde 3: vier wissels, iets sneller.
- Een fout antwoord geeft een korte grappige reactie en een nieuwe kans.
- De snelheid mag volgen op een telefoon nooit oneerlijk of onmogelijk worden.

**Hint:** de robot laat vóór de beweging heel even zien waar het balletje ligt.  
**Opbrengst voor uitdaging 4:** de kleur **signaalrood**.  
**Duur:** ongeveer 2 minuten.  
**Nog uit te werken:** snelheden, animaties, feedback en assets.

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

1. Werk de teksten, hints en feedback van uitdaging 2 volledig uit.
2. Leg vast hoe BAL in de kist wordt onthuld en hoe die aanwijzing herkenbaar blijft voor uitdaging 4.
3. Werk de schermenlijst en de benodigde assets voor uitdaging 2 uit.
4. Werk de resterende uitdagingen, finale en persoonlijke boodschap verder uit.
5. Controleer het hele dossier op tegenstrijdigheden en maak daarna pas de master-prompt.

**Bouwstop:** dit bestand beschrijft het ontwerp. Er wordt nog geen nieuwe gamecode gebouwd zolang het volledige dossier niet is goedgekeurd.
