from hyperon import *
from hyperon.ext import register_atoms
from .agents import *

@register_atoms(pass_metta=True)
def babyagi_atoms(metta):
    sentimentAnalyzerAtom = OperationAtom('sntmnt', lambda *args: analyze_sentiment(metta, *args), unwrap=False)
    responseGeneratorAtom = OperationAtom('rspgen', lambda *args: contextual_generate_response(metta, *args), unwrap=False)

    return {
        r"sntmnt": sentimentAnalyzerAtom,
        r"rspgen": responseGeneratorAtom
    }
