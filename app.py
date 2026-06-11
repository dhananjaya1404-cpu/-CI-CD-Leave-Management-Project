from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import uuid
import webbrowser
import threading
import os

app = Flask(__name__)
app.secret_key = "leavesync-2025"

# ── In-memory data ──────────────────────────────────────
EMPLOYEES = {
    "E001": {"name": "Azam Z",  "dept": "Backend",  "role": "Software Engineer"},
    "E002": {"name": "Dolly",    "dept": "Design",   "role": "UI Designer"},
    "E003": {"name": "Akash H",    "dept": "Backend",  "role": "DevOps Engineer"},
    "E004": {"name": "Manoj",    "dept": "QA",       "role": "Test Engineer"},
    "E005": {"name": "Dhanush D",   "dept": "DevOps",   "role": "Cloud Engineer"},
}

LEAVE_BALANCE = {
    "E001": {"Annual": 18, "Sick": 6, "Casual": 4, "Maternity": 90, "Comp Off": 2}
}

LEAVES = [
    {"id": "L001", "emp_id": "E001", "type": "Annual",   "from": "2025-12-23", "to": "2025-12-26", "days": 4, "reason": "Family vacation",      "status": "Pending"},
    {"id": "L002", "emp_id": "E001", "type": "Sick",     "from": "2025-11-10", "to": "2025-11-10", "days": 1, "reason": "Fever",                 "status": "Approved"},
    {"id": "L003", "emp_id": "E001", "type": "Casual",   "from": "2025-10-05", "to": "2025-10-06", "days": 2, "reason": "Personal work",         "status": "Rejected"},
    {"id": "L004", "emp_id": "E002", "type": "Annual",   "from": "2026-05-06", "to": "2026-05-09", "days": 4, "reason": "Vacation",              "status": "Approved"},
    {"id": "L005", "emp_id": "E003", "type": "Sick",     "from": "2026-05-05", "to": "2026-05-05", "days": 1, "reason": "Not well",              "status": "Approved"},
    {"id": "L006", "emp_id": "E004", "type": "Casual",   "from": "2026-05-07", "to": "2026-05-07", "days": 1, "reason": "Personal work",         "status": "Pending"},
    {"id": "L007", "emp_id": "E005", "type": "Annual",   "from": "2026-05-08", "to": "2026-05-12", "days": 5, "reason": "Trip",                  "status": "Approved"},
]


def get_stats(emp_id):
    emp_leaves = [l for l in LEAVES if l["emp_id"] == emp_id]
    taken = sum(l["days"] for l in emp_leaves if l["status"] == "Approved")
    pending = sum(1 for l in emp_leaves if l["status"] == "Pending")
    today = datetime.today().strftime("%Y-%m-%d")
    team_on_leave = sum(
        1 for l in LEAVES
        if l["status"] == "Approved" and l["from"] <= today <= l["to"]
    )
    return {
        "balance": LEAVE_BALANCE[emp_id]["Annual"],
        "taken": taken,
        "pending": pending,
        "team_on_leave": team_on_leave,
    }


# ── Routes ───────────────────────────────────────────────
@app.route("/")
def dashboard():
    emp_id = "E001"
    emp = EMPLOYEES[emp_id]
    stats = get_stats(emp_id)
    recent = [l for l in LEAVES if l["emp_id"] == emp_id][-3:]
    balance = LEAVE_BALANCE[emp_id]
    return render_template("dashboard.html", emp=emp, stats=stats,
                           recent=recent, balance=balance)


@app.route("/apply", methods=["GET", "POST"])
def apply():
    emp_id = "E001"
    if request.method == "POST":
        leave_type = request.form.get("type")
        from_date  = request.form.get("from_date")
        to_date    = request.form.get("to_date")
        reason     = request.form.get("reason", "").strip()
        days       = int(request.form.get("days", 1))

        if not reason:
            flash("Reason is required.", "danger")
            return redirect(url_for("apply"))

        new_leave = {
            "id":     str(uuid.uuid4())[:6].upper(),
            "emp_id": emp_id,
            "type":   leave_type,
            "from":   from_date,
            "to":     to_date,
            "days":   days,
            "reason": reason,
            "status": "Pending",
        }
        LEAVES.append(new_leave)
        flash(f"{leave_type} for {days} day(s) submitted successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("apply.html")


@app.route("/my-leaves")
def my_leaves():
    emp_id = "E001"
    emp = EMPLOYEES[emp_id]
    my = [l for l in LEAVES if l["emp_id"] == emp_id]
    return render_template("my_leaves.html", emp=emp, leaves=my)


@app.route("/team")
def team():
    today = datetime.today().strftime("%Y-%m-%d")
    team_leaves = [
        {**l, "emp": EMPLOYEES[l["emp_id"]]}
        for l in LEAVES if l["emp_id"] != "E001"
    ]
    return render_template("team.html", team_leaves=team_leaves, today=today)


@app.route("/admin")
def admin():
    pending = [
        {**l, "emp": EMPLOYEES[l["emp_id"]]}
        for l in LEAVES if l["status"] == "Pending"
    ]
    return render_template("admin.html", pending=pending)


@app.route("/admin/action/<leave_id>/<action>", methods=["POST"])
def admin_action(leave_id, action):
    for leave in LEAVES:
        if leave["id"] == leave_id:
            leave["status"] = "Approved" if action == "approve" else "Rejected"
            flash(f"Leave {leave_id} {leave['status']}.", "success")
            break
    return redirect(url_for("admin"))


@app.route("/health")
def health():
    return {"status": "healthy", "total_leaves": len(LEAVES)}, 200


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.2, lambda: webbrowser.open("http://localhost:5000")).start()
    app.run(host="0.0.0.0", port=5000, debug=True)