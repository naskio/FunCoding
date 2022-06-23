from fastapi import APIRouter
from fast_api.utils.fantomas_format import format_code
from fast_api.models import FormatDTO, RunDTO, RunRO

router = APIRouter(tags=["fsharp"])


@router.post("/format", response_model=FormatDTO)
async def format_endpoint(format_dto: FormatDTO) -> FormatDTO:
    formatted_code = format_code(format_dto.code)
    format_dto = FormatDTO(code=formatted_code)
    return format_dto


@router.post("/run", response_model=RunRO)
async def run_endpoint(format_dto: RunDTO) -> RunRO:
    return RunRO()
