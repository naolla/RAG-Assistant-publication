# GPU Requirements

This project does not require a GPU by default.

- No CUDA/TensorRT-specific packages are pinned in `requirements.lock`.
- If you want GPU acceleration for embeddings or LLMs:
  - Install a CUDA-enabled PyTorch per official instructions
  - Ensure your local CUDA drivers match the installed binary
  - Optionally select GPU-enabled models/providers

Example (PyTorch CUDA): see https://pytorch.org/get-started/locally/
