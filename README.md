# primal-salt

based on primer

we want to download various git repos that contain our formulas pillars and states and then we want to push them to a live salt-master but we may also want to push individual folders in the cloned repos to different spots on the salt master

```python3
python primalsalt/cli.py                                                                                  rosscdh@s
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  project
  remote
```

### current example
```
version: 1
primal:
  name: My example project
  salt:
    formulas:
      - https://github.com/thiccbois/registry-formula
      - https://github.com/thiccbois/scantrust-formula
    pillars:
      - https://github.com/thiccbois/secret-pillars
    profiles:
      - https://github.com/thiccbois/secret-profiles
  remote:
    host: 13.209.47.229
    paths:
      - from: registry-formula
        to: /etc/salt/formulas

      - from: secret-pillars
        to: /etc/salt/pillars

      - from: secret-profiles/_runners
        to: /etc/salt/runners

      - from: secret-profiles/[state|orchestrate]
        to: /etc/salt/state
```

## TODO

- make globbing on fab sync work
- webhooks?
- tests