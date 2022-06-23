from fastapi import APIRouter
from fast_api.utils.fantomas_format import format_code
from fast_api.models import FormatDTO

router = APIRouter(tags=["fsharp"])


@router.post("/format", response_model=FormatDTO)
async def format_code(format_dto: FormatDTO) -> FormatDTO:
    formatted_code = format_code(format_dto.code)
    format_ro = FormatDTO(code=formatted_code)
    return format_ro
