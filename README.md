Team Setup and Project Planning — Group-5~C3
Project Overview

This project aims to process and analyze MoMo SMS data exported in XML format. The pipeline will:

Parse raw SMS XML files.

Clean and normalize transaction data (amounts, dates, phone numbers).

Categorize transactions into types (e.g., cash in, cash out, fees).

Store results in a relational database (SQLite).

Export processed data into a JSON file for frontend visualization.

Provide a simple web dashboard for analysis and insights.

This Week 1 setup establishes our shared repository, system architecture draft, and Scrum workflow to support collaborative development.

Team Members

Member 1:Frank Musiime
Member 2:Placide Niyonizeye
Member 3:Olga Ikirezi

Repository Organization
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

System Architecture

High-Level Components:

ETL Pipeline: Parses XML → cleans/normalizes → categorizes → stores in SQLite → exports JSON.

Relational Database (SQLite): Central store of structured transaction data.

Processed Data (JSON): Feeds the dashboard with KPIs, charts, and tables.

Web Dashboard: Static frontend (HTML/CSS/JS) that fetches processed data for visualization.

Logs: ETL run logs and unparsed data for troubleshooting.

Diagram Link: [Insert link to Draw.io or Miro diagram]
Diagram File in Repo: web/assets/architecture.png

Scrum Board

Tool Used: [Insert: GitHub Projects / Trello / Jira]

Board Link: [Insert board link here]

Columns: To Do | In Progress | Done

Initial Tasks:

Repository setup & collaborators added

Draft system architecture diagram

Organize ETL scaffolding

Research sample XML data

Week 1 Deliverables

GitHub repository created with collaborators and complete README.

Architecture diagram drafted and committed in repo.

Scrum board created with required columns and populated tasks.
