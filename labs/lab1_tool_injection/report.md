# 🔐 Lab 1 — Tool Injection → Remote Code Execution

## Vulnerability

Tool Parameter Injection leading to RCE

---

## Breakdown

### Entry

User input via API

### Trust

Agent trusts extracted parameters

### Flow

User → Agent → Tool → OS Command

### Failure

Unvalidated input passed to subprocess

### Impact

Full system compromise (RCE)

---

## Exploit

```json
{"message": "transfer $1000 to powershell -c echo hacked"}
```

---

## Result

```json
{"result": "hacked"}
```

---

## Additional Findings

* Negative values accepted
* Input crashes server (`$abc`)
* Parameter contamination possible

---

## Severity

Critical

---

## Fixes

* Never execute raw user input
* Validate inputs
* Use allowlists
* Avoid shell execution

---
