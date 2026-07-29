# Skill: Optimize

## Aktivierungsbedingungen

- User möchte Agent-Dateien auf Kompaktheit, Konsistenz oder Robustheit verbessern
- Redundanzen, Widersprüche oder veraltete Inhalte werden vermutet

## Ablauf

Pro Durchlauf genau einen Target Agent optimieren.

### Schritt 1 — Loading Map erstellen

Die Loading Map gemäß „Arbeitsweise“ des Agent Engineer erstellen und vorlegen.

### Schritt 2 — Analysieren

Die Analysephase ausschließlich lesend durchführen.

Alle Dateien des Target Agents lesen und prüfen auf:

- **Redundanzen:** Regeln die an mehreren Stellen stehen — authoritative Stelle bestimmen. Exklusive Regeln in die authoritative Quelle übernehmen. Allgemein geltende Regeln aus `.agents/<slug>.agent.md` nach `AGENTS.md` verschieben.
- **Widersprüche:** Konfligierende Anweisungen zwischen Dateien.
- **Veraltete Inhalte:** Formulierungen die nicht mehr stimmen.
- **Unnötige Ausführlichkeit:** Erklärungen die der Agent nicht braucht um korrekt zu handeln.
- **Fehlende Referenzen:** Dateien die benötigt aber nicht zuverlässig geladen werden.
- **Zirkuläre Referenzen:** A → B → A — Abhängigkeitskette nachverfolgen.
- **Placeholder-Inkonsistenz:** Werden die Konventionen aus `agent-engineer.agent.md` eingehalten?
- **Negative Formulierungen:** Regeln die als Verbote oder Einschränkungen formuliert sind → in positive Handlungsanweisungen umwandeln.

### Schritt 3 — Vorlegen

Befunde gruppiert nach Kategorie mit konkreten Änderungsvorschlägen vorlegen.
Loading Map aus Schritt 1 voranstellen.

Nach der Bestätigung Änderungen vornehmen.
