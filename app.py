from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run

from typing import Optional

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline

# Initialize FastAPI application
app = FastAPI()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

# Allow all origins for Cross-Origin Resource Sharing (CORS)
origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    """
    DataForm class to handle and process incoming form data.
    Supports both user-friendly options (e.g. 'Male'/'Female', 'Yes'/'No', '< 1 Year')
    and numerical encodings (1/0) for backward compatibility.
    """
    def __init__(self, request: Request):
        self.request: Request = request
        self.raw_data: dict = {}
        self.Gender: Optional[int] = None
        self.Age: Optional[int] = None
        self.Driving_License: Optional[int] = None
        self.Region_Code: Optional[float] = None
        self.Previously_Insured: Optional[int] = None
        self.Annual_Premium: Optional[float] = None
        self.Policy_Sales_Channel: Optional[float] = None
        self.Vintage: Optional[int] = None
        self.Vehicle_Age: Optional[str] = None
        self.Vehicle_Age_lt_1_Year: Optional[int] = None
        self.Vehicle_Age_gt_2_Years: Optional[int] = None
        self.Vehicle_Damage_Yes: Optional[int] = None

    async def get_vehicle_data(self):
        """
        Method to retrieve and assign form data to class attributes with smart type casting.
        """
        form = await self.request.form()
        self.raw_data = {k: v for k, v in form.items()}

        # 1. Gender: 'Male' / 'Female' or 1 / 0
        gender_val = str(form.get("Gender", "Male")).strip().lower()
        self.Gender = 1 if gender_val in ["male", "1", "m"] else 0

        # 2. Age
        try:
            self.Age = int(float(form.get("Age", 30)))
        except (ValueError, TypeError):
            self.Age = 30

        # 3. Driving License: 'Yes' / 'No' or 1 / 0
        dl_val = str(form.get("Driving_License", "Yes")).strip().lower()
        self.Driving_License = 1 if dl_val in ["yes", "1", "true", "y"] else 0

        # 4. Region Code
        try:
            self.Region_Code = float(form.get("Region_Code", 28.0))
        except (ValueError, TypeError):
            self.Region_Code = 28.0

        # 5. Previously Insured: 'Yes' / 'No' or 1 / 0
        pi_val = str(form.get("Previously_Insured", "No")).strip().lower()
        self.Previously_Insured = 1 if pi_val in ["yes", "1", "true", "y"] else 0

        # 6. Annual Premium
        try:
            self.Annual_Premium = float(form.get("Annual_Premium", 25000.0))
        except (ValueError, TypeError):
            self.Annual_Premium = 25000.0

        # 7. Policy Sales Channel
        try:
            self.Policy_Sales_Channel = float(form.get("Policy_Sales_Channel", 152.0))
        except (ValueError, TypeError):
            self.Policy_Sales_Channel = 152.0

        # 8. Vintage (Days)
        try:
            self.Vintage = int(float(form.get("Vintage", 150)))
        except (ValueError, TypeError):
            self.Vintage = 150

        # 9. Vehicle Age: '< 1 Year', '1 - 2 Years', '> 2 Years'
        v_age = str(form.get("Vehicle_Age", "")).strip()
        self.Vehicle_Age = v_age
        if v_age == "< 1 Year" or form.get("Vehicle_Age_lt_1_Year") == "1":
            self.Vehicle_Age_lt_1_Year = 1
            self.Vehicle_Age_gt_2_Years = 0
        elif v_age == "> 2 Years" or form.get("Vehicle_Age_gt_2_Years") == "1":
            self.Vehicle_Age_lt_1_Year = 0
            self.Vehicle_Age_gt_2_Years = 1
        else:
            # 1 - 2 Years (reference category)
            self.Vehicle_Age_lt_1_Year = 0
            self.Vehicle_Age_gt_2_Years = 0

        # 10. Vehicle Damage: 'Yes' / 'No' or 1 / 0
        vd_val = str(form.get("Vehicle_Damage", form.get("Vehicle_Damage_Yes", "No"))).strip().lower()
        self.Vehicle_Damage_Yes = 1 if vd_val in ["yes", "1", "true", "y"] else 0


# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for vehicle data input.
    """
    return templates.TemplateResponse(
        request=request,
        name="vehicledata.html",
        context={"context": None, "form_data": {}},
    )

# Route to trigger the model training process
@app.get("/train")
async def trainRouteClient():
    """
    Endpoint to initiate the model training pipeline.
    """
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful!!!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Route to handle form submission and make predictions
@app.post("/")
async def predictRouteClient(request: Request):
    """
    Endpoint to receive form data, process it, and make a prediction.
    """
    try:
        form = DataForm(request)
        await form.get_vehicle_data()
        
        vehicle_data = VehicleData(
            Gender=form.Gender,
            Age=form.Age,
            Driving_License=form.Driving_License,
            Region_Code=form.Region_Code,
            Previously_Insured=form.Previously_Insured,
            Annual_Premium=form.Annual_Premium,
            Policy_Sales_Channel=form.Policy_Sales_Channel,
            Vintage=form.Vintage,
            Vehicle_Age_lt_1_Year=form.Vehicle_Age_lt_1_Year,
            Vehicle_Age_gt_2_Years=form.Vehicle_Age_gt_2_Years,
            Vehicle_Damage_Yes=form.Vehicle_Damage_Yes
        )

        # Convert form data into a DataFrame for the model
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Initialize the prediction pipeline
        model_predictor = VehicleDataClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=vehicle_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

        # Render the same HTML page with the prediction result and retained form data
        return templates.TemplateResponse(
            request=request,
            name="vehicledata.html",
            context={
                "context": status,
                "prediction_value": int(value),
                "form_data": form.raw_data,
            },
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)