# Skill: Optimize

## Aktivierungsbedingungen

- User möchte Agent-Dateien auf Kompaktheit, Konsistenz oder Robustheit verbessern
- Redundanzen, Widersprüche oder veraltete Inhalte werden vermutet

## Ablauf

Immer nur einen Target Agent pro Durchlauf optimieren.

### Schritt 1 — Loading Map erstellen

Welche Dateien werden wann geladen? Tabelle erstellen und vorlegen:

| Datei                               | Ladebedingung              | Referenziert von         |
| ----------------------------------- | -------------------------- | ------------------------ |
| `AGENTS.md`                         | immer — zuerst             | — (globale Basis)        |
| `.agents/<slug>.agent.md`           | immer                      | — (Einstiegspunkt)       |
| `.agents/engineer/skills/INDEX.md`   | immer (nur Engineer)       | `agent-engineer.agent.md` |
| `.agents/engineer/skills/<skill>.md` | on-demand: Skill aktiviert | `INDEX.md`               |

### Schritt 2 — Analysieren (nur lesen, nicht ändern)

Alle Dateien des Target Agents lesen und prüfen auf:

- **Redundanzen:** Regeln die an mehreren Stellen stehen — authoritative Stelle bestimmen. Prüfen ob eine Regel in `.agents/<slug>.agent.md` eigentlich allgemein gilt → dann nach `AGENTS.md` verschieben.
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

Auf Bestätigung warten bevor etwas geändert wird.
