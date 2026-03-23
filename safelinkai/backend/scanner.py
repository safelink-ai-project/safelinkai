from .url_heuristics import url_heuristics
from .dynamic_scan import dynamic_scan
from .behaviour_analysis import behaviour_analysis
from .risk_engine import calculate_risk

def scan_url(url):

    heuristic_score, heuristic_flags = url_heuristics(url)

    scan_data = dynamic_scan(url)

    threats = behaviour_analysis(scan_data)

    ai_result = 0

    risk_score, status = calculate_risk(
        ai_result,
        heuristic_score,
        threats
    )

    return {

        "url": url,

        "risk_score": risk_score,

        "status": status,

        "heuristic_flags": heuristic_flags,

        "behaviour_flags": threats,

        "page_info": scan_data
    }