# Design Brief — Organization Management Service

## High level diagram (ASCII)

```
[Client] --> [Uvicorn + FastAPI app] --> [MongoDB]
                   |
                   +--> [JWT auth] (stateless)
```

## Architecture summary
- **FastAPI** for the HTTP API: async, fast developer experience, automatic OpenAPI docs.
- **Motor** (AsyncIO MongoDB driver) for non-blocking DB access.
- **Passlib (pbkdf2_sha256 primary)** for password hashing to avoid bcrypt 72-byte truncation problems.
- **JWT** tokens for stateless admin authentication.
- **Docker + Docker Compose** to bundle app + mongo for reproducible runs.

## Design choices & tradeoffs

### Why pbkdf2_sha256 as default instead of bcrypt?
- bcrypt silently truncates passwords at 72 bytes.  
- pbkdf2_sha256 avoids truncation and is secure with proper iterations.
- **Tradeoff**: bcrypt is widely used, but pbkdf2 is equally secure and more flexible.

### Motor (async) vs pymongo (sync)
- Motor integrates well with async FastAPI → better concurrency.
- **Tradeoff**: async code is slightly more complex to reason about.

### JWT for auth
- **Pros**: stateless, scalable, no session storage.
- **Cons**: token revocation requires additional infra.

### Docker & Deployment
- Compose makes local development consistent.
- Production would require:
  - Proper secrets management
  - Multiple replicas of API service
  - Managed MongoDB

## Scalability & improvements
- Horizontal scaling possible due to stateless API.
- Upgrade suggestions:
  - Use Redis caching
  - Add background job runner (Celery, RQ)
  - Add rate limiting & API gateway
  - Implement metrics and observability stack

## Alternative architecture options
- Split org service + authentication into separate microservices.
- Use PostgreSQL instead of MongoDB for relational needs.
- Integrate a full OAuth2 provider (Auth0, AWS Cognito).