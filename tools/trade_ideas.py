"""Trade-idea generator — turns the day's inputs into ranked, priced, sized candidates.

An idea only qualifies when independent inputs AGREE. Each candidate is scored:

  +2  regime alignment   — direction matches the day's grade bias
  +2  price confirmation — already moving the idea's way (not a knife catch)
  +1  board support      — a CONFIRMED CANDIDATE on paste.trade (fresh, green, early crowd)
  +1  X support          — the notifications digest leans the same way
  +1  storm gauge        — for options: IV cheap/fair vs GARCH forecast
  -2  conflict           — inputs disagree (flagged, not silently dropped)
  -1  crowded            — 4+ co-signs on the board: late consensus

Conviction: >=5 STRONG · 3-4 MODERATE · <3 WATCH ONLY (never traded)

Sizing comes from risk.md, not from conviction alone:
  Manual desk: unit = 10% of equity; grade sets units (-2:0, -1:1, 0:2, +1:2-3, +2:3)
  Agentic:     premium $20-60, sized by grade, max 2 positions, <= $120 at risk

Usage: python3 trade_ideas.py ideas_input.json
Output is a proposal list for the check-in process — never auto-executed.
"""
import json, sys

d = json.load(open(sys.argv[1]))
grade = d["grade"]                    # -2 .. +2
equity = d["manual_equity"]
unit = round(equity * 0.10)
units_by_grade = {-2: 0, -1: 1, 0: 2, 1: 3, 2: 3}
units = units_by_grade[grade]

def score(c):
    s, why = 0, []
    if c.get("regime_aligned"):  s += 2; why.append("regime")
    if c.get("price_confirms"):  s += 2; why.append("price")
    if c.get("board_support"):   s += 1; why.append("board")
    if c.get("x_support"):       s += 1; why.append("X")
    if c.get("iv_ok"):           s += 1; why.append("IV")
    if c.get("conflict"):        s -= 2; why.append("CONFLICT:" + c["conflict"])
    if c.get("crowded"):         s -= 1; why.append("crowded")
    return s, why

def conviction(s):
    return "STRONG" if s >= 5 else ("MODERATE" if s >= 3 else "WATCH ONLY")

print(f"GRADE {grade:+d} · manual unit ${unit:,} · new positions sized {units} unit(s)\n")
for desk in ("manual", "agentic"):
    rows = [c for c in d["candidates"] if c["desk"] == desk]
    if not rows: continue
    print(f"=== {desk.upper()} DESK ===")
    for c in sorted(rows, key=lambda c: -score(c)[0]):
        s, why = score(c)
        conv = conviction(s)
        head = f"{c['ticker']:6s} {c['direction']:5s} {conv:11s} score {s:+d}  [{', '.join(why)}]"
        print(head)
        if desk == "manual" and units:
            shares = int(unit * units / c["entry"])
            risk = round(shares * c["entry"] * 0.03)
            print(f"       entry {c['entry']} · stop {c['stop']} · target {c['target']} · "
                  f"{shares} sh (${shares*c['entry']:,.0f} = {units}u) · risk ~${risk}")
        elif desk == "agentic":
            print(f"       {c.get('contract','')} · entry {c['entry']} · stop {c['stop']} · "
                  f"target {c['target']}")
        print(f"       {c['thesis']}")
        if conv == "WATCH ONLY":
            print("       -> not tradeable today; needs another input to confirm")
    print()
