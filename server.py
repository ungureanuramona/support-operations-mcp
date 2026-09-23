from mcp.server import MCPServer

mcp = MCPServer("Support Operations MCP")

INCIDENTS = {
    "INC-1001": {
        "incident_id": "INC-1001",
        "service": "Orders API",
        "status": "Investigating",
        "severity": "High",
        "summary": "Fictional Orders API requests are returning 500 responses.",
    },
    "INC-1002": {
        "incident_id": "INC-1002",
        "service": "Identity Service",
        "status": "Monitoring",
        "severity": "Medium",
        "summary": "Fictional users intermittently receive authentication errors.",
    },
}

SERVICES = {
    "orders-api": {
        "service": "Orders API",
        "status": "Degraded",
        "message": "Fictional elevated 500 error rate.",
    },
    "identity-service": {
        "service": "Identity Service",
        "status": "Operational",
        "message": "Fictional service is responding normally.",
    },
}

RUNBOOKS = {
    "api-errors": {
        "title": "API Error Investigation Runbook",
        "steps": [
            "Collect the endpoint URL, timestamp, request ID, and response code.",
            "Check the service health dashboard and recent deployments.",
            "Escalate to the owning team if the issue persists.",
        ],
    },
    "authentication": {
        "title": "Authentication Incident Runbook",
        "steps": [
            "Verify the identity service status.",
            "Check whether credentials, tokens, or certificates are valid.",
            "Review recent authentication configuration changes.",
        ],
    },
}


@mcp.tool()
def get_incident(incident_id: str) -> dict:
    """Return details for a fictional support incident by incident ID."""
    normalized_id = incident_id.upper()

    return INCIDENTS.get(
        normalized_id,
        {
            "error": f"Incident {normalized_id} was not found.",
        },
    )


@mcp.tool()
def get_service_status(service_name: str) -> dict:
    """Return the fictional operational status of a service."""
    service_key = service_name.lower().replace(" ", "-")

    return SERVICES.get(
        service_key,
        {
            "error": f"Service {service_name} was not found.",
        },
    )


@mcp.tool()
def get_runbook(topic: str) -> dict:
    """Return a fictional support runbook for API errors or authentication."""
    topic_key = topic.lower().strip()

    return RUNBOOKS.get(
        topic_key,
        {
            "error": (
                "Runbook not found. Available topics: "
                "api-errors, authentication."
            ),
        },
    )


if __name__ == "__main__":
    mcp.run()