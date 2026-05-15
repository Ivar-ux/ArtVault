# 🎨 ArtVault Marketplace

An online marketplace system designed for securely cataloging fine art, managing dynamic auction protocols, and protecting user privacy. Developed as a collaborative project for course evaluation at **Reykjavik University**.

## 👥 Authors & Contributions
* **Ivar** (`ivart25@ru.is`) - Core system architecture design, database schema routing, UC-03 provenance privacy controls, and UC-04/05 transaction validation mechanics.
* **Nökkvi** (`nokkvib25@ru.is`) - Front-end interface mapping, UC-02 search functionality implementation, and dynamic media grid/thumbnail processing.

## 🛠️ Features Implemented & Verified
* **UC-02: Search & Browse** – Case-insensitive database filtering allowing users to scan fine art items by title or category seamlessly.
* **UC-03: Provenance Security Shield** – Structural compliance protocol that securely blinds the physical street addresses and personal names of private individuals while explicitly verifying trusted commercial gallery partners.
* **UC-04: Active Bidding Pipeline** – Native Django token authentication integration for secure submission of transactional binding context offers.
* **UC-05: Status Restrictions** – Absolute operational lockouts on frontend controls when an item state transitions to "Sold" in the backend.

## 🚀 Local Installation & Setup

1. **Clone the repository and enter the directory:**
   ```bash
   git clone [https://github.com/Ivar-ux/ArtVault.git](https://github.com/Ivar-ux/ArtVault.git)
   cd ArtVault
