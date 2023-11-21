# Vendor Management API

## Setup Instructions:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/vendor-management.git
   cd vendor-management
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate  # Unix/MacOS
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Documentation:

### 1. Vendor Profile Management:

- **POST /api/vendors/:** Create a new vendor.
  ex: {
  "name": "John",
  "contact_details": "8529637410",
  "address": "Usa",
  "vendor_code": "MNO1011",
  "on_time_delivery_rate": 5.0,
  "quality_rating_avg": 4.2,
  "average_response_time": 4.7,
  "fulfillment_rate": 4.2
  }
- **GET /api/vendors/:** List all vendors.
- **GET /api/vendors/{vendor_id}/:** Retrieve a specific vendor's details.
- **PUT /api/vendors/{vendor_id}/:** Update a vendor's details.
- **DELETE /api/vendors/{vendor_id}/:** Delete a vendor.

### 2. Purchase Order Tracking:

- **POST /api/purchase_orders/:** Create a purchase order.
  ex:{
  "po_number": "PO211",
  "vendor": 1,
  "order_date": "2023-01-01T12:00:00Z",
  "items": [
  {
  "name": "Milk",
  "quantity": 10
  },
  {
  "name": "Mango Bites",
  "quantity": 5
  }
  ],
  "status": "completed", // Change the status to 'completed' to trigger acknowledgment
  "issue_date": "2023-01-01T12:00:00Z",
  "quantity":15,
  "acknowledgment_date": "2023-01-01T12:30:00Z" // Add acknowledgment date to calculate response time
  }
- **GET /api/purchase_orders/:** List all purchase orders with an option to filter by vendor.
- **GET /api/purchase_orders/{po_id}/:** Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/:** Update a purchase order.
- **DELETE /api/purchase_orders/{po_id}/:** Delete a purchase order.

### 3. Vendor Performance Evaluation:

- **GET /api/vendors/{vendor_id}/performance:** Retrieve a vendor's performance metrics.
  ex: {
  "on_time_delivery_rate": 80.0,
  "quality_rating_avg": 4.766666666666667,
  "average_response_time": 0.1,
  "fulfillment_rate": 60.0
  }
