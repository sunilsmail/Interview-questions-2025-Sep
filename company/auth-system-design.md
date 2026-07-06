Authentication & JWT Interview Questions and Answers
1. Design a Simple Authentication System
Question: How would you design a simple authentication system with Login and Register APIs?
Answer: I would expose these APIs:
POST /register
POST /login
GET /profile (Protected)
POST /logout
Register Flow
Client
   |
POST /register
   |
Validate Input
   |
Check User Exists
   |
Hash Password (bcrypt/Argon2)
   |
Store User
   |
201 Created
Login Flow
Client
   |
POST /login
   |
Validate Credentials
   |
Compare Password Hash
   |
Generate JWT
   |
Return Access Token
Protected API
Authorization: Bearer <JWT>

Backend
   |
Verify JWT
   |
Extract User ID
   |
Return Profile
Security
Hash passwords with bcrypt/Argon2
HTTPS only
Validate all inputs
Rate limit login APIs
Short-lived JWT (15–30 min)
Never store plain-text passwords
2. How do you ensure a JWT is not tampered with?
Answer:
A JWT consists of three parts:
Header.Payload.Signature
When the server receives the JWT:
Received Token
       |
Split Header.Payload.Signature
       |
Generate Signature using Secret Key
       |
Compare Generated Signature
        ==
Received Signature?
       |
Yes -> Valid Token
No  -> 401 Unauthorized
The server recalculates the signature using the received header and payload. If it matches the received signature, the token is valid.
3. What happens if someone modifies the JWT payload?
Answer:
Original Payload
{
  "userId":101,
  "role":"USER"
}
Attacker changes it to
{
  "userId":101,
  "role":"ADMIN"
}
The token becomes
New Header.New Payload.Old Signature
Server Verification
Header + Payload
        |
Generate New Signature
        |
Compare with Old Signature
        |
Mismatch
        |
401 Unauthorized
Because the attacker doesn't know the secret key, they cannot generate a valid signature.
4. Can someone decode a JWT?
Answer:
Yes.
JWT is Base64URL encoded, not encrypted.
Anyone can decode it and read the payload.
However, they cannot modify it without invalidating the digital signature.
Never store sensitive data such as:
Passwords
Credit card numbers
Personal secrets
inside a JWT.
5. What does jwt.verify() do internally?
Answer:
Internally it performs:
Receive Token
      |
Split Header.Payload.Signature
      |
Generate Signature
      |
Compare Signature
      |
Validate Expiration
      |
Validate Issuer
      |
Validate Audience
      |
Validate Algorithm
      |
Return Payload
6. Show JWT verification in Node.js without using a library.
Answer
const crypto = require("crypto");

const secret = "my_secret";

const token = "header.payload.signature";

const [header, payload, signature] = token.split(".");

const data = `${header}.${payload}`;

const generatedSignature = crypto
  .createHmac("sha256", secret)
  .update(data)
  .digest("base64url");

if (generatedSignature === signature) {
    console.log("Valid Token");
} else {
    console.log("Token Tampered");
}
7. How do JWT libraries verify tokens?
Answer
const jwt = require("jsonwebtoken");

try {
    const decoded = jwt.verify(token, "my_secret");
    console.log(decoded);
} catch {
    console.log("Invalid Token");
}
Internally it performs the same signature verification process.
8. What if an attacker steals your JWT signing key?
Answer
If the signing key is compromised, an attacker can generate valid tokens.
To protect against this:
Store keys in a Secret Manager/Key Vault
Rotate keys periodically
Limit access to signing keys
Prefer RS256, where only the authentication server has the private key
9. What validations should be performed on every JWT?
Answer
Always verify:
✅ Signature
✅ Expiration (exp)
✅ Issuer (iss)
✅ Audience (aud)
✅ Signing Algorithm (alg)
✅ Issued At (iat)
Never allow alg: none.
10. Why shouldn't JWTs be stored in localStorage?
Answer
Because JavaScript can read localStorage.
If an XSS attack occurs:
Attacker JS
      |
Read localStorage
      |
Steal JWT
Instead use:
HttpOnly Cookie
Secure
SameSite=Strict
JavaScript cannot access HttpOnly cookies.
11. Explain Refresh Token Rotation.
Answer
Login
   |
Access Token (15 min)
Refresh Token (30 days)

Refresh Request
       |
Use Refresh Token
       |
Generate New Access Token
Generate New Refresh Token
       |
Invalidate Old Refresh Token
If someone reuses an old refresh token:
Old Refresh Token
       |
Detected
       |
Revoke Session
12. Why are Access Tokens short-lived?
Answer
If an attacker steals an access token:
15 Minutes
is much safer than
24 Hours
A short expiration limits the impact of token theft.
13. Explain OAuth Authorization Code Flow with PKCE.
Answer
Client
   |
Generate Code Verifier
Generate Code Challenge
   |
Redirect User
   |
OAuth Provider
   |
Authorization Code
   |
Backend Exchanges Code
   |
Access Token
Refresh Token
PKCE prevents interception of the authorization code.
14. Why should OAuth client secrets never be stored in the frontend?
Answer
Frontend code is visible to users.
Only the backend should store:
OAuth Client Secret
Private Keys
API Secrets
Prefer Secret Manager or Key Vault.
15. How do you secure third-party authentication?
Answer
I would:
Use OAuth Authorization Code Flow with PKCE
Store tokens in HttpOnly Secure Cookies
Use HTTPS
Validate JWT Signature
Use Refresh Token Rotation
Enable CSRF protection
Apply CSP against XSS
Support MFA
Rate limit login APIs
Monitor suspicious logins
Revoke tokens after logout/password change
16. What is the architecture of a scalable authentication system?
Answer
React / Angular
       |
HTTPS
       |
API Gateway
       |
Authentication Service
       |
--------------------------
|                        |
User Database         Redis
                      Sessions/
                  Refresh Tokens
       |
JWT Generator
       |
HttpOnly Cookie
The authentication service remains stateless and scales horizontally.
17. What are the functional requirements of an authentication system?
Answer
User Registration
Login
Logout
Password Reset
Email Verification
Role-Based Access
Multi-Factor Authentication
Social Login
18. What are the non-functional requirements?
Answer
High Availability
Low Latency
Scalability
Security
Audit Logging
Compliance (GDPR/HIPAA)
Fault Tolerance
19. What security measures would you implement?
Answer
HTTPS
bcrypt/Argon2 Password Hashing
JWT Validation
Rate Limiting
Account Lockout
MFA
CSP
CSRF Protection
XSS Prevention
SQL Injection Prevention
Refresh Token Rotation
Secret Management
Audit Logging
20. Senior-Level (30-second) Interview Answer
Question: How do you ensure a JWT isn't tampered with?
Answer:
"When a JWT is received, the server splits it into Header, Payload, and Signature. It recalculates the signature using the received header and payload with the server's signing key (secret key for HS256 or private/public key pair for RS256). It compares the generated signature with the one in the token. If they match, the token hasn't been modified; otherwise, it's rejected with a 401 Unauthorized response. We also validate the expiration, issuer, audience, and expected signing algorithm before trusting the token."