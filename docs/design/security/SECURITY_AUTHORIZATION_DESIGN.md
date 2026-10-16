# RRMS Security & Authorization Design

**Document ID:** RRMS-SEC-001  
**Version:** 1.0  
**Status:** Draft for Technical Design Validation  
**Project Phase:** Stage 3 — Technical Design  
**Current Step:** Stage 3.6 — Security & Authorization Design  
**Related Architecture:** RRMS-ARCH-001  
**Related API Design:** RRMS-API-001  
**Related UI Architecture:** RRMS-UI-001  
**Related Requirements:** RRMS-SRS-001 v1.0  

---

## 1. Purpose

This document defines the security and authorization architecture for the Retail Resale Management System.

It specifies:

- authentication strategy;
- session handling;
- password protection;
- role-based authorization;
- API security;
- CSRF and CORS policy;
- brute-force and rate-limit protection;
- protected file access;
- secret management;
- logging and audit expectations;
- future storefront security boundaries;
- data protection expectations.

This document does not implement security code.

---

## 2. Security Principles

RRMS follows these principles:

1. Authentication proves identity.
2. Backend authorization decides whether an authenticated identity may perform an action.
3. Frontend visibility is never treated as a security control.
4. Least privilege is preferred.
5. Sensitive credentials and secrets are never stored in plaintext.
6. Historical financial and operational records are protected from destructive modification.
7. Security-sensitive events remain attributable to a user where possible.
8. Customer-facing functionality is separated from internal administration.
9. Database and file storage are never exposed directly to browsers.
10. Secure defaults are preferred over convenience.

---

## 3. Authentication Strategy

### 3.1 Internal Application

For the internal Administrator/Employee web application, RRMS should use **server-managed authenticated sessions with secure cookies**.

The browser receives a session identifier in a cookie configured with:

- `HttpOnly`
- `Secure` in production
- appropriate `SameSite` policy
- limited lifetime

The cookie must not contain plaintext credentials or sensitive business data.

### 3.2 Why Session-Based Authentication

Session-based authentication is preferred for Version 1 because RRMS is primarily a first-party web application.

Benefits include:

- simple server-side revocation;
- no access token stored in browser local storage;
- straightforward logout;
- strong fit for a modular monolith;
- easier control of account deactivation;
- reduced token-management complexity.

The architecture may later support token-based authentication for external/mobile clients if needed.

---

## 4. Password Security

Passwords must never be stored directly.

Use:

**Argon2id**

for password hashing.

Implementation requirements:

- use a reputable maintained password-hashing library;
- generate unique salts automatically;
- use secure parameters appropriate to the deployment environment;
- allow hashing parameters to be upgraded over time;
- never log passwords;
- never return password hashes through the API.

Password reset/recovery functionality must use time-limited, single-use mechanisms if introduced.

---

## 5. Login Security

Login behavior should:

- return a generic authentication error for invalid credentials;
- not reveal whether a particular account exists;
- reject inactive accounts;
- regenerate session identity after successful authentication;
- record relevant security events;
- apply brute-force protection.

Repeated failed login attempts should trigger rate limiting or temporary throttling.

The initial system does not require permanent account lockout because attackers could abuse it to deny legitimate users access.

---

## 6. Session Security

Sessions should support:

- creation after successful login;
- server-side expiry;
- logout invalidation;
- revocation when required;
- invalidation or revalidation after account deactivation;
- secure session identifier generation.

Recommended session behavior:

- idle timeout;
- absolute maximum lifetime;
- rotation after login;
- optional rotation after sensitive security changes.

Session IDs must never be exposed in URLs.

---

## 7. CSRF Protection

Because RRMS uses cookie-based authenticated sessions, state-changing requests require CSRF protection.

Protected methods include:

- POST
- PUT
- PATCH
- DELETE

The implementation should use a framework-supported CSRF defense or equivalent validated anti-CSRF token approach.

`SameSite` cookies improve protection but should not be treated as the only CSRF defense for sensitive state-changing requests.

---

## 8. CORS Policy

Production should prefer same-origin deployment where practical.

If frontend and backend use separate origins, CORS must use an explicit allowlist.

Do not use permissive authenticated CORS such as allowing arbitrary origins.

CORS rules should restrict:

- allowed origins;
- allowed methods;
- allowed headers;
- credential usage.

Development origins may be separately configured.

---

## 9. Role Model

Initial internal roles:

- `ADMINISTRATOR`
- `EMPLOYEE`

Roles are enforced on the backend.

The system may later evolve toward more granular permissions without changing the fundamental authorization boundary.

---

## 10. Authorization Matrix

### Administrator

Administrators may access:

- dashboard;
- products;
- purchasing;
- inventory;
- customers;
- reservations;
- sales;
- payments;
- customer balances;
- deliveries;
- returns;
- exchanges;
- expenses;
- reports;
- product cost/profit;
- business revenue;
- user management;
- authorized overrides.

### Employee

Employees may access operational functionality required for the business.

Under the validated SRS baseline, employees may view:

- product cost;
- product profit;
- business revenue;
- customer outstanding balances;

unless future configuration explicitly restricts those areas.

Employees must not automatically receive user-administration authority.

---

## 11. Permission Enforcement

Every protected backend operation must verify:

1. authenticated identity;
2. active account;
3. role/permission;
4. operation-specific business rules.

Examples:

- user creation → Administrator;
- employee deactivation → Administrator;
- below-cost override → authorized role;
- normal sale creation → authorized internal user;
- payment recording → authorized internal user;
- general reporting → authorized internal user;
- customer-facing storefront browse → public where intended.

The API must return `403 Forbidden` when an authenticated user lacks permission.

---

## 12. Object-Level Authorization

Role checks alone are not sufficient.

The backend must also validate access to the specific target resource when applicable.

Examples:

- payment must correspond to the selected Sale/Customer;
- ReturnItem must belong to the referenced Sale;
- replacement inventory must actually be available;
- reservation operation must target an existing valid reservation.

Client-supplied IDs are never trusted without server-side relationship validation.

---

## 13. Future Storefront Boundary

The future storefront is public-facing and must be separated from internal administrative routes.

Public access may include:

- browse products;
- view product details;
- submit guest order request.

Public users must never receive:

- acquisition costs;
- internal profit data;
- customer balances;
- administrative notes;
- internal user information;
- internal reporting data;
- unrestricted inventory-management operations.

Guest order requests must pass backend validation before any temporary hold is created.

---

## 14. API Security

All production API traffic uses HTTPS.

The API should enforce:

- authenticated session checks on protected routes;
- CSRF validation for state-changing authenticated requests;
- request size limits;
- input validation;
- file upload validation;
- rate limits on abuse-prone routes;
- consistent authorization checks;
- safe error responses.

The API must not return:

- stack traces;
- SQL errors;
- credentials;
- secrets;
- password hashes;
- internal file-system paths.

---

## 15. Rate Limiting

Rate limiting should prioritize abuse-sensitive routes.

High-priority examples:

- login;
- password recovery if introduced;
- public storefront search;
- guest order requests;
- file upload endpoints.

Authenticated internal business operations may use more generous limits.

Rate-limit responses should use a consistent API error and appropriate HTTP status such as `429 Too Many Requests`.

---

## 16. Input Validation

All client input is untrusted.

The backend validates:

- expected type;
- required fields;
- size/length limits;
- allowed enum/status values;
- numeric boundaries;
- dates;
- identifiers;
- file type/size;
- business relationships.

Parameterized database access or ORM parameter binding must be used.

Raw untrusted input must never be concatenated into SQL.

---

## 17. File Upload Security

Uploads may include:

- product images;
- purchase receipts;
- future supporting documents.

Security requirements:

- validate MIME/content type;
- enforce file-size limits;
- generate server-controlled file names/keys;
- prevent path traversal;
- do not trust original file names;
- restrict dangerous file types;
- prevent executable uploads from being served as application code;
- store metadata separately;
- authorize access to non-public files.

Purchase receipts should normally be treated as private business documents.

---

## 18. Product Image Access

Product images intended for the customer storefront may be public or served through public-safe storage.

Private/internal media remains protected.

The file architecture should distinguish:

- public product media;
- internal business documents.

Do not make an entire storage bucket/container public merely because some product images are public.

---

## 19. Secret Management

Secrets must never be committed to Git.

Examples:

- database password;
- session secret;
- encryption keys;
- external API credentials;
- production storage credentials.

Secrets must come from:

- environment variables;
- deployment secret manager;
- equivalent secure configuration mechanism.

Provide `.env.example` files only with placeholder values.

Actual `.env` files containing secrets must be ignored by Git.

---

## 20. Database Security

Application database access should use a dedicated database account.

The application account should have only the privileges required by RRMS.

Avoid:

- using PostgreSQL superuser credentials in the application;
- exposing PostgreSQL publicly without need;
- sharing production credentials across environments.

Production, staging, and development should use separate credentials and data stores.

---

## 21. Sensitive Data Handling

RRMS contains customer and business information such as:

- names;
- phone numbers;
- WhatsApp numbers;
- addresses;
- customer balances;
- sales history;
- profitability information.

Access should be limited to authenticated authorized business users.

Sensitive information should not appear unnecessarily in:

- logs;
- URLs;
- analytics tools;
- client-side storage.

---

## 22. Logging and Security Events

Structured logs should capture security-relevant events such as:

- successful login;
- failed login;
- logout;
- inactive-account login attempt;
- authorization denial;
- user creation/deactivation;
- below-cost override;
- unusual file-upload rejection;
- repeated rate-limit events.

Logs should include:

- timestamp;
- request ID;
- user ID where available;
- event type;
- result.

Do not log:

- passwords;
- password hashes;
- session IDs;
- secret tokens;
- sensitive request payloads unless deliberately redacted.

---

## 23. Auditability

Important business actions should remain attributable to an authenticated User through fields already defined in the data model, including:

- `recorded_by_user_id`
- `created_by_user_id`
- `processed_by_user_id`

A generalized audit-log table may later be added for:

- field-level changes;
- before/after values;
- security-sensitive administrative actions.

The Version 1 architecture must not depend on such a table being present unless introduced during implementation planning.

---

## 24. Error Handling

Security failures should reveal as little information as necessary.

Examples:

### Authentication failure

Use a generic message such as:

`Invalid login credentials.`

### Authorization failure

Return:

`403 Forbidden`

without exposing hidden internal permission rules.

### Missing resource

Use `404 Not Found`.

Where revealing resource existence would itself be sensitive, authorization and not-found handling may intentionally be normalized.

---

## 25. Security Headers

Production web responses should use appropriate security headers.

Expected protections include:

- `Content-Security-Policy`
- `X-Content-Type-Options: nosniff`
- frame-embedding protection through CSP `frame-ancestors`
- `Referrer-Policy`
- HTTPS enforcement / HSTS where deployment supports it.

Exact values will be finalized against the implemented frontend and hosting environment.

---

## 26. Browser Storage

Do not store authentication secrets in:

- `localStorage`
- `sessionStorage`

when using the selected server-session architecture.

Browser storage may be used for non-sensitive UI preferences if needed.

Sensitive business data should not be persistently cached in browser storage without a clear requirement.

---

## 27. Data Backup and Recovery

Production database and private business-file storage require backups.

Security expectations:

- automated backups;
- restricted backup access;
- periodic restore testing;
- separation from the primary runtime;
- retention policy appropriate to the business.

Backup files are sensitive and require protection equivalent to production data.

---

## 28. Dependency Security

Implementation should:

- use actively maintained dependencies;
- keep dependencies updated;
- avoid unnecessary packages;
- review known vulnerabilities;
- pin or lock dependency versions appropriately.

Security-critical libraries such as password hashing and authentication components should be well-established rather than custom implementations.

---

## 29. Environment Separation

Use distinct configurations for:

- development;
- testing;
- production.

Production secrets and production customer data must not be copied casually into development environments.

Development environments should use test/sample data.

---

## 30. Security Testing Expectations

Implementation testing should later include:

- authentication tests;
- role authorization tests;
- object-level access tests;
- CSRF tests;
- input validation tests;
- SQL injection resistance;
- file upload tests;
- rate-limit tests;
- session expiry/logout tests;
- inactive-user tests;
- protected-route tests.

These become part of the testing phase rather than Stage 3.6 implementation.

---

## 31. Deliberate Deferrals

Stage 3.6 does not yet define:

- exact session library;
- exact backend framework security middleware;
- exact Argon2 parameters;
- exact timeout values;
- exact rate-limit numbers;
- MFA;
- OAuth/social login;
- password-reset UI;
- field-level encryption;
- WAF configuration;
- production hosting firewall rules.

These decisions should be made when the implementation/deployment environment is selected.

---

## 32. Diagram Files

- `SECURITY_ARCHITECTURE.drawio`
- `SECURITY_ARCHITECTURE.png`

---

## 33. Stage 3.6 Completion Gate

Stage 3.6 is complete when:

1. `SECURITY_AUTHORIZATION_DESIGN.md` is committed;
2. `SECURITY_ARCHITECTURE.drawio` is committed;
3. `SECURITY_ARCHITECTURE.png` is committed;
4. internal authentication uses server-managed secure sessions;
5. password hashing uses Argon2id;
6. backend RBAC responsibilities are defined;
7. CSRF/CORS behavior is documented;
8. API, file, secret, and logging security boundaries are documented;
9. future storefront access remains separated from internal administration;
10. no unresolved security-architecture issue blocks implementation planning.
