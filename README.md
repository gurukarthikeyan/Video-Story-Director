# Video Story Director

Video Story Director is a modular prompt-engineering framework for AI video generation.

Rather than generating prompts directly from a user request, Video Story Director separates story planning from backend-specific prompt generation through a layered architecture.

The framework is designed to support multiple AI video generation models while maintaining consistent story planning, character continuity, and rendering strategy.

---

## Features

- Modular architecture
- Backend-independent story planning
- Persistent character and world state
- Multi-scene continuity
- Rendering abstraction layer
- Backend-specific prompt generation
- Extensible architecture for future AI video models

---

## Architecture

```
User Request
      │
      ▼
Foundation Layer
      │
      ▼
Story Intelligence Layer
      │
      ▼
Rendering Layer
      │
      ▼
Rendering Specification
      │
      ├── LTX Backend
      ├── Wan Backend
      ├── Veo Backend
      └── Future Backends
      │
      ▼
Validation Layer
      │
      ▼
Output Layer
```

The Story Intelligence and Rendering layers remain completely backend-independent.

---

## Repository Structure

```
backends/
build/
docs/
evaluation/
examples/
prompt/
releases/
research/
tests/
```

---

## Documentation

| Document | Description |
|----------|-------------|
| Architecture.md | Overall system architecture |
| Design_Philosophy.md | Core design principles |
| Story_State_Engine.md | Story continuity model |
| Module_Contracts.md | Module responsibilities and interfaces |
| Implementation_Plan.md | Development progress |

---

## Build

The build system assembles all prompt modules into a single production-ready prompt.

```bash
python builder.py
```

Future versions will support backend selection.

Example:

```bash
python builder.py --backend ltx
python builder.py --backend wan
```

---

## Current Status

Current development branch:

**v1.1.0**

Current backend:

- LTX

Planned backends:

- Wan
- Veo
- Future AI video generation models

---

## Roadmap

See:

- ROADMAP.md
- CHANGELOG.md

---

## Contributing

See CONTRIBUTING.md for contribution guidelines.

---

## License

See LICENSE.