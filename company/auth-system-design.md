Absolutely. Under the hood, this is exactly what JWT libraries do. Let's implement it manually in Node.js so you understand the process.
Step 1: Create a JWT
const crypto = require("crypto");

const secret = "my_super_secret_key";

const header = {
  alg: "HS256",
  typ: "JWT"
};

const payload = {
  userId: 101,
  role: "USER"
};

function base64UrlEncode(obj) {
  return Buffer.from(JSON.stringify(obj))
    .toString("base64url");
}

const encodedHeader = base64UrlEncode(header);
const encodedPayload = base64UrlEncode(payload);

// Create signature
const data = `${encodedHeader}.${encodedPayload}`;

const signature = crypto
  .createHmac("sha256", secret)
  .update(data)
  .digest("base64url");

const jwt = `${data}.${signature}`;

console.log(jwt);
JWT looks like this:
xxxxx.yyyyy.zzzzz
where:
Header.Payload.Signature
Step 2: Verify the JWT
Suppose the client sends back:
const receivedToken = jwt;
Split it into 3 parts.
const [header, payload, receivedSignature] =
    receivedToken.split(".");
Step 3: Recalculate Signature
const data = `${header}.${payload}`;

const generatedSignature = crypto
    .createHmac("sha256", secret)
    .update(data)
    .digest("base64url");
Step 4: Compare
if (generatedSignature === receivedSignature) {
    console.log("✅ Valid Token");
} else {
    console.log("❌ Token Tampered");
}
This is exactly what JWT libraries do internally.
What Happens if Someone Changes the Payload?
Original payload
{
   "userId":101,
   "role":"USER"
}
Attacker changes it to
{
   "userId":101,
   "role":"ADMIN"
}
Now the token becomes
Header.NewPayload.OldSignature
When the server verifies:
const generatedSignature = HMAC(
    Header.NewPayload,
    secret
);

generatedSignature !== oldSignature
Result
401 Unauthorized
because
Header.NewPayload

↓

New Hash

↓

abc123456
Received Signature
xyz987654
Comparison
abc123456 == xyz987654

False
The token is rejected.
How jsonwebtoken Does It
In a real application, you normally use the jsonwebtoken library instead of implementing it manually.
Create Token
const jwt = require("jsonwebtoken");

const token = jwt.sign(
    {
        userId: 101,
        role: "USER"
    },
    "my_secret",
    {
        expiresIn: "15m"
    }
);
Verify Token
try {
    const decoded = jwt.verify(token, "my_secret");

    console.log("Valid Token");
    console.log(decoded);

} catch (err) {

    console.log("Token Tampered");
}
Internally, jwt.verify() performs the same steps:
Received Token
      |
Split Header.Payload.Signature
      |
Generate New Signature using Secret Key
      |
Compare Signatures
      |
Validate exp
      |
Validate algorithm
      |
Return Payload
Interview Tip
If an interviewer asks "How do you ensure the token isn't tampered with?", you can even sketch this on a whiteboard:
Client
   |
   | Header.Payload.Signature
   |
Server
   |
Split Token
   |
Header + Payload
   |
HMAC(secret)
   |
Generated Signature
   |
Compare
   |
Match?
 ├── Yes → Continue
 └── No  → 401 Unauthorized
That demonstrates you understand the mechanism behind JWT verification, not just how to call a library.
Your answer was on the right track, but the interviewer was likely asking how the server actually verifies that the token hasn't been modified. They wanted the mechanism, not just "it's signed."
A strong answer is:
"When a JWT is received, the server does not trust it directly. It splits the token into three parts: Header, Payload, and Signature. Using the Header and Payload, the server recalculates the signature with its secret key (or public key if using asymmetric signing). It then compares the newly generated signature with the signature included in the token. If they match, the token has not been tampered with. If they don't match, the request is rejected with a 401 Unauthorized."
Explain it visually
JWT

Header.Payload.Signature
Suppose the payload is:
{
  "userId": 101,
  "role": "USER"
}
An attacker changes it to:
{
  "userId": 101,
  "role": "ADMIN"
}
Now the token becomes:
New Header + New Payload + Old Signature
On the server:
Received Token
       |
Extract Header + Payload
       |
Generate Signature using Secret Key
       |
Compare Generated Signature
        ==
Received Signature ?
       |
Yes --> Valid
No  --> Token Tampered (401)
Because the attacker doesn't know the secret/private key, they cannot generate a matching signature.
If the interviewer pushes further
They may ask:
"What if the attacker steals your secret key?"
A good answer:
Store signing keys securely (e.g., a secret manager or key vault).
Rotate keys periodically.
Use asymmetric signing (e.g., RS256), where only the authentication server has the private key and other services verify with the public key.
Limit key access to authorized services only.
A senior-level answer (30 seconds)
"The server ensures a JWT hasn't been tampered with by verifying its digital signature. It recalculates the signature from the received header and payload using its signing key and compares it with the signature embedded in the token. Since only the server possesses the signing key, any modification to the header or payload causes the signatures to differ, and the token is rejected. We also validate the expiration, issuer, audience, and expected signing algorithm before accepting the token."
This is usually the level of detail interviewers are looking for when they ask, "How do you ensure the token is not tampered with?"

This is a classic follow-up question. The interviewer is checking whether you understand JWT integrity.
Interview Answer
"A JWT is digitally signed by the server. When the token is created, the server signs it using a secret key (HS256) or a private key (RS256). Whenever a client sends the token back, the server verifies the signature using the same secret key or the corresponding public key. If anyone modifies even a single character in the payload, the signature validation fails, and the server rejects the token with a 401 Unauthorized response."
Example
When the server creates a token:
Header
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload
{
  "userId": 101,
  "role": "USER",
  "exp": 1750000000
}
The server signs it:
JWT = Header.Payload.Signature
Suppose an attacker changes:
{
  "userId": 101,
  "role": "ADMIN"
}
The payload changes, but the attacker cannot generate a valid new signature because they don't know the server's secret key (or don't have the private key if using asymmetric signing). During verification:
Received JWT
      ↓
Recalculate Signature
      ↓
Compare with JWT Signature
      ↓
Match?
   Yes → Accept
   No  → Reject (401)
Additional points that impress interviewers
Also mention that you verify:
✅ JWT signature
✅ Expiration (exp)
✅ Issuer (iss)
✅ Audience (aud)
✅ Algorithm (don't allow alg: none or unexpected algorithms)
If they ask "Can someone decode the JWT?"
A good answer is:
"Yes. A JWT is Base64URL encoded, not encrypted, so anyone can decode and read its payload. However, they cannot modify it without invalidating the digital signature. That's why we never put sensitive information like passwords or credit card details inside a JWT."
This concise explanation demonstrates that you understand the difference between encoding, signing, and encryption, which is often what the interviewer is testing.



If the interviewer says "Design a simple authentication system with Login and Register APIs", don't overcomplicate it with OAuth or SSO. Explain it step by step.
APIs
POST /register
POST /login
GET /profile (Protected)
POST /logout
Register Flow
Client
   |
POST /register
(email, password)
   |
   v
Auth Service
   |
Validate input
   |
Check if email already exists
   |
Hash password (bcrypt/Argon2)
   |
Store user in database
   |
Return 201 Created
Register API
Request
{
  "name": "Sunil",
  "email": "sunil@gmail.com",
  "password": "Password@123"
}
Database
User
-----------------------
id
name
email
password_hash
created_at
Store:
password_hash

NOT

password
Login Flow
Client
   |
POST /login
(email,password)
   |
   v
Auth Service
   |
Find user by email
   |
Compare password with hash
   |
Generate JWT
   |
Return token
Login Request
{
  "email": "sunil@gmail.com",
  "password": "Password@123"
}
Response
{
  "accessToken": "eyJhbGc..."
}
Protected API
GET /profile
Client sends
Authorization

Bearer JWT_TOKEN
Backend
Read JWT

↓

Verify Signature

↓

Extract UserId

↓

Return profile
JWT Payload
{
    "userId":101,
    "email":"sunil@gmail.com",
    "exp":1710000000
}
Password Storage
Never
123456
Store
bcrypt("123456")

↓

$2b$10$ajshdhasd...
Login Verification
Entered Password

↓

bcrypt.compare()

↓

Hash Matches?

↓

Generate JWT
Database
Users

----------------------------
Id
Name
Email
PasswordHash
CreatedAt
UpdatedAt
Security
Mention these points:
Hash passwords using bcrypt or Argon2
Use HTTPS for all requests
Validate all user inputs
Return generic errors like "Invalid email or password"
Add JWT expiration (e.g., 15–30 minutes)
Apply rate limiting to prevent brute-force attacks
Never expose password hashes in API responses
End-to-End Flow
Register
=========
Client
   |
POST /register
   |
Validate
   |
Hash Password
   |
Save User
   |
Success

----------------------------

Login
======
Client
   |
POST /login
   |
Find User
   |
Compare Password
   |
Generate JWT
   |
Return JWT

----------------------------

Protected API
==============
Client
   |
Authorization: Bearer JWT
   |
Backend verifies JWT
   |
Return Data
Interview Answer (1–2 minutes)
"I would expose two main APIs: /register and /login. During registration, I'd validate the input, check if the email already exists, hash the password using bcrypt or Argon2, and store only the password hash in the database. During login, I'd fetch the user by email, compare the entered password with the stored hash, and if it's valid, generate a JWT containing the user ID and role with an expiration time. The client sends this JWT in the Authorization: Bearer <token> header for protected APIs. On every protected request, the server verifies the JWT signature and expiry before authorizing access. To secure the system, I'd use HTTPS, validate inputs, rate-limit login attempts, and never store or return plain-text passwords."


For a Senior Software Engineer/System Design interview, when someone says "Build an authentication system", they're looking for your design approach, security considerations, scalability, and trade-offs—not just a login API.
Here's a structured answer you can use.
Step 1: Clarify Requirements
Start by asking questions:
Functional Requirements
Do users register with email/password or use social login (Google, Microsoft)?
Do we need Single Sign-On (SSO)?
Should we support Multi-Factor Authentication (MFA)?
Do users stay logged in across devices?
Do we need role-based access (Admin/User)?
Should we support password reset?
Non-Functional Requirements
High availability (99.9%+)
Low login latency (<200 ms)
Secure against common attacks
Horizontally scalable
Audit logging
Compliance (GDPR/HIPAA if needed)
Step 2: High-Level Architecture
                +------------------+
                | React / Angular  |
                +--------+---------+
                         |
                    HTTPS Request
                         |
                 +-------v--------+
                 | API Gateway    |
                 +-------+--------+
                         |
                +--------v---------+
                | Auth Service     |
                +--------+---------+
                         |
        +----------------+----------------+
        |                                 |
+-------v--------+               +---------v---------+
| User Database  |               | Redis (Sessions) |
+----------------+               +------------------+
                         |
                 +-------v--------+
                 | JWT Generator  |
                 +-------+--------+
                         |
              HttpOnly Secure Cookie
Step 3: Registration Flow
User enters email/password
        ↓
Validate input
        ↓
Check if user already exists
        ↓
Hash password using bcrypt/Argon2
        ↓
Store hashed password
        ↓
Send verification email
        ↓
User verifies account
        ↓
Account activated
Never store plain-text passwords.
Step 4: Login Flow
User submits credentials
        ↓
Validate request
        ↓
Fetch user from DB
        ↓
Compare password hash
        ↓
Generate JWT Access Token
        ↓
Generate Refresh Token
        ↓
Store Refresh Token securely
        ↓
Return HttpOnly Secure Cookie
Step 5: JWT Structure
{
  "sub": "12345",
  "email": "user@example.com",
  "role": "Admin",
  "exp": 1750000000
}
Don't include sensitive information like passwords or personal data.
Step 6: Token Strategy
Token
Lifetime
Purpose
Access Token
15 minutes
Authenticate API requests
Refresh Token
30 days
Issue new access tokens
Use refresh token rotation so each refresh invalidates the previous refresh token.
Step 7: Secure Token Storage
Don't use:
localStorage
sessionStorage
Use:
HttpOnly cookie
Secure cookie
SameSite=Lax or SameSite=Strict
This reduces the risk of token theft via JavaScript.
Step 8: Security Measures
Protect against:
SQL Injection → Parameterized queries
XSS → Input validation, output encoding, Content Security Policy
CSRF → SameSite cookies and CSRF tokens where appropriate
Brute Force → Rate limiting and account lockout
Password attacks → Strong password policy and bcrypt/Argon2 hashing
Token theft → HTTPS everywhere, short-lived access tokens, refresh token rotation
Sensitive accounts → MFA
Step 9: Password Reset
Forgot Password
      ↓
Generate one-time token
      ↓
Store hashed reset token with expiry
      ↓
Email reset link
      ↓
User clicks link
      ↓
Validate token
      ↓
Set new password
      ↓
Invalidate reset token
Step 10: Scaling
For millions of users:
Multiple Auth Service instances behind a load balancer
Shared user database
Redis for refresh token/session storage
Read replicas for heavy read traffic
Caching for user profile lookups
Auto-scaling based on CPU or request rate
Step 11: Monitoring
Track:
Failed login attempts
Successful logins
Password resets
Token refresh activity
Suspicious login locations
Audit logs for authentication events
Step 12: API Design
POST /register

POST /login

POST /refresh

POST /logout

POST /forgot-password

POST /reset-password

GET /me
How to Answer in an Interview (3-minute version)
"I would start by clarifying requirements such as email/password versus social login, MFA, session duration, and role-based access. For the architecture, I'd place an Auth Service behind an API Gateway, with a user database for credentials and Redis for refresh tokens or sessions. During registration, passwords are hashed using bcrypt or Argon2 and users verify their email before activation. During login, credentials are validated, an access token with a short expiry and a refresh token are generated, and they're returned using HttpOnly, Secure, SameSite cookies. I avoid storing tokens in localStorage. To secure the system, I'd enforce HTTPS, validate JWT signatures and claims, implement refresh token rotation, rate limiting, CSRF protection, XSS prevention, MFA for sensitive accounts, and audit logging. For scalability, the Auth Service remains stateless, scales horizontally behind a load balancer, and uses Redis for shared session or refresh token storage."
This structure demonstrates both system design and security best practices, which is typically what interviewers expect for a senior-level authentication design question.


This is a very common system design + security interview question. The interviewer wants to know how you secure authentication in a third-party application (Google Login, Microsoft Login, OAuth providers, etc.) and how you prevent token hijacking.
A good answer is structured in layers.
Architecture
Client (React/Angular)
        |
        | Login with Google/Microsoft
        |
OAuth Provider
        |
   Authorization Code
        |
Backend API
        |
Exchange code for Access Token + Refresh Token
        |
Create own JWT Session
        |
Return HttpOnly Secure Cookie
Never let the frontend directly manage sensitive OAuth tokens if you can avoid it.
1. Use Authorization Code Flow with PKCE
Never use the Implicit Flow.
Client
   |
Generate Code Verifier
Generate Code Challenge
   |
Redirect to Google
   |
Google returns Authorization Code
   |
Backend exchanges code
PKCE prevents authorization code interception.
2. Store Token Securely
❌ Don't store JWT in
localStorage
sessionStorage
Because JavaScript can read it during an XSS attack.
Instead
✅ Store token in
HttpOnly Cookie
Secure Cookie
SameSite=Lax or Strict
Example
Set-Cookie:

token=xxxxx;

HttpOnly
Secure
SameSite=Strict
JavaScript cannot access it.
3. HTTPS Everywhere
Never send tokens over HTTP.
https://
Use
TLS 1.2+
or
TLS 1.3
Without HTTPS
Attacker
     |
Wireshark
     |
Reads JWT
4. Short-lived Access Token
Instead of
Access Token

24 hours
Use
15 minutes
or
10 minutes
If stolen
It expires quickly.
5. Refresh Token Rotation
Instead of
Refresh Token
being valid forever
Use
Refresh Token

↓

Use once

↓

Issue new Refresh Token

↓

Invalidate previous one
If attacker reuses old refresh token
Immediately
Logout user

Invalidate session
6. Validate JWT Properly
Check
Signature

Expiration

Issuer

Audience

Algorithm
Example
iss

aud

exp

iat

sub
Never trust token contents without verifying the signature.
7. CSRF Protection
Since cookies are sent automatically
Use
CSRF Token

OR

SameSite Cookie

OR

Double Submit Cookie
to prevent cross-site request forgery.
8. XSS Protection
Even with HttpOnly cookies
Prevent XSS using
Content Security Policy

Input Sanitization

Output Encoding
Avoid
innerHTML
Use
textContent
or Angular/React's default escaping.
9. Device Binding
Store
Device ID

Browser Fingerprint

IP Address (optional)

Location
If token suddenly appears from another country
Challenge user again

OTP

MFA
10. Token Revocation
Keep
Blacklist

or

Revocation Store
When
Logout

Password change

Account disabled
Immediately reject token.
11. Rate Limiting
Prevent brute force
5 login attempts

↓

Wait 30 sec

↓

Captcha

↓

Temporary lock
12. Multi-factor Authentication (MFA)
Even if attacker steals password
Need
OTP

Authenticator App

FIDO2

Passkeys
13. Least Privilege
JWT should contain only required claims.
Bad
Admin=true

Salary

Credit Card
Good
UserId

Role

Permissions
14. Monitor Suspicious Activity
Detect
Multiple countries

Impossible travel

100 login failures

Token replay

Unknown device
Automatically
Block account

Ask MFA

Revoke session
15. Protect Secrets
OAuth client secrets should never be exposed in frontend code.
Store them in
Backend secret manager
Environment variables
Cloud secret vault (such as managed secret storage)
The frontend should only receive data it needs to establish the user session.
Interview Answer (2-minute version)
"To secure a third-party login system, I would use OAuth 2.0 Authorization Code Flow with PKCE so the authorization code can't be intercepted. The backend exchanges the authorization code for tokens, keeping client secrets off the frontend. I would issue my own short-lived JWT and store it in an HttpOnly, Secure, SameSite cookie instead of localStorage to protect against XSS. All communication would use HTTPS. Access tokens would be short-lived, while refresh tokens would use rotation so each refresh invalidates the previous token. Every JWT would be validated for its signature, issuer, audience, and expiration. I'd also enable CSRF protection, apply Content Security Policy to reduce XSS risk, implement rate limiting on authentication endpoints, support MFA for sensitive actions, monitor for suspicious logins, and revoke sessions immediately on logout, password changes, or detected compromise."
This answer demonstrates knowledge of OAuth, browser security, token lifecycle management, and defense-in-depth, which is what interviewers are typically looking for.





