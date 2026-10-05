# quorum-test

Mock service for testing a two-person release quorum on the `prod` branch.

- `main`: development.
- `prod`: what is deployed. Changes only through an approved PR from `main`.

See `app.py` for the mock handler.
