For a Sanofi Digital R&D Software Engineering Lead interview, this is a very common system design and leadership question.
Question: "We have a legacy application. How would you modernize it using new technologies?"
A good answer should cover business, architecture, execution, and risk management.
Sample Answer
"I wouldn't rewrite the entire application at once because it's high risk. Instead, I'd follow an incremental modernization strategy."
1. Understand the existing system
Understand business-critical modules.
Identify pain points.
Analyze dependencies.
Review database schema.
Check performance bottlenecks.
Measure code quality and test coverage.
Example:
"First I'd identify which modules change frequently and which are stable."
2. Define modernization goals
Examples:
Better performance
Cloud readiness
Easier maintenance
Faster deployments
Better developer productivity
Improved security
3. Break the monolith
Instead of rewriting everything:
Legacy Monolith

├── Authentication
├── Patient Management
├── Reports
├── Notifications
├── Billing
Extract one module at a time into microservices.
API Gateway

        |
-------------------------
|       |        |
Auth   Patient  Reports
Service Service Service
4. Use the Strangler Fig Pattern
Don't replace everything.
Client
   |
API Gateway
   |
--------------------------
|                        |
Legacy App         New React UI
                       |
                  New FastAPI/.NET Services
Initially
20% New
80% Legacy
Later
50% New
50% Legacy
Eventually
100% New
No downtime.
5. Modernize the UI
If it's an old AngularJS/jQuery application:
Move to
React
Angular 18
TypeScript
Component-based architecture
Micro Frontends if multiple teams work independently.
6. Modernize Backend
Example:
Old
ASP.NET MVC
New
FastAPI
or
.NET 8
Split into services:
User Service
Patient Service
Notification Service
Reporting Service
7. Database Strategy
Don't migrate everything immediately.
Use
Database per service
Data migration scripts
CDC (Change Data Capture)
Event-driven synchronization
8. CI/CD
Implement
GitHub Actions/Azure DevOps
Automated testing
Docker
Kubernetes
Blue-Green or Canary deployment
9. Testing
Before replacing anything:
Unit Tests
Integration Tests
Contract Tests
Regression Testing
Performance Testing
Ensure old and new systems produce the same results.
10. Security
Especially important in healthcare.
OAuth2
JWT
RBAC
Encryption
Audit Logs
HIPAA/GxP compliance
API Gateway
Secrets in Azure Key Vault
11. Observability
Application Insights
Prometheus
Grafana
Distributed Tracing
Centralized Logging
12. Rollout
Never deploy to all users.
5%

↓

20%

↓

50%

↓

100%
Monitor:
Errors
Latency
User feedback
Rollback if necessary.
Mention Healthcare Considerations
For Sanofi R&D, add:
Patient data security
Regulatory compliance (HIPAA/GxP)
Full audit trail
Backward compatibility with laboratory and clinical systems
Zero or minimal downtime
A concise 2-minute interview answer
"I would avoid a big-bang rewrite because it's risky. I'd start by assessing the application's architecture, dependencies, and business-critical modules. Then I'd prioritize high-value areas and modernize incrementally using the Strangler Fig pattern. For the frontend, I'd migrate to React or the latest Angular with TypeScript, and for the backend I'd move toward microservices using .NET or FastAPI behind an API Gateway. I'd introduce CI/CD, automated testing, Docker, and Kubernetes for reliable deployments. During migration, I'd keep the legacy and new systems running together, using APIs or events for integration, and roll out changes gradually with monitoring and rollback capabilities. Since this is an R&D healthcare application, I'd also ensure regulatory compliance, strong security, audit logging, and protection of sensitive data throughout the modernization process."
This answer demonstrates architectural thinking, risk management, and delivery strategy—qualities expected from a Software Engineering Lead at Sanofi.