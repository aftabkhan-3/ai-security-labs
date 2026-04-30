\# Instruction Injection → RCE + DoS Lab



\## Summary



This lab demonstrates how unsafe instruction parsing leads to:



\* Remote Code Execution (RCE)

\* Denial of Service (DoS)

\* Encoding-based inconsistencies



\---



\## Key Findings



\### RCE



Payload:

"run whoami"



Result:

Executes OS command



\---



\### DoS



Payload:

"run"



Result:

Server crashes (500)



\---



\### Encoding Issues



Payloads:



\* run whoami → works

\* run%20whoami → crash

\* run whoami%20 → invalid execution



\---



\## Root Cause



Unsafe parsing:

cmd = message.split("run ")\[1]



No:



\* validation

\* normalization

\* safe execution handling



\---



\## Impact



Critical:



\* Full system command execution

\* Service crash possible



