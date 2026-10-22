KNX-Based Building Automation Design — Melbourne Building

Project Overview

This repository documents a conceptual building automation design developed as part of an Electronic Engineering graduation project at Universidad Central, Bogotá, Colombia.

The project explores the proposed use of KNX-based building automation to improve energy management in a hypothetical multi-level administrative and service building with an approximate floor area of 1,015.9 m².

The design considers occupancy-aware lighting control, daylight-responsive lighting strategies, DALI lighting control, user-operated lighting scenes, environmental monitoring, and a proposed interface between KNX and HVAC equipment.

Building and Functional Zones

The conceptual building design considers the following functional areas:

Lobby and reception

Cafeteria

Open-plan collaborative workspaces

Private administrative offices

Data centre/server room

The automation concept considers the different operational requirements of these zones, including variable occupancy in shared spaces and continuous operation requirements in the server room.

Proposed Automation Architecture

The original design considers the following technologies:

KNX: proposed building automation and control architecture.

ETS6: engineering and configuration environment for KNX devices.

DALI: proposed integration for lighting control.

HVAC integration: proposed communication between the KNX system and compatible HVAC equipment through an interface gateway.

Sensors and user interfaces: proposed occupancy, environmental and user-control functions.

The project report documents the proposed system architecture, selected devices, functional zones and building layouts. These elements represent a design proposal rather than evidence of a completed physical installation.

Preliminary Energy Assessment

The original project report presents a theoretical comparison between a conventional operating scenario and a proposed automated scenario.

The report estimates annual energy consumption as follows:

Scenario

Estimated annual energy consumption

Conventional operation

Approximately 142,000 kWh/year

Proposed automated operation

Approximately 107,000 kWh/year

Estimated difference

Approximately 35,000 kWh/year

These figures correspond to an estimated reduction of approximately 24.6%, rounded to 25%.

The values are design-stage estimates reported in the original project document. They are not measurements from an operating building, and the available report does not establish experimental validation of the projected savings.

Scope and Limitations

The original graduation project is a conceptual engineering design. It does not document a completed physical KNX installation or field measurements validating the estimated energy reduction.

The annual energy estimates should therefore be interpreted as preliminary projections, not as experimentally demonstrated performance.

Any supplementary computational model included in this repository must be assessed separately from the original project. Its assumptions, equations, units, implementation, and results must be documented independently and must not be presented as experimentally validated building performance.

Original Academic Project

Title: KNX Automation Project — Melbourne Building
Authors: Daniel Felipe Villegas Castellanos
Institution: Universidad Central, Bogotá, Colombia
Date: November 2025
Academic context: Electronic Engineering graduation project completed through the thematic advanced course Automation and Control of Smart and Sustainable Buildings.

Future Work

Potential future work includes developing a more detailed and reproducible energy model, validating the model against clearly defined building operating assumptions, refining the proposed KNX device configuration, and evaluating the system through a physical implementation or an appropriate experimental test environment.
pip install -r requirements.txt
python tests/test_model.py     # 4 sanity checks
python main.py                 # prints results, writes results/*.png and results/summary.json
Authors

Daniel Felipe Villegas Castellanos · Santiago Guarnizo Domínguez Universidad Central, Colombia — dvillegasc@ucentral.edu.co
