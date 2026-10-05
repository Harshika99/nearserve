# 📍 NearServe — Real-Time Hyperlocal Service Network

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.2-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-5.1-646CFF?logo=vite)](https://vitejs.dev/)
[![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-199900?logo=leaflet)](https://leafletjs.com/)

**NearServe** is a real-time hyperlocal service dispatch platform designed to connect people in Indian cities with verified local professionals (Plumbers, Electricians, AC Technicians, Deep Cleaners, Internet Technicians, Painters, and Appliance Repair Experts) in under 10 minutes.

---

## ✨ Key Features

- **🌐 Keyless & Watermark-Free Interactive Maps**: Clean Leaflet map integration powered by CartoDB Voyager and OpenStreetMap tiles (no Google Maps API key required).
- **📍 GPS Geolocation & Reverse Geocoding**: HTML5 Geolocation API coupled with OpenStreetMap Nominatim reverse geocoding for instant suburb and locality resolution across all major Indian metro hubs (Hyderabad, Bengaluru, Mumbai, Delhi NCR, Chennai, Pune, Kolkata, Ahmedabad).
- **🤖 Natural Language AI Urgency Parser**: Analyzes user query prompts using multi-tier intent classification:
  - `High Urgency` (e.g., *"sparking wires emergency right now"*)
  - `Medium Urgency` (e.g., *"AC service needed today by evening"*)
  - `Low Urgency` (e.g., *"fan installation next weekend"*)
  - `Urgency: Not specified` (when no explicit timeline is specified)
- **⏳ Real-Time Dispatch & 15s Provider Acceptance Countdown**:
  - Live 15-second countdown timer (`00:15s`) when a customer requests a service provider.
  - Progressive step unlocking: **Request Sent** ➔ **Provider Accepted** ➔ **En-Route** ➔ **Arrived** ➔ **In-Progress** ➔ **Completed**.
- **🛠️ Dual Role Dashboard (Customer & Provider)**:
  - **Provider View**: Toggle status (**Available**, **Busy**, **Offline**), accept incoming requests, track completed job counts, view earned fees (+₹250 per job), and inspect **Work Accomplished** history.
  - **Customer View**: Search by category or map pin, dispatch requests, track live ETA, and submit 5-star rating feedback upon job completion.

---

## 🛠️ Architecture & Tech Stack

| Layer | Technology Used |
| :--- | :--- |
| **Frontend Framework** | React 18 + TypeScript + Vite |
| **Mapping & Geospatial** | Leaflet 1.9 + React-Leaflet (`CartoDB Voyager`, `OpenStreetMap`) |
| **Geocoding API** | OpenStreetMap Nominatim Reverse Geocoding API |
| **Iconography & Styling** | Lucide React + Glassmorphic CSS Engine |
| **State & Auth** | React Context & LocalStorage Session Engine (`nearserve_session`) |

---

## 🚀 Quick Start & Installation

### Prerequisites
- Node.js (v18.0.0 or higher)
- npm or yarn

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nearserve.git
cd nearserve/frontend
