---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Code to reproduce the behavior and error message:

```python
from ds2000 import DS2000
from ds2000.func import simple_plot

ip = "192.168.30.186"
with DS2000(ip) as o:
    print("info:", o.info())
    o.waveform.start(1)
    simple_plot(o, recorded=False)
```

```
The complete traceback here.
```

**Expected behavior**
A clear and concise description of what you expected to happen.

**Desktop (please complete the following information):**
 - OS: [e.g. Windows 10 x64 Workstation Build: 19042.746 (20H2)]
 - Version of ds2000 [e.g. 0.1.0]

**Additional context**
Add any other context about the problem here.
