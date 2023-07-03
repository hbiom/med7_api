from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import spacy

app = FastAPI()
templates = Jinja2Templates(directory="templates/") 

med7 = spacy.load("en_core_med7_lg")


# https://github.com/kormilitzin/med7
# https://www.andrewvillazon.com/clinical-natural-language-processing-python/
#!pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg.tar.gz

class Item(BaseModel):
    text: str


@app.post('/api/')
async def api(item: Item):

    try:
        data = item.text

        # create distinct colours for labels
        col_dict = {}
        seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
        
        for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
            col_dict[label] = colour

        options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}
        doc = med7(data)

        print(doc.ents)

        prediction = [(ent.text, ent.label_) for ent in doc.ents]

    except Exception as e:
        return {"error": str(e)}

    return {"prediction": prediction}


@app.post('/predict/', response_class=HTMLResponse)
async def predict(request: Request, item: Item):

    try:
        data = item.text

        # create distinct colours for labels
        col_dict = {}
        seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']

        for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
            col_dict[label] = colour

        options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}
        doc = med7(data)

        prediction = [(ent.text, ent.label_) for ent in doc.ents]

    except Exception as e:
        return {"error": str(e)}

    return templates.TemplateResponse("template.html", {"request": request, "entities": prediction, "colors": col_dict})
