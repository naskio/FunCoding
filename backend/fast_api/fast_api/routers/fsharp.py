from fastapi import APIRouter
from fast_api.utils.fantomas_format import format_code
from fast_api.utils.run_fsharp_mock import run_fsharp
from fast_api.models import FormatDTO, RunDTO, RunRO
import random

router = APIRouter(tags=["fsharp"])


@router.post("/format", response_model=FormatDTO)
async def format_endpoint(format_dto: FormatDTO) -> FormatDTO:
    formatted_code = format_code(format_dto.code)
    format_dto = FormatDTO(code=formatted_code)
    return format_dto


@router.post("/run", response_model=RunRO)
async def run_endpoint(run_dto: RunDTO) -> RunRO:
    cpu_time = round(3 * random.random(), 2)
    memory = random.randint(10000, 100000)
    is_correct = random.choice([True, False])

    return RunRO(
        cpu_time=cpu_time,
        memory=memory,
        is_correct=is_correct,
        stdout=run_fsharp(run_dto.code),
        # stderr="",
    )
