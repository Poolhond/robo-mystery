# De mysterieuze fabriek — Techniekregels

**Versie:** 0.7  
**Status:** Conceptuele technische randvoorwaarden; nog geen definitieve implementatiespecificatie. Deze regels moeten vóór de master-prompt worden aangevuld met een concrete schermenlijst, statusmodel en acceptatietests.

## 1. Platform
- Statische website, gratis gehost op GitHub Pages.
- Mobile-first, bedoeld voor iPhone Safari (portret). Moet ook werken op iPad en desktop.
- Geen account, geen server, geen externe diensten.

## 2. Bestandsstructuur
```
index.html          # structuur van het spel
style.css           # alle stijlen en kleurvariabelen
game.js             # spelogica
content.js          # alle teksten, raadsels, antwoorden, personalisatie
assets/
  characters/       # aap, schildpad, panda, octopus en signaalvogel
  rooms/            # laboratorium en andere scènes
  ui/               # knoppen, kaders, iconen, texturen
  audio/            # (optioneel) geluiden
```
- Alle verwijzingen zijn **relatief** (`assets/...`), nooit beginnend met `/`, zodat het op GitHub Pages werkt.
- Geen frameworks, geen bibliotheken, geen externe lettertypen of scripts.

## 3. Eén bron voor teksten en personalisatie
Alle spelertekst staat in `content.js`: raadsels, antwoorden, hints, feedback, de naam "Wannes", de slottekst en de eventuele echte opdracht aan het einde. Dit maakt aanpassen voor iedereen mogelijk zonder de spelcode te raken.

## 4. Spelstatus en opslag
- Eén `state`-object bewaart huidig scherm en locatie in het laboratorium, voltooide uitdagingen, voortgang binnen elke deelpuzzel, verzamelde aanwijzingen, ingevoerde slotgegevens en gebruikte hints.
- Elke uitdaging moet hervatbaar zijn op de exacte deelstap. Voorbeelden: huidig match-3-bord en resterende zetten; laatst voltooide bekerronde; geopende deur, verdiende sleutel en huidige stap in de raadselketting.
- Sla lokaal op na elke betekenisvolle actie, zoals een geldige match, een voltooide ronde, een correct opgeloste deelpuzzel, een verdiende aanwijzing of wijziging aan het slot.
- Bij terugkeer naar een uitdaging wordt de opgeslagen toestand hersteld; begin geen uitdaging opnieuw tenzij Wannes daar bewust voor kiest.
- Herladen, een slapende telefoon of het sluiten en later opnieuw openen van Safari mag geen voortgang kosten. Voorzie ook een veilige standaardtoestand als er nog geen opslag bestaat.
- Een verborgen resetknop (bijvoorbeeld lang indrukken op de titel) om opnieuw te beginnen.
- Als `localStorage` niet werkt, blijft het spel speelbaar zonder opslaan.

## 5. Scènes, locaties en schermtoestanden

Maak onderscheid tussen **locaties in de wereld** en **schermtoestanden**. De grote deur is een interactief object binnen het laboratorium, niet automatisch een aparte locatie. Het slot is een toestand/paneel dat verschijnt wanneer Wannes de deur onderzoekt; het mag niet als een tweede, losstaande deur worden behandeld.

De definitieve scèneslijst wordt uitgewerkt in het dossier. Navigatieregel: elke uitdaging zoomt in op het bestaande voorwerp in de vaste werkplaatsillustratie. Gebruik overal dezelfde terugknop en dezelfde overgangslogica; terugkeren brengt Wannes naar exact dezelfde werkplaatsweergave. De volledige spelstatus van de verlaten uitdaging blijft behouden, inclusief de exacte puzzelstap en visuele toestand. Hervatten mag geen puzzel resetten of opnieuw laten beginnen.

De voorlopige structuur bestaat uit:
- start en proloog;
- één verkenbaar laboratorium met drie uitdaginglocaties en de grote deur;
- de afzonderlijke speeltoestanden van uitdaging 1, 2 en 3;
- het slotpaneel bij de grote deur, inclusief onvolledige voortgang, foutfeedback en correcte combinatie;
- de deuropening en feestfinale.

Iedere locatie/toestand krijgt een stabiele ID, een beschrijving van wat zichtbaar is, de beschikbare acties, de mogelijke overgangen en de voortgang die bij verlaten moet worden opgeslagen. De precieze lijst wordt vastgesteld vóór de master-prompt en de bouw.

## 6. iPhone- en mobielregels
- Alleen tikbediening; geen hover, geen rechtsklik, geen dubbelklik.
- Raakvlakken minimaal 44×44 px.
- Gebruik `100svh` en `env(safe-area-inset-*)` zodat niets achter de notch of onderbalk verdwijnt.
- Viewport: `width=device-width, initial-scale=1, viewport-fit=cover`.
- Geen horizontale scroll. Tekst blijft leesbaar op een smal scherm (minimaal 16 px voor lopende tekst).
- Geluid start pas na de eerste tik van Wannes. Het spel moet ook zonder geluid volledig te spelen zijn.
- Voorkom dubbeltik-zoom en per ongeluk selecteren van tekst (`touch-action`, `user-select`).

## 7. Prestaties en robuustheid
- Afbeeldingen maximaal ongeveer 1200 px breed, bij voorkeur PNG of WebP; één keer vooraf laden.
- Als een afbeelding niet laadt, blijft de interactie bruikbaar (kleurvlak of tekstlabel als noodoplossing).
- Animaties mogen sterk zijn, maar respecteren `prefers-reduced-motion`.
- Elke uitdaging werkt zonder dat een andere uitdaging nodig is om te laden.
- Geen eindeloze lussen of timers die doorlopen op een ander scherm.

## 8. Stijl in code
- Kleuren als CSS-variabelen op één plek in `style.css`. Het palet is vastgelegd in `docs/ART-DIRECTION.md`.
- Interface in de zeefdrukstijl uit `docs/ART-DIRECTION.md` (kaders, knoppen, paneel).
- Essentiële tekst is echte HTML-tekst, nooit alleen in een afbeelding.

## 9. Testen (na de bouw)
Op een echte iPhone controleren:
- Het spel laadt snel en zonder fouten.
- Start tot en met slotscène is uit te spelen, ook met fouten en hints.
- Herladen halverwege verliest niets.
- Alle knoppen zijn met één duim te bereiken en te raken.
- Tekst is overal leesbaar en past op het scherm.
- Geluid, als aanwezig, werkt pas na tikken en kan uit.

## 10. Wat niet gebouwd wordt
- Geen accounts, ranglijsten of netwerkfuncties.
- Geen advertenties of tracking.
- Geen aankopen of externe links, behalve eventueel een duidelijke link terug naar het begin.


## 11. Status van deze specificatie

Dit document beschrijft de beoogde richting en is nog geen volledige bouwopdracht. Voor de master-prompt moeten minimaal de exacte scherm-/toestandslijst, de vorm van de opgeslagen spelstatus, herstelgedrag bij ontbrekende of beschadigde opslag, de regels voor oplosbare match-3-borden en concrete acceptatietests worden vastgelegd. Een ontwikkelaar mag deze open punten niet oplossen door ongemerkt nieuwe spelregels te verzinnen.
