import re
from typing import Tuple

EVENT_RULES = [
    (re.compile(r"restructur(ing|e)" , re.I), ("liquidity", -0.6)),
    (re.compile(r"downgrad", re.I), ("credit_rating", -0.5)),
    (re.compile(r"default", re.I), ("credit_event", -0.9)),
    (re.compile(r"bankrupt", re.I), ("credit_event", -1.0)),
    (re.compile(r"invest(ment)? plan|capex", re.I), ("growth", 0.2)),
    (re.compile(r"guidance (cut|lower)", re.I), ("earnings", -0.4)),
    (re.compile(r"beats? (estimates|expectations)", re.I), ("earnings", 0.3)),
    (re.compile(r"lawsuit|probe|investigation", re.I), ("governance", -0.3)),
]

def map_event(title: str) -> Tuple[str, float]:
    for pat, (etype, impact) in EVENT_RULES:
        if pat.search(title or ""):
            return etype, impact
    return ("general", 0.0)