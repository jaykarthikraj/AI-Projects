# Harness

You are the developer. The architect designs one door at a time. You build that door, then we read it together.

Start with the comic: [docs/Start-here.pdf](docs/Start-here.pdf).

Then, in this order:

1. [docs/HLD.md](docs/HLD.md) is the one-page picture of the whole system.
2. [docs/BLUEPRINT.md](docs/BLUEPRINT.md) is the order of work and the test effort for each door.
3. [docs/LLD-stage-1.md](docs/LLD-stage-1.md) is the only low-level design that is open.
4. [docs/TEST-stage-1.md](docs/TEST-stage-1.md) is how you know door 1 is done.

Your first code change is the body of `PretendProvider.complete` in `src/harness/provider.py`. The four tests should pass. Do not start door 2 in the same change.
