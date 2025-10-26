# NCIF and the Conditional Impossibility of Decimal Digit Extraction for π

Supplementary materials for the preprint "NCIF and the Conditional Impossibility of Decimal Digit Extraction for π" by Patrick Böhme.

---

## Overview

This repository accompanies the paper investigating the computational complexity of extracting arbitrary decimal digits from π using the Non-Carry Information Field (NCIF) framework. We establish conditional impossibility results for base-10 O(log n) digit extraction, showing that current O(n log³ n) methods via Chudnovsky are near-optimal under standard assumptions.

**Key Contributions:**
- Formal NCIF theory with oracle equivalence theorem
- Exhaustive PSLQ search for base-10 BBP formulas (1000+ combinations, 0 hits)
- Carry-isolation analysis establishing κ(n) ∈ Ω(log² n)
- p-adic barrier analysis demonstrating why base-10 is fundamentally harder than base-16

---

## Files

| File | Description |
|------|-------------|
| `NCIF_Theory.md` | Complete paper in Markdown format |
| `NCIF_Theory.tex` | LaTeX source (compressed version) |
| `bibliography.bib` | BibTeX bibliography with key references |
| `phase2_investigation1_lis_pslq.py` | Implementation of PSLQ-based BBP-10 search (§3.1) |
| `requirements.txt` | Python dependencies for reproducibility |

---

## Reproducibility

### Prerequisites

```bash
python>=3.8
pip install -r requirements.txt
```

**Core dependencies:**
- `numpy` ≥ 1.24.0
- `mpmath` ≥ 1.3.0 (high-precision arithmetic)
- `sympy` ≥ 1.12 (symbolic computation)

### Running Experiments

**PSLQ Search (Section 3.1):**

```bash
python phase2_investigation1_lis_pslq.py
```

This systematically searches for base-10 BBP formulas across 1000+ parameter combinations, documenting hits/non-hits as reported in Section 3.1 of the paper.

**Expected output:**
- Search log with 0 hits across tested parameter space
- Documented non-hits supporting Theorem 1 (no BBP-10 formula exists in tested structures)
- Carry-isolation preview estimates

### Parameters (from Section 7.2)

```
Pattern types: 4 (Single, Double, Triple, Quadruple Rational)
Parameter space: a ∈ {1,2,4}, b ∈ {1,3,4,5,6,7,8,9,11,13,14,15,16}
Precision: 200 decimal digits
Terms: 10,000 per series
Threshold: relative error < 10^(-30)
```

---

## Key Results

**Theorem 1 (Oracle Equivalence):** True NCIF existence for π is constructively equivalent to random-access oracle existence.

**Theorem 2 (Carry-Isolation Window):** κ(n) ∈ Ω(log² n) for extracting the n-th decimal digit of π.

**Theorem 3 (p-adic Barrier):** Dual p-adic barriers (p ∈ {2,5}) establish κ(n) ∈ Ω(log² n) from combined effects.

**Meta-Theorem (Conditional Impossibility):** Base-10 O(log n) extraction for π is impossible under standard assumptions unless either:
- A base-10 BBP formula exists (currently unknown)
- True NCIF exists (oracle-equivalent)

---

## Paper Structure

**Section 2:** NCIF theory, axioms, oracle equivalence, information lower bounds  
**Section 3:** Phase II investigations (PSLQ search, carry-isolation, p-adic barriers)  
**Section 4:** Conditional impossibility meta-theorem with proof sketch  
**Section 5:** Discussion of limitations, breakthroughs, and connections to hex-BBP  
**Section 6:** Practical implications for Chudnovsky algorithm  
**Section 8:** Future work directions  

---

## References

Key papers:
- Bailey-Borwein-Plouffe (1997): O(log n) extraction in base 16
- Chudnovsky (1989): Current O(n log³ n) optimum
- Kolmogorov (1965): Information-theoretic lower bounds

Full bibliography in `bibliography.bib`.

---

## License

This work is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material for any purpose

Under the following terms:
- **Attribution** — You must give appropriate credit to the author

See [LICENSE](LICENSE) for details.

---

## Contact

**Correspondence:** Patrick Böhme

**Paper Subject Classification:**
- 68Q15 (Computational complexity)
- 11Y60 (Number-theoretic computations)
- 11J04 (Irrationality and transcendence)

---

## Citation

If you use this work, please cite:

```bibtex
@unpublished{bohme2024ncif,
  title={NCIF and the Conditional Impossibility of Decimal Digit Extraction for $\pi$},
  author={B{\"o}hme, Patrick},
  year={2025},
  note={Preprint},
  repository={https://github.com/...}
}
```

---

**Status:** Publish-Ready (v3.0)  
**Date:** 2025  
**Keywords:** Computational complexity, Information theory, Oracle complexity, Digital extraction, NCIF, p-adic analysis
