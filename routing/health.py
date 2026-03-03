from fastapi import APIRouter, status

router_health = APIRouter()


@router_health.get("/healthcheck", status_code=status.HTTP_200_OK)
def healthcheck() -> dict[str, str]:
    return {"status": "OK"}
