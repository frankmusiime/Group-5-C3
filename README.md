# Team Setup
## Project Overview

> Group-5-C3

This project aims to process and analyze MoMo SMS data exported in XML format. The pipeline will:

Parse raw SMS XML files.

Clean and normalize transaction data (amounts, dates, phone numbers).

Categorize transactions into types (e.g., cash in, cash out, fees).

Store results in a relational database (SQLite).

Export processed data into a JSON file for frontend visualization.

Provide a simple web dashboard for analysis and insights.

This Week 1 setup establishes our shared repository, system architecture draft, and Scrum workflow to support collaborative development.

## Team Members

* Member 1:Frank Musiime
* Member 2:Placide Niyonizeye
* Member 3:Olga Ikirezi

## Repository Organization
.
├── README.md                         # Setup, run, overview
├── .env.example                      # Example environment variables
├── requirements.txt                  # Python dependencies
├── index.html                        # Dashboard entry point
├── web/                              # Frontend assets
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/                       # Icons, images, architecture diagram
├── data/
│   ├── raw/                          # Input XML (not committed)
│   ├── processed/                    # Processed JSON for dashboard
│   ├── db.sqlite3                    # SQLite database
│   └── logs/                         # ETL logs and dead-letter files
├── etl/                              # ETL pipeline scripts
│   ├── config.py
│   ├── parse_xml.py
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
├── scripts/                          # Helper shell scripts
│   ├── run_etl.sh
│   ├── export_json.sh
│   └── serve_frontend.sh
└── tests/                            # Unit tests
    ├── test_parse_xml.py
    ├── test_clean_normalize.py
    └── test_categorize.py

## System Architecture

### High-Level Components:

ETL Pipeline: Parses XML → cleans/normalizes → categorizes → stores in SQLite → exports JSON.

* Relational Database (SQLite): Central store of structured transaction data.

* Processed Data (JSON): Feeds the dashboard with KPIs, charts, and tables.

* Web Dashboard: Static frontend (HTML/CSS/JS) that fetches processed data for visualization.

* Logs: ETL run logs and unparsed data for troubleshooting.

* Diagram Link: https://app.diagrams.net/#G1LY8yB77TmslvLp_aLrv4BXHMCONO9wBB#%7B%22pageId%22%3A%227LU1rX8EdJsmNZgxLKIX%22%7D
* Diagram File in Repo: web/assets/architecture.png

Scrum Board Access

* Tool Used: Trello 

* Board Link:  https://trello.com/invite/b/68c02e0265dd9c507007771b/ATTI1ea804be72db315ff8d71eff0f6c976eA1E8CB15/group-5-c3-momo-sms-dashboard-scrum-board

* Columns: To Do | In Progress | Done

* Initial Tasks:

Repository setup & collaborators added

Draft system architecture diagram

Organize ETL scaffolding

Research sample XML data

