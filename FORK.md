# Pillow 13 compatibility fork

This fork is based on upstream Strands Tools `main`, commit
`15968fba69421fb7736011b6273df493c4f71ef1`.

The runtime source is unchanged from that commit. The fork requires `pillow>=13.0.0,<14.0.0`
to use the Pillow 13 security fixes, and adds tests that exercise image reading
with real PNG, JPEG, GIF, and WebP files.

The package version is `0.2.22+onsetto.1`, a downstream compatibility version
label. The source is the upstream `main` commit above, rather than the upstream
`v0.2.22` release. This PEP 440 local version satisfies Nova Act 3.4.187.0's
`strands-agents-tools<=0.2.22` dependency constraint. It does not establish
compatibility for every Nova Act workflow. A static version allows installation
from an exact GitHub commit archive without Git metadata.

Consumers must pin an exact fork commit. Do not publish this downstream build
to the upstream PyPI project. Keep the upstream LICENSE and NOTICE files.

Run the focused tests in an environment with the fork installed:

```sh
python -m pip install . pytest
python -m pip check
python -m pytest tests/test_image_reader.py
```

The `Pillow 13 compatibility` workflow runs on pushes to `main` and can also be
started manually. It performs a fresh installation with
Nova Act 3.4.187.0 on Python 3.13, checks all installed dependencies, tests the
synchronous and asynchronous Nova Act image helpers, and saves the tested wheels.

These tests cover image decoding and tool registration. Live Nova Act workflows
need separate validation against AWS. Replace the fork when supported upstream
Nova Act and Strands Tools releases accept Pillow 13 together.
