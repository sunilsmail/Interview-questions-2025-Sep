You are a senior full-stack engineer. Generate a complete working microservices-based project with the following requirements:

## 🎯 Goal

Build a real-time order processing system with:

* Parallel validation (product, price, location)
* Kafka-based async communication
* WebSocket-based real-time UI updates
* Angular frontend
* Node.js backend (multiple services)

---

## 🧱 Architecture Requirements

### Backend Services:

1. API Gateway (Express + Socket.IO)
2. Order Service
3. Payment Service (mock)
4. Kafka Producer/Consumer module

### Frontend:

* Angular app with:

  * Checkout page
  * Real-time order status page

---

## ⚙️ Functional Flow

1. User clicks "Place Order"
2. Order Service creates orderId
3. Trigger parallel async events:

   * PRODUCT_CHECK
   * PRICE_CHECK
   * LOCATION_CHECK
4. Kafka handles communication
5. Services respond with events:

   * PRODUCT_AVAILABLE
   * PRICE_CONFIRMED
   * LOCATION_VALID
6. After all success → trigger PAYMENT
7. Payment Service emits:

   * PAYMENT_SUCCESS / PAYMENT_FAILED
8. WebSocket pushes real-time updates to UI

---

## 🔌 WebSocket Requirements

* Use Socket.IO
* Authenticate using JWT
* Map userId to socket
* Use "orderId" as room
* UI subscribes to order updates
* Emit event: "order-update"

---

## 🖥️ Frontend Requirements (Angular)

* Service to call backend API
* WebSocket service
* Checkout component:

  * Create order
  * Join WebSocket room
* Status component:

  * Show real-time updates
  * Handle success/failure UI

---

## 📦 Kafka Requirements (NO Docker)

* Use KafkaJS library
* Assume Kafka is installed locally
* Provide commands to:

  * Start Zookeeper
  * Start Kafka
  * Create topic "order-events"

---

## 💻 Local Setup Instructions (IMPORTANT)

Provide step-by-step instructions:

1. Install Kafka locally (no Docker)
2. Start Kafka + Zookeeper
3. Run backend services individually:

   * node gateway/server.js
   * node order-service/index.js
4. Run Angular app:

   * npm install
   * ng serve
5. Open browser and test flow

---

## 🔐 Authentication

* Use simple JWT token (hardcoded secret)
* Include sample token generation

---

## 📁 Folder Structure

Provide complete folder structure like:

backend/
gateway/
order-service/
payment-service/
kafka/

frontend/
angular-app/

---

## 🧪 Testing Flow

Explain how to test:

* Start all services
* Click "Place Order"
* Observe real-time updates

---

## 🚀 Code Expectations

* Provide COMPLETE runnable code
* No pseudo code
* Minimal but working implementation
* Add comments for clarity

---

## ⚠️ Constraints

* DO NOT use Docker
* DO NOT skip Kafka setup
* Keep code simple and readable
* Use only:

  * express
  * socket.io
  * kafkajs
  * jsonwebtoken

---

## 🎯 Output Format

1. Folder structure
2. Backend code (all files)
3. Frontend Angular code
4. Kafka setup commands
5. Run instructions
6. Test steps

---

Make sure everything works together end-to-end on a local machine.
