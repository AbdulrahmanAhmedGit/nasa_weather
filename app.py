</style>
</head>

<body>
    <div id="preloader">
        <h2>Loading Weather Data...</h2>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <div id="progress-text">0%</div>
        <div id="loading-status">Preparing resources...</div>
    </div>

    <div id="app" class="hidden">
        <div class="container-wrapper">
            <div class="main-container">
                <div class="side-bar">
                    <div class="side_Cs" data-tooltip="How the temperature feels">
                        <span class="label"><i class="bi bi-thermometer-half"></i> Feels Like</span>
                        <span class="value">{{ result[1] }}<small>°C</small></span>
                    </div>
                    <div class="side_Cs" data-tooltip="Temperature adjusted for wind">
                        <span class="label"><i class="bi bi-wind"></i> Wind Chill</span>
                        <span class="value">{{ result[4] }}<small>°C</small></span>
                    </div>
                    <div class="side_Cs" data-tooltip="Current wind velocity">
                        <span class="label"><i class="bi bi-speedometer2"></i> Wind Speed</span>
                        <span class="value">{{ result[2] }}<small> km/h</small></span>
                    </div>
                    <div class="side_Cs" data-tooltip="Atmospheric pressure">
                        <span class="label"><i class="bi bi-speedometer"></i> Pressure</span>
                        <span class="value">{{ result[-3] }}<small> in</small></span>
                    </div>
                    <div class="side_Cs" data-tooltip="Moisture in the air">
                        <span class="label"><i class="bi bi-droplet"></i> Humidity</span>
                        <span class="value">{{ result[3] }}<small>%</small></span>
                    </div>
                    <div class="side_Cs" data-tooltip="Sky cloud coverage">
                        <span class="label"><i class="bi bi-clouds"></i> Cloud Cover</span>
                        <span class="value">{{ result[-2] }}<small>%</small></span>
                    </div>
                    {% if spec == True %}
                    <div class="side_Cs" id="newadd" data-tooltip="Daily rainfall amount">
                        <span class="label"><i class="bi bi-cloud-drizzle"></i> Precipitation</span>
                        <span class="value">{{ rsult }}<small>mm/day</small></span>
                    </div>
                    {% endif %}
                    <div class="side_Cs" data-tooltip="Weather classification">
                        <span class="label"><i class="bi bi-tags"></i> Category</span>
                        <span class="value">{{ text }}</span>
                    </div>
                </div>

                <div class="weather-cards">
                    <div class="card_ma" id="city-card" tabindex="0" role="button" aria-label="Click to change location">
                        <div class="weather-icon">
                            <i class="bi bi-geo-alt"></i>
                        </div>
                        <h1 class="city-name"><strong>{{ city }}</strong></h1>
                        <div class="click-indicator">
                            <i class="bi bi-cursor"></i>
                            <span>Click to change location</span>
                        </div>
                    </div>

                    <div class="card_ma temperature-display">
                        <div class="weather-icon">
                            <i class="bi bi-thermometer-sun"></i>
                        </div>
                        <h1 class="no0"><strong>{{ result[0] }}<small>°C</small></strong></h1>
                    </div>

                    <div class="card_ma">
                        <div class="weather-icon">
                            <i class="bi bi-cloud-sun"></i>
                        </div>
                        <h3 class="weather-state">{{ final }}</h3>
                    </div>
                </div>

                <div class="card_ma time-card">
                    <div class="weather-icon">
                        <i class="bi bi-clock"></i>
                    </div>
                    <h3 class="section-title">Current Time</h3>
                    <div class="time-display">
                        <p id="time" role="timer" aria-live="polite">--:--:--</p>
                        <p id="date-pop">--</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="map-modal" id="map-modal" role="dialog" aria-modal="true" aria-labelledby="map-modal-title">
        <div class="map-container">
            <button class="close-modal" id="close-map" aria-label="Close map">&times;</button>
            <h3 class="section-title" id="map-modal-title">Select a Location</h3>
            <div id="map" role="application" aria-label="Interactive map for location selection"></div>
            <div class="map-controls">
                <div class="coordinates-display" id="coordinates" aria-live="polite">
                    Latitude: --, Longitude: --
                </div>
                <div id="app">
                    <div id="clock">
                        <p id="date"></p>
                    </div>
                </div>
                <div class="map-buttons">
                    <button class="map-btn cancel" id="cancel-map">Cancel</button>
                    <button class="map-btn" id="submit-location">Submit</button>
                    <button onclick="datepopup()" class="Choose" data-tooltip="View historical weather">
                        <i class="bi bi-calendar3"></i> Choose Date
                    </button>
                </div>

                <div class="date-picker-modal" id="date-picker-modal" role="dialog" aria-modal="true" aria-labelledby="date-picker-title">
                    <form id="date-form" action="/{{lat}}/{{lon}}" method="get">
                        <div class="date-picker-container">
                            <h3 class="date-picker-title" id="date-picker-title">Select Date</h3>
                            <div class="date-inputs-container">
                                <div class="date-input-group">
                                    <label class="date-input-label" for="day-select">Day</label>
                                    <select class="date-select" id="day-select" name="day" aria-label="Select day"></select>
                                </div>
                                <div class="date-input-group">
                                    <label class="date-input-label" for="month-select">Month</label>
                                    <select class="date-select" id="month-select" name="month" aria-label="Select month"></select>
                                </div>
                                <div class="date-input-group">
                                    <label class="date-input-label" for="year-select">Year</label>
                                    <select class="date-select" id="year-select" name="year" aria-label="Select year"></select>
                                </div>
                            </div>
                            <div class="date-picker-buttons">
                                <button type="button" class="date-picker-btn cancel" id="cancel-date">Cancel</button>
                                <button type="submit" class="date-picker-btn" id="apply-date">Apply</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

    <script>
        'use strict';

        // Utility functions
        const debounce = (func, wait) => {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        };

        // Clock functionality
        function updateClock() {
            const timeElement = document.getElementById("time");
            const dateElement = document.getElementById("date");
            const dateElementPop = document.getElementById("date-pop");

            try {
                const now = new Date();
                const hours = String(now.getHours()).padStart(2, "0");
                const minutes = String(now.getMinutes()).padStart(2, "0");
                const seconds = String(now.getSeconds()).padStart(2, "0");

                const timeString = `${hours}:${minutes}:${seconds}`;
                const dateOptions = {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                };
                const dateString = now.toLocaleDateString('en-US', dateOptions);

                if (timeElement) timeElement.textContent = timeString;
                if (dateElement) dateElement.textContent = dateString;
                if (dateElementPop) dateElementPop.textContent = dateString;

            } catch (error) {
                console.error('Error updating clock:', error);
                if (timeElement) timeElement.textContent = "Error";
                if (dateElement) dateElement.textContent = "--/--/----";
                if (dateElementPop) dateElementPop.textContent = "--/--/----";
            }
        }

        function initializeClock() {
            updateClock();
            setInterval(updateClock, 1000);
        }

        // Loading Manager Class
        class LoadingManager {
            constructor() {
                this.totalResources = 0;
                this.loadedResources = 0;
                this.isComplete = false;
                this.progressFill = document.getElementById("progress-fill");
                this.progressText = document.getElementById("progress-text");
                this.loadingStatus = document.getElementById("loading-status");
                this.preloader = document.getElementById("preloader");
                this.app = document.getElementById("app");
                this.init();
            }

            init() {
                this.countResources();
                this.setupEventListeners();
                this.startBasicProgress();
            }

            countResources() {
                const images = document.querySelectorAll('img');
                const elementsWithBgImages = document.querySelectorAll('*');
                let bgImageCount = 0;

                elementsWithBgImages.forEach(element => {
                    const style = window.getComputedStyle(element);
                    const bgImage = style.backgroundImage;
                    if (bgImage && bgImage !== 'none' && bgImage.includes('url(')) {
                        bgImageCount++;
                    }
                });

                const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
                const scripts = document.querySelectorAll('script[src]');
                this.totalResources = images.length + bgImageCount + stylesheets.length + scripts.length + 3;

                if (this.totalResources === 3) {
                    this.totalResources = 10;
                }
            }

            setupEventListeners() {
                const images = document.querySelectorAll('img');
                images.forEach(img => {
                    if (img.complete) {
                        this.resourceLoaded();
                    } else {
                        img.addEventListener('load', () => this.resourceLoaded());
                        img.addEventListener('error', () => this.resourceLoaded());
                    }
                });

                const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
                stylesheets.forEach(link => {
                    if (link.sheet) {
                        this.resourceLoaded();
                    } else {
                        link.addEventListener('load', () => this.resourceLoaded());
                        link.addEventListener('error', () => this.resourceLoaded());
                    }
                });

                const scripts = document.querySelectorAll('script[src]');
                scripts.forEach(script => {
                    script.addEventListener('load', () => this.resourceLoaded());
                    script.addEventListener('error', () => this.resourceLoaded());
                });

                if (document.fonts) {
                    document.fonts.ready.then(() => {
                        this.resourceLoaded('Fonts loaded');
                        this.resourceLoaded('Google Fonts loaded');
                        this.resourceLoaded('Icon fonts loaded');
                    });
                } else {
                    setTimeout(() => {
                        this.resourceLoaded('Fonts loaded');
                        this.resourceLoaded('Google Fonts loaded');
                        this.resourceLoaded('Icon fonts loaded');
                    }, 2000);
                }

                this.checkBackgroundImages();

                window.addEventListener('load', () => {
                    setTimeout(() => {
                        if (!this.isComplete) {
                            this.completeLoading();
                        }
                    }, 1000);
                });
            }

            checkBackgroundImages() {
                const elementsWithBgImages = document.querySelectorAll('*');
                elementsWithBgImages.forEach(element => {
                    const style = window.getComputedStyle(element);
                    const bgImage = style.backgroundImage;

                    if (bgImage && bgImage !== 'none' && bgImage.includes('url(')) {
                        const match = bgImage.match(/url\(["']?(.*?)["']?\)/);
                        if (match) {
                            const imageUrl = match[1];
                            const img = new Image();
                            img.onload = () => this.resourceLoaded(`Background loaded`);
                            img.onerror = () => this.resourceLoaded(`Background error`);
                            img.src = imageUrl;
                        }
                    }
                });
            }

            resourceLoaded(statusMessage = '') {
                this.loadedResources++;
                if (statusMessage) {
                    this.updateStatus(statusMessage);
                }
                this.updateProgress();

                if (this.loadedResources >= this.totalResources && !this.isComplete) {
                    setTimeout(() => {
                        this.completeLoading();
                    }, 500);
                }
            }

            updateProgress() {
                const progress = Math.min(Math.round((this.loadedResources / this.totalResources) * 100), 99);
                if (this.progressFill) this.progressFill.style.width = progress + "%";
                if (this.progressText) this.progressText.textContent = progress + "%";
            }

            updateStatus(message) {
                if (this.loadingStatus) {
                    this.loadingStatus.textContent = message;
                }
            }

            startBasicProgress() {
                const steps = [
                    { progress: 10, message: "Loading stylesheets..." },
                    { progress: 20, message: "Initializing components..." },
                    { progress: 30, message: "Loading fonts..." }
                ];

                steps.forEach((step, index) => {
                    setTimeout(() => {
                        if (this.loadedResources < (this.totalResources * step.progress / 100)) {
                            this.updateStatus(step.message);
                        }
                    }, (index + 1) * 800);
                });
            }

            completeLoading() {
                if (this.isComplete) return;
                this.isComplete = true;
                this.loadedResources = this.totalResources;
                if (this.progressFill) this.progressFill.style.width = "100%";
                if (this.progressText) this.progressText.textContent = "100%";
                this.updateStatus("Ready!");

                setTimeout(() => {
                    if (this.preloader) {
                        this.preloader.style.opacity = "0";
                        this.preloader.style.transition = "opacity 0.5s ease-out";

                        setTimeout(() => {
                            this.preloader.style.display = "none";
                            if (this.app) {
                                this.app.classList.remove("hidden");
                                this.app.style.opacity = "0";
                                requestAnimationFrame(() => {
                                    this.app.style.transition = "opacity 0.5s ease-in";
                                    this.app.style.opacity = "1";
                                });
                            }
                        }, 500);
                    }
                }, 800);
            }
        }

        // Map functionality
        let map;
        let marker;
        let selectedLat;
        let selectedLon;

        function initMap() {
            try {
                map = L.map('map').setView([30.0444, 31.2357], 10);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                }).addTo(map);

                map.on('click', function (e) {
                    const { lat, lng } = e.latlng;
                    selectedLat = lat;
                    selectedLon = lng;

                    const coordsEl = document.getElementById('coordinates');
                    if (coordsEl) {
                        coordsEl.textContent = `Latitude: ${lat.toFixed(4)}, Longitude: ${lng.toFixed(4)}`;
                    }

                    if (marker) {
                        map.removeLayer(marker);
                    }

                    marker = L.marker([lat, lng]).addTo(map)
                        .bindPopup('Selected Location').openPopup();
                });

                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        function (position) {
                            const { latitude, longitude } = position.coords;
                            map.setView([latitude, longitude], 13);

                            L.marker([latitude, longitude])
                                .addTo(map)
                                .bindPopup('Your Current Location')
                                .openPopup();
                        },
                        function (error) {
                            console.log('Geolocation error:', error);
                        }
                    );
                }
            } catch (error) {
                console.error('Error initializing map:', error);
            }
        }

        function openMapModal() {
            const modal = document.getElementById('map-modal');
            if (modal) {
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
                
                setTimeout(() => {
                    if (!map) {
                        initMap();
                    } else {
                        map.invalidateSize();
                    }
                }, 100);
            }
        }

        function closeMapModal() {
            const modal = document.getElementById('map-modal');
            if (modal) {
                modal.classList.remove('active');
                document.body.style.overflow = '';
            }
        }

        function submitLocation() {
            if (selectedLat != null && selectedLon != null) {
                const mapModal = document.getElementById('map-modal');
                if (mapModal) {
                    mapModal.style.transition = 'opacity 0.5s ease-out';
                    mapModal.style.opacity = '0';
                }

                setTimeout(() => {
                    if (mapModal) {
                        mapModal.classList.remove('active');
                        mapModal.style.opacity = '1';
                    }
                    document.body.style.overflow = '';

                    const pre = document.getElementById('preloader');
                    const appEl = document.getElementById('app');
                    const statusEl = document.getElementById('loading-status');

                    if (pre) {
                        pre.style.display = 'flex';
                        pre.style.opacity = '0';
                        setTimeout(() => pre.style.opacity = '1', 50);
                    }
                    if (appEl) {
                        appEl.style.transition = 'opacity 0.3s ease-out';
                        appEl.style.opacity = '0';
                        setTimeout(() => appEl.classList.add('hidden'), 300);
                    }

                    const messages = [
                        'Sending location data...',
                        'Fetching weather information...',
                        'Processing results...',
                        'Almost ready...'
                    ];

                    let msgIndex = 0;
                    const statusInterval = setInterval(() => {
                        if (statusEl && msgIndex < messages.length) {
                            statusEl.style.opacity = '0';
                            setTimeout(() => {
                                statusEl.textContent = messages[msgIndex];
                                statusEl.style.opacity = '1';
                                msgIndex++;
                            }, 200);
                        }
                    }, 1000);

                    const lat = selectedLat.toFixed(6);
                    const lon = selectedLon.toFixed(6);

                    setTimeout(() => {
                        clearInterval(statusInterval);
                        window.location.href = `/${encodeURIComponent(lat)}/${encodeURIComponent(lon)}`;
                    }, 1500);
                }, 500);
            } else {
                alert('Please select a location on the map first.');
            }
        }

        // Date picker functionality
        function populateDateSelects() {
            const daySelect = document.getElementById('day-select');
            const monthSelect = document.getElementById('month-select');
            const yearSelect = document.getElementById('year-select');

            if (!daySelect || !monthSelect || !yearSelect) return;

            for (let i = 1; i <= 31; i++) {
                daySelect.add(new Option(i, i));
            }

            const months = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'];
            months.forEach((month, index) => {
                monthSelect.add(new Option(month, index + 1));
            });

            const currentYear = new Date().getFullYear();
            for (let i = currentYear - 50; i <= currentYear + 50; i++) {
                yearSelect.add(new Option(i, i));
            }

            const now = new Date();
            daySelect.value = now.getDate();
            monthSelect.value = now.getMonth() + 1;
            yearSelect.value = now.getFullYear();
        }

        function clos<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="1800">
    <link rel="manifest" href="../static/manifest.json">
    <link rel="shortcut icon" href="../static/img/icons8-cloud-96.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <meta name="theme-color" content="#667eea">
    <title>Weather App</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
        integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Orbitron:wght@400;500;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

        /* ===== Preloader ===== */
        #preloader {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            color: #fff;
            font-family: "Montserrat", sans-serif;
            transition: opacity 0.5s ease-out;
        }

        #progress-bar {
            width: 70%;
            max-width: 400px;
            height: 20px;
            border: 2px solid #fff;
            border-radius: 20px;
            overflow: hidden;
            margin-top: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }

        #progress-fill {
            height: 100%;
            width: 0;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            transition: width 0.3s ease-out;
        }

        #progress-text {
            margin-top: 10px;
            font-size: 18px;
            font-weight: 600;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
        }

        #loading-status {
            margin-top: 15px;
            font-size: 14px;
            opacity: 0.8;
            text-align: center;
            transition: opacity 0.3s ease-in-out;
        }

        .hidden {
            display: none;
        }

        /* ===== CSS VARIABLES ===== */
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --tertiary-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --dark-gradient: linear-gradient(135deg, #232526 0%, #414345 100%);
            --glass-bg: rgba(255, 255, 255, 0.12);
            --glass-border: rgba(255, 255, 255, 0.25);
            --glass-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            --glass-hover-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
            --neon-blue: #00d4ff;
            --neon-pink: #ff0080;
            --neon-purple: #8a2be2;
            --neon-green: #39ff14;
            --text-primary: #ffffff;
            --text-secondary: rgba(255, 255, 255, 0.85);
            --text-accent: #00d4ff;
            --border-radius: 25px;
            --border-radius-small: 15px;
            --transition-smooth: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            --transition-bounce: all 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: "Montserrat", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--primary-gradient);
            background-image: url("{{ background }}");
            background-position: center;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            color: var(--text-primary);
            min-height: 100vh;
            padding: 10px;
            overflow-x: hidden;
            position: relative;
            font-weight: 400;
            line-height: 1.6;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes floatParticles {
            0%, 100% { transform: translateY(0) translateX(0); }
            50% { transform: translateY(-20px) translateX(20px); }
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image:
                radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120, 200, 255, 0.2) 0%, transparent 50%);
            animation: floatParticles 20s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
        }

        .container-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: calc(100vh - 20px);
            width: 100%;
        }

        .main-container {
            display: grid;
            grid-template-columns: 280px 1fr;
            grid-template-rows: 1fr auto;
            gap: 20px;
            background: var(--glass-bg);
            border: 2px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: clamp(20px, 3vw, 30px);
            box-shadow: var(--glass-shadow), inset 0 2px 0 rgba(255, 255, 255, 0.2), 0 0 80px rgba(0, 212, 255, 0.1);
            backdrop-filter: blur(25px) saturate(150%);
            -webkit-backdrop-filter: blur(25px) saturate(150%);
            max-width: 1200px;
            width: 100%;
            transition: var(--transition-smooth);
            position: relative;
            overflow: hidden;
        }

        .side-bar {
            grid-column: 1;
            grid-row: 1 / 3;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius-small);
            padding: clamp(15px, 2.5vw, 25px);
            display: flex;
            flex-direction: column;
            gap: clamp(10px, 1.5vw, 15px);
            transition: var(--transition-smooth);
            position: relative;
            overflow: hidden;
        }

        .side-bar::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.8s ease-in-out;
        }

        .side-bar:hover::before {
            left: 100%;
        }

        .side_Cs {
            font-size: clamp(0.85rem, 2vw, 1rem);
            padding: clamp(10px, 1.5vw, 14px);
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: var(--border-radius-small);
            transition: var(--transition-smooth);
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: relative;
            cursor: pointer;
            backdrop-filter: blur(10px);
            font-family: "Inter", sans-serif;
        }

        .side_Cs:hover, #newadd {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(255, 0, 128, 0.2) 100%);
            transform: translateX(5px);
            border-color: var(--neon-blue);
            box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
        }

        .side_Cs .label {
            font-weight: 500;
            color: var(--text-secondary);
            font-size: 0.9em;
            letter-spacing: 0.3px;
        }

        .side_Cs .value {
            font-weight: 600;
            color: var(--text-primary);
            font-size: 1.1em;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
            font-family: "Montserrat", sans-serif;
        }

        .weather-cards {
            grid-column: 2;
            grid-row: 1;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .card_ma {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius-small);
            padding: clamp(20px, 3vw, 30px);
            transition: var(--transition-bounce);
            text-align: center;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 250px;
        }

        .card_ma::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 50%, transparent 70%);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }

        .card_ma:hover::after {
            transform: translateX(100%);
        }

        .card_ma:hover, .side-bar:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: var(--glass-hover-shadow), inset 0 2px 0 rgba(255, 255, 255, 0.3), 0 0 50px var(--neon-blue);
            border-color: rgba(255, 255, 255, 0.4);
        }

        .temperature-display {
            position: relative;
        }

        .no0 {
            font-family: 'Orbitron', monospace;
            font-size: clamp(2rem, 5vw, 3.5rem);
            font-weight: 700;
            margin: 0;
            background: linear-gradient(135deg, var(--neon-blue) 0%, var(--neon-pink) 50%, var(--neon-purple) 100%);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: textGlow 3s ease-in-out infinite;
            text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
            position: relative;
            letter-spacing: -1px;
        }

        @keyframes textGlow {
            0%, 100% {
                background-position: 0% 50%;
                filter: brightness(1);
            }
            50% {
                background-position: 100% 50%;
                filter: brightness(1.3);
            }
        }

        .city-name {
            font-size: clamp(1.6rem, 4vw, 1.8rem);
            font-weight: 700;
            margin: 0;
            color: var(--text-primary);
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
            position: relative;
            font-family: "Montserrat", sans-serif;
            letter-spacing: -0.5px;
        }

        .weather-state {
            font-size: clamp(1.1rem, 3vw, 1.5rem);
            margin: 15px 0 0 0;
            color: var(--text-secondary);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-family: "Inter", sans-serif;
        }

        .click-indicator {
            position: relative;
            margin-top: auto;
            padding-top: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.7);
            animation: pulseHint 2s ease-in-out infinite;
            opacity: 0.8;
        }

        @keyframes pulseHint {
            0%, 100% {
                opacity: 0.8;
                transform: translateY(0);
            }
            50% {
                opacity: 1;
                transform: translateY(-3px);
            }
        }

        .click-indicator i {
            font-size: 0.9rem;
        }

        #city-card:hover .click-indicator {
            animation: none;
            opacity: 0.9;
        }

        .time-card {
            grid-column: 2;
            grid-row: 2;
        }

        .time-display {
            position: relative;
        }

        #time {
            font-family: 'Orbitron', monospace;
            font-size: clamp(2rem, 5vw, 3.2rem);
            font-weight: 600;
            margin: 0;
            color: var(--text-primary);
            text-shadow: 0 0 20px var(--neon-green);
            background: linear-gradient(90deg, var(--neon-green), var(--neon-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: pulse 2s ease-in-out infinite;
            letter-spacing: -0.5px;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }

        #date {
            margin-top: 10px;
            font-size: clamp(1rem, 2.5vw, 1.3rem);
            color: var(--text-secondary);
            font-weight: 400;
            letter-spacing: 0.5px;
            font-family: "Inter", sans-serif;
        }

        .section-title {
            font-size: clamp(1.2rem, 3vw, 1.6rem);
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--text-primary);
            text-align: center;
            position: relative;
            font-family: "Montserrat", sans-serif;
            letter-spacing: 0.5px;
            cursor: default;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-pink));
            border-radius: 2px;
        }

        .weather-icon {
            font-size: clamp(2rem, 4vw, 3rem);
            margin-bottom: 10px;
            color: var(--neon-blue);
            text-shadow: 0 0 20px var(--neon-blue);
            animation: iconFloat 3s ease-in-out infinite;
        }

        @keyframes iconFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .map-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            z-index: 10000;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            justify-content: center;
            align-items: center;
            animation: fadeIn 0.3s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .map-modal.active {
            display: flex;
        }

        .map-container {
            width: 90%;
            max-width: 1000px;
            height: 80%;
            max-height: 700px;
            background: var(--glass-bg);
            border: 2px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: 20px;
            box-shadow: var(--glass-shadow);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            position: relative;
            display: flex;
            flex-direction: column;
            animation: slideInUp 0.4s ease-out;
        }

        #map {
            flex: 1;
            border-radius: var(--border-radius-small);
            overflow: hidden;
            margin-bottom: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .map-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        .coordinates-display {
            font-family: 'Orbitron', monospace;
            color: var(--text-primary);
            background: rgba(0, 0, 0, 0.4);
            padding: 12px 18px;
            border-radius: var(--border-radius-small);
            border: 1px solid var(--glass-border);
            font-size: 0.95rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .map-buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .map-btn {
            padding: 12px 24px;
            border: none;
            border-radius: var(--border-radius-small);
            background: linear-gradient(135deg, var(--neon-blue) 0%, var(--neon-purple) 100%);
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition-smooth);
            font-family: "Montserrat", sans-serif;
            font-size: 0.95rem;
            box-shadow: 0 4px 10px rgba(0, 212, 255, 0.3);
        }

        .map-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 212, 255, 0.5);
        }

        .map-btn:active {
            transform: translateY(-1px);
        }

        .map-btn.cancel {
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
            box-shadow: 0 4px 10px rgba(245, 87, 108, 0.3);
        }

        .map-btn.cancel:hover {
            box-shadow: 0 8px 20px rgba(245, 87, 108, 0.5);
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            font-size: 24px;
            transition: var(--transition-smooth);
            z-index: 10001;
        }

        .close-modal:hover {
            background: rgba(255, 0, 0, 0.4);
            transform: rotate(90deg);
            box-shadow: 0 4px 15px rgba(255, 0, 0, 0.4);
        }

        @media (max-width: 1200px) {
            .main-container {
                grid-template-columns: 250px 1fr;
            }
        }

        @media (max-width: 1024px) {
            .main-container {
                grid-template-columns: 1fr;
                grid-template-rows: auto auto auto;
                gap: 20px;
            }
            .side-bar {
                grid-column: 1;
                grid-row: 1;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 15px;
            }
            .weather-cards {
                grid-column: 1;
                grid-row: 2;
            }
            .time-card {
                grid-column: 1;
                grid-row: 3;
            }
        }

        @media (max-width: 768px) {
            body {
                padding: 5px;
            }
            .main-container {
                padding: 20px;
                gap: 15px;
            }
            .weather-cards {
                grid-template-columns: 1fr !important;
                gap: 15px !important;
            }
            .card_ma {
                min-height: 180px;
                padding: 20px !important;
            }
            .city-name {
                font-size: 1.6rem !important;
                margin: 10px 0 !important;
            }
            .click-indicator {
                margin-top: auto;
                padding-top: 15px;
            }
            .temperature-display .no0 {
                font-size: 2.8rem !important;
                margin: 10px 0;
            }
            .weather-state {
                font-size: 1.2rem !important;
                margin: 10px 0 !important;
            }
            .side-bar {
                grid-template-columns: 1fr;
            }
            .side_Cs {
                padding: 15px;
                flex-direction: column;
                text-align: center;
                gap: 8px;
            }
            .side_Cs .label, .side_Cs .value {
                font-size: 1rem;
            }
            .map-container {
                width: 95%;
                height: 85%;
                padding: 15px;
            }
            .map-controls {
                flex-direction: column;
                gap: 10px;
            }
            .map-buttons {
                width: 100%;
                justify-content: space-between;
            }
            .coordinates-display {
                width: 100%;
                text-align: center;
            }
        }

        @media (max-width: 480px) {
            .main-container {
                padding: 15px;
                border-radius: 20px;
            }
            .card_ma {
                min-height: 160px;
                padding: 15px !important;
            }
            .city-name {
                font-size: 1.4rem !important;
            }
            .temperature-display .no0 {
                font-size: 2.5rem !important;
            }
            .weather-icon {
                font-size: 2.2rem !important;
            }
            .click-indicator {
                font-size: 0.8rem;
            }
            .side-bar {
                padding: 20px;
                border-radius: 12px;
            }
            .side_Cs {
                padding: 12px;
                border-radius: 10px;
            }
            .map-container {
                padding: 10px;
            }
            .map-btn {
                padding: 10px 18px;
                font-size: 0.85rem;
            }
        }

        .loading-shimmer {
            background: linear-gradient(90deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.3) 50%, rgba(255, 255, 255, 0.1) 100%);
            background-size: 200% 100%;
            animation: shimmer 2s ease-in-out infinite;
        }

        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .main-container {
            animation: slideInUp 0.8s ease-out;
        }

        .side-bar {
            animation: slideInLeft 1s ease-out 0.2s both;
        }

        .weather-cards .card_ma:nth-child(1) {
            animation: slideInUp 1s ease-out 0.4s both;
        }

        .weather-cards .card_ma:nth-child(2) {
            animation: slideInUp 1s ease-out 0.6s both;
        }

        .weather-cards .card_ma:nth-child(3) {
            animation: slideInUp 1s ease-out 0.8s both;
        }

        .time-card {
            animation: slideInRight 1s ease-out 1s both;
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        @media (prefers-contrast: high) {
            :root {
                --glass-bg: rgba(0, 0, 0, 0.9);
                --glass-border: rgba(255, 255, 255, 0.9);
                --text-primary: #ffffff;
                --text-secondary: #ffffff;
            }
        }

        .card_ma:focus, .side_Cs:focus, .map-btn:focus {
            outline: 3px solid var(--neon-blue);
            outline-offset: 2px;
        }

        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-pink));
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
        }

        .date-picker-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            z-index: 10000;
            justify-content: center;
            align-items: center;
            transition: opacity 0.3s ease-out;
            animation: fadeIn 0.3s ease-out;
        }

        .date-picker-modal.active {
            display: flex;
        }

        .date-picker-container {
            background: var(--glass-bg);
            border: 2px solid var(--glass-border);
            border-radius: var(--border-radius);
            padding: 30px;
            box-shadow: var(--glass-shadow);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            max-width: 500px;
            width: 90%;
            animation: slideInUp 0.5s ease-out;
        }

        .date-picker-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text-primary);
            text-align: center;
            margin-bottom: 25px;
            font-family: "Montserrat", sans-serif;
        }

        .date-inputs-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }

        .date-input-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .date-input-label {
            font-size: 0.9rem;
            color: var(--text-secondary);
            font-weight: 500;
            text-align: center;
        }

        .date-select {
            padding: 12px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--glass-border);
            border-radius: var(--border-radius-small);
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 600;
            font-family: 'Orbitron', monospace;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }

        .date-select:hover {
            background: rgba(0, 212, 255, 0.2);
            border-color: var(--neon-blue);
            box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
        }

        .date-select:focus {
            outline: none;
            border-color: var(--neon-blue);
            box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.2);
        }

        .date-select option {
            background: #1a1a2e;
            color: white;
            padding: 10px;
        }

        .date-picker-buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
        }

        .date-picker-btn {
            padding: 12px 30px;
            border: none;
            border-radius: var(--border-radius-small);
            background: linear-gradient(135deg, var(--neon-blue) 0%, var(--neon-purple) 100%);
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: "Montserrat", sans-serif;
        }

        .date-picker-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 212, 255, 0.4);
        }

        .date-picker-btn:active {
            transform: translateY(-1px);
        }

        .date-picker-btn.cancel {
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        }

        .date-picker-btn.cancel:hover {
            box-shadow: 0 8px 20px rgba(245, 87, 108, 0.4);
        }

        @media (max-width: 768px) {
            .date-inputs-container {
                grid-template-columns: 1fr;
            }
            .date-picker-container {
                padding: 25px;
            }
        }

        .Choose {
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: var(--text-secondary);
            border-radius: var(--border-radius-small);
            padding: 12px 24px;
            background: rgba(255, 255, 255, 0.05);
            cursor: pointer;
            transition: var(--transition-smooth);
            font-family: "Montserrat", sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
        }

        .Choose:hover {
            color: var(--text-primary);
            border-color: var(--neon-blue);
            background: rgba(0, 212, 255, 0.1);
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
            transform: translateY(-2px);
        }

        /* Tooltip for better UX */
        [data-tooltip] {
            position: relative;
        }

        [data-tooltip]::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(-5px);
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease, transform 0.3s ease;
            z-index: 10002;
        }

        [data-tooltip]:hover::after {
            opacity: 1;
            transform: translateX(-50%) translateY(-10px);
        }

        /* Enhanced loading states */
        .skeleton {
            background: linear-gradient(90deg, 
                rgba(255, 255, 255, 0.05) 25%, 
                rgba(255, 255, 255, 0.15) 50%, 
                rgba(255, 255, 255, 0.05) 75%
            );
            background-size: 200% 100%;
            animation: skeleton-loading 1.5s ease-in-out infinite;
            border-radius: var(--border-radius-small);
        }

        @keyframes skeleton-loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }