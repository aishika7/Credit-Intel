import shap
import pandas as pd
from typing import Dict
from app.model import MODEL, FEATURES

# Use linear model → shap LinearExplainer is fast and clear

def shap_explain(feature_row: Dict) -> Dict[str, float]:
    X = pd.DataFrame([feature_row], columns=FEATURES).fillna(0.0)
    if not MODEL.fitted:
        return {f: 0.0 for f in FEATURES}
    explainer = shap.LinearExplainer(MODEL.pipe.named_steps["clf"], MODEL.pipe.named_steps["scaler"].transform(pd.DataFrame([feature_row], columns=FEATURES).fillna(0.0)))
    # Fallback simple method when shap linear explainer is complex; use coefficients approximation
    try:
        shap_vals = explainer.shap_values(X)
        vals = shap_vals[0] if hasattr(shap_vals, "__len__") else shap_vals
        return {f: float(v) for f, v in zip(FEATURES, vals)}
    except Exception:
        coef = getattr(MODEL.pipe.named_steps["clf"], "coef_", None)
        if coef is not None:
            vals = (X.values[0] * coef[0]).tolist()
            return {f: float(v) for f, v in zip(FEATURES, vals)}
        return {f: 0.0 for f in FEATURES}