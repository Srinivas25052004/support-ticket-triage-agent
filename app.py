from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from services import (
    process_single_ticket,
    process_csv,
    download_results
)

from analytics import (
    get_dashboard_stats,
    get_recent_tickets
)

app = FastAPI(
    title="SupportIQ - AI Ticket Intelligence Platform",
    version="3.0"
)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    stats = get_dashboard_stats()
    recent = get_recent_tickets()

    chart_data = {
        "categories": {
            "Authentication": stats["authentication"],
            "Billing": stats["billing"],
            "Technical": stats["technical"],
            "General": stats["general"]
        },
        "urgency": {
            "High": stats["high"],
            "Medium": stats["medium"],
            "Low": stats["low"]
        }
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None,
            "upload_message": None,
            "stats": stats,
            "recent": recent,
            "chart_data": chart_data
        }
    )



@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    subject: str = Form(...),
    body: str = Form(...)
):

    result = process_single_ticket(subject, body)

    stats = get_dashboard_stats()
    recent = get_recent_tickets()

    chart_data = {
        "categories": {
            "Authentication": stats["authentication"],
            "Billing": stats["billing"],
            "Technical": stats["technical"],
            "General": stats["general"]
        },
        "urgency": {
            "High": stats["high"],
            "Medium": stats["medium"],
            "Low": stats["low"]
        }
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "upload_message": None,
            "stats": stats,
            "recent": recent,
            "chart_data": chart_data
        }
    )



@app.post("/upload", response_class=HTMLResponse)
async def upload(
    request: Request,
    file: UploadFile = File(...)
):

    try:

        count = process_csv(file.file)

        stats = get_dashboard_stats()
        recent = get_recent_tickets()

        chart_data = {
            "categories": {
                "Authentication": stats["authentication"],
                "Billing": stats["billing"],
                "Technical": stats["technical"],
                "General": stats["general"]
            },
            "urgency": {
                "High": stats["high"],
                "Medium": stats["medium"],
                "Low": stats["low"]
            }
        }

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "result": None,
                "upload_message": f"✅ Successfully processed {count} tickets.",
                "stats": stats,
                "recent": recent,
                "chart_data": chart_data
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "result": None,
                "upload_message": f"❌ {str(e)}",
                "stats": get_dashboard_stats(),
                "recent": get_recent_tickets(),
                "chart_data": {
                    "categories": {},
                    "urgency": {}
                }
            }
        )



@app.get("/download")
async def download():

    file_path = download_results()

    if file_path:
        return FileResponse(
            path=file_path,
            filename="results.csv",
            media_type="text/csv"
        )

    return {"message": "No results found."}



@app.get("/health")
async def health():

    return {
        "status": "running",
        "application": "SupportIQ",
        "version": "3.0"
    }