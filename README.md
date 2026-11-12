# TECM Dashboard

Transformer and Equipment Condition Monitoring System. This dashboard demonstration includes six assets at three sample stations, thirty days of transformer readings, oil tests, inspection records, relay events, and maintenance logs. All condition data and alert thresholds are simulated.

| Role view | Workflow |
| --- | --- |
| Asset / Reliability | Explore trends, compare oil tests, review evidence, and request verification. |
| Operations | Review relay events, acknowledge alerts, confirm equipment state, and hand off work. |
| Maintenance | Review assignments, save field findings, and close acknowledged alerts after verification. |
| Supervisor | Review coverage, open risks, acknowledgement times, and clarity ratings. |

## Run on Windows

Use 64-bit Python 3.15. Extract the archive and open the `TECM` folder in VS Code. In the PowerShell terminal, run the following commands from the folder containing `app.py`.

```powershell
py -3.15 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

For Python 3.12 or 3.13, use `py -3.12` or `py -3.13` in the first command. If you already created `.venv` with a different interpreter, rename that folder before creating the new environment. The dashboard opens at [http://127.0.0.1:8501](http://127.0.0.1:8501). Stop it with **Ctrl+C** in the terminal.

On macOS or Linux, use `python3 -m venv .venv` and run the remaining commands with `.venv/bin/python`.

## Walk through an alert

1. Open **Operations → Review relay event**. Under **Workflow**, acknowledge the feeder trip, confirm its equipment state, and record a handoff.
2. Switch to **Maintenance → Overview** and open the new assignment. Record a field finding and close the alert.
3. Switch to **Supervisor**. Open the closed alert under **Alerts** to rate its clarity, then return to **Overview** to see the updated evaluation metrics.

The role switcher changes the demonstration view. The first run creates `data/tecm_demo.sqlite3`. Later runs retain acknowledgements, handoffs, findings, closures, and ratings in that file. Set the `TECM_DB_PATH` environment variable to an unused path to start a fresh demonstration database.

## Share the code privately on GitHub

Create an empty **private** repository. From the `TECM` folder, initialize Git and push the contents. Replace the sample URL with the repository URL.

```powershell
git init -b main
git add .
git commit -m "Add TECM condition monitoring dashboard"
git remote add origin https://github.com/YOUR-USERNAME/tecm-dashboard.git
git push -u origin main
```

Invite your supervisor through the repository settings. After accepting the invitation, they can clone the repository or download its ZIP and follow the run instructions. Each installation starts with its own sample data and saves its own workflow activity. [GitHub collaborator instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)

## Project structure

| Path | Purpose |
| --- | --- |
| `app.py` | Streamlit entry point and navigation |
| `dashboard/views.py` | Role dashboards, evidence, trends, and forms |
| `modules/monitoring.py` | Dashboard queries and alert workflow rules |
| `database/` | SQLAlchemy models, SQLite setup, and first-run seeding |
| `data/sample_data/condition_demo.json` | Demonstration assets, readings, and evidence |

The SQLite schema supports this single-workspace dashboard demonstration. The full TECM schema, tenant isolation, and authenticated role permissions are separate implementation milestones.
